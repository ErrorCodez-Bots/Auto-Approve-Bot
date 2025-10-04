import os
from typing import List

API_ID = os.environ.get("API_ID", "20293219")
API_HASH = os.environ.get("API_HASH", "4aef7d9e065d92f4a95736eaeb93d3ac")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8383692292:AAGEO7N8LliIeKB6fciWRd_MzBIBKSia4lc")
ADMIN = int(os.environ.get("ADMIN", "6091537598"))
PICS = (os.environ.get("PICS", "https://telegra.ph/file/7a408e30f2beeb78b5020-af7cbf2907f8d842ea.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003179370080"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://nshubh345:1FmseyW0TKaWNMNo@cluster0.pgewb.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "AutoApprovalBot")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002172875461 -1002484621427").split())) # Add Multiple channel ids
