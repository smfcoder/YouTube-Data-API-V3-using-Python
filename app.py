# pip install --upgrade google-api-python-client
from googleapiclient.discovery import build
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_video_details(video_id):
    youtube = build('youtube', 'v3', developerKey=config['CREDS']['dev_key'])
    request = youtube.videos().list(part='snippet,statistics', id=video_id)
    response = request.execute()
    return response

def print_video_details(details):
    title = details['items'][0]['snippet']['title']
    view_count = details['items'][0]['statistics']['viewCount']
    like_count = details['items'][0]['statistics']['likeCount']
    print(f'Title: {title}')
    print(f'View count: {view_count}')
    print(f'Like count: {like_count}')


video_id = '4sYPuSi8FVw'
details = get_video_details(video_id)
print_video_details(details)