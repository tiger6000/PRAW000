# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pprint

import requests
import requests.auth
import praw
import json
from praw.models import MoreComments


#   How to debug PRAW auth comments:
#   from bboe Perhaps your authentication isn't set up properly.
# What does print(reddit.user.me()) result in? If you get an exception you haven't successfully authenticated.
def authentication():
    client_auth = requests.auth.HTTPBasicAuth('66AfkXHprP5E5Q', 'U19IWBHU4Ukg5onuqRBU3JbJlsdoXA')
    post_data = {"grant_type": "password", "username": "CandyEnvironmental",
                 "password": "_Qa]Lk_sRF8Slr=>RolO>)Bqn&>_x%sL00An-H#?dY3K4zvEs1WqA7CEUyMU&kdr"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                             headers=headers)
    r = response.json()

    r = praw.Reddit(
        client_id="66AfkXHprP5E5Q",
        client_secret="U19IWBHU4Ukg5onuqRBU3JbJlsdoXA",
        password="_Qa]Lk_sRF8Slr=>RolO>)Bqn&>_x%sL00An-H#?dY3K4zvEs1WqA7CEUyMU&kdr",
        user_agent="USERAGENT",
        username="CandyEnvironmental",
    )
    return r


if __name__ == '__main__':

    reddit = authentication()
    for submission in reddit.front.hot(limit=1):
        # this prints the attributes
        #pprint.pprint(vars(submission))

        # so the following will print the title of each title on the front hot page : print(submission.title)  - or print(submission.url)

        #So I got the following JSON data... i want to get the description:Watch this video on Streamable.
        #Therefore i use OBJECTsubmission.DICTIONARYsecure_media[KEY1][KEY of KEY1(key2)]
        #'secure_media': {'oembed': {'description': 'Watch this video on Streamable.',
        #print(submission.secure_media['oembed']['description'])

        #This returns a string  'media': {'oembed': {'description': 'Watch this video on Streamable.',
                     # 'height': 338,
                     # 'html': '<iframe class="embedly-embed" '
        #print(submission.secure_media['oembed']['html'][10])



