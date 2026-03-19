# LLM Translation App using Groq and LCEL

This is a simple translation tool built using:

- Streamlit  
- LangChain (LCEL)  
- Groq (Llama 3)  
- Python

## What It Does

You send a sentence and the language you want it translated into.  
It uses a Groq-hosted Llama 3 model to give you the translated sentence.

## How It Works

- Streamlit runs the app as a web UI.  
- LangChain formats the input and runs the chain.  
- Groq's Llama 3 model generates the translation.

## How to Run

1. Clone this repo
2. Install requirements  
   `pip install -r requirements.txt`
3. Create a `.env` file and add:  
   `GROQ_API_KEY=your_groq_api_key_here`
4. Run the Streamlit app  
   `streamlit run streamlit_app.py`

## Notes

- Never share or commit your real `GROQ_API_KEY`. If you accidentally exposed it, rotate it in the Groq console immediately.
