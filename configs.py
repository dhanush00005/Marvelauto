# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27402354"))
    API_HASH = getenv("API_HASH", "60c51bb87f0d213d954695dd8f636afd")
    BOT_TOKEN = getenv("BOT_TOKEN", "7464128394:AAG5BQgc5u_vHh3lQNVOaj89nUsRi8k7u_M")
    SUDO = list(map(int, getenv("SUDO", "5798247275 5364478284").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://fino:fino@cluster0.ko0stef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
