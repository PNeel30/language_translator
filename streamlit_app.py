import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Missing `GROQ_API_KEY`. Add it to your `.env` file and restart Streamlit.")
    st.stop()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key,
)

system_template = "Translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)
parser = StrOutputParser()
chain = prompt | llm | parser


st.set_page_config(page_title="LLM Translator (Groq)", page_icon="🌐", layout="centered")

st.title("LLM Translator")
st.caption("Powered by Groq Llama 3 via LangChain.")

language_options = [
    "French",
    "Spanish",
    "German",
    "Hindi",
    "Telugu",
    "Tamil",
    "Kannada",
    "Malayalam",
    "Arabic",
    "Chinese (Simplified)",
    "Japanese",
    "Korean",
    "Other (custom)",
]

selected_language = st.selectbox("Target language", options=language_options, index=0)

custom_language = ""
if selected_language == "Other (custom)":
    custom_language = st.text_input(
        "Custom target language",
        value="",
        placeholder="e.g. Thai, Gujarati, Bengali",
    )

effective_language = custom_language if selected_language == "Other (custom)" else selected_language

text = st.text_area("Text to translate", value="Hello, how are you?\n I'm Translator", height=140)

col1, col2 = st.columns([1, 2])
with col1:
    translate_btn = st.button("Translate", type="primary", use_container_width=True)
with col2:
    model_name = st.text_input("Model", value="llama-3.3-70b-versatile", disabled=True)

if translate_btn:
    if not text.strip():
        st.warning("Please enter some text to translate.")
    elif not effective_language.strip():
        st.warning("Please select or enter a target language.")
    else:
        with st.spinner("Translating..."):
            try:
                out = chain.invoke({"language": effective_language.strip(), "text": text})
                st.subheader("Translation")
                st.write(out)
            except Exception as e:
                st.error(str(e))

