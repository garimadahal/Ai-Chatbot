import tkinter as tk
from tkinter import scrolledtext
import requests
import threading

# ------------------ AI FUNCTION (TINYLLAMA) ------------------
def ask_ai(prompt):
    try:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=data)
        return response.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"

# ------------------ SEND MESSAGE ------------------
def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return

    chat_area.insert(tk.END, "You: " + user_text + "\n")
    entry.delete(0, tk.END)

    chat_area.insert(tk.END, "AI: thinking...\n")
    chat_area.see(tk.END)

    def run_ai():
        response = ask_ai(user_text)

        chat_area.insert(tk.END, "AI: " + response + "\n\n")
        chat_area.see(tk.END)

    threading.Thread(target=run_ai, daemon=True).start()

# ------------------ GUI WINDOW ------------------
window = tk.Tk()
window.title("AI chatbot by Garima (TinyLlama)")
window.geometry("700x600")

# ------------------ TITLE ------------------
title = tk.Label(
    window,
    text="AI Chatbot by Garima",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# ------------------ CHAT AREA ------------------
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 11))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# ------------------ INPUT BOX ------------------
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(fill=tk.X, padx=10, pady=5)

# ------------------ SEND BUTTON ------------------
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

# ------------------ ENTER KEY SUPPORT ------------------
window.bind("<Return>", lambda event: send_message())

# ------------------ START APP ------------------
window.mainloop()
