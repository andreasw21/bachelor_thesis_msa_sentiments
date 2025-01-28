# Microservice post extraction

## Project Overview
The **microservice_post_extraction** project is a tool for extracting, filtering, and preprocessing posts from Reddit and Hackernews. 
The processed posts are saved in the **Discussions** folder. Each Discussion is in a extra csv file. The files are in subfolders that reflect the original posts creation date.

Details about the project and the implementation can be found in the Bachelor's thesis.

## Requirements
- Python 3.12.4 was used for development
- Dependencies in "requirements.txt" (pip install -r requirements.txt)

## How to get Reddit Access Token
FOllow the steps in https://www.educative.io/courses/reddit-api-python/get-started-with-the-reddit-api#Get-the-API-tokens, which can be summed up like this:

1. Login with a Reddit Account to https://www.reddit.com/prefs/apps
2. Click on the "are you a developer? create an app..." button.
3. Create application
    - choose "WebApp"
    - as redirect URL you can put https://localhost:8080/reddit, but it should not matter what you put here
4. Put your secret (In German at "geheim") and your id (Can be found under "Netzanwendung") into the file reddit_user_config.py

## How to run
 Make sure you updated RedditApi/reddit_user_config.py with your reddit credentials.
 Then open a Terminal in project\microserviceAnalysis\ExtractionTool and run: 
 - py -m src.main
    - to run the main end extract the posts
     
- pytest
    - to run the unit tests
