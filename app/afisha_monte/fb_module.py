from facebook_scraper import get_posts

# FB_LOGIN = os.environ['FB_LOGIN']
# FB_PASSWORD = os.environ['FB_PASSWORD']
FB_LOGIN = '+382067365851'
FB_PASSWORD = 'Shtanga228'


def get_last_fb_post(url):
    posts = get_posts(
        post_urls=[url],
        credentials=(FB_LOGIN, FB_PASSWORD),
        options={"comments": True}
    )
    return next(posts, {})
