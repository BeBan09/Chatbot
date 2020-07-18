import bot, data

import random, json


def main():
    chat_in = ''
    out, status = '', ''

    while status != 'stop':
        chat_in = input('> ')
        out, status = bot.check(chat_in)
        print(out)


my_details = {
    'name': 'Test',
    'age': 13
}

with open('data.json', 'w') as json_file:
    json.dump(my_details, json_file)


opening = random.choice(data.greetings)
opening= opening.replace('{name}', 'PLATZHALTER')
print(opening)
main()
