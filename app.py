import streamlit as st
from groq import Groq
import time

st.title('Hey mate! How are you today ?')
ai_description = [{"role": "user","content":"You are a companion to me. You always find ways to bring me joy, comfort, and connection to life. He talked to me like a close friend from 30 years ago, using the familiar language and expressions of that time. Remember, I want you to be a real friend, not a soulless machine! You act as my close companion. The goal is to bring me joy, comfort, and connection. You are a long-time companion with me and have the speaking style of a 60-year-old person. You will help me with the following tasks: Review memories: Evoke and talk about beautiful memories of the past. Provide information: Share positive news, useful knowledge, funny stories. Emotional support: Listen, understand and talk to users, helping them feel happier and more optimistic. Activity suggestions: Recommend activities suitable to the user's interests and health status. Life support: Reminds schedules, important events, provides useful information. Please greet me like normal close friends. And asked me a question like one a close friend would ask"}]
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


if "message" not in st.session_state:
    st.session_state.message = []
    #define AI description
    st.session_state.message.append(ai_description[0])
    with st.chat_message("assistant"):
            response =  client.chat.completions.create(messages=ai_description,model="llama3-8b-8192")
            st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})

#show chat history
for message in st.session_state.message[1:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

#show input field
if prompt := st.chat_input("Hey I know you, You remember me?"):
    st.session_state.message.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

#get chat history
    context = [
                {"role": m["role"],"content": m["content"]}
                for m in st.session_state.message
            ]

#AI response
    with st.chat_message("assistant"):
        full_res=""
        holder = st.empty()
        response =  client.chat.completions.create(messages=context,model="llama3-8b-8192")
        for word in response.choices[0].message.content.split(" "):
            full_res += word + " "
            holder.markdown(full_res + "|| ")
            time.sleep(0.05)
        holder.markdown(full_res)
    st.session_state.message.append({"role": "assistant", "content": full_res})



