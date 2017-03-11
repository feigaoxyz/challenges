import csv
import os
from collections import namedtuple

import tweepy

from config import ACCESS_TOKEN, ACCESS_SECRET
from config import CONSUMER_KEY, CONSUMER_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', ['id_str', 'created_at', 'text'])


class UserTweets(object):
    """TODOs:
    - create a tweepy api interface
    - get all tweets for passed in handle
    - optionally get up until 'max_id' tweet id
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    def __init__(self, handle, max_id=None):
        self.handle = handle
        self._auth()

        self.tweets = [Tweet(id_str=status.id_str, created_at=status.created_at, text=status.text.replace('\n', ' '))
                       for status in self._api.user_timeline(self.handle,
                                                             max_id=max_id,
                                                             count=NUM_TWEETS)]
        self._store()

    def _auth(self):
        """Auth twitter api"""
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        self._api = tweepy.API(auth)

    def __len__(self):
        return len(self.tweets)

    def __getitem__(self, item):
        return self.tweets[item]

    def _store(self):
        self.output_file = os.path.join(DEST_DIR, self.handle + '.csv')
        if os.path.exists(self.output_file):
            pass
        with open(self.output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id_str', 'created_at', 'text'])
            writer.writerows(self.tweets)


if __name__ == "__main__":

    for handle in ('pybites', 'techmoneykids', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
