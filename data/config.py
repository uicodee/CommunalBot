from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
DB_NAME = env.str("DB_NAME")
MONGO_HOST = env.str("MONGO_HOST")
