import GigaBot
import random
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

def rules(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'To play RPS u should enter 1 of 3 choices: rock, papper or scissors\n Lets go!')

def result(update: Update, context: CallbackContext) -> None:
    a = 0
    b = 0
    file1 = open('PlSC.txt', 'r')
    file2 = open('CmSC.txt', 'r')
    for line in file1:
        line = float(line)
        a += line
    for line in file2:
        line = float(line)
        b += line
    update.message.reply_text(f'Finished. Ur score: {a}, bot score {b}')
    file1 = open('PlSC.txt', 'w')
    file2 = open('CmSC.txt', 'w')
    file1.close()
    file2.close()

def RPS(update: Update, context: CallbackContext):
    rpsList = ['rock', 'papper', 'scissors']
    playerScore = 0
    computerScore = 0
    playerChoice =  update.message.text 
    if playerChoice not in rpsList:
        update.message.reply_text('Retry')
    else:       
        computerChoice = random.choice(rpsList)
        update.message.reply_text(f'Computer choice is --> {computerChoice}')
    if playerChoice == computerChoice:
        update.message.reply_text('Draw in this round!')
        playerScore = 0.5
        computerScore = 0.5
    elif ((playerChoice == 'rock' and computerChoice == 'scissors') or 
          (playerChoice == 'papper' and computerChoice == 'rock') or 
          (playerChoice == 'scissors' and computerChoice == 'papper')):
        update.message.reply_text('You won this round!')
        playerScore = 1
    else:
        update.message.reply_text('You lost this round!')
        computerScore = 1
    file1 = open('PlSC.txt', 'a')
    file1.write(f'{playerScore}\n')
    file1.close()
    file2 = open('CmSC.txt', 'a')
    file2.write(f'{computerScore}\n')
    file2.close()
    
updater = Updater(GigaBot.token())


updater.dispatcher.add_handler(CommandHandler('rules', rules))
updater.dispatcher.add_handler(CommandHandler('result', result))
updater.dispatcher.add_handler(MessageHandler(Filters.text, RPS))

print('server start')
updater.start_polling()
updater.idle()