from googleapiclient.discovery import build
from config import API_KEY

def get_channel_videos(channel_id, youtube):
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()

    uploads_playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=uploads_playlist_id,
                                       part='snippet',
                                       pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break  
    return videos

def get_video_title(video_data):
    return video_data['snippet']['title']

def get_video_url(video_data):
    video_id = video_data['snippet']['resourceId']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}"

def get_videos_titles(channel_id, youtube):
    videos = get_channel_videos(channel_id, youtube)
    video_titles = [get_video_title(video) for video in videos]
    return video_titles

def get_videos_urls(channel_id, youtube):
    videos = get_channel_videos(channel_id, youtube)
    video_urls = [get_video_url(video) for video in videos]
    return video_urls

if __name__ == '__main__':
    youtube = build('youtube', 'v3', developerKey=API_KEY)

