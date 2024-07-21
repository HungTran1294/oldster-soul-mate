# oldster-soul-mate
Here's the content for your `README.md`, formatted for easier copying and readability:

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
4. **Groq Account:** Create a free account with Groq to access their API and the Llama 3 model: [https://groq.com/](https://groq.com/).

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv .venv 
   source .venv/bin/activate
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
   streamlit run your_app.py
   ```
   - Replace `your_app.py` with your Streamlit app filename.

### Deploying to Streamlit Sharing

1. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   ```
2. **Push to GitHub:** 
   - Create a new repository on GitHub.
   - Push your code to the repository:
     ```bash
     git remote add origin https://github.com/your-username/your-repo-name.git
     git push -u origin main
     ```
3. **Deploy on Streamlit:**
   - Go to [https://share.streamlit.io/](https://share.streamlit.io/) and log in.
   - Click "New app" and select your GitHub repository.
   - Streamlit will build and deploy your application. 

## Customization

- **AI Personality:** Modify the prompts in the `ai_description` variable within the code to adjust the AI's communication style. 
- **User Profiles:** Create multiple `user_profile.txt` files for different user personas or provide a way for users to input their preferences.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to its development. 
```

**Remember:**

- Replace the placeholders (`your-username`, `your-repo-name`, `YOUR_GROQ_API_KEY`) with your real information! 
- Use a Markdown editor (like the one on GitHub) to preview the formatted README. 


