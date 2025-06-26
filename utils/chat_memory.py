def update_summary(chat_summary, query, response):
    summary_line = f"User asked about '{query}'. Assistant responded helpfully. "
    chat_summary += summary_line
    return chat_summary[-600:]  # Trim if too long
