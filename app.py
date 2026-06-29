import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text")

target = st.selectbox(
    "Translate To",
    ["hi", "en", "fr", "de", "es"]
)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source="auto",
            target=target
        ).translate(text)

        st.success("Translation Completed!")
        st.write(translated)
    else:
        st.warning("Please enter some text.")