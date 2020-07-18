import json


def platzhalter():
    return 'Platzhalter'


def test():
    return 'Test bestanden'


def print_help():
    out = 'Hier ist eine Liste der Commands: \n'
    for key in cmds.keys():
        out = '{}{}\n'.format(out, key)
    return out


def change_name(name):
    return ''


def change_age(age):
    return ''


cmds = {
    'stop': platzhalter,
    'bye': platzhalter,
    'test': test,
    'help': print_help,
    'hilfe': print_help
}


def check(msg):
    msg = msg.lower()
    output = ''
    if 'stop' in msg or 'bye' in msg:
        return 'Stoppt', 'stop'
    for d in cmds.keys():
        if d in msg:
            output = f'{cmds[d]()}\n{output}'
    if output == '':
        output = 'Unbekannter Befehl :( \nBenutze help für Hilfe'
    return output, ''


