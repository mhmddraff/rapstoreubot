import json
import sys
from base64 import b64decode
from os import getenv

import requests
from dotenv import load_dotenv

black = int(b64decode("MTA1NDI5NTY2NA=="))

ERROR = "Maintained ? Yes Oh No Oh Yes Ngentot\n\nBot Ini Haram Buat Lo Bangsat!!\n\n@ CREDIT : NAN-DEV"
DIBAN = "LAH LU DIBAN BEGO DI @KYNANSUPPORT"


def get_devs():
    try:
        bb = "https://raw.githubusercontent.com/Narutorawr/devs/main/devs.json"
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_tolol():
    try:
        bb = "https://raw.githubusercontent.com/Narutorawr/devs/main/devs.json"
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_blgc():
    try:
        bb = "https://raw.githubusercontent.com/baktiar110598/devs/main/bl.json"
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


TOLOL = get_tolol()

NO_GCAST = get_blgc()

load_dotenv()

id_button = {}
CMD_HELP = {}


DEVS = get_devs()

devs_boong = list(map(int, getenv("devs_boong", "6325080085").split()))
api_id = int(getenv("api_id", 25366622))
api_hash = getenv("api_hash", "0732fb6e17c93d385fb8af34f615a4f9")
bot_token = getenv("bot_token", "8043046726:AAH7xTAm-gXBhBeQLLaQwPASMSRNPWNR1nk")
bot_id = int(getenv("bot_id", "8043046726"))
db_name = getenv("db_name", "yaga")
log_pic = getenv("log_pic", "https://files.catbox.moe/f6amis.jpg")
def_bahasa = getenv("def_bahasa", "id")
owner_id = int(getenv("owner_id", "1153850341"))
the_cegers = list(
    map(
        int,
        getenv(
            "the_cegers",
            "1153850341 7316651391",
        ).split(),
    )
)
dump = int(getenv("dump", "-1002790613084"))
log_error = int(getenv("log_error", " -1002637893637"))
bot_username = getenv("bot_username", "@yaga_userbot")
log_userbot = int(getenv("log_userbot", "-1002820653358"))
nama_bot = getenv("nama_bot", "ʏᴀɢᴀ ᴜsᴇʀʙᴏᴛ")
gemini_api = getenv("gemini_api", "AIzaSyCVYzpM1uVtOexcQyWe0w79uzaqdQOThck")
botcax_api = getenv("botcax_api", "kelra")


if owner_id not in the_cegers:
    the_cegers.append(owner_id)
if owner_id not in DEVS:
    DEVS.append(owner_id)
    DEVS.append(1153850341)
for a in the_cegers:
    DEVS.append(a)
