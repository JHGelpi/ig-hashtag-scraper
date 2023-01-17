# Credit to Medium article
# https://kevinjnguyen.medium.com/scraping-hashtags-on-instagram-python-and-instaloader-subtle-clothing-collection-a50c7c229c95

import threading
from instaloader import Instaloader, Profile
import instaloader
# import engagement
# import pickle
import datetime
from datetime import date
from datetime import datetime
import pandas as pd

# L = instaloader.Instaloader()
# L.login('USERNAME', 'PASSWORD')

loader = Instaloader()
NUM_POSTS = 10
start_date = datetime(2022, 5, 1)
end_date = datetime(2022, 5, 31, 23, 59, 59, 0)
post_date = datetime.now()
post_data = []
post_vid_yn = False

def get_hashtags_posts(query):
    posts = loader.get_hashtag_posts(query)
    users = {}
    count = 0
    for post in posts:
        post_date = post.date_utc
        if start_date <= post_date <= end_date:
            post_vid_yn = post.is_video
            profile = post.owner_profile
            if profile.username not in users:
                # summary = engagement.get_summary(profile)
                # users[profile.username] = summary
                count += 1
                print('{}: {}, {}, {}'.format(count, profile.username, post_date, post_vid_yn))
                #post_data[]
                if count == NUM_POSTS:
                    break
    return users, post_date, post_vid_yn

if __name__ == "__main__":
    hashtag = "projecttikka"
    # hashtag = "selftapemay2022"
    users = get_hashtags_posts(hashtag)
    # post_data = get_hashtags_posts(hashtag)
    # print(users)
    # print(post_data)