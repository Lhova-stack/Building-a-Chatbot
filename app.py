from flask import Flask, request, jsonify

app = Flask(__name__)

# Chatbot name
BOT_NAME = "uNtsika"

# Sample intents with responses
RESPONSES = {
    "greet": f"Hello! I'm {BOT_NAME}, your virtual banking assistant. How can I help you today?",
    "check_balance": "For your security, please log into your banking app to check your balance.",
    "find_branch": "You can find the nearest branch using our locator here: https://mzansibank.co.za/branches",
    "open_account": "To open a savings account, bring your SA ID and proof of residence to any branch, or apply online on our website.",
    "loan_info": "We offer personal and home loans. Visit https://mzansibank.co.za/loans for more info.",
    "transaction_limit": "Your default daily limit is R5,000. You can increase it via the app or by visiting a branch.",
    "fees": "You can view our updated fee structure here: https://mzansibank.co.za/fees",
    "connect_human": "Alright, connecting you to a consultant... Please hold on a moment.",
    "goodbye": f"Thanks for chatting with {BOT_NAME}. Stay safe!"
}

# Simple keyword-to-intent mapping (can be replaced with NLP later)
KEYWORDS = {
    "balance": "check_balance",
    "nearest": "find_branch",
    "branch": "find_branch",
    "account": "open_account",
    "loan": "loan_info",
    "limit": "transaction_limit",
    "fees": "fees",
    "charges": "fees",
    "human": "connect_human",
    "consultant": "connect_human",
    "hi": "greet",
    "hello": "greet",
    "bye": "goodbye",
    "thanks": "goodbye"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Match keyword to intent
    for keyword, intent in KEYWORDS.items():
        if keyword in user_message:
            response = RESPONSES.get(intent, "I'm not sure how to help with that just yet.")
            return jsonify({"response": response})

    return jsonify({"response": "I'm not sure I understand. Can I connect you to a consultant?"})

if __name__ == "__main__":
    app.run(debug=True)
