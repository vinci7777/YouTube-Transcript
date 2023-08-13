# YouTube-Transcript
To make this work please first run: 
pip install youtube-transcript-api

This is a Python API that I'm using for this project to get transcription from YouTube videos: https://pypi.org/project/youtube-transcript-api/#api

Also, please remember to update the values of API_KEY (YouTube API Key), USER_CHANNEL_ID, and DATABASE_URL.

If you are not able to find the user's channel id, you can convert the channel's username to id here: https://commentpicker.com/youtube-channel-id.php.

The database that I used for this project is PostgreSQL, so the value of the DATABASE_URL for me was something like: DATABASE_URL = "postgresql://postgres:postgres@localhost/hamza-ai"
