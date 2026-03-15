import os

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://anujedits:anujedits@cluster0.tc5voup.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Anujedits")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "09c3f9bc3a8b121b1e6b82a954e59da523dd188e")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/ultroid_official/18") # shareus ka tut_vid he 
