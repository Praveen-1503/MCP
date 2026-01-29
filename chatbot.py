import os 
from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()
os.environ["CEREBRAS_API_KEY"] = os.getenv("CEREBRAS_API_KEY")


prompt = ChatPromptTemplate.from_messages([
        ("system", "You are good assistant. Help me with my prompts."),
        ("user", "{question}")
    ]
)

llm = ChatCerebras(model="gpt-oss-120b")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser


st.write("Caramel AI - A Personal Chatbot")
input_text = st.text_input("Ask me anything")

if input_text:
    st.write(chain.invoke({"question": {input_text}}))