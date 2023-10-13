import requests
import json
import os
import time
from api_keys import api_key


def text_to_speech(content):

    url = "https://play.ht/api/v1/convert"

    payload = {
        "content": [content],
        "voice": "en-US-JennyNeural"
    }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "AUTHORIZATION": api_key.AUTHORIZATION,
        "X-USER-ID": api_key.X_USER_ID
    }

    response = requests.post(url, json=payload, headers=headers)

    response_text=response.text
    response_dict=json.loads(response_text)
    transcription_id = response_dict['transcriptionId']
    print(transcription_id)
    return transcription_id
    

def get_audio_file_url(transcription_id):
    
    url = f'https://play.ht/api/v1/articleStatus?transcriptionId={transcription_id}'

    headers = {
        "accept": "application/json",
        "AUTHORIZATION": "c0992c1fed8447c8b7e11c1d666c5e2f",
        "X-USER-ID": "hteBfjHzFgT9MRZ6ehQ4vT2d8vz2"
    }
    
    print("Converting text to audio ....")
    time.sleep(30)
    response = requests.get(url, headers=headers)

    print(response.text)
    response_text=response.text
    response_dict=json.loads(response_text)
    audioUrl = response_dict['audioUrl']
    print(audioUrl)
    return audioUrl
    
    

def download_audio_file(audioUrl):
    
    url=audioUrl
    directory_path = "audio"
    file_name = "audio_file.mp3"

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, file_name)

    response = requests.get(url)

    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("File downloaded and saved successfully.")
    else:
        print("Failed to download the file. Status code:", response.status_code)
        
        
    



 