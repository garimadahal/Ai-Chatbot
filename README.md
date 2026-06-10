🤖 AI Chatbot (TinyLlama + Tkinter)

A simple desktop AI chatbot built using Python Tkinter GUI and powered by TinyLlama running locally via Ollama API.

🚀 Features
🧠 Local AI responses using TinyLlama (no cloud API needed)
💬 Simple chat-style interface
🖥️ Desktop GUI built with Tkinter
⚡ Fast response using threading (no UI freezing)
⌨️ Press Enter to send messages
📜 Scrollable chat history
🛠️ Requirements

Make sure you have:

Python 3.8+
Ollama installed and running
TinyLlama model downloaded
Install dependencies:
pip install requests
📦 Setup Instructions
1. Install Ollama

Download and install Ollama:
👉 https://ollama.com

2. Pull TinyLlama model
ollama run tinyllama

or:

ollama pull tinyllama
3. Start Ollama server

Make sure Ollama is running locally:

http://localhost:11434
4. Run the chatbot
python your_file_name.py
🧑‍💻 How it works
User types a message in the GUI

Message is sent to local Ollama API:

http://localhost:11434/api/generate
TinyLlama generates a response
Response is displayed in the chat window
📁 Project Structure
ai-chatbot/
│
├── chatbot.py   # Main Python file (your script)
└── README.md
⚠️ Notes
This project works offline after model is installed
Make sure Ollama is running before starting the app
If the chatbot shows an error, check if port 11434 is active
💡 Future Improvements
Add chat memory (context history)
Add dark mode UI
Save chat logs
Support multiple models

Voice input/output
👩‍💻 Author
Garima
