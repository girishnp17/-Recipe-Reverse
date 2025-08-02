import streamlit as st
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from huggingface_hub import login
from PIL import Image
import torch

st.title("Qwen2.5-VL-7B-Instruct Image Analyzer")

# Authenticate with Hugging Face
HF_TOKEN = st.text_input("Enter Hugging Face Access Token:", value="", type="password")
if HF_TOKEN:
    login(HF_TOKEN)

# Cache model loading to speed up UI
@st.cache_resource
def load_model():
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2-VL-7B-Instruct",
        torch_dtype="auto",
        device_map="auto",
        token=HF_TOKEN  # ensures authentication is passed
    )
    processor = AutoProcessor.from_pretrained(
        "Qwen/Qwen2-VL-7B-Instruct",
        token=HF_TOKEN
    )
    return model, processor

if HF_TOKEN:
    model, processor = load_model()
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        prompt = st.text_input("Enter your prompt for the image:", value="Describe this image.")
        if st.button("Analyze Image"):
            messages = [
                {"role": "user", "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": prompt},
                ]}
            ]
            # Prepare inputs
            text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            image_inputs, video_inputs = process_vision_info(messages)
            inputs = processor(
                text=[text],
                images=image_inputs,
                videos=video_inputs,
                padding=True,
                return_tensors="pt"
            ).to("cuda" if torch.cuda.is_available() else "cpu")
            with st.spinner("Analyzing..."):
                generated_ids = model.generate(**inputs, max_new_tokens=300)
                output_text = processor.batch_decode(
                    generated_ids,
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False
                )[0]
                st.success("Result:")
                st.write(output_text)
else:
    st.warning("Please enter your Hugging Face access token to begin.")

