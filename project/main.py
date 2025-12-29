from fastapi import FastAPI
import redis



app = FastAPI()

redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)




@app.get("/")
def root():
    redis_client.incr("count")
    count = redis_client.get("count")

    return {"message": "FastAPI + MongoEngine", "visits": count}


