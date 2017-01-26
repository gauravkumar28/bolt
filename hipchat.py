# -*- coding: utf-8 -*-
from chatterbot import ChatBot
#from settings import HIPCHAT

'''
See the HipChat api documentation for how to get a user access token.
https://developer.atlassian.com/hipchat/guide/hipchat-rest-api/api-access-tokens
'''

chatbot = ChatBot(
    'HipChatBot',
    hipchat_host='https://olashuttle.hipchat.com',
    hipchat_room='Olashuttle Staging',
    hipchat_access_token='U3Zp8IYBmeiCDQH92C3XO1IdXvM4eeP4bWgdRVGn',
    input_adapter='chatterbot.input.HipChat',
    output_adapter='chatterbot.output.HipChat',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train('chatterbot.corpus.english')

# The following loop will execute each time the user enters input
while True:
    try:
        response = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
