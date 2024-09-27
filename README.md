# oldster-soul-mate
This web application provides an AI-powered companion chatbot designed for senior users. It utilizes Groq's platform to access Llama 3, a large language model, to create engaging and personalized conversations. 

## Features

- **Tailored Conversations:** The chatbot remembers user preferences and adapts its communication style based on provided user profiles.
- **Reminiscing and Sharing:** The AI encourages conversations about past memories and experiences, fostering a sense of connection. 
- **Information and Fun:** Provides news, stories, and other entertaining content to keep users engaged.
- **Senior-Friendly Interface:**  Features a simple and easy-to-use chat interface designed with seniors in mind. 

## Deployment with Streamlit and Groq

### Prerequisites

1. **Python 3.7+:** Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **pip:** Make sure you have `pip` (the Python package installer) installed.
3. **Streamlit Account:** Sign up for a free Streamlit account at [https://streamlit.io/](https://streamlit.io/).
4. **Groq Account:** Create a free account with Groq to access their API and the Llama 3 model: [https://groq.com/]
(https://groq.com/).
5. **Aconda3 to manage evn [Condamini](https://docs.anaconda.com/miniconda/)

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/HungTran1294/oldster-soul-mate.git
   cd oldster-soul-mate
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   conda create -n oldster-soul-mate python==3.10
   conda activate oldster-soul-mate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Groq API Key:**
   - Create a file named `secrets.toml` in your project directory.
   - Add your Groq API key to the `secrets.toml` file:
     ```toml
     [secrets]
     GROQ_API_KEY = "YOUR_GROQ_API_KEY" 
     ```

5. **Create `user_profile.txt`:**
   - Create a file named `user_profile.txt` in your project directory.
   - Add your JSON-formatted user profile data to this file. Follow the format provided in the code comments or examples.

### Running Locally with Streamlit

   ```bash
   streamlit run app.py
   ```

## Customization

- **AI Personality:** Modify the prompts in the `ai_description` variable within the code to adjust the AI's communication style. 
- **User Profiles:** Create multiple `user_profile.txt` files for different user personas or provide a way for users to input their preferences.


**Remember:**
- Replace  `YOUR_GROQ_API_KEY` with your real information! 


## Roadmap

Here's the future development plan for this project:

- **Enhanced Personalization:**  Integrate more advanced user profiling, potentially allowing users to customize their experience within the app. 
- **Multilingual Support:** Explore adding support for additional languages to make the chatbot accessible to a wider audience.
- **Voice Integration:**  Investigate the possibility of incorporating text-to-speech and speech-to-text capabilities for a more natural interaction.
- **Content Expansion:**  Continuously add new conversation topics, stories, news sources, and activities to keep the experience fresh and engaging.

## Customization

- **AI Personality:** Modify the prompts in the `ai_description` variable within the code to adjust the AI's communication style. 
- **User Profiles:** Create multiple `user_profile.txt` files for different user personas or provide a way for users to input their preferences.
