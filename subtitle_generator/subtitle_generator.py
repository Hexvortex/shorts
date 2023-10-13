import whisper
import hashlib
from pytube import YouTube
from datetime import timedelta
import os


def transcribe_audio():
    model = whisper.load_model("base")  # Change this to your desired model
    print("Whisper model loaded.")
    
    audio = 'audio/audio_file.mp3'  # Use the audio file path directly
    
    transcribe = model.transcribe(audio)
    
    segments = transcribe['segments']
    
    if not os.path.exists("srt"):
        os.makedirs("srt")
    # srtFilename = os.path.join("srt", "audio_subtitle.srt")
    srtFilename = 'srt/audio_subtitle.srt'

    
    with open(srtFilename, 'w', encoding='utf-8') as srtFile:
        for segment in segments:
            startTime = str(timedelta(seconds=int(segment['start']))) + ',000'
            endTime = str(timedelta(seconds=int(segment['end']))) + ',000'
            text = segment['text']
            segmentId = segment['id'] + 1
            segment_text = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

            srtFile.write(segment_text)

    return srtFilename

 