from collections import Counter
from difflib import SequenceMatcher

import bs4

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as f:
        bs = bs4.BeautifulSoup(f)
    return [cat.text.strip().replace('-', ' ').lower() for cat in bs.find_all('category')]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return (Counter(tags).most_common(TOP_NUMBER))


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    return [(w1, w2) for w1 in tags for w2 in tags if w1 < w2 and SequenceMatcher(None, w1, w2).ratio() > SIMILAR]


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
