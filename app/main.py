from fastapi import FastAPI
from .services import SomeService
from .schemas import ExampleSchema

app = FastAPI()

@app.get("/example1", response_model=ExampleSchema)
def read_example1():
    result = SomeService.get_example1()
    return result

@app.get("/example2", response_model=ExampleSchema)
def read_example2():
    result = SomeService.get_example2()
    return result

@app.get("/example3", response_model=ExampleSchema)
def read_example3():
    result = SomeService.get_example3()
    return result
