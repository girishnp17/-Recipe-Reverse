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
    
    def get_calorie_count(self, image):
        """Get calorie count of all food items in the image"""
        try:
            prompt = f"""{SYSTEM_PROMPT}

IMPORTANT: Please provide ONLY the calorie information for the food in this image. Answer this specific question only:

"What is the calorie count of each food item visible in this image and what is the total calorie count?"

Please list each food item with its estimated calories and provide the total calories. Do not provide any other information."""
            
            response = self.model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            return f"Error getting calorie count: {str(e)}"
    
    def get_ingredients(self, image):
        """Get ingredients needed to make the food"""
        try:
            prompt = f"""{SYSTEM_PROMPT}

IMPORTANT: Please provide ONLY the ingredients information. Answer this specific question only:

"What are all the ingredients needed to make this dish?"

Please list only the ingredients with approximate quantities. Do not provide cooking instructions or other information."""
            
            response = self.model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            return f"Error getting ingredients: {str(e)}"
    
    def get_recipe(self, image):
        """Get recipe for the food"""
        try:
            prompt = f"""{SYSTEM_PROMPT}

IMPORTANT: Please provide ONLY a detailed, comprehensive recipe. Answer this specific question only:

"What is the complete step-by-step recipe to make this dish from start to finish?"

Please provide:
1. Complete ingredients list with exact quantities
2. Detailed preparation steps (prep work, chopping, etc.)
3. Step-by-step cooking instructions from beginning to end
4. Cooking times and temperatures
5. Tips for best results and presentation
6. Serving suggestions

Make it detailed enough for a beginner to follow successfully. Do not provide calorie information or other details."""
            
            response = self.model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            return f"Error getting recipe: {str(e)}"
    
    def analyze_food_image(self, image, user_question):
        """
        Analyze food image and answer only the specific user question
        """
        try:
            # Use system prompt but focus only on the user's question
            prompt = f"""{SYSTEM_PROMPT}

IMPORTANT: The user has asked a specific question. Please answer ONLY that question directly and concisely. Do not provide additional information unless specifically requested.

User Question: {user_question}

Please provide a focused answer to this question only."""
            
            # Generate response
            response = self.model.generate_content([prompt, image])
            return response.text
        
        except Exception as e:
            return f"Error analyzing image: {str(e)}"

def main():
    st.set_page_config(
        page_title="🍽️ AI Food Analyzer",
        page_icon="🍽️",
        layout="centered"
    )
    
    # Simple header
    st.title("🍽️ AI Food Analyzer")
    st.markdown("Upload a food image and get detailed analysis!")
    
    # Image upload section
    st.subheader("📷 Upload Food Image")
    uploaded_file = st.file_uploader(
        "Choose a food image...",
        type=['jpg', 'jpeg', 'png', 'webp']
    )
    
    # Display uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Food Image", use_container_width=True)
        st.session_state.uploaded_image = image
        
        # Initialize analyzer
        analyzer = FoodAnalyzer()
        
        # Three main sections
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔥 Get Calories", use_container_width=True):
                with st.spinner("Calculating calories..."):
                    result = analyzer.get_calorie_count(st.session_state.uploaded_image)
                    st.session_state.calorie_result = result
        
        with col2:
            if st.button("🥬 Get Ingredients", use_container_width=True):
                with st.spinner("Identifying ingredients..."):
                    result = analyzer.get_ingredients(st.session_state.uploaded_image)
                    st.session_state.ingredients_result = result
        
        with col3:
            if st.button("👨‍🍳 Get Recipe", use_container_width=True):
                with st.spinner("Generating recipe..."):
                    result = analyzer.get_recipe(st.session_state.uploaded_image)
                    st.session_state.recipe_result = result
        
        # Display results
        if 'calorie_result' in st.session_state:
            st.markdown("### 🔥 Calorie Count")
            st.markdown(st.session_state.calorie_result)
            st.markdown("---")
        
        if 'ingredients_result' in st.session_state:
            st.markdown("### 🥬 Ingredients")
            st.markdown(st.session_state.ingredients_result)
            st.markdown("---")
        
        if 'recipe_result' in st.session_state:
            st.markdown("### 👨‍🍳 Recipe")
            st.markdown(st.session_state.recipe_result)
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
                    st.markdown("### 🤖 Custom Analysis")
                    st.markdown(result)
            else:
                st.error("Please enter a question.")
    
    else:
        st.info("👆 Please upload a food image to get started!")
    
    # Simple footer
    st.markdown("---")
    st.markdown("*Made with ❤️ using Gemini AI*")

if __name__ == "__main__":
    # Check if API key is configured
    if not os.getenv("GEMINI_API_KEY"):
        st.error("🔑 Please configure your GEMINI_API_KEY in the .env file")
        st.stop()
    
    main()
