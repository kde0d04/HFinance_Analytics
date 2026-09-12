def parse_query(user_input):
    """Simple query parser (can be extended later)"""
    # Example: split into keywords
    keywords = user_input.lower().split()
    return {"original": user_input, "keywords": keywords}
