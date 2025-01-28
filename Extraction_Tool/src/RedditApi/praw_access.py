import praw
from .reddit_user_config import (
    reddit_client_id,
    reddit_client_secret,
    reddit_user_agent,
)

# these a the default values in reddit_user_config, I use them to check if you changed the config correctly in reddit_user_config
default_client_id = "YourClientID"
default_client_secret = "YourClientSecret"
default_user_agent = "YourApplicationName/YourVersion by YourRedditUserName"


class RedditAccess:

    if not reddit_client_id or reddit_client_id is (default_client_id):
        raise Exception(
            "Please generate a Reddit client ID on https://www.reddit.com/prefs/apps. See explanation in project README to find out more."
        )
    if not reddit_client_secret or reddit_client_secret is (default_client_secret):
        raise Exception(
            "Please generate a Reddit secret ID on https://www.reddit.com/prefs/apps. See explanation in project README to find out more."
        )
    if not reddit_user_agent or reddit_user_agent is (default_user_agent):
        raise Exception(
            "Please generate a Reddit user agent on https://www.reddit.com/prefs/apps. See explanation in project README to find out more."
        )

    accessor = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent=reddit_user_agent,
    )
