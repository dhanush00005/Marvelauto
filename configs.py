# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27501733"))
    API_HASH = getenv("API_HASH", "687b5c7656849e9a3b125d691f824497")
    BOT_TOKEN = getenv("BOT_TOKEN", "6692227713:AAE6lantNZAbkmBgeONi3IeJJHaiKgIR7lo")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1001623633000"))
    SUDO = list(map(int, getenv("SUDO", "5452354891 1392184089 5602172369").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://thewalter3699:thewalter3699@cluster0.yko9zob.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
