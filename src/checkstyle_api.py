from fastapi import FastAPI
from pydantic import BaseModel

import subprocess
import os

class File(BaseModel):
    text: str

CS_JAR_PATH = os.getcwd() + "/checkstyle/target/"
CS_JAR_NAME = "checkstyle-10.7.1-SNAPSHOT-all.jar"
CS_CHECK_PATH = os.getcwd() + "/checkstyle/src/main/resources/"
CS_CHECK_NAME = "cse123_checks.xml"

app = FastAPI()

def parse_error_out(error: str):
    error = error.replace("Starting audit...", "")
    error = error.replace("Audit done.\n", "")
    error_list = []

    for e in error.strip().split("\n"):
        error_list.append(e)
    
    return error_list

@app.post("/")
async def root(file: File):

    with open("temp.java", "w") as f:
        f.write(file.text)

    print("=================================================")
    print(file.text)
    result = subprocess.run(["java", "-jar", CS_JAR_PATH + CS_JAR_NAME, "-c", CS_CHECK_PATH + CS_CHECK_NAME, "temp.java"], capture_output=True)
    print(result)

    os.remove("temp.java")

    return {"message": parse_error_out(result.stdout.decode())}
