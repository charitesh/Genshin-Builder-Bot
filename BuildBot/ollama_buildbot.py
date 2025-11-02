import json
import subprocess

from buildbot import get_build_info

import subprocess


def query_ollama(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", "deepseek-v3.1:671b-cloud", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        output = result.stdout.strip()
        if not output:
            return "⚠️ Ollama returned an empty response."
        return output
    except subprocess.CalledProcessError as e:
        err_output = e.stderr.strip() if e.stderr else "No error output."
        return f"⚠️ Error contacting Ollama: {err_output}"



def enriched_build_response(user_msg: str) -> str:
    """
    Combine JSON structured data with Ollama LLM for a conversational response.
    """
    # Step 1: Get JSON build info (structured)
    json_response = get_build_info(user_msg)

    # Step 2: Create prompt for Ollama
    prompt = f"""
You are BuilderMon, a friendly Genshin Impact build assistant.
The user asked: "{user_msg}"
You have the following build info from JSON:
{json_response}
Enrich this information with tips, suggestions, and a friendly conversational style.
Don't make up your own stories or facts. 
Use the web to find relevant information about the character and the character's build, talent information, weapons and artifacts sets.
Keep the response concise and focused on the user's query and try to provide information on the talent, weapons and artifacts sets from the web.
Suggest the best builds, best teams and best weapons based on popular meta builds from enka.network.
If the character is not found, check genshin.gg and enka.network.
If character is not on genshin.gg, politely inform the user and dont assume they are talking about a different character and politely tell them your database is based on old data and ask them to check other sources.
"""
    return query_ollama(prompt)
