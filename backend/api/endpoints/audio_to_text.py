from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import speech_recognition as sr
import shutil
# import os
router = APIRouter()
app = FastAPI()


class AudioData(BaseModel):
    audio: bytes


@router.post("/audio_to_text",tags=["Audio To Text"])
async def audio_to_text(audio: UploadFile = File(...)):
    if not audio:
        raise HTTPException(status_code=400, detail="No file part")

    # Save the uploaded audio file
    with open("16-122828-0002.wav", "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return {"filename": "16-122828-0002.wav", "message": "Audio file uploaded successfully"}


@router.get("/speech_to_text/", tags=["Audio To Text"])
def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        # Capture audio input from the microphone
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use recognizer to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    speech_to_text()
    audio_to_text()



