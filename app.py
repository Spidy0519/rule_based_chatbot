from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary
responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello!",
    "how are you": "I am fine.",
    "what is your name": "I am a Rule-Based Chatbot.",
    "help": "Ask me simple questions."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    # Sanitization
    user_message = user_message.lower().strip()

    # Exit command
    if user_message in ["bye", "quit"]:
        return jsonify({"reply": "Goodbye!"})

    # Show available commands
    elif user_message == "commands":

        # Get dictionary keys
        keys = list(responses.keys())

        # Convert list to string
        command_list = ", ".join(keys)

        return jsonify({
            "reply": "Available commands: " + command_list
        })

    # Fallback
    reply = responses.get(user_message,
                          "I do not understand.")

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)