import datetime
from typing import List, Optional

from src.RedditApi.reddit_post_type import RedditPost
from .praw_access import RedditAccess
import csv
import praw


reddit = RedditAccess.accessor


def reddit_get_comments(
    submission: praw.models.Submission,
) -> List[praw.models.Comment]:
    """
    Fetches all comments for a specific Reddit post.

    :param submission: The Reddit submission to get comments for.
    :return: A list of comments, excluding MoreComments instances.

    Reference: https://praw.readthedocs.io/en/latest/tutorials/comments.html
    """
    # Replace all 'MoreComments' instances with the actual comments
    submission.comments.replace_more(limit=None)
    comments = submission.comments.list()  #  all comments
    num_comments = len(comments)
    print(
        f"{num_comments} comments fetched for a Reddit Thread."  # Note that num_comments may differ cause of deleted comments.
    )
    return comments


def reddit_get_submissions(
    search_term: str, num_posts: Optional[int] = None
) -> List[praw.models.Submission]:
    """
    Retrieves a list of reddit submissions based on a search term.

    :param search_term: Search term to look for.
    :param num_posts: Number of posts to retrieve, defaults to None (all posts).
    :return: A list of reddit submissions.
    """

    submissions = reddit.subreddit("all").search(
        search_term, sort="relevance", time_filter="all", limit=num_posts
    )

    return submissions


def get_posts_then_comments_testing_helper():
    from discussion_dataclasses import Comment

    search_term = "microservices"

    posts = reddit_get_submissions(search_term)

    first_post = posts[0]

    comments = reddit_get_comments(first_post.submission)
    first_comm = Comment.create_from_reddit_comment(comments[0])

    return first_comm


# saveToCsv(comments)


if __name__ == "__main__":
    get_posts_then_comments_testing_helper()
    search_term = "microservices"

    posts = reddit_get_submissions(search_term, 1)
# print(len(posts))
