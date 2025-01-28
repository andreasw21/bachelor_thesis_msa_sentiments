from typing import List

from src.discussion_dataclasses import Discussion
from .keywords import relevant_keywords, irrelevant_keywords


def is_relevant_post(post: Discussion, threshold: int) -> bool:
    """Checks if a post is relevant based on number of comments, points (from community upvotes/downvotes) and relevancy of the post title."""

    min_num_comments = 50
    if post.num_comments < min_num_comments:
        return False

    if post.score <= threshold:
        return False

    return relevant_title(post.title)


def relevant_title(title: str) -> bool:
    """Checks if the title is relevant based on keywords or sentiment."""
    if any(keyword in title.lower() for keyword in irrelevant_keywords):
        return False

    if any(keyword in title.lower() for keyword in relevant_keywords):
        return True

    return True




def filter_discussions_with_too_few_comments(
    discussions: List["Discussion"], min_comments: int = 25
) -> List["Discussion"]:
    """
    Filters out discussions that have fewer than the minimum number of comments.
    """
    filtered_discussions = [
        discussion
        for discussion in discussions
        if len(discussion.comments) >= min_comments
    ]
    return filtered_discussions
