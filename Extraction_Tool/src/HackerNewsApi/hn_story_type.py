from dataclasses import dataclass
from datetime import date, datetime, timezone
import json
from typing import List, Any


@dataclass
class HN_Story:
    """
    A data class representing a Hacker News Story.

    Attributes:
        id (str): The id of the Hacker News Story.
        title (str): The title of the Hacker News Story.
        score (int): The ponits (upvotes) of the Hacker News Story.
        created (date): The creation date of the Hacker News Story.
        content (str): The content of the Hacker News Story, or the URL to the article.
        num_comments (int): Number of comments under the story
    """

    id: str
    title: str
    score: int
    created: date
    content: str
    num_comments: int
