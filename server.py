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

def is_prime(num: int):
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

def count_primes(num: int):
    count = 1
    for i in range(3, num + 1, 2):
        if is_prime(i):
            count += 1

    return count


@app.get("/count/prime/{num}")
async def get_count_primes(num: int):
    return count_primes(num)
