from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Uncomment the following line to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train("chatterbot.corpus.english")


CONVERSATION_ID = bot.storage.create_conversation()


def get_feedback():
    from chatterbot.utils import input_function

    text = input_function()

    if 'yes' in text.lower():
        return False
    elif 'no' in text.lower():
        return True
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response = bot.generate_response(input_statement, CONVERSATION_ID)

        bot.output.process_response(response)
        print('\n Is "{}" a coherent response to "{}"? \n'.format(response, input_statement))
        if get_feedback():
            print("please input the correct one")
            response1 = bot.input.process_input_statement()
            bot.learn_response(response1, input_statement)
            bot.storage.add_to_conversation(CONVERSATION_ID, statement, response1)
            print("Responses added to bot!")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


#
# # -*- coding: utf-8 -*-
#EXAMPLE 1: pretty simple only greetings.
# from chatterbot.trainers import ListTrainer
#
# from chatterbot import ChatBot
#
# bot = ChatBot('Test')
#
# greetings = ["oi", "olá", "olá, bom dia", "bom dia","e ai?", "tudo certo", "boa tarde", "boa noite",
#              "fala ae", "e ai?","como vai?", "estou bem"]
#
# movies = []
#
# bot.set_trainer(ListTrainer)
#
# bot.train(greetings)
#
#
# while True:
#     quest = input("Você: ")
#     response = bot.get_response(quest)
#
#     print("Bot: ",response)
#
#
# #EXAMPLE 2:
# # # -*- coding: utf-8 -*-
# # from chatterbot import ChatBot
# #
# #
# # # Uncomment the following lines to enable verbose logging
# # # import logging
# # # logging.basicConfig(level=logging.INFO)
# #
# # # Create a new instance of a ChatBot
# # bot = ChatBot(
# #     "Terminal",
# #     storage_adapter="chatterbot.storage.SQLStorageAdapter",
# #     logic_adapters=[
# #         "chatterbot.logic.MathematicalEvaluation",
# #         "chatterbot.logic.TimeLogicAdapter",
# #         "chatterbot.logic.BestMatch"
# #     ],
# #     input_adapter="chatterbot.input.TerminalAdapter",
# #     output_adapter="chatterbot.output.TerminalAdapter",
# #     database="../database.db"
# # )
# #
# # print("Type something to begin...")
# #
# # # The following loop will execute each time the user enters input
# # while True:
# #     try:
# #         # We pass None to this method because the parameter
# #         # is not used by the TerminalAdapter
# #         bot_input = bot.get_response(None)
# #
# #     # Press ctrl-c or ctrl-d on the keyboard to exit
# #     except (KeyboardInterrupt, EOFError, SystemExit):
# #         break