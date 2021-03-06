import logging
import bot
logging.basicConfig(level=logging.INFO)

def readToken():
    with open('bot/secrets/bot.token') as f:
        token = f.read()
        return token

if __name__ == '__main__':
    try:
        token = readToken()
        poll = bot.bot
        poll.run(token)
    except Exception as e:
        logging.exception('Program Crashed: {e=}')

    else:
        logging.info('Process finished with error code 0')