import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from pydantic import BaseModel
from typing import Annotated

from langchain_groq import ChatGroq

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver


# -------------------------
# State Definition
# -------------------------

class ChatState(BaseModel):
    messages: Annotated[list, add_messages]


# -------------------------
# LLM
# -------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


# -------------------------
# Chatbot Node
# -------------------------

def chatBotNode(state: ChatState):

    response = llm.invoke(
        state.messages
    )

    return {
        "messages": [response]
    }


# -------------------------
# Create LangGraph
# -------------------------

@st.cache_resource
def create_graph():

    memory = InMemorySaver()

    graph = StateGraph(ChatState)

    graph.add_node(
        "chatBot",
        chatBotNode
    )

    graph.add_edge(
        START,
        "chatBot"
    )

    graph.add_edge(
        "chatBot",
        END
    )

    app = graph.compile(
        checkpointer=memory
    )

    return app


app = create_graph()


# -------------------------
# Streamlit UI
# -------------------------

st.title("🤖 LangGraph Chatbot")


# Maintain UI history

if "messages" not in st.session_state:
    st.session_state.messages = []


if "thread_id" not in st.session_state:
    st.session_state.thread_id = "my-bot-1"



# Display previous messages

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])



# User input

query = st.chat_input(
    "Ask me anything..."
)


if query:


    # Display user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )


    with st.chat_message("user"):
        st.write(query)



    # LangGraph config

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }


    # Invoke graph

    result = app.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        },
        config
    )


    answer = result["messages"][-1].content



    # Display AI response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    with st.chat_message("assistant"):
        st.write(answer)