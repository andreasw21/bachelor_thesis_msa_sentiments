from datetime import datetime
import json
from typing import List

from src.HackerNewsApi.hn_story_type import HN_Story


def convert_json_to_hn_story(hits: json) -> List["HN_Story"]:
    stories = []

    for hit in hits:
        convert_hit_to_hn_story(stories, hit)

    return stories


def convert_hit_to_hn_story(stories, hit):

    post_content = hit.get("url")  # This works if hit is parsed as a dictionary

    if not post_content:  # if post_content is not a url
        post_content = extract_content(hit)

    stories.append(
        create_hn_story_from_hit(
            hit,
            post_content,
        )
    )


def extract_content(hit):
    if "story_text" in hit:
        if isinstance(hit["story_text"], dict):
            post_content = hit["story_text"].get("value", "No content available")
        else:
            post_content = hit["story_text"]
    else:
        post_content = "No content available"
    return post_content


def create_hn_story_from_hit(hit, post_content):
    post_creation_date = datetime.fromtimestamp(hit["created_at_i"]).date()
    post_points = hit["points"]
    post_num_comments = hit["num_comments"]

    return HN_Story(
        id=hit["objectID"],
        title=hit["title"],
        score=post_points,
        created=post_creation_date,
        content=post_content,
        num_comments=post_num_comments,
    )
