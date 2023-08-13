from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "tByVn0whyYc"
sample_video_transcription = YouTubeTranscriptApi.get_transcript(video_id)

data_string = sample_video_transcription.replace("'", "\"")
data_list = json.loads(data_string)

# Now you can save the data_list into a database, for example, a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print("Data saved to data.json")
