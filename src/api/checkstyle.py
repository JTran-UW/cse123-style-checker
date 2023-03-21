from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import subprocess
import os

class File(BaseModel):
    text: str
    check_name: str

CS_JAR_PATH = os.getcwd() + "/checkstyle/target/"
CS_JAR_NAME = "checkstyle-10.7.1-SNAPSHOT-all.jar"
CS_CHECK_PATH = os.getcwd() + "/checkstyle/src/main/resources/"

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def parse_error_out(error: str):
    error = error.replace("Starting audit...\n", "")
    error = error.replace("Audit done.\n", "")
    error = error.strip().split("\n")
    if "" in error:
        error.remove("")

    error_list = []

    for e in error:
        e_specs = {}

        # For line type messages
        if e.count(":") == 2:
            _, e_specs["line"], message = e.split(":")
            e_specs["col"] = 0
        else:
            _, e_specs["line"], e_specs["col"], message = e.split(":", 3)

        split_message = message.split("[")
        e_specs["type"] = split_message[-1][:-1]
        e_specs["message"] = "".join(split_message[:-1]).strip()
        e_specs["full_message"] = e

        error_list.append(e_specs)
    
    return error_list

import json

@app.post("/")
async def root(file: File):

    with open("temp.java", "w") as f:
        f.write(file.text)

    print("=================================================")
    print(file.text)
    result = subprocess.run(["java", "-jar", CS_JAR_PATH + CS_JAR_NAME, "-c", CS_CHECK_PATH + file.check_name + ".xml", "temp.java"], capture_output=True)
    print(result)

    os.remove("temp.java")
    
    if result.stderr.decode()[:20] != "Checkstyle ends with" and len(result.stderr) != 0:
        raise HTTPException(status_code=422, detail="Provided file could not be parsed.")

    return {"errors": parse_error_out(result.stdout.decode())}
