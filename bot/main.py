import bot, data

import random, json


with open('data.json', 'r') as json_file:
    json_data = json_file.read()
    obj = json.loads(json_data)
    prefix = obj['prefix']
    name = obj['name']


def main():
    chat_in = ''
    out, status = '', ''

    while status != 'stop':
        chat_in = input(f'{prefix} ')
        out, status = bot.check(chat_in)
        print(out)


opening = random.choice(data.greetings)
opening = opening.replace('{name}', name)
print(opening)
main()
