import json
import GigaBot
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

def FAQ(update: Update, context: CallbackContext):
    update.message.reply_text('Command list:\n' +
                              '/create name --> to create new database\n' +
                              '/load name --> to load existing database\n' +
                              '/add id/name/surname/dd.mm.yyyy/phoneNumber/adress --> to add person to DB.\n' +
                              '     WARNING:\n' +
                              '     / --> is required to input info in to database.\n' + 
                              '     If u dont have some info about person, dont leave fields empty.\n' +
                              '     In this case enter smt like: "none or -", but dont leave empty fields. U can edit person info later.\n' +
                              '/del id --> to delete person from database\n' + 
                              '/show --> to print loaded or created database\n' +
                              '/list --> to show all created or imported database\n' +
                              'TIP: To edit info about person u can just use command /add with id for this person, end enter all info again + edited info.\n' +
                              'If u need to change person ID, first u must del this person from database and then add person again with correct id')

def Cr8(update: Update, context: CallbackContext):
    global name
    global newDB
    newDB = {}
    name = update.message.text
    name = name.replace('/create ', '')
    with open(f'{name}.json', 'w', encoding = 'utf-8') as d:
        d.write(json.dumps(newDB, ensure_ascii = False))
        update.message.reply_text(f'DB {name} was sucsefully created.')
    with open('data.txt', 'a') as d:
        d.write(f'{name}\n')
        d.close()

def Load(update: Update, context: CallbackContext):
    global name
    global newDB
    name = update.message.text
    name = name.split(' ')
    name = name.pop(1)
    with open(f'{name}.json', 'r', encoding = 'utf-8') as outfile:
        newDB = json.load(outfile)
        update.message.reply_text(f'DB {name} was sucsefully loaded.')
    with open('data.txt', 'r') as d:
        data = d.readlines()
        if (f'{name}\n') not in data:
            with open('data.txt', 'a') as d:
                d.write(f'{name}\n')
                d.close()

def Add_guy(update: Update, context: CallbackContext):
    n = update.message.text
    n = n.replace('/add ', '')
    db = n.split('/')
    newDB[db[0]] = [db[i] for i in range(1,6)]
    with open(f'{name}.json', 'w', encoding = 'utf-8') as outfile:
        outfile.write(json.dumps(newDB, ensure_ascii = False))
        update.message.reply_text(f'Guy is added')

def Del_guy(update: Update, context: CallbackContext):
    n = update.message.text
    n = n.split(' ')
    if n[1] not in newDB.keys():
        update.message.reply_text(f'Key --> {n[1]} not in DB: {name}.')
    else:
        a = ' '.join(newDB.pop(n[1]))
        with open(f'{name}.json', 'w', encoding = 'utf-8') as d:
            d.write(json.dumps(newDB, ensure_ascii = False))
            update.message.reply_text(f'{a} was deleted.')

def Show(update: Update, context: CallbackContext):
    for k,v in newDB.items():
        update.message.reply_text(f'id: {k};\n' + 
                                f'name: {v[0]};\n' + 
                                f'surname: {v[1]};\n' + 
                                f'birthday: {v[2]};\n' + 
                                f'phone number: {v[3]};\n' +
                                f'adress: {v[4]};')

def ListDB(update: Update, context: CallbackContext):
    count = 1
    with open('data.txt', 'r', encoding = 'utf-8') as d:
        for line in d:
            update.message.reply_text(f'{count}: {line}')
            count += 1

def Switchman(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi, {update.effective_user.first_name}.\n/faq to see commands list')


updater = Updater(GigaBot.token())

updater.dispatcher.add_handler(CommandHandler('faq', FAQ))
updater.dispatcher.add_handler(CommandHandler('create', Cr8))
updater.dispatcher.add_handler(CommandHandler('load', Load))
updater.dispatcher.add_handler(CommandHandler('add', Add_guy))
updater.dispatcher.add_handler(CommandHandler('del', Del_guy))
updater.dispatcher.add_handler(CommandHandler('show', Show))
updater.dispatcher.add_handler(CommandHandler('list', ListDB))
updater.dispatcher.add_handler(MessageHandler(Filters.text, Switchman))

print('server start')
updater.start_polling()
updater.idle()