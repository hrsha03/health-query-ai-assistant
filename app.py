# app.py
from core.index_manager import build_or_load_index
from core.retriever import retrieve
from core.responder import generate_response
from utils.chat_memory import update_summary

index, docs = build_or_load_index("data")
chat_summary = ""

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break

    context, source_file = retrieve(query, index, docs, filenames)[0]
    response = generate_response(query, context, chat_summary)

    print("\n\U0001FA7A Assistant:\n", response, "\n")

    chat_summary = update_summary(chat_summary, query, response)
