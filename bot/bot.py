def test():
    return 'Test bestanden', ''


def stop():
    return 'Stoppt', 'stop'


def print_help():
    out = 'Hier ist eine Liste der Commands: \n'
    for key in cmds.keys():
        out = '{}{}\n'.format(out, key)
    return out, ''


cmds = {
    'stop': stop,
    'bye': stop,
    'test': test,
    'help': print_help
}


def check(msg):
    if msg in cmds:
        ouput = cmds[msg]()
        return ouput
    else:
        output = 'Unbekannter Befehl :( \nBenutze help für Hilfe'
        return output, ''


