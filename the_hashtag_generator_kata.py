def generate_hashtag(s):
    hashtag = '#'+s.title().strip('. ').replace(' ', '')
    if (len(hashtag) <= 140 and len(hashtag) > 1):
        return hashtag
    else:
        return False
