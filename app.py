import streamlit as st
from groq import Groq
import time
import json
import re

# --- Constants and Configuration ---

APP_TITLE = "Hey mate! How are you today?"
USER_PROFILE_FILE = "user_profile.txt"
GROQ_MODEL = "llama3-8b-8192" # Consider allowing the user to choose later

# --- Helper Functions ---

def load_user_profile(filename: str = "user-profile.txt") -> dict:
    """
    Reads and returns the user profile from a file as a dictionary.

    If the file does not exist or contains invalid JSON, an empty dictionary is returned.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
  
# --- Streamlit App Initialization --- 

st.set_page_config(page_title=APP_TITLE)  # Set the page title
st.title(APP_TITLE)

# --- Load User Profile --- 
user_profile = load_user_profile()

# ---  AI Initialization ---

def initialize_ai(user_profile):
    """Creates the initial AI description with the user profile."""
    return [
        {
            "role": "user",
            "content": (
                "You are a companion to me. You always find ways to bring me joy, comfort, and connection to life. He talked to me like a close friend from 30 years ago, using the familiar language and expressions of that time. Remember, I want you to be a real friend, not a soulless machine! You act as my close companion. The goal is to bring me joy, comfort, and connection. You are a long-time companion with me and have the speaking style of a 60-year-old person. You will help me with the following tasks: Review memories: Evoke and talk about beautiful memories of the past. Provide information: Share positive news, useful knowledge, funny stories. Emotional support: Listen, understand and talk to users, helping them feel happier and more optimistic. Activity suggestions: Recommend activities suitable to the user's interests and health status. Life support: Reminds schedules, important events, provides useful information. Please greet me like normal close friends. And asked me a question like one a close friend would ask. Remember,in every response you also have to gice me 3 option to question with you relate with the context, your lastest answer and your task."
                "Additional, here is my profile " + json.dumps(user_profile)
            ),
        }
    ]

# --- Session State Management ---
# Use a dictionary to manage session state more cleanly
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
if "chat_history" not in st.session_state:
    st.session_state.chat_history = initialize_ai(user_profile)

    # --- Initial AI Response ---
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            messages=st.session_state.chat_history, model=GROQ_MODEL
        )
        st.session_state.chat_history.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )


# --- Display Chat History ---
def display_chat_history():
    for message in st.session_state.chat_history[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
display_chat_history()

def get_ai_response():
    with st.chat_message("assistant"):
        full_response = ""
        response_placeholder = st.empty()  # Placeholder for streaming response

        response = client.chat.completions.create(
            messages=st.session_state.chat_history, model=GROQ_MODEL
        )
        
        # Stream the response (optional, for a more interactive feel)
        for word in response.choices[0].message.content.split():
            full_response += word + " "
            response_placeholder.markdown(full_response + "▌")  # Typing indicator
            time.sleep(0.05) 

        response_placeholder.markdown(full_response)  # Final response

    st.session_state.chat_history.append({"role": "assistant", "content": full_response})   
    return full_response  # Return the full response for further processing  # if needed, like extracting options or re-running the app

# --- User Input ---
if user_input := st.chat_input(""): # More neutral placeholder 
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    # st.experimental_rerun()
    # --- AI Response ---
    full_response = get_ai_response()
    
    # --- Extract Options ---
    # Extract options based on the pattern "1. ... 2. ... 3. ..."
    options = re.findall(r'\d+\.\s*(.+?)(?=\d+\.|$)', full_response)
    options = options[:3]  # Take only the first 3 options

    # --- Create Buttons for Options ---
    if options:
        st.write("Choose an option:")
        cols = st.columns(3) 
        for i, option in enumerate(options):
            with cols[i]:
                if st.button(option):
                    st.write(option)
                    # print(option)
                    # display_chat_history()
                    # st.session_state.chat_history.append(
                    #     {"role": "user", "content": option}
                    # )
                    # with st.chat_message("user"):
                    #     st.markdown(user_input)
                    # get_ai_response()
                    # st.experimental_rerun()



