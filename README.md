# 🍽️ AI Food Analyzer

A simple and powerful food analysis application powe## 📱 How to Use

**Super Simple Interface with 4 Main Features:**

1. **📷 Upload Image**: Click the upload area and select a food image (JPG, PNG, WEBP)
2. **🔥 Get Calories**: Click to get detailed calorie breakdown of all food items
3. **� Get Ingredients**: Click to get complete ingredients list with quantities
4. **👨‍🍳 Get Recipe**: Click to get detailed step-by-step cooking instructions from start to finish
5. **💬 Ask Custom Questions**: Type any specific question about the food in the text box

**Each analysis is focused and detailed - no overwhelming information, just what you need!**advanced AI models. Upload any food image and ask questions to get detailed information about recipes, nutrition, ingredients, and more!

![Food Analyzer Demo](https://img.shields.io/badge/AI-Food%20Analyzer-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![AI Models](https://img.shields.io/badge/AI-Gemini%20%7C%20Qwen-yellow)

## 🌟 Features

### 🔍 **Smart Food Recognition**
- Accurately identify food items from images
- Detect ingredients and cooking methods
- Recognize cuisine types and cultural origins

### 📝 **Recipe Generation**
- Get detailed step-by-step cooking instructions
- Complete ingredient lists with measurements
- Cooking tips and variations

### 🥗 **Advanced Nutritional Analysis**
- Precise calorie estimation per serving
- Complete macronutrient breakdown (proteins, carbs, fats)
- Micronutrient analysis (vitamins, minerals, antioxidants)
- Health benefits and dietary considerations
- Portion size analysis and cooking method impact

### 💬 **Simple Interactive Interface**
- Just upload an image and ask any question
- Clean, minimal interface without complexity
- Instant AI-powered responses

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

### 3. Configure API Keys

#### For Gemini AI:
1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file and add:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

#### For Qwen AI (Optional):
1. Get your Hugging Face token from [Hugging Face](https://huggingface.co/settings/tokens)
2. Add to your `.env` file:
   ```
   HUGGINGFACE_TOKEN=your_huggingface_token_here
   ```

### 4. Run the Application

#### Option 1: Gemini AI (Recommended)
```bash
streamlit run gemini.py
```

#### Option 2: Qwen AI (Advanced)
```bash
streamlit run Qwen-VLM.py
```

#### Option 3: SmolVLM AI (Lightweight)
```bash
streamlit run Smol.py
```

The app will open in your browser at `http://localhost:8501`

## 📱 How to Use

**Simple 3-Step Process:**

1. **📷 Upload Image**: Click the upload area and select a food image (JPG, PNG, WEBP)
2. **� Ask Question**: Type any question about the food in the text box
3. **🤖 Get Analysis**: Click "Analyze" to receive detailed, expert-level responses

### Example Questions You Can Ask:

### Recipe & Cooking
- "How do I make this dish step by step?"
- "What cooking techniques are used here?"
- "Can you suggest variations or substitutions?"
- "What equipment do I need?"

### Nutrition & Health
- "How many calories are in each item?"
- "What's the total calorie count?"
- "Is this healthy for my diet?"
- "What nutrients does this provide?"

### Cultural & Origin
- "What cuisine is this from?"
- "What's the cultural significance?"
- "Are there similar dishes from other regions?"

## 🏗️ Project Structure

```
Week-End-Project/
├── gemini.py            # Simple Gemini AI interface (Recommended)
├── Qwen-VLM.py         # Simple Qwen AI interface (Advanced)
├── Smol.py             # SmolVLM AI interface (Lightweight)
├── prompt.py            # Enhanced system prompt for AI models
├── requirements.txt     # Python dependencies
├── .env                # Your API keys (create this)
├── README.md           # This file
```

## 🔧 Technical Details

### Technologies Used
- **Frontend**: Streamlit (Simple and clean interface)
- **AI Models**: 
  - Google Gemini 1.5 Flash (Vision + Language) - Recommended
  - Qwen2.5-VL-7B-Instruct (Advanced Vision-Language Model)
- **Image Processing**: PIL (Python Imaging Library)
- **Environment**: Python-dotenv for configuration

### Why Three AI Models?

#### 🟢 **Gemini AI (gemini.py)** - Recommended for most users
- Cloud-based, no local model download required
- Fast response times
- Excellent food analysis capabilities
- Lower hardware requirements

#### 🔵 **Qwen AI (Qwen-VLM.py)** - For advanced users
- Runs locally on your machine
- More privacy (no data sent to cloud)
- Requires powerful hardware (8GB+ RAM, GPU recommended)
- First run downloads ~15GB model

#### 🟡 **SmolVLM AI (Smol.py)** - Lightweight option
- Uses HuggingFace SmolVLM-Instruct model
- Balanced performance and resource usage
- Good for detailed recipe analysis
- Tabular calorie format
- No API keys required (uses transformers)

## 🎨 Simple Interface Design

All three interfaces feature the same minimal design:
- **Upload Box**: Simply drag and drop or click to upload food images
- **Three Main Buttons**: Get Calories (tabular format), Get Ingredients, Get Recipe (detailed process)
- **Custom Question Box**: Type any specific question about the food
- **Clean Results**: Easy-to-read analysis without clutter

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

**Gemini API Key Error**
- Ensure your Gemini API key is correctly set in `.env`
- Verify the key is valid and has appropriate permissions

**Qwen/Hugging Face Token Error**
- Ensure your Hugging Face token is correctly set in `.env`
- Verify you have access to the Qwen model

**Image Upload Issues**
- Check file format (JPG, PNG, WEBP only)
- Ensure image file size is reasonable (<10MB)
- Try with a different image

**Dependencies Error**
- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.8 or higher

**Qwen Model Loading Issues**
- Ensure you have enough RAM (8GB+ recommended)
- First-time model download may take time
- Check your internet connection for model download

### Getting Help

If you encounter issues:
1. Check the console for error messages
2. Verify all dependencies are installed
3. Ensure your API key is configured correctly
4. Open an issue on GitHub with details

## 🌟 Acknowledgments

- Google AI for the Gemini API
- Qwen team for the open-source VLM model
- Hugging Face for model hosting and transformers
- Streamlit team for the amazing framework
- The open-source community for inspiration

---

**Made with ❤️ using AI and modern web technologies**

*Upload a food image and discover the magic of AI-powered culinary analysis!*
