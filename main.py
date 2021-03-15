# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import requests.auth
import praw
import json
from praw.models import MoreComments
#   How to debug PRAW auth comments:
#   from bboe Perhaps your authentication isn't set up properly.
# What does print(reddit.user.me()) result in? If you get an exception you haven't successfully authenticated.


if __name__ == '__main__':
    client_auth = requests.auth.HTTPBasicAuth('66AfkXHprP5E5Q', 'U19IWBHU4Ukg5onuqRBU3JbJlsdoXA')
    post_data = {"grant_type": "password", "username": "CandyEnvironmental", "password": "_Qa]Lk_sRF8Slr=>RolO>)Bqn&>_x%sL00An-H#?dY3K4zvEs1WqA7CEUyMU&kdr"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    reddit = response.json()


    reddit = praw.Reddit(
        client_id="66AfkXHprP5E5Q",
        client_secret="U19IWBHU4Ukg5onuqRBU3JbJlsdoXA",
        password="_Qa]Lk_sRF8Slr=>RolO>)Bqn&>_x%sL00An-H#?dY3K4zvEs1WqA7CEUyMU&kdr",
        user_agent="USERAGENT",
        username="CandyEnvironmental",
    )
    for submission in reddit.front.hot():
        print(submission)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # headers = {"Authorization": "bearer 546149535203-ebZe4rP46dQfnebQB3NWXbNLqKFphw",
    #            "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    # response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    # reddit = response.json()