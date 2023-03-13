from facebook_scraper import get_posts
# FB_LOGIN = os.environ['FB_LOGIN']
# FB_PASSWORD = os.environ['FB_PASSWORD']
FB_LOGIN = 'admitry564@gmail.com'
FB_PASSWORD = 'Laka31892'


def get_last_fb_post(url):
    posts = get_posts(
        post_urls=[url],
        credentials=(FB_LOGIN, FB_PASSWORD),
        options={"comments": True},
        # cookies='cookie.txt'
    )
    return next(posts, {})
