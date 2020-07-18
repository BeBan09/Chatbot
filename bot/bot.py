import json
import wikipedia

def platzhalter():
    return 'Platzhalter'


def test():
    return 'Test bestanden'


def print_help():
    out = 'Hier ist eine Beispielliste von Commands: \n'
    for key in cmds.keys():
        out = '{}{}\n'.format(out, key)
    return out


def change_name():
    name = input('Zu was soll dein Name geändert werden?\n')
    with open('data.json', 'r') as json_file:
        json_data = json_file.read()
        obj = json.loads(json_data)
    with open('data.json', 'w') as json_file:
        obj['name'] = name
        json.dump(obj, json_file)
    return 'Name geändert zu ' + name


def change_age():
    age = input('Zu was soll dein Alter geändert werden?\n')
    with open('data.json', 'w') as json_file:
        json_data = json_file.read()
        obj = json.loads(json_data)
    with open('data.json', 'w') as json_file:
        obj['age'] = age
        json.dump(obj, json_file)
    return 'Alter geändert zu ' + age


def wiki_summary():
    inp = input('Suche:\n')
    try:
        result = wikipedia.search(inp)
        r_final = wiki_summary(result[0].split()[0].lower())
        out = f'\nWiki-Suche:\n {r_final}'
    except Exception as e:
        out = 'Wiki konnte deine Suche nicht richtig erkennen. Versuche es bitte noch einmal!'
    finally:
        return out


def wiki_search():
    inp = input('Suche:\n')
    try:
        r_final = ''
        result = wikipedia.search(inp)
        for item in result:
            r_final = f'{r_final}\n{item}'
        out = f'\nWiki-Suche:\n {r_final}'
    except:
        out = 'Wiki konnte deine Suche nicht richtig erkennen. Versuche es bitte noch einmal!'
    finally:
        return out


cmds = {
    'stop': platzhalter,
    'bye': platzhalter,
    'test': test,
    'help': print_help,
    'hilfe': print_help,
    'wiki': wiki_summary,
    'search': wiki_search
}


def check(msg):
    msg = msg.lower()
    output = ''
    if 'stop' in msg or 'bye' in msg:
        return 'Stoppt', 'stop'
    if 'change' in msg and 'name' in msg:
        return change_name(), ''
    if 'change' in msg and 'age' in msg:
        return change_age(), ''
    for d in cmds.keys():
        if d in msg:
            output = f'{cmds[d]()}\n{output}'
    if output == '':
        output = 'Unbekannter Befehl :( .\nBenutze "help" für Hilfe.'
    return output, ''
