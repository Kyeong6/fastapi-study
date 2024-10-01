from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# long-running I/O bound 작업 시뮬레이션
async def long_running_task():
    # 특정 초동안 수행 시뮬레이션
    # 다른 request 받을 수 있음
    # await를 통한 비동기함수 호출
    await asyncio.sleep(20)
    return {"status": "long_running task completed"}

# 비동기방식
# @app.get("/task")
# async def run_task():
#     # await를 통한 비동기함수 호출
#     result = await long_running_task()
#     return result

# 동기방식: Block 처리가 되어있음
# 일반적으로 동기방식 프레임워크는 ThreadPool을 사용
# @app.get("/task")
# async def run_task():
#     time.sleep(20)
#     return {"status": "long_running task completed"}

# FastAPI에서 ThreadPool 사용
# async를 지우기
@app.get("/task")
def run_task():
    time.sleep(20)
    return {"status": "long_running_task completed"}


@app.get("/quick")
async def quick_response():
    return {"status": "quick response"}