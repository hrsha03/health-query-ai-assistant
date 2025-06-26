# 🩺 HealthQuery AI Assistant — Local RAG + LLM Symptom Guide

A privacy-friendly, AI-powered virtual healthcare assistant that helps users understand their symptoms and guides them on whether to seek medical attention.

This assistant runs **locally** using:
- Amazon Titan Embeddings (for vector search)
- Meta LLaMA3-8B via Amazon Bedrock (for response generation)
- FAISS for fast document search
- Streamlit for interactive chat UI

---

## ⚠️ Ensure Normal Model Response First

LLaMA models can occasionally return unintended outputs (like internal logic or code) **especially on the first prompt after a fresh start**.

To ensure stable and informative results:

###  Prompting Tips:
- Start with direct, natural questions like:
  - `"I'm experiencing chest pain and breathlessness."`
  - `"I've had a persistent cough. Should I worry?"`
- **Avoid:** technical or feedback-style prompts like:
  - `"Why did you say that?"`
  - `"Can you summarize what you told me?"`

> If the message seems off: press **Reset Chat** in the sidebar and refresh the page.

---

## 🛠 How to Run Locally

 ### Clone the repository:
```bash
git clone https://github.com/hrsha03/health-query-ai-assistant.git
cd health-query-ai-assistant
```
 ### Set up a virtual environment
```bash
# for first run
python3 -m venv venv
# for subsequent runs
source venv/bin/activate 
```
 ### Install required dependencies
```bash
pip install -r requirements.txt
```
 ### Set up AWS credentials:
```bash
aws configure
```
 ### Run the chatbot UI:
```bash
streamlit run streamlit_app.py
```


