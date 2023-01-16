# Credit to Medium article
# https://kevinjnguyen.medium.com/scraping-hashtags-on-instagram-python-and-instaloader-subtle-clothing-collection-a50c7c229c95

import threading
from instaloader import Instaloader, Profile
# import engagement
import pickle
import datetime

loader = Instaloader()
NUM_POSTS = 10
post_date = datetime.datetime.now()
post_data = []
post_vid_yn = False

def get_hashtags_posts(query):
    posts = loader.get_hashtag_posts(query)
    users = {}
    count = 0
    for post in posts:
        profile = post.owner_profile
        post_date = post.date_utc
        post_vid_yn = post.is_video
        if profile.username not in users:
            # summary = engagement.get_summary(profile)
            # users[profile.username] = summary
            count += 1
            print('{}: {}, {}, {}'.format(count, profile.username, post_date, post_vid_yn))
            if count == NUM_POSTS:
                break
    return users, post_date

if __name__ == "__main__":
    hashtag = "projecttikka"
    users = get_hashtags_posts(hashtag)
    # post_data = get_hashtags_posts(hashtag)
    # print(users)
    # print(post_data)