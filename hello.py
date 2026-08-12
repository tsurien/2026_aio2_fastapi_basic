from fastapi import FastAPI

app = FastAPI() # 앱 생성

@app.get("/") # 기능 추가
def read_root(): # 맨 꼭대기 = root
    return {"message":"Hello World!!!"}
