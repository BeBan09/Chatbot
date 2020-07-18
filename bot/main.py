from bot import bot


def main():
    chat_in = ''
    out, status = '', ''

    while status != 'stop':
        chat_in = input('> ')
        out, status = bot.check(chat_in)
        print(out)
