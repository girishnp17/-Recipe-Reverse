import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import io
import base64
from prompt import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class FoodAnalyzer:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def analyze_food_image(self, image, user_question):
        """
        Analyze food image and answer user questions
        """
        try:
            # Prepare the prompt with system instructions and user question
            prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_question}"
            
            # Generate response
            response = self.model.generate_content([prompt, image])
            return response.text
        
        except Exception as e:
            return f"Error analyzing image: {str(e)}"
    
    def get_recipe_suggestions(self, image):
        """
        Get recipe suggestions based on the food image
        """
        recipe_prompt = f"{SYSTEM_PROMPT}\n\nPlease provide a detailed recipe for this dish, including ingredients and step-by-step cooking instructions."
        
        try:
            response = self.model.generate_content([recipe_prompt, image])
            return response.text
        except Exception as e:
            return f"Error getting recipe: {str(e)}"
    
    def get_nutritional_info(self, image):
        """
        Get nutritional information about the food
        """
        nutrition_prompt = f"{SYSTEM_PROMPT}\n\nPlease provide detailed nutritional information for this food, including calories, macronutrients, vitamins, and health benefits."
        
        try:
            response = self.model.generate_content([nutrition_prompt, image])
            return response.text
        except Exception as e:
            return f"Error getting nutritional info: {str(e)}"

def main():
    st.set_page_config(
        page_title="🍽️ AI Food Analyzer",
        page_icon="🍽️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #4ecdc4;
        margin: 1rem 0;
    }
    .upload-section {
        border: 2px dashed #4ecdc4;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">🍽️ AI Food Analyzer</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Features")
        st.markdown("""
        ### What can I do?
        
        🔍 **Food Recognition**
        - Identify food items in images
        - Detect ingredients and cooking methods
        
        📝 **Recipe Generation**
        - Get step-by-step cooking instructions
        - Ingredient lists and measurements
        
        🥗 **Nutritional Analysis**
        - Calorie estimation
        - Macronutrient breakdown
        - Health benefits
        
        💬 **Interactive Q&A**
        - Ask any question about the food
        - Get detailed explanations
        """)
        
        st.markdown("---")
        st.markdown("### 📸 Supported Formats")
        st.markdown("JPG, JPEG, PNG, WEBP")
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        st.subheader("📷 Upload Food Image")
        
        uploaded_file = st.file_uploader(
            "Choose a food image...",
            type=['jpg', 'jpeg', 'png', 'webp'],
            help="Upload a clear image of food for analysis"
        )
        
        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Food Image", use_column_width=True)
            
            # Store image in session state
            st.session_state.uploaded_image = image
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("💬 Ask About Your Food")
        
        # Quick action buttons
        st.markdown("### Quick Actions")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            recipe_btn = st.button("🍳 Get Recipe", use_container_width=True)
        
        with col_btn2:
            nutrition_btn = st.button("🥗 Nutrition Info", use_container_width=True)
        
        with col_btn3:
            identify_btn = st.button("🔍 Identify Food", use_container_width=True)
        
        # Custom question input
        st.markdown("### Custom Question")
        user_question = st.text_area(
            "Ask anything about the food:",
            placeholder="e.g., How many calories does this have? What spices were used? Is this healthy?",
            height=100
        )
        
        analyze_btn = st.button("🤖 Analyze", type="primary", use_container_width=True)
    
    # Analysis section
    if 'uploaded_image' in st.session_state:
        analyzer = FoodAnalyzer()
        
        # Handle quick actions
        if recipe_btn:
            with st.spinner("🍳 Generating recipe..."):
                result = analyzer.get_recipe_suggestions(st.session_state.uploaded_image)
                st.markdown("### 🍳 Recipe")
                st.markdown(result)
        
        elif nutrition_btn:
            with st.spinner("🥗 Analyzing nutrition..."):
                result = analyzer.get_nutritional_info(st.session_state.uploaded_image)
                st.markdown("### 🥗 Nutritional Information")
                st.markdown(result)
        
        elif identify_btn:
            with st.spinner("🔍 Identifying food..."):
                result = analyzer.analyze_food_image(
                    st.session_state.uploaded_image,
                    "What food is this? Describe its ingredients, cooking method, and origin."
                )
                st.markdown("### 🔍 Food Identification")
                st.markdown(result)
        
        elif analyze_btn and user_question:
            with st.spinner("🤖 Analyzing your question..."):
                result = analyzer.analyze_food_image(st.session_state.uploaded_image, user_question)
                st.markdown("### 🤖 Analysis Result")
                st.markdown(result)
        
        elif analyze_btn and not user_question:
            st.warning("Please enter a question about the food.")
    
    else:
        # Show sample questions when no image is uploaded
        st.markdown("### 🌟 Sample Questions You Can Ask")
        st.markdown("""
        <div class="feature-card">
        <strong>🍕 About the Food:</strong><br>
        • "What dish is this?"<br>
        • "What ingredients can you identify?"<br>
        • "What cooking method was used?"
        </div>
        
        <div class="feature-card">
        <strong>🍳 Recipe Questions:</strong><br>
        • "How do I make this dish?"<br>
        • "What's the recipe for this?"<br>
        • "Can you suggest variations?"
        </div>
        
        <div class="feature-card">
        <strong>🥗 Health & Nutrition:</strong><br>
        • "How many calories does this have?"<br>
        • "Is this healthy?"<br>
        • "What nutrients does this provide?"
        </div>
        
        <div class="feature-card">
        <strong>🌍 Cultural & Origin:</strong><br>
        • "What cuisine is this from?"<br>
        • "What's the cultural significance?"<br>
        • "Are there similar dishes in other cultures?"
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666;'>Made with ❤️ using Gemini AI | Upload a food image to get started!</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    # Check if API key is configured
    if not os.getenv("GEMINI_API_KEY"):
        st.error("🔑 Please configure your GEMINI_API_KEY in the .env file")
        st.stop()
    
    main()
