import subprocess
import os
from youtube_uploader.upload_video import get_authenticated_service,initialize_upload
import time

from googleapiclient.errors import HttpError
 



def generate_video():



    if not os.path.exists("generated_video"):
        os.makedirs("generated_video")
        
    path = 'generated_video'
    file_path_for_title = 'chatgpt_dumps/ytxtitle.txt'
    file_path_for_keywords = 'chatgpt_dumps/keywords.txt'
    file_path_for_description = 'chatgpt_dumps/description.txt'

    with open(file_path_for_title, 'r') as file:
        # Read the contents of the file
        yt_title = file.read().strip()
         

    with open(file_path_for_keywords, 'r') as file:
        # Read the contents of the file
        yt_keywords = file.read().strip()

    with open(file_path_for_description, 'r') as file:
        # Read the contents of the file
        yt_description = file.read().strip()


    # sf=64bit

    video_command = video_command = f'ffmpeg.exe -y -framerate 1/5 -i stock_image/input_%03d.jpeg -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -r 25 -c:v libx264 -pix_fmt yuv420p -b:v 500k -s 1080x1920 {path}/output.mp4'
    audio_command = f'ffmpeg.exe -y -i {path}/output.mp4 -i audio/audio_file.mp3 -c:v copy -c:a aac -shortest {path}/final_output.mp4'
    subtitle_command = f'ffmpeg.exe -y -i {path}/final_output.mp4 -vf "subtitles=srt/audio_subtitle.srt" -c:a copy {path}/mango.mp4'



    # Execute video_command
    subprocess.run(video_command, shell=True, check=True)

    # Execute audio_command
    subprocess.run(audio_command, shell=True, check=True)

    # Execute subtitle_command
    subprocess.run(subtitle_command, shell=True, check=True)

    # Remove output.mp4
    os.remove(f'{path}/output.mp4')
    # Remove final_output.mp4
    os.remove(f'{path}/final_output.mp4')

    print("Video generated successfully 😊")
    time.sleep(10)
    print("Uploading video to YouTube, please wait...")
    # upload_video(f'{path}/mango.mp4', yt_title, yt_description, yt_keywords, "22", "public")



    args = {
        "file": f'{path}/mango.mp4',
        "title": yt_title,
        "description": yt_description,
        "keywords": yt_keywords,
        "category": "22",
        "privacyStatus": "public"
    }


    if not os.path.exists(args["file"]):
        exit("Please specify a valid file using the --file= parameter.")
 
    youtube = get_authenticated_service()
    try:
        initialize_upload(youtube, args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))



