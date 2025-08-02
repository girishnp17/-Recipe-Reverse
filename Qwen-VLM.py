import streamlit as st
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from huggingface_hub import login
from PIL import Image
import torch

import streamlit as st
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from huggingface_hub import login
from PIL import Image
import torch

# Import the system prompt
from prompt import SYSTEM_PROMPT

class QwenFoodAnalyzer:
    def __init__(self):
        self.model = None
        self.processor = None
        self.model_loaded = False
        self.error_message = "Model not loaded. Please enter your HuggingFace token and wait for model initialization."
    
    def load_model(self, token):
        """Load the Qwen2VL model"""
        try:
            login(token)
            self.model = Qwen2VLForConditionalGeneration.from_pretrained(
                "Qwen/Qwen2-VL-7B-Instruct",
                torch_dtype="auto",
                device_map="auto",
                token=token
            )
            self.processor = AutoProcessor.from_pretrained(
                "Qwen/Qwen2-VL-7B-Instruct",
                token=token
            )
            self.model_loaded = True
            return True, "Model loaded successfully!"
        except Exception as e:
            self.model_loaded = False
            return False, f"Failed to load model: {str(e)}"
    
    def analyze_image(self, image, custom_prompt):
        """Analyze image with custom prompt"""
        if not self.model_loaded:
            return self.error_message
        
        try:
            full_prompt = f"{SYSTEM_PROMPT}\n\n{custom_prompt}"
            
            messages = [
                {"role": "user", "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": full_prompt},
                ]}
            ]
            
            # Prepare inputs
            text = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            image_inputs, video_inputs = process_vision_info(messages)
            inputs = self.processor(
                text=[text],
                images=image_inputs,
                videos=video_inputs,
                padding=True,
                return_tensors="pt"
            ).to("cuda" if torch.cuda.is_available() else "cpu")
            
            generated_ids = self.model.generate(**inputs, max_new_tokens=500)
            output_text = self.processor.batch_decode(
                generated_ids,
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False
            )[0]
            
            return output_text
            
        except Exception as e:
            return f"Error analyzing image: {str(e)}"
    
    def get_calorie_count(self, image):
        """Get calorie count of the food"""
        prompt = """IMPORTANT: Please provide ONLY the calorie information for the food in this image. Answer this specific question only:

"What is the calorie count of each food item visible in this image and what is the total calorie count?"

Please format your response as a clear table with:
- Food Item | Estimated Calories | Portion Size
- Then provide the total calories at the end

Make it clear and organized in a tabular format. Do not provide any other information."""
        
        return self.analyze_image(image, prompt)
    
    def get_ingredients(self, image):
        """Get ingredients needed to make the food"""
        prompt = """IMPORTANT: Please provide ONLY the ingredients list for the food in this image. Answer this specific question only:

"What are the ingredients needed to make this dish and in what approximate quantities?"

Please format your response as:
- Clear list of ingredients with quantities
- Organized by category (proteins, vegetables, spices, etc.)

Make it recipe-ready and well-organized. Do not provide any other information."""
        
        return self.analyze_image(image, prompt)
    
    def get_recipe(self, image):
        """Get detailed recipe for the food"""
        prompt = """IMPORTANT: Please provide ONLY a detailed recipe for the food in this image. Answer this specific question only:

"How do I make this dish step by step from start to finish?"

Please provide:
- Complete ingredients list with exact quantities
- Detailed step-by-step cooking instructions
- Cooking times and temperatures
- Equipment needed
- Pro tips for success

Make it a complete, detailed recipe that a beginner can follow. Do not provide any other information."""
        
        return self.analyze_image(image, prompt)

def main():
    # Enhanced page configuration
    st.set_page_config(
        page_title="Qwen Food Analyzer",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #dee2e6;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        border-left: 5px solid #667eea;
    }
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    .result-container {
        border-radius: 15px;
        border: 2px solid;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .calories-result {
        background-color: #e3f2fd;
        border-color: #2196f3;
        color: #0d47a1;
    }
    .ingredients-result {
        background-color: #e8f5e8;
        border-color: #4caf50;
        color: #1b5e20;
    }
    .recipe-result {
        background-color: #fff3e0;
        border-color: #ff9800;
        color: #e65100;
    }
    .custom-result {
        background-color: #f3e5f5;
        border-color: #9c27b0;
        color: #4a148c;
    }
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header with enhanced styling
    st.markdown('<h1 class="main-header">🤖 Qwen2.5-VL Food Analyzer</h1>', unsafe_allow_html=True)
    st.markdown("**Upload a food image and get detailed AI-powered analysis using advanced Vision-Language AI!**")
    
    # Initialize analyzer
    if 'analyzer' not in st.session_state:
        st.session_state.analyzer = QwenFoodAnalyzer()
    
    analyzer = st.session_state.analyzer
    
    # Authentication section
    st.markdown("### 🔐 Authentication")
    HF_TOKEN = st.text_input(
        "Enter your HuggingFace Access Token:",
        value="",
        type="password",
        help="Required to access the Qwen2.5-VL model from HuggingFace"
    )
    
    if HF_TOKEN and not analyzer.model_loaded:
        with st.spinner("🔄 Loading Qwen2.5-VL model... This may take a few minutes..."):
            success, message = analyzer.load_model(HF_TOKEN)
            if success:
                st.success(message)
            else:
                st.error(message)
    
    if analyzer.model_loaded:
        # Info banner
        st.info("✅ Qwen2.5-VL-7B-Instruct model loaded successfully! Ready for analysis.")
        
        # Image upload section
        st.markdown("### 📷 Upload Food Image")
        uploaded_file = st.file_uploader(
            "Choose a food image...",
            type=['jpg', 'jpeg', 'png', 'webp'],
            help="Upload clear, well-lit images for best results"
        )
        
        if uploaded_file is not None:
            # Store image in session state
            st.session_state.uploaded_image = Image.open(uploaded_file)
            
            # Display image
            st.image(st.session_state.uploaded_image, caption="Uploaded Food Image", use_column_width=True)
            
            # Analysis buttons
            st.markdown("### 🔍 Choose Analysis Type")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🔥 Get Calorie Count", use_container_width=True, help="Get detailed calorie breakdown"):
                    with st.spinner("🔍 Analyzing calories..."):
                        result = analyzer.get_calorie_count(st.session_state.uploaded_image)
                        st.session_state.calorie_result = result
                        st.success("Calorie analysis completed!")
            
            with col2:
                if st.button("🥬 Get Ingredients", use_container_width=True, help="Get complete ingredients list"):
                    with st.spinner("🔍 Identifying ingredients..."):
                        result = analyzer.get_ingredients(st.session_state.uploaded_image)
                        st.session_state.ingredients_result = result
                        st.success("Ingredients identified!")
            
            with col3:
                if st.button("👨‍🍳 Get Recipe", use_container_width=True, help="Get detailed cooking instructions"):
                    with st.spinner("🔍 Generating detailed recipe..."):
                        result = analyzer.get_recipe(st.session_state.uploaded_image)
                        st.session_state.recipe_result = result
                        st.success("Recipe generated!")
            
            # Custom question section
            st.markdown("### 💬 Ask Custom Question")
            custom_question = st.text_input(
                "Ask anything about this food:",
                placeholder="e.g., What cuisine is this? Is it healthy? How spicy is it?",
                help="Ask any specific question about the food image"
            )
            
            if st.button("🤔 Ask Question", use_container_width=True) and custom_question:
                with st.spinner("🔍 Analyzing your question..."):
                    result = analyzer.analyze_image(st.session_state.uploaded_image, custom_question)
                    st.session_state.custom_result = result
                    st.success("Analysis completed!")
            
            # Display results with enhanced styling
            if 'calorie_result' in st.session_state:
                st.markdown("### 🔥 Calorie Count Analysis")
                st.markdown(f'<div class="result-container calories-result">{st.session_state.calorie_result}</div>', unsafe_allow_html=True)
            
            if 'ingredients_result' in st.session_state:
                st.markdown("### 🥬 Ingredients List")
                st.markdown(f'<div class="result-container ingredients-result">{st.session_state.ingredients_result}</div>', unsafe_allow_html=True)
            
            if 'recipe_result' in st.session_state:
                st.markdown("### 👨‍🍳 Detailed Recipe")
                st.markdown(f'<div class="result-container recipe-result">{st.session_state.recipe_result}</div>', unsafe_allow_html=True)
            
            if 'custom_result' in st.session_state:
                st.markdown("### 💬 Custom Analysis")
                st.markdown(f'<div class="result-container custom-result">{st.session_state.custom_result}</div>', unsafe_allow_html=True)
        
        else:
            # Enhanced welcome section
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin: 1rem 0;">
                <h3>👆 Please upload a food image to get started!</h3>
                <p>Upload any food image and get instant AI-powered analysis</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Example section with enhanced styling
            st.markdown("### 🌟 What Qwen2.5-VL Can Do")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="feature-card">
                    <h4>🔥 Advanced Calorie Analysis</h4>
                    <ul>
                        <li>📊 Precise calorie calculations</li>
                        <li>📋 Professional nutritional breakdown</li>
                        <li>🍽️ Detailed portion analysis</li>
                        <li>📏 Scientific accuracy</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="feature-card">
                    <h4>🥬 Expert Ingredient Detection</h4>
                    <ul>
                        <li>📝 Comprehensive ingredients list</li>
                        <li>⚖️ Precise quantities</li>
                        <li>🗂️ Professional organization</li>
                        <li>🛒 Recipe-ready format</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="feature-card">
                    <h4>👨‍🍳 Professional Recipes</h4>
                    <ul>
                        <li>📋 Master-level instructions</li>
                        <li>🔥 Advanced cooking techniques</li>
                        <li>⏰ Precise timing and temps</li>
                        <li>👶 Beginner to expert guidance</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    else:
        # Authentication required section
        if not HF_TOKEN:
            st.warning("🔐 Please enter your HuggingFace access token to begin.")
            st.markdown("""
            ### How to get your token:
            1. Go to [HuggingFace](https://huggingface.co)
            2. Sign up/Login to your account
            3. Go to Settings → Access Tokens
            4. Create a new token with 'Read' permissions
            5. Copy and paste it above
            """)
    
    # Enhanced footer section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 15px; color: white; margin: 1rem 0;">
        <p style="font-size: 18px; margin: 0 0 0.5rem 0;"><strong>🤖 Qwen2.5-VL-7B-Instruct</strong> - Advanced Vision-Language AI</p>
        <p style="margin: 0; opacity: 0.9;">🧠 Powerful Analysis • 🎯 High Accuracy • 📱 Professional Results • 🔬 Scientific Precision</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

