from typing import List
from src.Filter.filter_posts import is_relevant_post
from src.RedditApi.reddit_post_type import RedditPost
from src.Utils.statistics import calculate_third_quartil


IRRELEVANT_SUBREDDITS = [
    "dotnet",
    "programmerhumor",
    "sysadmin",
    "cscareerquestions",
    "de_edv",
    "nintendo",
    "aws",
    "django",
    "videos",
    "node",
    "postgresql",
    "springboot",
    "sre",
    "cpp",
    "moonlightstreaming",
    "corporatefacepalm",
    "supabase",
    "kubernetes",
    "clojure",
    "apachekafka",
    "voip",
    "rails",
    "opentelemetry",
    "azure",
    "gradle",
]
IRRELEVANT_FLAIRS = [
    "meme",
    "humor",
    "schizoposting",
    "tutorial",
    "intermediate showcase",
    "cloud firestore",
    "carreira",
]


def my_reddit_filter(posts: List["RedditPost"]) -> List["RedditPost"]:
    """Filters relevant Reddit Posts based on score, subreddit, fölair and post relevancy."""

    relevant_posts = []

    scores = [post.score for post in posts]
    threshold = calculate_third_quartil(scores)

    for post in posts:
        if isRelevantSubreddit(post):
            if hasRelevantFlairs(post):
                if is_relevant_post(post, threshold):
                    relevant_posts.append(post)

    return relevant_posts


def hasRelevantFlairs(post: RedditPost):
    return not any(flair.lower() in IRRELEVANT_FLAIRS for flair in post.flairs)


def isRelevantSubreddit(post: RedditPost):
    return not post.subreddit.lower() in IRRELEVANT_SUBREDDITS
