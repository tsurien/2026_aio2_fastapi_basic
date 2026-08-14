from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/slow-async")
async def slow_async():
    # async 방식의 대기시간 측정
    await asyncio.sleep(3) # 비동기를 기다려주는 함수
    return {"type": "block", "message": "3초 대기 완료"}

@app.get("/slow-block")
async def slow_block():
    # sync 방식의 대기시간 측정
    time.sleep(3) # 그냥 무작정 3초 기다려!
    return {"type": "block", "message": "3초 대기 완료"}
