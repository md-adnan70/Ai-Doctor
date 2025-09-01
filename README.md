🩺 AI Doctor – Intelligent Medical Assistant

AI Doctor is an intelligent, multimodal medical assistant that leverages state-of-the-art large language models (LLMs), speech recognition, and computer vision to provide an interactive diagnostic experience. Built with a user-friendly Gradio frontend and deployed via Docker, it offers an end-to-end AI health consultation platform.

🚀 Features

🧠 LLM-powered medical reasoning via Groq's Inference API

🗣️ Voice interaction using ElevenLabs Speech-to-Text API

👁️ Image-based diagnosis using Meta's Vision Model (Segment Anything, DINO, etc.)

🖥️ Web-based UI with Gradio

📦 Containerized deployment with Docker

🖼️ Demo

Add a demo GIF or screenshot here for a visual preview (optional but highly recommended).

🔧 Tech Stack
Component	Description
Frontend	Gradio
LLM Inference	Groq API
Speech-to-Text	ElevenLabs API
Vision Model	Meta AI Vision (e.g., SAM, DINO)
Deployment	Docker
🛠️ Installation
🔗 Prerequisites

Docker & Docker Compose

API keys for:

Groq Inference API

ElevenLabs

Meta’s Vision Model (or access to weights)

📦 Clone the Repo
git clone https://github.com/yourusername/ai-doctor.git
cd ai-doctor

⚙️ Environment Setup

Create a .env file and add your credentials:

GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
# Add any other required variables

🐳 Run with Docker
docker-compose up --build


Once running, access the app at: http://localhost:7860

🧠 How It Works

User Input: The user can speak or type symptoms/questions.

Speech Recognition: Audio is converted to text via ElevenLabs API.

Vision Analysis: Uploaded medical images are analyzed using Meta's vision models.

LLM Reasoning: All inputs are sent to a Groq-hosted LLM for diagnosis or suggestions.

Response Generation: The response is displayed and optionally spoken back to the user.

📁 Project Structure
ai-doctor/
│
├── app/                   # Main application logic
│   ├── llm_interface.py   # Handles interaction with Groq LLM
│   ├── vision_module.py   # Meta Vision integration
│   ├── speech_module.py   # ElevenLabs speech recognition
│   └── interface.py       # Gradio UI
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🧪 Sample Use Cases

Symptom checking & preliminary diagnosis

Analyzing skin images or medical scans

Conversational health Q&A

Audio-based medical consultations

⚠️ Disclaimer

This app is not a substitute for professional medical advice, diagnosis, or treatment. Always seek advice from a qualified healthcare provider.

📬 Contact

For feature requests or issues, please open an Issue
 or reach out via [email@example.com
].

📄 License

This project is licensed under the MIT License
.
