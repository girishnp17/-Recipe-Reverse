import streamlit as st
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch
from PIL import Image
import os
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT
import time

# Load environment variables
load_dotenv()

class QwenFoodAnalyzer:
    def __init__(self):
        """Initialize the Qwen VL food analyzer"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "Qwen/Qwen2.5-VL-7B-Instruct"
        
        # Initialize with loading state
        self.model = None
        self.processor = None
        self.tokenizer = None
        
        # Check for Hugging Face token
        self.hf_token = os.getenv("HUGGINGFACE_TOKEN")
        
    def load_model(self):
        """Load the Qwen model with progress indicator"""
        if self.model is None:
            try:
                # Load model components
                self.model = Qwen2VLForConditionalGeneration.from_pretrained(
                    self.model_name,
                    torch_dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
                    attn_implementation="flash_attention_2" if self.device == "cuda" else "eager",
                    device_map="auto" if self.device == "cuda" else None,
                    token=self.hf_token
                )
                
                self.processor = AutoProcessor.from_pretrained(
                    self.model_name,
                    token=self.hf_token
                )
                
                self.tokenizer = AutoTokenizer.from_pretrained(
                    self.model_name,
                    token=self.hf_token
                )
                
                # Move to device if not using device_map
                if self.device == "cpu":
                    self.model = self.model.to(self.device)
                
                return True, "Model loaded successfully!"
                
            except Exception as e:
                return False, f"Error loading model: {str(e)}"
        
        return True, "Model already loaded"
    
    def validate_image(self, image):
        """Validate uploaded image"""
        if image is None:
            return False, "No image provided"
        
        # Check image size
        if image.size[0] * image.size[1] > 16777216:  # 4096x4096 max
            return False, "Image too large. Please upload a smaller image."
        
        return True, "Valid image"
    
    def analyze_with_qwen(self, prompt, image, max_retries=3):
        """Analyze image with Qwen VL model"""
        for attempt in range(max_retries):
            try:
                # Prepare messages for Qwen
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "image": image,
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ]
                
                # Prepare inputs
                text = self.processor.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True
                )
                
                image_inputs, video_inputs = process_vision_info(messages)
                
                inputs = self.processor(
                    text=[text],
                    images=image_inputs,
                    videos=video_inputs,
                    padding=True,
                    return_tensors="pt",
                )
                
                inputs = inputs.to(self.device)
                
                # Generate response
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=1024,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
                
                generated_ids_trimmed = [
                    out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
                ]
                
                output_text = self.processor.batch_decode(
                    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
                )
                
                return output_text[0] if output_text else "No response generated"
                
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(1)  # Wait before retry
                    continue
                else:
                    return f"Error analyzing image after {max_retries} attempts: {str(e)}"
    
    def analyze_food_image(self, image, user_question):
        """Main analysis function"""
        is_valid, message = self.validate_image(image)
        if not is_valid:
            return message
        
        # Load model if not already loaded
        success, load_message = self.load_model()
        if not success:
            return load_message
        
        prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_question}"
        return self.analyze_with_qwen(prompt, image)
    
    def get_comprehensive_analysis(self, image):
        """Get a comprehensive analysis of the food"""
        is_valid, message = self.validate_image(image)
        if not is_valid:
            return message
        
        # Load model if not already loaded
        success, load_message = self.load_model()
        if not success:
            return load_message
        
        comprehensive_prompt = f"""{SYSTEM_PROMPT}

Please provide a comprehensive analysis of this food image including:

## 🔍 Food Identification
- Main dish name and type
- Visible ingredients
- Cooking method used
- Cuisine origin

## 🍳 Recipe Overview
- Brief recipe summary
- Key preparation steps
- Approximate cooking time

## 🥗 Nutritional Highlights
- Estimated calories per serving
- Main nutrients
- Health benefits

## 🌍 Cultural Context
- Origin and cultural significance
- Traditional serving occasions

Please format your response clearly with the sections above."""
        
        return self.analyze_with_qwen(comprehensive_prompt, image)

def create_qwen_sidebar():
    """Create and populate the sidebar for Qwen version"""
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=80)
        st.title("🤖 Qwen Food AI")
        
        st.markdown("### 🧠 Model Info")
        st.info("""
        **Model**: Qwen2.5-VL-7B-Instruct
        
        **Capabilities**:
        - Advanced vision-language understanding
        - Multilingual support
        - High-quality reasoning
        """)
        
        st.markdown("### 🎯 What I Can Do")
        st.success("""
        **🔍 Identify** any food or dish
        
        **📝 Generate** detailed recipes
        
        **🥗 Analyze** nutritional content
        
        **🌍 Explain** cultural background
        
        **💬 Answer** any food questions
        """)
        
        st.markdown("### 📸 Upload Tips")
        st.warning("""
        ✅ Clear, well-lit images work best
        
        ✅ Show the full dish if possible
        
        ✅ Avoid blurry or dark photos
        
        ✅ Supported: JPG, PNG, WEBP
        """)
        
        # Hardware info
        device = "🖥️ GPU" if torch.cuda.is_available() else "💻 CPU"
        st.markdown(f"### ⚡ Running on: {device}")

def main():
    """Main application function for Qwen version"""
    st.set_page_config(
        page_title="Qwen Food AI Analyzer",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .upload-area {
        border: 3px dashed #667eea;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    .upload-area:hover {
        border-color: #764ba2;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .analysis-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
    .qwen-button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .qwen-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .model-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create sidebar
    create_qwen_sidebar()
    
    # Main header
    st.markdown('<h1 class="main-header">🤖 Qwen Food AI Analyzer</h1>', unsafe_allow_html=True)
    
    # Model info banner
    st.markdown("""
    <div class="model-info">
        <h3>🧠 Powered by Qwen2.5-VL-7B-Instruct</h3>
        <p>Advanced Vision-Language Model for Food Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Warning about model loading
    st.warning("🔄 **First-time setup**: The model will download and load automatically (may take a few minutes)")
    
    # Check for Hugging Face token
    if not os.getenv("HUGGINGFACE_TOKEN"):
        st.error("🔑 **Hugging Face Token Required**: Please add your HUGGINGFACE_TOKEN to the .env file")
        st.info("💡 Get your token from: https://huggingface.co/settings/tokens")
        st.stop()
    
    # Main layout
    col1, col2 = st.columns([1.2, 1.8])
    
    with col1:
        st.markdown('<div class="upload-area">', unsafe_allow_html=True)
        st.subheader("📷 Upload Food Image")
        
        uploaded_file = st.file_uploader(
            "Choose your food image",
            type=['jpg', 'jpeg', 'png', 'webp'],
            help="Upload a clear image of any food item",
            label_visibility="collapsed"
        )
        
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="📸 Your Food Image", use_column_width=True)
                st.session_state.qwen_image = image
                st.success("✅ Image uploaded successfully!")
            except Exception as e:
                st.error(f"❌ Error loading image: {str(e)}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick analysis buttons
        if 'qwen_image' in st.session_state:
            st.subheader("⚡ Quick Analysis")
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("🔍 Identify Food", use_container_width=True, key="qwen_identify"):
                    st.session_state.qwen_action = "identify"
                if st.button("🥗 Nutrition Facts", use_container_width=True, key="qwen_nutrition"):
                    st.session_state.qwen_action = "nutrition"
            
            with col_btn2:
                if st.button("🍳 Get Recipe", use_container_width=True, key="qwen_recipe"):
                    st.session_state.qwen_action = "recipe"
                if st.button("📊 Full Analysis", use_container_width=True, key="qwen_comprehensive"):
                    st.session_state.qwen_action = "comprehensive"
    
    with col2:
        if 'qwen_image' in st.session_state:
            # Initialize analyzer
            if 'qwen_analyzer' not in st.session_state:
                st.session_state.qwen_analyzer = QwenFoodAnalyzer()
            
            analyzer = st.session_state.qwen_analyzer
            
            # Custom question section
            st.subheader("💬 Ask About Your Food")
            user_question = st.text_area(
                "What would you like to know?",
                placeholder="e.g., What spices are used? How healthy is this? Can I make this vegan?",
                height=100,
                help="Ask any question about the food in the image",
                key="qwen_question"
            )
            
            if st.button("🤖 Analyze Question", type="primary", use_container_width=True, key="qwen_analyze"):
                if user_question.strip():
                    with st.spinner("🧠 Qwen is analyzing your question..."):
                        result = analyzer.analyze_food_image(st.session_state.qwen_image, user_question)
                        st.markdown("### 🤖 Qwen AI Analysis")
                        st.markdown(f'<div class="analysis-card">{result}</div>', unsafe_allow_html=True)
                else:
                    st.warning("⚠️ Please enter a question first!")
            
            # Handle quick actions
            if hasattr(st.session_state, 'qwen_action'):
                action = st.session_state.qwen_action
                
                if action == "identify":
                    with st.spinner("🔍 Qwen is identifying the food..."):
                        result = analyzer.analyze_food_image(
                            st.session_state.qwen_image,
                            "What food is this? Describe its main components, cooking style, and likely origin."
                        )
                        st.markdown("### 🔍 Food Identification")
                        st.markdown(f'<div class="analysis-card">{result}</div>', unsafe_allow_html=True)
                
                elif action == "recipe":
                    with st.spinner("🍳 Qwen is generating the recipe..."):
                        result = analyzer.analyze_food_image(
                            st.session_state.qwen_image,
                            "Please provide a detailed recipe for this dish with ingredients and step-by-step instructions."
                        )
                        st.markdown("### 🍳 Recipe")
                        st.markdown(f'<div class="analysis-card">{result}</div>', unsafe_allow_html=True)
                
                elif action == "nutrition":
                    with st.spinner("🥗 Qwen is analyzing nutrition..."):
                        result = analyzer.analyze_food_image(
                            st.session_state.qwen_image,
                            "Provide detailed nutritional information including calories, macros, vitamins, and health benefits."
                        )
                        st.markdown("### 🥗 Nutritional Analysis")
                        st.markdown(f'<div class="analysis-card">{result}</div>', unsafe_allow_html=True)
                
                elif action == "comprehensive":
                    with st.spinner("📊 Qwen is performing comprehensive analysis..."):
                        result = analyzer.get_comprehensive_analysis(st.session_state.qwen_image)
                        st.markdown("### 📊 Comprehensive Analysis")
                        st.markdown(f'<div class="analysis-card">{result}</div>', unsafe_allow_html=True)
                
                # Clear the action after processing
                del st.session_state.qwen_action
        
        else:
            # Show example when no image is uploaded
            st.markdown("### 🌟 Example Questions for Qwen")
            st.markdown("""
            <div class="analysis-card">
            <h4>🍕 Food Identification</h4>
            <ul>
            <li>"What dish is this and where does it originate?"</li>
            <li>"What ingredients can you identify in this image?"</li>
            <li>"What cooking techniques were used here?"</li>
            </ul>
            </div>
            
            <div class="analysis-card">
            <h4>🍳 Advanced Cooking Queries</h4>
            <ul>
            <li>"How do I achieve this texture and color?"</li>
            <li>"What alternative ingredients could I use?"</li>
            <li>"What's the difficulty level of this recipe?"</li>
            </ul>
            </div>
            
            <div class="analysis-card">
            <h4>🥗 Detailed Nutrition</h4>
            <ul>
            <li>"Break down the macronutrients in this meal"</li>
            <li>"What vitamins and minerals are present?"</li>
            <li>"How does this fit into different dietary plans?"</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #888; font-size: 0.9rem;'>🤖 Powered by Qwen2.5-VL-7B-Instruct | Advanced AI Food Analysis</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
