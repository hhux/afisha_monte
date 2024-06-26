from typing import Dict
import os
from facebook_scraper import get_posts

FB_LOGIN = os.environ['FB_LOGIN']
FB_PASSWORD = os.environ['FB_PASSWORD']
# FB_LOGIN = 'dmitriydada8@gmail.com'
# FB_PASSWORD = 'Larry345777'


def get_last_fb_post(url: str) -> Dict:
    posts = get_posts(
        post_urls=[url],
        credentials=(FB_LOGIN, FB_PASSWORD),
        options={"comments": True},
        # cookies='cookie.txt'
    )
    return next(posts, {})
