# llm.py (Using Gemini API)
from google import genai
from google.genai.errors import APIError # We need this to handle errors
import json 

# IMPORTANT: The api_key will now be a Gemini API key, not an OpenAI key.
def generate_planner_summary(api_key, name, reminders):
    try:
        # Initialize the client with the Gemini API key
        client = genai.Client(api_key=api_key)
    except Exception as e:
        # Better error handling if the key is bad or environment is wrong
        return f"ERROR: Could not initialize Gemini Client. Check API Key. Details: {e}"

    # Convert the Python dictionary into a JSON string for the model
    data_json = json.dumps(reminders, indent=2)

    prompt = f"""
    You are a personal daily planner assistant for a command-line interface. 
    Your tone must be concise, friendly, and helpful.

    Here is the user's data for the day:
    {data_json}

    Based on the information above:
    1. Start with a friendly greeting, addressing the user by name ({name}).
    2. Give a brief summary of the **Weather** (condition and temperature).
    3. Mention the **Transit** status and reason.
    4. List any upcoming **Reminders** and include any weather-relevant notes for outside events.
    5. The entire response must be a single, easy-to-read block of text.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Powerful, fast, and great for this task
            contents=[prompt]
        )
        
        # The response structure is slightly different for Gemini
        return response.text

    except APIError as e:
        # Handles issues like running out of free quota or invalid prompts
        return f"ERROR: Gemini API call failed. Details: {e}"
    except Exception as e:
        # General error fallback
        return f"ERROR: An unexpected error occurred during LLM call. Details: {e}"