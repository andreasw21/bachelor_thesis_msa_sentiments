from dataclasses import dataclass
from typing import List
from datetime import datetime, date


@dataclass
class Comment:
    """Object for saving a comment."""

    id: str
    creation_date: date
    content: str

    @classmethod
    def create_from_reddit_comment(cls, comment):
        return cls(
            id=comment.id,
            creation_date=datetime.fromtimestamp(comment.created_utc),
            content=comment.body,
        )

    @classmethod
    def create_from_hn_comment(cls, hn_response):
        post_creation_date = datetime.fromtimestamp(hn_response["created_at_i"]).date()
        post_content = (
            hn_response["_highlightResult"]
            .get("comment_text", {})
            .get("value", "No content available.")
        )

        return Comment(
            id=hn_response["objectID"],
            creation_date=post_creation_date,
            content=post_content,
        )


@dataclass
class Discussion:
    """Object for saving a discussion."""

    from src.HackerNewsApi.hn_story_type import HN_Story

    id: str
    source: str
    creation_date: date
    title: str
    content: str
    comments: List["Comment"]

    @classmethod
    def create_from_hn_response(cls, story: HN_Story, comment_list: List[Comment]):

        post_source = "HackerNews"
        post_creation_date = story.created
        post_content = story.content

        return Discussion(
            id=story.id,
            source=post_source,
            creation_date=post_creation_date,
            title=story.title,
            content=post_content,
            comments=comment_list,
        )

    from src.RedditApi.reddit_post_type import RedditPost

    @classmethod
    def create_from_reddit_post(
        cls, reddit_post: RedditPost, comment_list: List[Comment]
    ):
        post_source = "Reddit"

        return Discussion(
            id=reddit_post.id,
            source=post_source,
            creation_date=reddit_post.created,
            title=reddit_post.title,
            content=reddit_post.content,
            comments=comment_list,
        )
