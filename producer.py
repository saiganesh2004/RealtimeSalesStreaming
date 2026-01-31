import redis
import time
import random
from datetime import datetime

print("Connecting to Redis...")

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

try:
    print("PING:", r.ping())
except Exception as e:
    print("REDIS CONNECTION FAILED:", e)
    exit(1)

print("Connected. Sending data...")

while True:
    data = {
        "amount": random.randint(100, 1000),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    r.xadd("sales_stream", data)
    print("Sent:", data)
    time.sleep(2)
