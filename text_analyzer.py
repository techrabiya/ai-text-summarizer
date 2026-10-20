import streamlit as st

st.set_page_config(page_title="AI Text Summarizer", page_icon="📝", layout="centered")
st.title("📝 AI Text Summarizer & Word Counter")
st.write("Paste your long text below to get instant word counts, character stats, and key sentence extraction!")

text_input = st.text_area("Enter your text here:", height=150)

if st.button("Analyze & Summarize"):
    if text_input.strip():
        words = text_input.split()
        num_words = len(words)
        num_chars = len(text_input)
        sentences = [s.strip() for s in text_input.replace('!', '.').replace('?', '.').split('.') if s.strip()]
        num_sentences = len(sentences)

        st.subheader("📊 Text Statistics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Words", num_words)
        col2.metric("Characters", num_chars)
        col3.metric("Sentences", num_sentences)

        st.subheader("💡 Key Summary Insight (First 2 Sentences)")
        summary = ". ".join(sentences[:2]) + ("." if sentences else "")
        st.success(summary if summary else "Text is too short to summarize.")
    else:
        st.warning("Please enter some text to analyze.")
