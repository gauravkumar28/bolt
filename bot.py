from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import request, json
import os
from os import environ

app = Flask(__name__)

chatbot = ChatBot("Bolt",
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    database="bolt-chatbot",
    database_uri='mongodb://localhost:27017/',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods = ["PUT","GET"])
def get_raw_response():
    msg = request.json["msg"]
    return json.dumps(str(chatbot.get_response(msg)))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
