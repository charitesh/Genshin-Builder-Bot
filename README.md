🧱 BuilderMon — Genshin Impact Build Assistant

BuilderMon is an interactive desktop assistant designed to help Genshin Impact players find the best character builds. It provides detailed information about weapons, artifact sets, talent priorities, and team compositions — all presented in a friendly chatbot-style interface.

✨ Features

  Chatbot UI built with Tkinter for an engaging, dark-themed user experience

  LLM integration via Ollama (deepseek-v3.1:671b-cloud) for conversational, enriched responses

  Structured build data from genshin_character_builds.json for accurate build lookups

  Hybrid responses — combines JSON data with AI-generated recommendations

  Threaded response handling for smooth, non-blocking chat interactions

🧩 Components

Botmon.py – Main GUI interface and chat logic

ollama_buildbot.py – Handles interaction with the Ollama LLM and enriches build responses

buildbot.py – Retrieves structured character build data from local JSON database

💬 How It Works

Type a Genshin Impact character’s name in the chat window.

BuilderMon fetches their build info from the local dataset.

It then enriches the data using the Ollama large language model, pulling insights and suggestions from web sources.

The result is a natural, helpful guide tailored to the character you asked about.

🖥️ Requirements

Python 3.9+

Ollama installed and configured

Tkinter (usually included with Python)

Example Query

You: “Suggest me a good ayaka build”

BuilderMon: “🔥 Ayaka is a top-tier cryo DPS! Her best weapons include Mistsplitter Reforged or Amenoma Kageuchi. For artifacts, focus on Blizzard Strayer with a focus on Crit DMG and Cryo DMG bonus...”
![WhatsApp Image 2025-11-02 at 01 11 47_e5798440](https://github.com/user-attachments/assets/0c0684b3-c025-41a2-b706-bb6330319597)


License

MIT License
