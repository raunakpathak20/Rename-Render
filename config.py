# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27951184")

API_HASH = os.environ.get("API_HASH", "40a5e4e67bf652eb67cea2f4e01dcb88")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6695697591:AAFUlSjMcjn4tnvyRf-n-h8dXJrde2lfxUs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "RR_BOTS_UPDATE") 

             # Don't Remove Credit @RR_BOTS_UPDATE

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "raunakpp208:zpcBDVxsLVJzXPLU@cluster0.qiwwccy.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1383130034').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
