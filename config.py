import os

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rohitplayer87089:rohit870@cluster0.4wt927p.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "neon1")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "rglinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "cedfe548e9b4ac8d706ea4e23b86e13a1eaaaa9c")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 57600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/TutorialsNG/5") # shareus ka tut_vid he
