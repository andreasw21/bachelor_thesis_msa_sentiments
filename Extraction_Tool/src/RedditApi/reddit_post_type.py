from dataclasses import dataclass
import datetime
from typing import List, Any

import praw


@dataclass
class RedditPost:
    """
    A data class representing a Reddit post.

    Attributes:
        id (str): The id of the Reddit post.
        title (str): The title of the Reddit post.
        score (int): The score (upvotes/downvotes) of the post.
        created (date): The creation date of the post.
        subreddit (str): The subreddit where the post was submitted.
        content: (str):The submissions selftext or an url if a link post
        flairs (List[str]): A list of flairs associated with the post
        num_comments: (int): The number of comments under a Reddit Post
    """

    id: str
    title: str
    score: int
    created: datetime.date
    subreddit: str
    content: str
    flairs: List[str]
    num_comments: int

    @classmethod
    def create_reddit_post_from_submission(
        cls,
        submission: praw.models.Submission,
    ):

        if submission.is_self:
            content = submission.selftext
        else:
            content = submission.url

        return RedditPost(
            id=submission.id,
            title=submission.title,
            score=submission.score,
            created=datetime.datetime.fromtimestamp(
                submission.created_utc, tz=datetime.timezone.utc
            ).date(),
            subreddit=submission.subreddit.display_name,
            content=content,
            flairs=([submission.link_flair_text] if submission.link_flair_text else []),
            num_comments=submission.num_comments,
        )
