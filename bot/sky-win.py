#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that awaits an answer from the user
# This program is dedicated to the public domain under the CC0 license.

import logging
from telegram import Emoji, ForceReply, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define the different states a chat can be in
MENU, AWAIT_CONFIRMATION, AWAIT_TEAM, AWAIT_INPUT = range(4)

# Python 2 and 3 unicode differences
try:
    YES, NO = (Emoji.THUMBS_UP_SIGN.decode('utf-8'), Emoji.THUMBS_DOWN_SIGN.decode('utf-8'))
except AttributeError:
    YES, NO = (Emoji.THUMBS_UP_SIGN, Emoji.THUMBS_DOWN_SIGN)
    
INTER_JUVE, NAPOLI_ROMA = ("Inter - Juve", "Napoli - Roma")

# States are saved in a dict that maps chat_id -> state
state = dict()
# Sometimes you need to save data temporarily
context = dict()
# This dict is used to store the settings value for the chat.
# Usually, you'd use persistence for this (e.g. sqlite).
values = dict()


# Example handler. Will be called on the /set command and on regular messages
def set_value(bot, update):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    text = update.message.text
    chat_state = state.get(getId(chat_id, user_id), MENU)
    chat_context = context.get(getId(chat_id, user_id), None)

    # Since the handler will also be called on messages, we need to check if
    # the message is actually a command
        
    if chat_state == MENU and "mostr" in text.lower():
        showResults(bot, update, chat_id, user_id)
        
    elif chat_state == MENU and "gioc" in text.lower():
        startChooseTeam(bot, update, chat_id, user_id)

    # If we are waiting for input and the right user answered
    elif chat_state == AWAIT_TEAM and chat_context == user_id:
        askPlayer(bot, update, chat_id, user_id)
        
    elif chat_state == AWAIT_INPUT and chat_context[0] == user_id:
        savePlayer(bot, update, chat_id, user_id)

    # If we are waiting for confirmation and the right user answered
    elif chat_state == AWAIT_CONFIRMATION and chat_context[0] == user_id:
        del state[getId(chat_id, user_id)]
        del context[getId(chat_id, user_id)]
        if text == YES:
            team = chat_context[1]
            player = chat_context[2]
            print chat_id, chat_id, getId(chat_id, user_id)
            values[getId(chat_id, user_id) + team] = update.message.from_user.first_name + ": Goal di " + player + " (" + team + ")"
            bot.sendMessage(chat_id, text=u"Bene! Hai puntato su %s." % player)
        else:
            bot.sendMessage(chat_id,
                            text="Hai annullato l'ultima modifica")
            
def startChooseTeam(bot, update, chat_id, user_id):
    state[getId(chat_id, user_id)] = AWAIT_TEAM  # set the state
    context[getId(chat_id, user_id)] = user_id  # save the user id to context
    bot.sendMessage(chat_id,
				  text="Bene, scegli la partita su cui vuoi giocare\n"
				  "/cancel per cancellare",
				  reply_markup=ReplyKeyboardMarkup(
                    [[KeyboardButton(INTER_JUVE), KeyboardButton(NAPOLI_ROMA)]],
                    one_time_keyboard=True))
    
def askPlayer(bot, update, chat_id, user_id):
    state[getId(chat_id, user_id)] = AWAIT_INPUT  # set the state
    context[getId(chat_id, user_id)] = (user_id, update.message.text)   # save the user id to context
    bot.sendMessage(chat_id,
				  text=u"Secondo te chi sarà il prossimo giocatore che segna?\n"
				  "/cancel per cancellare")
    
def savePlayer(bot, update, chat_id, user_id):
    state[getId(chat_id, user_id)] = AWAIT_CONFIRMATION

    # Save the user id and the answer to context
    context[getId(chat_id, user_id)] = (context[getId(chat_id, user_id)][0], context[getId(chat_id, user_id)][1], update.message.text)
    reply_markup = ReplyKeyboardMarkup(
        [[KeyboardButton(YES), KeyboardButton(NO)]],
        one_time_keyboard=True)
    bot.sendMessage(chat_id, text=unicode(u"Sei sicuro che segnerà " + update.message.text + "?"), reply_markup=reply_markup)
    
def showResults(bot, update, chat_id, user_id):
    print values
    choosesStr = ""
    
    for k in values.keys():
        if k.startswith(str(chat_id)):
            choosesStr += values[k] + "\n"
        
        
    bot.sendMessage(chat_id, text="Ecco qui le giocate in corso:\n" + choosesStr)
    

def getId(chat_id, user_id):
    return str(chat_id) + str(user_id)
  

# Handler for the /cancel command.
# Sets the state back to MENU and clears the context
def cancel(bot, update):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    del state[getId(chat_id, user_id)]
    del context[getId(chat_id, user_id)]


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text="Salve! Sono il tuo assistente Sky Win.")

# Create the Updater and pass it your bot's token
updater = Updater("232161513:AAEsreQl7mGA-mtPRWHmkXwFT_BRmJNO8bs")

# The command
updater.dispatcher.add_handler(CommandHandler('set', set_value))
# The answer and confirmation
updater.dispatcher.add_handler(MessageHandler([Filters.text], set_value))
updater.dispatcher.add_handler(CommandHandler('cancel', cancel))
updater.dispatcher.add_handler(CommandHandler('start', help))
updater.dispatcher.add_handler(CommandHandler('help', help))

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()