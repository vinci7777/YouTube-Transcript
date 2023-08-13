from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
from youtube_transcript_api import YouTubeTranscriptApi
from appclient.discovery import build
from get_videos_data import get_video_ids
from config import API_KEY, USER_CHANNEL_ID, DATABASE_URL

def main():
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
if __name__ == '__main__':
    main()

