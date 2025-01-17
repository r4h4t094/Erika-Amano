import os
import sys
import logging
from pyrogram import Client

# Remove old error log
if os.path.exists('error.log'):
    os.remove('error.log')

# <-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log', format='%(asctime)s - %(levelname)s - %(message)s')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(logging.INFO)

# <-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')

TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '6392899197:AAGdYygGAZT0gkxxrcjoLOB-HOlief8lZ9I')  # BOT Token Add
API_ID = int(os.environ.get('API_ID', 24720817))  # Telegram API ID
API_HASH = os.environ.get('APP_HASH', '43669876f7dbd754e157c69c89ebf3eb')  # Telegram App Hash
OWNER_ID = int(os.environ.get('OWNER_ID', 1235222889))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://94:94@cluster0.lijgjzi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # MongoDB for Anime Data
FILES_CHANNEL = int(os.environ.get("FILES_CHANNEL", -1002027997392))  # Log Channel
BOT_NAME = os.environ.get('BOT_NAME', 'shadow_video_encoder_bot')

# <-----------Variables for 4GB Support (Optional)-------------->
SESSION_STRING = os.environ.get("SESSION_STRING", 'None')  # Replace None with a valid session string
ubot = None  # Don't Touch This

# <---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder = Client('AutoEncoder', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Successfully')
    except Exception as e:
        LOG.warning(f'😞 Error While Connecting to Bot\nCheck Errors: {e}')
        sys.exit()

# <---------------4GB Connecting-------------->
def create_ubot():
    global SESSION_STRING
    global ubot
    if SESSION_STRING != "None":
        try:
            ubot = Client("AutoEncoder", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Bot/plugins"))
            LOG.info("❤️ 4GB String Session Connected")
            return ubot
        except Exception as e:
            LOG.warning(f'😞 Error While Connecting to String Session: {e}')
            sys.exit()
            return None
