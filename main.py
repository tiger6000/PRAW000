# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import requests.auth
import praw


def grantToken():
    client_auth = requests.auth.HTTPBasicAuth('66AfkXHprP5E5Q', 'U19IWBHU4Ukg5onuqRBU3JbJlsdoXA')
    post_data = {"grant_type": "password", "username": "CandyEnvironmental",
                 "password": "_Qa]Lk_sRF8Slr=>RolO>)Bqn&>_x%sL00An-H#?dY3K4zvEs1WqA7CEUyMU&kdr"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by CandyEnvironmental"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                             headers=headers)
    # Press the green button in the gutter to run the script.
    jsonObject = response.json()
    accessToken = jsonObject['access_token']
    print(jsonObject)
    #return accessToken

def testToken(accessToken):
    headers = {"Authorization": "bearer 546149535203-_dEA-knoVFOgTnbbxsF671lkbPDC_Q",
               "User-Agent": "ChangeMeClient/0.1 by CandyEnvironmental"}
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    jsonObject = response.json()
    print(jsonObject)

def connectToPRAW():
    reddit = praw.Reddit(
        client_id="66AfkXHprP5E5Q",
        client_secret="546149535203-_dEA-knoVFOgTnbbxsF671lkbPDC_Q",
        user_agent="PRAW000/0.1 by CandyEnvironmental - just checking out the api!",
        username="CandyEnvironmental",
        password="_Qa]Lk_sRF8Slr=>RolO>)Bqn&>_x%sL00An-H#?dY3K4zvEs1WqA7CEUyMU&kdr",
    )
    print(reddit.get())

if __name__ == '__main__':
    #grantToken()
    #testToken()
    connectToPRAW()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
