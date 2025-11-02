import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from ollama_buildbot import enriched_build_response

# --- GUI SETUP ---
root = tk.Tk()
root.title("Ask BuilderMon")
root.geometry("650x700")
root.config(bg="#1e1e1e")  # Dark background

# --- Title ---
title_label = tk.Label(
    root,
    text="Ask BuilderMon",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e1e",
    fg="#00bfff"
)
title_label.pack(pady=15)

# --- Chat Display ---
chat_frame = tk.Frame(root, bg="#2e2e2e")
chat_frame.pack(padx=10, pady=5, fill="both", expand=True)

chat_window = scrolledtext.ScrolledText(
    chat_frame,
    wrap="word",
    state="disabled",
    font=("Segoe UI", 11),
    bg="#2e2e2e",
    fg="#ffffff",
    relief="flat",
)
chat_window.pack(fill="both", expand=True, padx=10, pady=10)

# --- Entry Box Frame ---
bottom_frame = tk.Frame(root, bg="#1e1e1e")
bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)

# Input box
entry_box = tk.Entry(
    bottom_frame,
    font=("Segoe UI", 11),
    relief="flat",
    fg="#ffffff",
    bg="#3e3e3e",
    insertbackground="#ffffff",
)
entry_box.insert(0, "Tell me the character name...")
entry_box.bind("<FocusIn>", lambda e: entry_box.delete(0, "end"))
entry_box.pack(side="left", fill="x", expand=True, padx=(0, 5), ipady=6)

# Send Button
send_button = tk.Button(
    bottom_frame,
    text="Send",
    bg="#00bfff",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    bd=0
)
send_button.pack(side="right", pady=5)

# --- Display Messages ---
def display_message(message, sender="bot"):
    """Display chat messages in the window."""
    chat_window.config(state="normal")

    if sender == "user":
        bubble = f"\nYou: {message}\n"
        chat_window.insert(tk.END, bubble, "user")
    else:
        # Split BuilderMon's name from the message
        name = "BuilderMon: "
        chat_window.insert(tk.END, "\n")
        chat_window.insert(tk.END, name, "bot_name")
        chat_window.insert(tk.END, message + "\n", "bot_text")

    chat_window.config(state="disabled")
    chat_window.yview(tk.END)

# --- Function to fetch response in a thread ---
def fetch_response(user_msg):
    # Show typing indicator using a unique tag
    chat_window.config(state="normal")
    chat_window.insert(tk.END, "\nBuilderMon is typing...\n", "typing")
    chat_window.config(state="disabled")
    chat_window.yview(tk.END)

    # Get LLM response
    response = enriched_build_response(user_msg)

    # Remove only the typing indicator
    chat_window.config(state="normal")
    chat_window.tag_delete("typing")  # remove the tag reference
    start_index = chat_window.search("BuilderMon is typing...", "1.0", tk.END)
    while start_index:
        end_index = f"{start_index}+{len('BuilderMon is typing...')+1}c"  # +1c for newline
        chat_window.delete(start_index, end_index)
        start_index = chat_window.search("BuilderMon is typing...", "1.0", tk.END)
    chat_window.config(state="disabled")

    # Display actual response
    display_message(response, sender="bot")


# --- Send Message ---
def send_message():
    user_msg = entry_box.get().strip()
    if not user_msg or user_msg == "Tell me the character name...":
        return

    display_message(user_msg, sender="user")
    entry_box.delete(0, "end")

    # Start thread to fetch LLM response
    Thread(target=fetch_response, args=(user_msg,), daemon=True).start()

# --- Text Styles ---
chat_window.tag_config("user", foreground="#00bfff", justify="right", spacing3=5)
chat_window.tag_config("bot_name", foreground="#ffffff", font=("Segoe UI", 11, "bold"))
chat_window.tag_config("bot_text", foreground="#cccccc", font=("Segoe UI", 11), justify="left", spacing3=10)
chat_window.tag_config("bot_text_placeholder", foreground="#888888", font=("Segoe UI", 11, "italic"), justify="left")


# --- Initial Greeting ---
display_message("Hi there, Traveler! 👋\n\n"
              "I'm BuilderMon, your friendly Genshin Impact build assistant. "
              "Just type the character's name, and BuilderMon is ready to help! 😊"
              "Once you let me know the correct name, I'll be happy to pull up their best builds, including:\n"
              "* Top Talents to prioritize.\n"
              "* Recommended Weapons from 5-star to 4-star options.\n"
              "* Best Artifact Sets for their role (like a DPS, support, etc.).\n"
              "* Strong Team Compositions based on the current meta.\n\n"
              , sender="bot")

# Link Send button to function
send_button.config(command=send_message)

root.mainloop()
