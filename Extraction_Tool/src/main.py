import copy
import threading
import queue

from src.Workflow.hackernews_extractor import HackerNewsExtractor
from src.Workflow.reddit_extraction_workflow import RedditExtractor
from src.DataManipulation.clean_content import preprocess_discussions

from src.Filter.filter_comments import (
    filter_comments_for_discussions,
    skip_short_comments,
)
from src.Filter.filter_posts import filter_discussions_with_too_few_comments

from src.config import MS_SEARCH_TERM

from src.Utils.save_to_file import save_to_csv


def get_discussions_dataset():
    """Gets a fresh discussion dataset by fetching posts from Reddit&Hackernews,
    filtering the Posts,
    preprocessing them
    and saving them in CSV files"""

    discussions_queue = queue.Queue()

    reddit_extractor = RedditExtractor()
    hn_extractor = HackerNewsExtractor()

    reddit_thread_instance = threading.Thread(
        target=reddit_extractor.extract_relevant_discussions,
        args=(MS_SEARCH_TERM, discussions_queue),
    )

    hn_thread_instance = threading.Thread(
        target=hn_extractor.extract_relevant_discussions,
        args=(MS_SEARCH_TERM, discussions_queue),
    )

    reddit_thread_instance.start()
    hn_thread_instance.start()

    # Wait for both threads
    reddit_thread_instance.join()
    hn_thread_instance.join()

    discussions = []
    while not discussions_queue.empty():
        for discussion in discussions_queue.get():
            discussions.append(discussion)

    filtered_discussions = filter_comments_for_discussions(discussions)
    cleaned_discussions = preprocess_discussions(filtered_discussions)

    skip_short_comments_for_discussions(cleaned_discussions)

    min_comments = 50
    final_discussions = filter_discussions_with_too_few_comments(
        cleaned_discussions, min_comments
    )

    save_to_csv(final_discussions)


def skip_short_comments_for_discussions(cleaned_discussions):

    discussions_without_short_comments = []
    min_comment_length = 4

    for discussion in cleaned_discussions:
        discussion_copy = copy.deepcopy(discussion)
        long_enough_comments = skip_short_comments(
            discussion_copy.comments, min_comment_length
        )
        discussion_copy.comments = long_enough_comments
        discussions_without_short_comments.append(discussion_copy)


if __name__ == "__main__":
    get_discussions_dataset()
