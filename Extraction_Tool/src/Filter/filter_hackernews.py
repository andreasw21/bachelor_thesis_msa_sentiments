from typing import List

from src.Filter.filter_posts import is_relevant_post
from src.HackerNewsApi.hn_story_type import HN_Story
from src.Utils.domain_extractor import get_domain
from src.Utils.statistics import calculate_third_quartil


IRRELEVANT_DOMAINS = ["github.com", "youtube.com"]


def my_hn_filter(posts: List[HN_Story]) -> List[HN_Story]:
    """Filters relevant Hacker News Posts basend on score, domain and post relevancy."""

    relevant_posts = []

    scores = [post.score for post in posts]
    threshold = calculate_third_quartil(scores)

    for post in posts:
        domain = get_domain(post.content)
        if domain not in IRRELEVANT_DOMAINS:
            if is_relevant_post(post, threshold):
                relevant_posts.append(post)

    return relevant_posts
