import streamlit as st
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from PIL import Image
import torch
from prompts import (
    FOOD_VALIDATION_PROMPT,
    INGREDIENTS_SYSTEM_PROMPT,
    RECIPE_SYSTEM_PROMPT,
    NUTRITION_SYSTEM_PROMPT,
    GENERAL_FOOD_PROMPT
)

st.title("🍽️ Advanced Culinary Food Analyzer")
st.markdown("*Upload a food image and choose your analysis type*")

@st.cache_resource
def load_model():
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2-VL-7B-Instruct",
        torch_dtype="auto",
        device_map="auto"
    )
    processor = AutoProcessor.from_pretrained(
        "Qwen/Qwen2-VL-7B-Instruct"
    )
    return model, processor

def validate_food_image(image, model, processor):
    """Check if image contains food items"""
    messages = [
        {"role": "system", "content": [{"type": "text", "text": FOOD_VALIDATION_PROMPT}]},
        {"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "Is this image a food item?"},
        ]}
    ]
    
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt"
    ).to("cuda" if torch.cuda.is_available() else "cpu")
    
    generated_ids = model.generate(**inputs, max_new_tokens=10)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )[0].strip()
    
    return "VALID_FOOD" in output_text

def analyze_food(image, system_prompt, analysis_type, model, processor, user_question=""):
    """Analyze food image with specific system prompt"""
    
    user_text = f"Please provide a detailed {analysis_type} analysis of this food image."
    if user_question.strip():
        user_text = f"{user_question.strip()}"
    
    messages = [
        {"role": "system", "content": [{"type": "text", "text": system_prompt}]},
        {"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": user_text},
        ]}
    ]
    
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt"
    ).to("cuda" if torch.cuda.is_available() else "cpu")
    
    generated_ids = model.generate(**inputs, max_new_tokens=1024)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )[0]
    
    return output_text

# Load model
model, processor = load_model()

# File uploader
uploaded_file = st.file_uploader("📸 Upload a Food Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Food Image', use_column_width=True)
    
    # Validate if image contains food
    if not validate_food_image(image, model, processor):
        st.error("🚫 **Not Recognized as Food Item**")
        st.warning("The uploaded image is not recognized as a food item. Please upload an image containing food, beverages, or edible items.")
    else:
        st.success("✅ Food item detected! Choose your analysis:")
        
        # Create columns for buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ingredients_btn = st.button("🥕 **Ingredients Analysis**", use_container_width=True)
        
        with col2:
            recipe_btn = st.button("👨‍🍳 **Recipe & Instructions**", use_container_width=True)
            
        with col3:
            calories_btn = st.button("🔢 **Calories & Nutrition**", use_container_width=True)
        
        # Additional questions section
        st.markdown("---")
        st.subheader("❓ Ask Additional Questions")
        user_question = st.text_area(
            "Have a specific question about this food?",
            placeholder="e.g., What cuisine is this? How spicy is it? Can I make it vegan?",
            height=100
        )
        
        ask_question_btn = st.button("💬 **Ask Question**", use_container_width=True)
        
        # Handle button clicks
        if ingredients_btn:
            with st.spinner("🔍 Analyzing ingredients..."):
                result = analyze_food(image, INGREDIENTS_SYSTEM_PROMPT, "ingredients", model, processor)
                st.markdown("## 🥕 Ingredients Analysis")
                st.markdown(result)
        
        elif recipe_btn:
            with st.spinner("👨‍🍳 Creating recipe..."):
                result = analyze_food(image, RECIPE_SYSTEM_PROMPT, "recipe", model, processor)
                st.markdown("## 👨‍🍳 Complete Recipe & Cooking Instructions")
                st.markdown(result)
        
        elif calories_btn:
            with st.spinner("🔢 Calculating nutrition..."):
                result = analyze_food(image, NUTRITION_SYSTEM_PROMPT, "nutrition", model, processor)
                st.markdown("## 🔢 Calorie Count & Nutritional Analysis")
                st.markdown(result)
        
        elif ask_question_btn:
            if user_question.strip():
                with st.spinner("💭 Processing your question..."):
                    result = analyze_food(image, GENERAL_FOOD_PROMPT, "general", model, processor, user_question)
                    st.markdown("## 💬 Answer to Your Question")
                    st.markdown(result)
            else:
                st.warning("Please enter a question first.")

else:
    st.info("👆 Please upload a food image to begin analysis")

# Add footer
st.markdown("---")
st.markdown("*🤖 Powered by Qwen2.5-VL-7B-Instruct | Advanced Food AI Assistant*")