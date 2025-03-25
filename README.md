# 📜 Text & Podcast Summarizer

## 🚀 Overview
This project is an AI-powered **text and podcast summarizer** that automatically generates short, insightful summaries from long-form content. It supports:
- 🎙️ **Podcast & Audio Summarization** (via OpenAI Whisper API)
- 📄 **Text Summarization** (via OpenAI LLM)
- 🎞️ **Video-to-Short Clips** (Auto-generates highlight reels)
- 📝 **Content Moderation** (via Google Perspective API)

## ⚡ Features
- 🎯 Extract key insights from **long audio, video, and text**
- ✂️ Automatically generate **5 short clips** from videos
- 🖼️ Generate **custom thumbnails** for social media
- 🔄 REST API with **FastAPI backend**
- 🚀 CLI tool for easy access
- ☁️ **Deployable on Heroku**

## 🛠️ Installation
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/text-podcast-summarizer.git
cd text-podcast-summarizer
```

### 2️⃣ Set up a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Usage
### 1️⃣ Run the FastAPI server
```sh
uvicorn main:app --reload
```
API will be available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2️⃣ Use the CLI Tool
```sh
python cli.py --input video.mp4 --output highlights/
```

### 3️⃣ Deploy to Heroku (Optional)
```sh
git push heroku main
```

## 📌 Tech Stack
- **Backend:** FastAPI, Python
- **AI APIs:** OpenAI Whisper, OpenAI GPT, Google Perspective API
- **Processing:** FFmpeg, MoviePy
- **Deployment:** Heroku, Docker (optional)

## 📜 License
This project is licensed under the MIT License.

## 🙌 Contributing
Pull requests are welcome! Feel free to submit an issue or feature request.

---
👨‍💻 Created by **Shanmukh** 🚀

