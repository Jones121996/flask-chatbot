from flask import Flask, render_template, request
import re
import datetime

app = Flask(__name__)

def chatbot_response(user_input):
    responses = {
        r"\bhi\b|\bhello\b|\bhey\b": "Hello! How can I assist you?",
        r"\bhow are you\b|\bhow do you do\b": "I'm just a bot, but I'm doing great!",
        r"\bwhat time is it\b|\bcurrent time\b": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
        r"\bbye\b|\bgoodbye\b": "Goodbye! Have a nice day!",
        r"\bhelp\b": "I can answer basic questions like time, greetings, and simple responses."
    }

    user_input = user_input.lower()

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "Sorry, I don't understand."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    return chatbot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
