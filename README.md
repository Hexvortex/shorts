
<a name="readme-top"></a>





<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Imagine generating and uploading engaging YouTube Shorts without having to spend countless hours in video editing software. Our tool automates the video creation process from start to finish. Just provide a list of topics via a CSV file and let the tool do the rest: create, generate, and upload each video to YouTube - all while you relax, sip your coffee, and watch your content library grow!

Check out my youtube channel for example videos : https://www.youtube.com/channel/UC7zOHk1gj7ElntRNhp3XxmA

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python: Forms the robust backbone, managing video generation, editing, and uploading.
* ChatGPT: Infuses life into the videos by generating articulate and enthralling narrations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python
* pip
* windows 64 bit (Fully tested)
* Linux (Also runs on linux havent tested extensively)
* ChatGPT API key
* Play.ht API key (https://play.ht/)
* pexels.com API Key (https://www.pexels.com/)
* Youtube API key (follow this tutorial to grab api key https://www.youtube.com/watch?v=eq-mjehACe4 )

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Hexvortex/shorts.git
   ```
2. create and activate python virtualenv
   
3. Enter API keys in api_keys.txt file
   
   ![api_keys(3)](https://github.com/Hexvortex/shorts/assets/66158651/336f8985-9ae9-4c93-90b2-e5a7842c1d2a)
   
4. Open client_secrets.json file and enter Youtube video upload API key

    ![client_secrets](https://github.com/Hexvortex/shorts/assets/66158651/1fbe2997-6c69-4f8e-a106-10509b559164)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Open topic.csv file with notepad or any other tool and enter your topic as shown in image below.
   
    ![topic](https://github.com/Hexvortex/shorts/assets/66158651/88278e87-37fd-4449-ae9f-daef1df41935)

2. Open powershell in current working directory and type
   ```bash
    python3 .\algo.py
   ```
3. Enter video generation and upload durations between each topics

4. If needed google will ask for authentication to youtube channel please procced with it to upload video to youtube .This is one time requirement.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Aim & Purpose

Our tool is not merely a video generation utility; it is a vessel that carries your message to the world without demanding technical expertise in video creation from you. It's designed to:

  1. Enhance Productivity: Minimize time and effort spent on video production and channel management.
  2. Consistent Content Deployment: Maintain a consistent content upload schedule on YouTube, enhancing viewer engagement and channel growth.
  3. Accessible to All: Be it a content creator, a marketer, or an entrepreneur - anyone can use this tool to enhance their digital presence.
  4. Limitless Scalability: No matter if you have 10 topics or 1000, effortlessly create and manage a vast array of content.


                               Handcrafted  with ❤️ in Bharat 

