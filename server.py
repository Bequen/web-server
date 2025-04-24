from fastapi import FastAPI

app = FastAPI()

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

@app.get("/fib/{num}")
async def test(num: int):
    return fib(num)
