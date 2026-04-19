BuilderMon — Genshin Impact Build Assistant

BuilderMon is an interactive desktop assistant that helps Genshin Impact players find effective character builds. It presents information about weapons, artifact sets, talent priorities, and team compositions through a simple chatbot-style interface.

Features
A chatbot-style interface built with Tkinter, designed with a clean dark theme for comfortable use
Integration with an LLM via Ollama (deepseek-v3.1:671b-cloud) to provide more detailed and conversational responses
Uses structured data from genshin_character_builds.json to ensure accurate build recommendations
Combines reliable local data with AI-generated insights for more useful and contextual answers
Threaded response handling to keep the interface responsive during interactions

Components:
Botmon.py – Handles the graphical interface and chat flow
ollama_buildbot.py – Connects to the Ollama model and enhances responses
buildbot.py – Fetches character build data from the local JSON file

How It Works:
Enter the name of a Genshin Impact character in the chat.
BuilderMon retrieves relevant build information from its local dataset.
The system then uses the Ollama model to refine and expand the response with additional insights.
You receive a clear, structured build recommendation tailored to the character.

Requirements:
Python 3.9 or higher
Ollama installed and configured
Tkinter (included with most Python installations)

Example Query:
You: “Suggest me a good ayaka build”

BuilderMon: “Ayaka is a top-tier cryo DPS! Her best weapons include Mistsplitter Reforged or Amenoma Kageuchi. For artifacts, focus on Blizzard Strayer with a focus on Crit DMG and Cryo DMG bonus...”
!(https://github.com/user-attachments/assets/0c0684b3-c025-41a2-b706-bb6330319597)


License
MIT License
