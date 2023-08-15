from apiclient.discovery import build
from config import API_KEY, USER_CHANNEL_ID
from database_connection import Video, session
from get_videos_data import get_channel_videos, get_video_title, get_video_url

if __name__ == '__main__':
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    channel_id = USER_CHANNEL_ID
    
    videos = get_channel_videos(channel_id, youtube)
    print(f"Total videos fetched: {len(videos)}")

    for video in videos:
        video_title = get_video_title(video)
        video_url = get_video_url(video)

        # Check if the video URL already exists in the database
        existing_video = session.query(Video).filter_by(url=video_url).first()
        
        if existing_video is None:
            new_video = Video(title=video_title, url=video_url)
            session.add(new_video)
            # print(f"Added video: {video_title}")
            print(f"Added video: {video_title.encode('utf-8')}")
        else:
            print(f"Video already exists: {video_title.encode('utf-8')}")
        
    try:
        session.commit()
        print("Commit successful.")
    except Exception as e:
        print(f"Error during commit: {e}")
        session.rollback()
    finally:
        session.close()
