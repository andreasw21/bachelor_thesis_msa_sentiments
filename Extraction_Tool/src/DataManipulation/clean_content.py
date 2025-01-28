import re
from typing import List, Tuple

from src.DataManipulation.special_characters import special_character_list

from src.discussion_dataclasses import Comment, Discussion


# Code is based on:https://alanpbandeira.github.io/stackoverservices/  (code/clean_data.py)
open_tags = [
    r"&#xA;",
    r"&#xD;",
    r"<br>",
    r"<em>",
    r"</em>",
    r"<p>",
    r"</p>",
    r"<ul>",
    r"</ul>",
    r"<li>",
    r"</li>",
    r"<strong>",
    r"</strong>",
    r"<img src=[^>]*>",
    r"<blockquote>",
    r"</blockquote>",
    r"<ol>",
    r"</ol>",
    r"<hrs>" r"<sub>",
    r"</sub>",
    r"<h3>",
    r"</h3>",
    r"<h1>",
    r"</h1>",
    r"<h2>",
    r"</h2>",
    r"<h4>",
    r"</h4>",
    r"<h5>",
    r"</h5>",
    r"<div[^>]*>",
    r"</div>",
    r"<pre>",
    r"</pre>",
    r"<code>",
    r"</code>",
    r"<a href=[^>]*>",
    r"(</a>)",
    r"<br>",
    r"<br/>",
    r"&gt",
    r"\\n",
    r"\\r",
]

closed_tags = [
    (r"<a href=[^>]*>", r"(</a>)"),
    (r"<div[^>]*>", r"(</div>)"),
    (r"<code>", r"</code>"),
    (r"<blockquote>", r"</blockquote>"),
]


def preprocess_discussions(discussions: List["Discussion"]) -> List["Discussion"]:
    """Preprocesses a list of discussions by cleaning comments and fitting discussion content into a single line."""

    for discussion in discussions:
        cleaned_comments = []
        discussion.content = turn_multiple_line_to_single_line(discussion.content)
        for comment in discussion.comments:
            to_lower_case(comment)
            cleaned_comments.append(clean_comment(comment))

        discussion.comments = remove_citations(cleaned_comments)

    return discussions


def to_lower_case(comment: Comment) -> Comment:
    """Converts the content of a comment to lowercase."""
    comment.content = comment.content.lower()
    return comment


def extract_text_between_tags(openingtag: str, closingtag: str, text: str) -> List[str]:
    """Extracts all the content between the specified tags (e.g., <i> and </i>) from a string."""
    pattern = rf"<{openingtag}>(.*?)<\/{closingtag}>"
    return re.findall(pattern, text)


def remove_citations(
    comments: List["Comment"],
) -> List[Comment]:
    """Removes citations that refer to other comments found between <i> tags."""
    all_comments_texts = [comment.content for comment in comments]

    for comment in comments:

        italicized_blocks = extract_text_between_tags("<i>", "</i>", comment.content)
        for block in italicized_blocks:

            word_count = len(block.split())
            if word_count > 3:

                for other_comment_text in all_comments_texts:
                    if block in other_comment_text:

                        remove_block_tag(("<i>", "</i>"), comment.content)
                        break
    return comments


def clean_comment(comment: "Comment") -> Comment:
    """Cleans the content of a comment."""
    clean_content = clean(comment.content)
    clean_content = remove_urls(clean_content)
    comment.content = clean_content
    return comment


def clean(content: str) -> str:
    """
    Cleans the given content by removing block tags and single tags,
    and removes special characters.
    """

    for closed_tag in closed_tags:
        content = remove_block_tag(closed_tag, content)

    for open_tag in open_tags:
        content = remove_single_tag(open_tag, content)

    single_line_text = turn_multiple_line_to_single_line(content)

    cleaned_content = remove_special_characters(single_line_text)

    return cleaned_content


def turn_multiple_line_to_single_line(content: str) -> str:
    """Converts multi-line content into a single line."""
    return " ".join(content.splitlines())


def remove_single_quotes(word: str) -> str:
    """
    Removes single quotes around a word if they exist.
    """
    word = word.strip()
    if len(word) > 1 and word[0] == "'" and word[-1] == "'":
        word = word[1:-1]

    return word


def remove_block_tag(tags_exp: Tuple[str, str], text: str) -> str:
    """
    Removes a block tag and all its enclosed content from the text.
    A block tag has both an opening and closing tag.
    """

    tag_open, tag_close = tags_exp

    while True:
        start_match = re.search(tag_open, text)
        end_match = re.search(tag_close, text)

        if not (start_match and end_match):
            break

        # Remove everything between the opening and closing tag
        text = text[: start_match.start()] + " " + text[end_match.end() :]

    return text


def remove_single_tag(tag_exp: str, text: str) -> str:
    """Removes a single tag (self-closing or unpaired) from the text."""
    while True:
        matched = re.search(tag_exp, text)
        if not matched:
            break
        # Remove the tag
        text = text[: matched.start()] + "" + text[matched.end() :]

    return text


def remove_urls(content: str) -> str:
    """Removes URLs from the given content string."""

    url_pattern = r"http[s]?://\S+|www\.\S+|https?://\S+"

    cleaned_content = re.sub(url_pattern, "", content)

    cleaned_content = re.sub(r"\s+", " ", cleaned_content).strip()

    return cleaned_content


import re


def remove_extra_spaces(content: str) -> str:
    """Removes extra spaces from the given content string so there is never more than 1 space between words."""

    cleaned_content = re.sub(r"\s+", " ", content).strip()

    return cleaned_content


def remove_special_characters(content: str) -> str:
    """Removes special characters from the content, allowing only letters, numbers, and basic punctuation."""

    cleaned_content = content

    for special_character in special_character_list:
        cleaned_content = cleaned_content.replace(special_character, "")

    return cleaned_content.strip()
