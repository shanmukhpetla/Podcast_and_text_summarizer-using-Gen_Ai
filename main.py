from fastapi import FastAPI, UploadFile, File
from models import PromptRequest
import services
import os

app = FastAPI()


@app.post("/generate-text/")
async def generate_text(request: PromptRequest):
    return {"response": services.generate_text(request.prompt)}


@app.post("/summarize/")
async def summarize_text(request: PromptRequest):
    return {"summary": services.summarize_text(request.prompt)}


@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Ensure the temp directory exists
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)

    file_path = f"{temp_dir}/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Transcribe the audio
    transcription = services.transcribe_audio(file_path)

    # Summarize the transcription
    summary = services.summarize_text(transcription)

    return {
        "transcription": transcription,
        "summary": summary
    }


@app.post("/moderate/")
async def moderate_text(request: PromptRequest):
    return services.moderate_text(request.prompt)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
