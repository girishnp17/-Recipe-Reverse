# 🍽️ AI Food Analyzer

An intelligent food analysis application powered by Google's Gemini Vision Language Model. Upload food images and get detailed information about recipes, nutrition, ingredients, and more!

![Food Analyzer Demo](https://img.shields.io/badge/AI-Food%20Analyzer-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-yellow)

## 🌟 Features

### 🔍 **Smart Food Recognition**
- Accurately identify food items from images
- Detect ingredients and cooking methods
- Recognize cuisine types and cultural origins

### 📝 **Recipe Generation**
- Get detailed step-by-step cooking instructions
- Complete ingredient lists with measurements
- Cooking tips and variations

### 🥗 **Nutritional Analysis**
- Calorie estimation per serving
- Macronutrient breakdown (proteins, carbs, fats)
- Vitamin and mineral content
- Health benefits and dietary considerations

### 💬 **Interactive Q&A**
- Ask custom questions about any food
- Get expert culinary advice
- Cultural and historical food information

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Week-End-Project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Add your API key to `.env`:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 4. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📱 How to Use

1. **Upload Image**: Click the upload area and select a food image (JPG, PNG, WEBP)
2. **Choose Analysis Type**:
   - 🍳 **Get Recipe**: Detailed cooking instructions
   - 🥗 **Nutrition Info**: Calorie and nutrient analysis
   - 🔍 **Identify Food**: Basic food identification
3. **Ask Custom Questions**: Type any question about the food
4. **Get AI Analysis**: Receive detailed, expert-level responses

## 🍕 Example Questions

### Recipe & Cooking
- "How do I make this dish?"
- "What ingredients do I need?"
- "Can you suggest variations?"
- "What's the cooking time?"

### Nutrition & Health
- "How many calories does this have?"
- "Is this healthy?"
- "What nutrients does this provide?"
- "Any dietary considerations?"

### Cultural & Origin
- "What cuisine is this from?"
- "What's the cultural significance?"
- "Are there similar dishes?"

## 🏗️ Project Structure

```
Week-End-Project/
├── app.py                 # Main Streamlit application
├── prompt.py             # System prompt for Gemini model
├── requirements.txt      # Python dependencies
├── .env                 # Your API keys (create this)
├── README.md           # This file
```

## 🔧 Technical Details

### Technologies Used
- **Frontend**: Streamlit for web interface
- **AI Model**: Google Gemini 1.5 Flash (Vision + Language)
- **Image Processing**: PIL (Python Imaging Library)
- **Environment**: Python-dotenv for configuration

### Key Components

#### `FoodAnalyzer` Class
- Handles all interactions with Gemini API
- Processes images and generates responses
- Provides specialized methods for different analysis types

#### System Prompt (`prompt.py`)
- Comprehensive instructions for the AI model
- Defines expertise areas and response formats
- Ensures consistent, high-quality responses

#### Streamlit UI
- Clean, intuitive interface
- Responsive design with custom CSS
- Real-time image upload and analysis

## 🎨 Features in Detail

### Advanced Food Recognition
The AI can identify:
- Main dishes and side items
- Cooking techniques (grilled, fried, baked, etc.)
- Visible ingredients and seasonings
- Cuisine type and cultural origin
- Presentation style and plating

### Comprehensive Nutritional Analysis
Get detailed information about:
- Realistic calorie estimates
- Macronutrient breakdown
- Vitamin and mineral content
- Health benefits and considerations
- Portion size analysis

### Expert Recipe Generation
Receive professional-quality recipes with:
- Complete ingredient lists
- Step-by-step instructions
- Prep and cooking times
- Equipment requirements
- Tips and variations

## 📊 Supported Image Formats

- **JPEG/JPG**: Standard photo format
- **PNG**: High-quality images with transparency
- **WEBP**: Modern, efficient format

## 🔐 Security & Privacy

- API keys are stored securely in environment variables
- Images are processed temporarily and not stored
- No personal data is collected or retained

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**API Key Error**
- Ensure your Gemini API key is correctly set in `.env`
- Verify the key is valid and has appropriate permissions

**Image Upload Issues**
- Check file format (JPG, PNG, WEBP only)
- Ensure image file size is reasonable (<10MB)
- Try with a different image

**Dependencies Error**
- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.8 or higher

### Getting Help

If you encounter issues:
1. Check the console for error messages
2. Verify all dependencies are installed
3. Ensure your API key is configured correctly
4. Open an issue on GitHub with details

## 🌟 Acknowledgments

- Google AI for the Gemini API
- Streamlit team for the amazing framework
- The open-source community for inspiration

---

**Made with ❤️ using AI and modern web technologies**

*Upload a food image and discover the magic of AI-powered culinary analysis!*
