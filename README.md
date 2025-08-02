# 🍽️ Advanced Culinary Food Analyzer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io/)
[![AI Models](https://img.shields.io/badge/AI-Gemini%20%7C%20Qwen%20%7C%20SmolVLM-yellow)](https://github.com/girishnp17/Recipe-Reverse)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive AI-powered food analysis application that combines multiple state-of-the-art vision-language models to provide detailed culinary insights. Upload any food image and get professional-grade analysis including ingredients, recipes, nutrition facts, and cultural context.

![Food Analyzer Demo](https://img.shields.io/badge/Status-Active-brightgreen)

## 🌟 Key Features

### 🔍 **Intelligent Food Recognition & Analysis**
- **Advanced Ingredient Detection**: Identify main ingredients, spices, seasonings, and garnishes with quantities
- **Professional Recipe Generation**: Step-by-step cooking instructions from prep to plating
- **Comprehensive Nutrition Analysis**: Detailed calorie breakdown, macronutrients, and health insights
- **Cultural & Culinary Context**: Cuisine origins, regional variations, and cultural significance
- **Smart Food Validation**: Automatically detects if uploaded image contains food items

### 🤖 **Multiple AI Model Options**
- **Gemini AI**: Cloud-based, fast, and efficient (Recommended)
- **Qwen2-VL-7B**: Advanced local model with superior accuracy
- **SmolVLM Models**: Lightweight options (256M & 2.2B parameters)

### 📊 **Professional Output Formats**
- **Structured Tables**: Ingredients, spices, and nutrition data in organized tables
- **Step-by-Step Guides**: Chronological cooking instructions with professional tips
- **Cultural Insights**: Historical context, regional variations, and food traditions

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/girishnp17/Recipe-Reverse.git
cd Recipe-Reverse
``` Analyzer

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

### 3. Configure API Keys (For Gemini Only)

Create a `.env` file in the project root:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

**Get Gemini API Key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and paste it into your `.env` file

### 4. Run the Application

Choose one of the three available interfaces:

#### Option 1: Gemini AI (Recommended - Cloud-based)
```bash
streamlit run gemini.py
```

#### Option 2: Qwen AI (Advanced - Local processing)
```bash
streamlit run Qwen-VLM.py
```

#### Option 3: SmolVLM AI (Lightweight - Multiple model options)
```bash
streamlit run Smol.py
```

The app will open in your browser at `http://localhost:8501`

## 📱 User Interface

### 🎯 **Main Application (Qwen-VLM.py & Smol.py)**
- **Smart Upload Area**: Drag & drop or click to upload food images
- **Four Analysis Buttons**:
  - 🥕 **Ingredients Analysis**: Detailed ingredient tables with quantities
  - 👨‍🍳 **Recipe & Instructions**: Complete cooking guide with pro tips
  - 🔢 **Calories & Nutrition**: Comprehensive nutritional breakdown
  - 💬 **Ask Questions**: Custom queries about the food
- **Model Selection** (Smol.py): Choose between three SmolVLM variants

### 🎨 **Simple Interface (gemini.py)**
- **Clean Upload Interface**: Streamlined design for quick analysis
- **Text-based Queries**: Ask any question about your food image
- **Instant Results**: Fast cloud-based processing

## 🏗️ Project Structure

```
Recipe-Reverse/
├── 📄 gemini.py              # Gemini AI interface (Cloud-based)
├── 📄 Qwen-VLM.py           # Qwen AI interface (Local processing)
├── 📄 Smol.py               # SmolVLM AI interface (Multi-model)
├── 📄 prompts.py            # Centralized AI prompts library
├── 📄 prompt.py             # Legacy prompt file
├── 📄 requirements.txt      # Python dependencies
├── 📄 README.md            # Project documentation
├── 📄 .env                 # Environment variables (create this)
└── 📁 __pycache__/         # Python cache files
```

## 🔧 Technical Architecture

### 🤖 **AI Models Comparison**

| Model | Size | Speed | Accuracy | Hardware | Internet |
|-------|------|-------|----------|----------|----------|
| **Gemini 1.5 Flash** | Cloud | ⚡ Fast | 🎯 High | 💻 Low | ✅ Required |
| **Qwen2-VL-7B** | 7B params | 🐌 Medium | 🎯 Very High | 🖥️ High | ❌ Optional |
| **SmolVLM-256M** | 256M params | ⚡ Very Fast | 🎯 Good | 💻 Low | ❌ No |
| **SmolVLM2-2.2B** | 2.2B params | 🐌 Medium | 🎯 High | 💻 Medium | ❌ No |

### 📋 **Advanced Prompt Engineering**

The application uses sophisticated, role-based prompts stored in `prompts.py`:

- **INGREDIENTS_SYSTEM_PROMPT**: World-class culinary analyst for ingredient identification
- **RECIPE_SYSTEM_PROMPT**: Master chef for complete recipe development
- **NUTRITION_SYSTEM_PROMPT**: Certified nutritionist for detailed analysis
- **GENERAL_FOOD_PROMPT**: Cultural food expert for custom queries
- **FOOD_VALIDATION_PROMPT**: Strict validator for food image detection

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
## 💡 Usage Examples

### 🥕 **Ingredients Analysis**
Get comprehensive ingredient breakdown in structured tables:
- Main ingredients with estimated quantities
- Spices, seasonings, and garnishes
- Cooking methods and cuisine classification
- Professional notes and alternatives

### �‍🍳 **Recipe Generation**
Complete cooking guidance from prep to plating:
- Detailed ingredient lists with measurements
- Step-by-step chronological instructions
- Equipment requirements and alternatives
- Pro tips and creative variations
- Dietary notes and substitutions

### 🔢 **Nutrition Analysis**
Scientific nutritional breakdown:
- Per-item calorie calculations
- Macronutrient profiles (carbs, proteins, fats)
- Micronutrient analysis and health benefits
- Cooking method impact assessment
- Healthier preparation alternatives

### 💬 **Custom Questions**
Ask anything about the food:
- Cultural origins and historical context
- Regional variations and traditions
- Dietary adaptations and substitutions
- Cooking techniques and equipment
- Pairing suggestions and serving ideas

## 📊 Supported Features

### 🖼️ **Image Formats**
- **JPEG/JPG**: Standard photo format
- **PNG**: High-quality images with transparency
- **WEBP**: Modern, efficient format

### � **Analysis Types**
- **Food Validation**: Automatic detection of food items
- **Ingredient Recognition**: Comprehensive ingredient identification
- **Recipe Reconstruction**: Complete cooking instructions
- **Nutritional Assessment**: Detailed health and calorie analysis
- **Cultural Context**: Cuisine origins and traditions

### 🎛️ **Model Selection** (Smol.py)
- **SmolVLM-256M**: Ultra-fast, lightweight processing
- **SmolVLM2-2.2B**: Balanced performance and accuracy
- **Qwen2-VL-7B**: Maximum accuracy and detail

## 🔐 Security & Privacy

- **Local Processing**: Qwen and SmolVLM models run entirely offline
- **Secure API Keys**: Environment variables for safe key storage
- **No Data Retention**: Images processed temporarily, not stored
- **Privacy Options**: Choose between cloud and local processing

## 🛠️ Installation Requirements

### **Hardware Requirements**

| Model | RAM | GPU | Storage | Internet |
|-------|-----|-----|---------|----------|
| Gemini | 2GB | No | Minimal | Required |
| SmolVLM-256M | 4GB | Optional | 1GB | No |
| SmolVLM2-2.2B | 6GB | Recommended | 5GB | No |
| Qwen2-VL-7B | 16GB | Required | 15GB | No |

### **Software Dependencies**
- Python 3.8 or higher
- CUDA-compatible GPU (optional for SmolVLM, required for Qwen)
- Modern web browser for Streamlit interface

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 **Bug Reports**
- Use GitHub Issues to report bugs
- Include screenshots and error messages
- Describe steps to reproduce the issue

### ✨ **Feature Requests**
- Suggest new AI models or analysis types
- Propose UI/UX improvements
- Request additional output formats

### 🔧 **Development**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### **Common Issues & Solutions**

#### 🔑 **API Configuration**
```bash
# Gemini API key error
echo "GEMINI_API_KEY=your_key_here" > .env
```

#### 📦 **Dependencies**
```bash
# Install requirements
pip install -r requirements.txt
# Upgrade if needed
pip install --upgrade streamlit transformers torch
```

#### 🖼️ **Image Upload Issues**
- Supported formats: JPG, PNG, WEBP only
- Maximum file size: 10MB recommended
- Ensure image contains visible food items

#### 🤖 **Model Loading Problems**
```bash
# For Qwen model issues
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
# Check available GPU memory
nvidia-smi
```

### **Performance Optimization**
- **For slow processing**: Use Gemini or SmolVLM-256M
- **For better accuracy**: Use Qwen2-VL-7B with GPU
- **For offline use**: Use SmolVLM models
- **For cloud usage**: Use Gemini with API key

## 🌟 Acknowledgments

### **AI Models & Frameworks**
- [Google Gemini](https://deepmind.google/technologies/gemini/) - Advanced multimodal AI
- [Qwen-VL](https://github.com/QwenLM/Qwen-VL) - Open-source vision-language model
- [SmolVLM](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct) - Efficient vision-language models
- [Streamlit](https://streamlit.io/) - Rapid web app development
- [Hugging Face](https://huggingface.co/) - Model hosting and transformers library

### **Development Tools**
- [Python](https://python.org/) - Core programming language
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [PIL/Pillow](https://pillow.readthedocs.io/) - Image processing

---

## 🚀 **Ready to Analyze Food?**

1. **Clone** the repository
2. **Install** dependencies 
3. **Configure** your API key (optional)
4. **Run** your preferred interface
5. **Upload** a food image
6. **Discover** the magic of AI culinary analysis!

**Made with ❤️ by the open-source community**

*Transform any food image into detailed culinary insights with the power of AI!*
