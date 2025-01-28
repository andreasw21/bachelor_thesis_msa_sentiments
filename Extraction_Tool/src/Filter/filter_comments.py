from typing import List

from src.discussion_dataclasses import Comment, Discussion


def filter_comments_for_discussions(
    discussions: List["Discussion"],
    keyword: str = "microservice",
) -> List["Discussion"]:
    """Filters discussions based on a keyword and a minimum number of comments."""
    filtered_discussions = []
    for discussion in discussions:
        discussion.comments = filter_comments(discussion.comments, keyword)
        filtered_discussions.append(discussion)
    return filtered_discussions


def filter_comments(
    comments: List["Comment"], keyword: str = "microservice"
) -> List["Comment"]:
    """Filters comments based on a minimum word count and a keyword."""
    not_deleted_comments = [comment for comment in comments if not isDeleted(comment)]
    long_enough_comments = skip_short_comments(not_deleted_comments)
    return filter_by_keyword(long_enough_comments, keyword)


def filter_by_keyword(comments: List["Comment"], keyword: str) -> List["Comment"]:
    """Filters comments within a discussion based on a keyword."""
    relevant_comments = [
        comment for comment in comments if keyword.lower() in comment.content.lower()
    ]
    return relevant_comments


def skip_short_comments(comments: List[Comment], min_words: int = 4) -> List[Comment]:
    """Filters out comments that are shorter than the minimum word count."""
    return [
        comment for comment in comments if len(comment.content.split()) >= min_words
    ]


def isDeleted(comment):
    return comment.content == "[deleted]" and comment.content == "[removed]"
