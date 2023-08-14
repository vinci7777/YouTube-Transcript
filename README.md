# YouTube-Transcript

Before running the project please make sure you run these:

pip install psycopg2

pip install SQLAlchemy

pip install youtube-transcript-api

pip install google-api-python-client



Also, please remember to update the values of variables in the **config.py** file.

If you are not able to find the user's channel id, you can convert the channel's username to id here: _https://commentpicker.com/youtube-channel-id.php._

The database that I used for this project is PostgreSQL, so the value of the DATABASE_URL for me was something like 
**DATABASE_URL = "postgresql://username:password@localhost/databasename"**
