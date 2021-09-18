from fastapi import FastAPI 

app = FastAPI()

@app.get("/even/{num}")
async def is_even(num: int):
    '''
    Checks if a number passed is even or not.
    '''
    if num % 2 == 0:
        return {num: "is even"}
    else:
        return {num: "is not even"}