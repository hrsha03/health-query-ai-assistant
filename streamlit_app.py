# streamlit_app.py
import os
import streamlit as st
from core.index_manager import build_or_load_index
from core.retriever import retrieve
from core.responder import generate_response
from utils.chat_memory import update_summary

st.set_page_config(page_title="Health Assist Bot", layout="centered")
st.title("🩺 Health Assist Chatbot")

if "chat_summary" not in st.session_state:
    st.session_state.chat_summary = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "transcript" not in st.session_state:
    st.session_state.transcript = []

# Load index and docs
@st.cache_resource
def load_kb():
    return build_or_load_index("data")

index, docs, filenames = load_kb()

# Sidebar controls
with st.sidebar:
    if st.button("🔁 Reset Chat"):
        st.session_state.chat_history = []
        st.session_state.chat_summary = ""
        st.session_state.transcript = []
        st.rerun()

    if st.download_button("📄 Export Transcript", data="\n".join(st.session_state.transcript), file_name="chat_transcript.txt"):
        st.toast("Transcript downloaded")

# Chat input
query = st.chat_input("Describe your symptom...")

if query:
    result = retrieve(query, index, docs, filenames)[0]
    context, source_file = result
    st.session_state["last_source"] = source_file
    st.session_state["last_context"] = context
    response = generate_response(query, context, st.session_state.chat_summary)

    # Update session state
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("assistant", response))
    st.session_state.chat_summary = update_summary(st.session_state.chat_summary, query, response)
    st.session_state.transcript.append(f"User: {query}")
    st.session_state.transcript.append(f"Assistant: {response}")

# Display chat
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Show document source (simple heuristic: just show index 0 file)
with st.expander("📎 Source Info", expanded=False):
    if "last_source" in st.session_state:
        st.markdown(f"**Matched file:** `{st.session_state.last_source}`")
    if "last_context" in st.session_state:
        st.code(st.session_state.last_context.strip(), language="markdown")
    else:
        st.caption("No document matched yet.")
