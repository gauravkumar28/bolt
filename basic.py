import sys
from chatterbot import ChatBot
from websocket import create_connection
from time import sleep
import json

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement

ws = create_connection("ws://localhost:8000")

try:
    ws.send(json.dumps({"name": name, "message": "Hello earthlings!"}))
    thingFrom = ws.recv()
    while(True):
        thingFrom = json.loads(ws.recv())
        messageFrom = thingFrom["message"]
        whoFrom = thingFrom["name"]
        if (whoFrom != name):
            print(messageFrom)
            messageTo = json.dumps({"name": name, "message": "@" + whoFrom + " " + chatbot.get_response(messageFrom).text})
            ws.send(messageTo)
finally:
    ws.close()

#print chatbot.get_response(sys.argv[1])
