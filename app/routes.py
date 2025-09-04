from fastapi import APIRouter, UploadFile, File, HTTPException
import os

router = APIRouter()

# ✅ Safer file read - use upload instead of raw path
@router.post("/read_file")
async def read_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        return {"filename": file.filename, "content": contents.decode("utf-8")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"File read error: {str(e)}")