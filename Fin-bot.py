import streamlit as st
import random
import time
# import phidata
from phi.agent import Agent
from phi.model.groq import Groq
from phi.run.response import RunResponse
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
from phi.utils.pprint import pprint_run_response

load_dotenv()
model_name = "llama-3.1-70b-versatile"
agent = Agent(
    model = Groq(id = "llama-3.1-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True, stock_fundamentals = True)],
    show_tool_calls = True,
    markdown = True,
    instructions = ["Use tables to display data"],
    # debug_mode = True
)

st.title("Fin-Bot")
st.subheader(f"Your finance assistant")
st.write("This bot can assist you with finance related queries*")
if st.button('Show T&Cs'):
    st.markdown(f"- *accuracy of answers is subject to model accuracy.")
    st.markdown(f"- Currently using {model_name} model ")
    st.markdown(f"- responses are subject to rate limits")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
prompt = st.chat_input("Type your query")

response: RunResponse = agent.run(prompt)

# React to user input
if prompt :
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    reply = f"Fin-bot: {response.content}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(reply)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})




