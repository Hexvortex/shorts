import os
import csv
import time
import openai
import time
from text_to_speech import text_to_speech,get_audio_file_url,download_audio_file
from image_grabber import pexel_search_image,download_image_file
from subtitle_generator.subtitle_generator import transcribe_audio
from api_keys import api_key

from affmpeg import generate_video  

 
openai.api_key = api_key.chatgpt_api_key


        


def read_chatgpt_dumps_article_file():
    result=''
    with open('chatgpt_dumps/article.txt') as f:
        result = f.read()
    print(result)
    return result

def read_chatgpt_dumps_image_string_file():
    
    # opening the file in read mode
    my_file = open("chatgpt_dumps/image_prompt.txt", "r")
    
    # reading the file
    data = my_file.read()
    
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    data_into_list = data.split("\n")
    print(data_into_list)
    my_file.close()
    return data_into_list

def call_and_downlaod_image_one_by_one():
    string_list=read_chatgpt_dumps_image_string_file()
    print(type(string_list))
    # Get length_of_list  to pass it to pexel_search_image function to reset counter to 0 so to overrite image files name
    len_of_list=len(string_list)
    
    for i in range(len(string_list)):
        download_image_file(pexel_search_image(string_list[i]),len_of_list)
        print(f"Downloading image ...  {[i]}")
        
        
result = ""

def chatgpt_content_generation(content):
    global result  # Declare result as global
    prompts = f'{content} in short and not more than 120 words.Please follow my 120 words rule.'


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": prompts},
        ]
    )

    result = response.choices[0].message.content
    
        # Create the chatgpt_dumps folder if it doesn't exist
    if not os.path.exists("chatgpt_dumps"):
        os.makedirs("chatgpt_dumps")

    # Write the result to the article.txt file
    with open("chatgpt_dumps/article.txt", "w") as file:
        file.write(result)
    
    
image_prompt=''    
def chatgpt_image_prompt_generation(result):
    global image_prompt  # Declare result as global
    content = result
     
    prompt = f'write 12 image search prompts for {content} and when writing image prompts please dont include any unnecessary details like here is a image prompt or like i am AI chatbot, only write image prompt as told so.Follow my rules strictly'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": prompt},
        ]
    )

    image_prompt = response.choices[0].message.content
    
        # Create the chatgpt_dumps folder if it doesn't exist
    if not os.path.exists("chatgpt_dumps"):
        os.makedirs("chatgpt_dumps")

    # Write the image_prompt to the image_prompt.txt file
    with open("chatgpt_dumps/image_prompt.txt", "w") as file:
        file.write(image_prompt)
        
    input_file = "chatgpt_dumps/image_prompt.txt"
    output_file = "chatgpt_dumps/image_prompt.txt"

    with open(input_file, "r") as file:
        lines = file.readlines()

    # Remove numbering from each line
    lines = [line.split('. ', 1)[-1] for line in lines]

    with open(output_file, "w") as file:
        file.writelines(lines)
        
        
        

        
        
title = ""
def chatgpt_youtube_title_generation(result):
    global title  # Declare result as global
    content=result
    prompt = f'Write youtube title for {content} and it should one line and should best and attractive for users '



    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": prompt},
        ]
    )

    title = response.choices[0].message.content
    updated_title = title.replace('"', '')
    
        # Create the chatgpt_dumps folder if it doesn't exist
    if not os.path.exists("chatgpt_dumps"):
        os.makedirs("chatgpt_dumps")

    # Write the result to the article.txt file
    with open("chatgpt_dumps/ytxtitle.txt", "w") as file:
        file.write(updated_title)
        
description = ""
def chatgpt_youtube_description_generation(result):
    global description  # Declare result as global
    content=result
    prompt = f'Write short youtube description for {content} content and it should be best and attractive for users '



    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": prompt},
        ]
    )

    description = response.choices[0].message.content
    
        # Create the chatgpt_dumps folder if it doesn't exist
    if not os.path.exists("chatgpt_dumps"):
        os.makedirs("chatgpt_dumps")

    # Write the result to the article.txt file
    with open("chatgpt_dumps/description.txt", "w") as file:
        file.write(description)
        
keywords = ""
def chatgpt_youtube_keywords_generation(result):
    global keywords  # Declare result as global
    content=result
    prompt = f'Write 7 short one word youtube keywords for {content} content and it should be best and attractive for users '



    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": prompt},
        ]
    )

    description = response.choices[0].message.content
    
        # Create the chatgpt_dumps folder if it doesn't exist
    if not os.path.exists("chatgpt_dumps"):
        os.makedirs("chatgpt_dumps")

    # Write the result to the article.txt file
    with open("chatgpt_dumps/keywords.txt", "w") as file:
        file.write(description)
        
    input_file = "chatgpt_dumps/keywords.txt"
    output_file = "chatgpt_dumps/keywords.txt"

    with open(input_file, "r") as file:
        lines = file.readlines()

    # Remove numbering from each line
    lines = [line.split('. ', 1)[-1] for line in lines]

    with open(output_file, "w") as file:
        file.writelines(lines)

 
#combines each function and transforms them into final video        
def video_transformer():
     download_audio_file(get_audio_file_url(text_to_speech(read_chatgpt_dumps_article_file())))
     call_and_downlaod_image_one_by_one()
     transcribe_audio()
     generate_video()
     
def read_csv_rows():
    hours = float(input("Enter the video upload duration in hours: "))
    
    # Convert hours to seconds
    seconds = hours * 3600
    
    filename = 'topic.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                # print(*row)  # Print each item in the row separated by space
                
                chatgpt_content_generation(*row)
                print(result)
                print("Guessing image prompt hold on .. .. .. .. .. ")
                chatgpt_image_prompt_generation(result)
                print(image_prompt)
                time.sleep(20)
                print("Generating youtube title")
                chatgpt_youtube_title_generation(result)
                time.sleep(20)
                print("Generating youtube description")
                chatgpt_youtube_description_generation(result)
                time.sleep(20)
                print("Generating youtube keywords")
                chatgpt_youtube_keywords_generation(result)
                time.sleep(20)
                video_transformer()
                print(f'Video upload will continue after {hours} hrs')
                time.sleep(seconds)

read_csv_rows()
 




 