# 🩺 Health Assist Bot — Local RAG + LLM Symptom Guide

A privacy-friendly, AI-powered virtual healthcare assistant that helps users understand their symptoms and guides them on whether to seek medical attention.

This assistant runs **locally** using:
- ✅ Amazon Titan Embeddings (for vector search)
- ✅ Meta LLaMA3-8B via Amazon Bedrock (for response generation)
- ✅ FAISS for fast document search
- ✅ Streamlit for interactive chat UI

---

## ⚠️ Ensure Normal Model Response First

LLaMA models can occasionally return unintended outputs (like internal logic or code) **especially on the first prompt after a fresh start**.

To ensure stable and informative results:

### ✅ Prompting Tips:
- Start with direct, natural questions like:
  - `"I'm experiencing chest pain and breathlessness."`
  - `"I've had a persistent cough. Should I worry?"`
- **Avoid:** technical or feedback-style prompts like:
  - `"Why did you say that?"`
  - `"Can you summarize what you told me?"`

> If the first message seems off: press **Reset Chat** in the sidebar or refresh the page.

---

## 🛠 How to Run Locally
```bash
 ### Clone the repository:
git clone https://github.com/your-username/health-assist-bot.git
cd health-assist-bot

 ### Set up a virtual environment
-- for first run
python3 -m venv venv
-- for later runs
source venv/bin/activate 

 ### Install required dependencies
pip install -r requirements.txt

 ### Set up AWS credentials:
aws configure

 ### Run the chatbot UI:
streamlit run streamlit_app.py

```


