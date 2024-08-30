from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os

class ScriptItem(BaseModel):
    file_path: str

app = FastAPI()

@app.post("/execute-script/")
async def execute_script(item: ScriptItem):
    file_path = item.file_path

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=400, detail="File does not exist.")
    
    # Check if the file is executable
    if not os.access(file_path, os.X_OK):
        raise HTTPException(status_code=400, detail="File is not executable.")

    try:
        # Execute the shell script at the given file path
        result = subprocess.run(
            ["/bin/bash", file_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return {
            "status": "success",
            "output": result.stdout.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        # Return an error if the script fails to execute
        raise HTTPException(
            status_code=500, 
            detail=f"Script execution failed: {e.stderr.decode('utf-8')}"
        )

@app.get("/test")
async def test():
    try:
        return {"Hello": "World.............."}
    except subprocess.CalledProcessError as e:
        # Return an error if the script fails to execute
        raise HTTPException(status_code=500, detail=f"Script failed: {e.stderr.decode('utf-8')}")
