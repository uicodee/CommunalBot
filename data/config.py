# from environs import Env
#
# env = Env()
# env.read_env()
#
# BOT_TOKEN = env.str("BOT_TOKEN")
# ADMINS = env.list("ADMINS")
# IP = env.str("ip")
# DB_NAME = env.str("DB_NAME")
# MONGO_HOST = env.str("MONGO_HOST")
DEBUG = True
ADMINS = [2005282759]
BOT_TOKEN = "5061494977:AAFNPedF52STWyMES8kt0MSOggHpXxilk5E"
ip = "localhost"
DB_NAME = "uservice"
MONGO_HOST = "mongodb+srv://uicode:uicode@cluster0.vwoke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" if DEBUG is False else "mongodb://localhost:27017/"
print(MONGO_HOST)