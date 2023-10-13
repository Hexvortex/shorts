 
from pexels_api import API
import os
import requests
from api_keys import api_key


 

def pexel_search_image(search_query):

    # Type your Pexels API
    
    PEXELS_API_KEY = api_key.PEXELS_API_KEY
    
    
    api = API(PEXELS_API_KEY)
    
    api.search(search_query, page=1, results_per_page=1)
    
    photos = api.get_entries()
    
    photo_url=' '
    for photo in photos:
    # Print photographer
    #   print('Photographer: ', photo.photographer)
    #   # Print url
    #   print('Photo url: ', photo.url)
    #   # Print original size url
        photo_url=photo.original
    return photo_url
  
counter=0

def download_image_file(photo_url,length_of_list):
    global counter

    url = photo_url
    directory_path = "stock_image"
    counter += 1
    counter_str = str(counter).zfill(3)  # Convert counter to a 3-digit string with leading zeros

    file_name = f"input_{counter_str}.jpeg"

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
    
    # take length_of_list  to reset counter to 0 so to overrite image files name
    if counter>=length_of_list:
        counter=0
  
# download_image_file(pexel_search_image('An elephant'))



