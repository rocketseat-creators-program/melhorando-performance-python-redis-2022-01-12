from datetime import date
from flask import Flask
import time
from flask_caching import Cache

config = {
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": "127.0.0.1",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_URL": "redis://127.0.0.1:6379/0",
    "DEBUG": True,
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/")
@cache.cached(timeout=40, key_prefix='ola_mundos')
def ola_mundo():
    time.sleep(20)
    cache.set("foo", "ola, salada")
    return "oi"


@app.route("/alo")
@cache.cached(timeout=40, key_prefix='alou')
def alou():
    time.sleep(20)
    today = date.today()
    return "alo"