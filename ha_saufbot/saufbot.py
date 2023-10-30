import random
from telegram import *
from telegram.ext import *
import json
import logging
import tracemalloc
import os



#logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
tracemalloc.start()
httpx_logger = logging.getLogger('httpx') # sonst macht der andauernd http requests....
httpx_logger.setLevel(logging.WARNING)
#

# Define the path to the config.json file
config_file_path = '/share/saufbot/config.json'

if os.path.exists(config_file_path):
    # Load the JSON configuration
    with open(config_file_path, 'r') as json_file:
        config = json.load(json_file)

    # Access configuration settings as needed
    telegram_bot_token = config['secrets']['telegram_bot_token']


    logging.info(f'Using Telegram Bot Token: {telegram_bot_token}')
else:
    # No config.json found, so close the script
    logging.error("config.json not found. The Script will now generate different errors because of the missing file.")
    
   
try:
    telegram_bot_token = config['secrets']['telegram_bot_token']
    application = Application.builder().token(telegram_bot_token).build()
except Exception as e:
    logging.error("config.json not found. The Script will now spit out different errors because of the missing file.")
    logging.exception(f'Error: {str(e)}')

    
async def saufen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    # Roll two 6-sided dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    logging.info(f"Command issued by {update.effective_user}. Results: {dice1} {dice2} {dice3}")


    dice1_file = f"1_{dice1}.png"
    dice2_file = f"2_{dice2}.png"
    dice3_file = f"3_{dice3}.png"

    await application.bot.send_photo(chat_id=update.effective_chat.id, photo = open(dice3_file, "rb"))
    await application.bot.send_photo(chat_id=update.effective_chat.id, photo = open(dice1_file, "rb"))
    await application.bot.send_photo(chat_id=update.effective_chat.id, photo = open(dice2_file, "rb"))


application.add_handler(CommandHandler("saufen", saufen))



# Run the bot until the user presses Ctrl-C
application.run_polling(drop_pending_updates = True)