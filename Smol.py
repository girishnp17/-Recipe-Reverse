import streamlit as st
from transformers import pipeline
from PIL import Image
import os
from dotenv import load_dotenv
import io
import base64
from prompt import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

class SmolFoodAnalyzer:
    def __init__(self):
        """Initialize the SmolVLM food analyzer"""
        try:
            # Initialize the pipeline with CPU device
            self.pipe = pipeline(
                "image-text-to-text", 
                model="HuggingFaceTB/SmolVLM-Instruct",
                device=-1  # Force CPU usage (-1 means CPU, 0+ means GPU)
            )
            self.model_loaded = True
        except Exception as e:
            self.model_loaded = False
            self.error_message = f"Error loading model: {str(e)}"
    
    def get_calorie_count(self, image):
        """Get calorie count of all food items in the image in tabular format"""
        if not self.model_loaded:
            return self.error_message
        
        try:
            # Convert PIL image to base64 for the pipeline
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            img_url = f"data:image/jpeg;base64,{img_str}"
            
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "url": img_url},
                        {"type": "text", "text": f"""{SYSTEM_PROMPT}

IMPORTANT: Please provide ONLY the calorie information for the food in this image. Answer this specific question only:

"What is the calorie count of each food item visible in this image and what is the total calorie count?"

Please format your response as a clear table with:
- Food Item | Estimated Calories | Portion Size
- Then provide the total calories at the end

Make it clear and organized in a tabular format. Do not provide any other information."""}
                    ]
                }
            ]
            
            result = self.pipe(messages)
            return result[0]['generated_text'] if result else "No response generated"
            
        except Exception as e:
            return f"Error getting calorie count: {str(e)}"
    
    def get_ingredients(self, image):
        """Get ingredients needed to make the food"""
        if not self.model_loaded:
            return self.error_message
        
        try:
            # Convert PIL image to base64 for the pipeline
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            img_url = f"data:image/jpeg;base64,{img_str}"
            
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "url": img_url},
                        {"type": "text", "text": f"""{SYSTEM_PROMPT}

IMPORTANT: Please provide ONLY the ingredients information. Answer this specific question only:

"What are all the ingredients needed to make this dish?"

Please list only the ingredients with approximate quantities in a clear, organized format. Do not provide cooking instructions or other information."""}
                    ]
                }
            ]
            
            result = self.pipe(messages)
            return result[0]['generated_text'] if result else "No response generated"
            
        except Exception as e:
            return f"Error getting ingredients: {str(e)}"
    
    def get_recipe(self, image):
        """Get detailed recipe for the food"""
        if not self.model_loaded:
            return self.error_message
        
        try:
            # Convert PIL image to base64 for the pipeline
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            img_url = f"data:image/jpeg;base64,{img_str}"
            
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "url": img_url},
                        {"type": "text", "text": f"""{SYSTEM_PROMPT}

IMPORTANT: Please provide ONLY a detailed, comprehensive recipe. Answer this specific question only:

"What is the complete step-by-step recipe to make this dish from start to finish?"

Please provide a CLEAR and DETAILED process with:

**INGREDIENTS:**
- Complete ingredients list with exact quantities

**PREPARATION STEPS:**
1. Detailed prep work (washing, chopping, measuring, etc.)
2. Equipment setup and preparation

**COOKING PROCESS:**
1. Step 1: [Clear instruction with time and temperature]
2. Step 2: [Clear instruction with time and temperature]
3. Continue with each step clearly numbered
4. Include cooking times, temperatures, and visual cues

**FINISHING & SERVING:**
- Final touches and presentation
- Serving suggestions and portion size

Make each step crystal clear so a complete beginner can follow successfully. Do not provide calorie information or other details."""}
                    ]
                }
            ]
            
            result = self.pipe(messages)
            return result[0]['generated_text'] if result else "No response generated"
            
        except Exception as e:
            return f"Error getting recipe: {str(e)}"
    
    def analyze_food_image(self, image, user_question):
        """Analyze food image and answer only the specific user question"""
        if not self.model_loaded:
            return self.error_message
        
        try:
            # Convert PIL image to base64 for the pipeline
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            img_url = f"data:image/jpeg;base64,{img_str}"
            
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "url": img_url},
                        {"type": "text", "text": f"""{SYSTEM_PROMPT}

IMPORTANT: The user has asked a specific question. Please answer ONLY that question directly and concisely. Do not provide additional information unless specifically requested.

User Question: {user_question}

Please provide a focused answer to this question only."""}
                    ]
                }
            ]
            
            result = self.pipe(messages)
            return result[0]['generated_text'] if result else "No response generated"
            
        except Exception as e:
            return f"Error analyzing image: {str(e)}"

def main():
    st.set_page_config(
        page_title="🤖 SmolVLM Food Analyzer",
        page_icon="🤖",
        layout="centered"
    )
    
    # Add custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
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
    
    # Simple header with enhanced styling
    st.markdown('<h1 class="main-header">🤖 SmolVLM Food Analyzer</h1>', unsafe_allow_html=True)
    st.markdown("**Upload a food image and get detailed AI-powered analysis!**")
    
    # Info banner
    st.info("💡 Using HuggingFace SmolVLM-Instruct model for advanced food analysis")
    
    # Image upload section
    st.markdown("### 📷 Upload Food Image")
    uploaded_file = st.file_uploader(
        "Choose a food image...",
        type=['jpg', 'jpeg', 'png', 'webp'],
        help="Upload clear, well-lit images for best results"
    )
    
    # Display uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Food Image", use_column_width=True)
        st.session_state.uploaded_image = image
        
        # Initialize analyzer
        if 'smol_analyzer' not in st.session_state:
            with st.spinner("Loading SmolVLM model..."):
                st.session_state.smol_analyzer = SmolFoodAnalyzer()
        
        analyzer = st.session_state.smol_analyzer
        
        # Check if model loaded successfully
        if not analyzer.model_loaded:
            st.error(f"❌ Model loading failed: {analyzer.error_message}")
            st.stop()
        
        # Three main sections with enhanced styling
        st.markdown("### 🎯 Analysis Options")
        st.markdown("Click any button below to get specific analysis:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔥 Get Calories", use_container_width=True, help="Get detailed calorie breakdown in tabular format"):
                with st.spinner("🔍 Calculating calories..."):
                    result = analyzer.get_calorie_count(st.session_state.uploaded_image)
                    st.session_state.calorie_result = result
                    st.success("Calorie analysis completed!")
        
        with col2:
            if st.button("🥬 Get Ingredients", use_container_width=True, help="Get complete ingredients list with quantities"):
                with st.spinner("🔍 Identifying ingredients..."):
                    result = analyzer.get_ingredients(st.session_state.uploaded_image)
                    st.session_state.ingredients_result = result
                    st.success("Ingredients identified!")
        
        with col3:
            if st.button("👨‍🍳 Get Recipe", use_container_width=True, help="Get detailed step-by-step cooking instructions"):
                with st.spinner("🔍 Generating detailed recipe..."):
                    result = analyzer.get_recipe(st.session_state.uploaded_image)
                    st.session_state.recipe_result = result
                    st.success("Recipe generated!")
        
        # Display results
        if 'calorie_result' in st.session_state:
            st.markdown("### 🔥 Calorie Count Analysis")
            
            # Create a nice container for the calorie results
            with st.container():
                st.markdown("""
                <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #ff6b6b;">
                """, unsafe_allow_html=True)
                
                # Parse and format the calorie result
                calorie_text = st.session_state.calorie_result
                st.markdown(f"**📊 Nutritional Breakdown:**")
                st.markdown(calorie_text)
                
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")
        
        if 'ingredients_result' in st.session_state:
            st.markdown("### 🥬 Required Ingredients")
            
            # Create a nice container for ingredients
            with st.container():
                st.markdown("""
                <div style="background-color: #f0fff0; padding: 20px; border-radius: 10px; border-left: 5px solid #4caf50;">
                """, unsafe_allow_html=True)
                
                st.markdown(f"**🛒 Shopping List:**")
                ingredients_text = st.session_state.ingredients_result
                st.markdown(ingredients_text)
                
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")
        
        if 'recipe_result' in st.session_state:
            st.markdown("### 👨‍🍳 Step-by-Step Recipe")
            
            # Create a nice container for recipe
            with st.container():
                st.markdown("""
                <div style="background-color: #fff8f0; padding: 20px; border-radius: 10px; border-left: 5px solid #ff9800;">
                """, unsafe_allow_html=True)
                
                st.markdown(f"**📋 Cooking Instructions:**")
                recipe_text = st.session_state.recipe_result
                
                # Split recipe into sections if possible
                if "INGREDIENTS:" in recipe_text and "PREPARATION" in recipe_text:
                    # Try to format the recipe nicely
                    sections = recipe_text.split("**")
                    formatted_recipe = ""
                    for section in sections:
                        if section.strip():
                            formatted_recipe += f"**{section}**" if not section.startswith("**") else section
                    st.markdown(formatted_recipe)
                else:
                    st.markdown(recipe_text)
                
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")
        
        # Custom question section
        st.subheader("💬 Ask Your Own Question")
        user_question = st.text_area(
            "What else would you like to know about this food?",
            placeholder="e.g., Is this healthy? What cuisine is this? Can I make this vegan?",
            height=100
        )
        
        # Custom question analyze button
        if st.button("🤖 Ask Custom Question", type="primary", use_container_width=True):
            if user_question:
                with st.spinner("Analyzing your question..."):
                    result = analyzer.analyze_food_image(st.session_state.uploaded_image, user_question)
                    
                    # Display custom analysis with nice formatting
                    st.markdown("### 🤖 AI Analysis Response")
                    with st.container():
                        st.markdown("""
                        <div style="background-color: #f5f5ff; padding: 20px; border-radius: 10px; border-left: 5px solid #6c5ce7;">
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"**❓ Your Question:** {user_question}")
                        st.markdown(f"**🤖 AI Response:**")
                        st.markdown(result)
                        
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error("Please enter a question.")
    
    else:
        # Enhanced welcome section
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin: 1rem 0;">
            <h3>👆 Please upload a food image to get started!</h3>
            <p>Upload any food image and get instant AI-powered analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Example section with enhanced styling
        st.markdown("### 🌟 What SmolVLM Can Do")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="feature-card">
                <h4>🔥 Calorie Analysis</h4>
                <ul>
                    <li>📊 Detailed calorie breakdown</li>
                    <li>📋 Tabular format for clarity</li>
                    <li>🍽️ Per-item and total calories</li>
                    <li>📏 Portion size estimates</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
                <h4>🥬 Ingredient Detection</h4>
                <ul>
                    <li>📝 Complete ingredients list</li>
                    <li>⚖️ Approximate quantities</li>
                    <li>🗂️ Clear organization</li>
                    <li>🛒 Recipe-ready format</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="feature-card">
                <h4>👨‍🍳 Detailed Recipes</h4>
                <ul>
                    <li>📋 Step-by-step instructions</li>
                    <li>🔥 Clear cooking process</li>
                    <li>⏰ Times and temperatures</li>
                    <li>👶 Beginner-friendly format</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Enhanced footer section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 15px; color: white; margin: 1rem 0;">
        <p style="font-size: 18px; margin: 0 0 0.5rem 0;"><strong>🤖 SmolVLM-Instruct</strong> - Lightweight Vision-Language AI</p>
        <p style="margin: 0; opacity: 0.9;">📱 CPU Optimized • 🚀 Fast Analysis • 🎯 Accurate Results • 💡 Easy to Use</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
