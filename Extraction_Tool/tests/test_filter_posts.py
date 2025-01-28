import unittest
from datetime import date
from src.Filter.filter_posts import (
    filter_discussions_with_too_few_comments,
    is_relevant_post,
    relevant_title,
)
from src.HackerNewsApi.hn_story_type import HN_Story
from src.RedditApi.reddit_post_type import RedditPost


from src.discussion_dataclasses import Comment, Discussion


posts_hn = [
    HN_Story(
        id="ID",
        title="An important news article",
        score=10,
        created=date.today(),
        content="Some content",
        num_comments=10,
    ),
    HN_Story(
        id="ID",
        title="A funny meme",
        score=5,
        created=date.today(),
        content="Serious content about msa",
        num_comments=10,
    ),
]

posts_reddit = [
    RedditPost(
        id="ID",
        title="An important post",
        created=date.today(),
        score=20,
        subreddit="news",
        content="content",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="ID",
        title="A meme post",
        created=date.today(),
        score=2,
        subreddit="dotnet",
        content="content",
        flairs=["meme"],
        num_comments=100,
    ),
]


class TestFilters(unittest.TestCase):

    def test_is_relevant_post_according_score(self):
        """Test the is_relevant_post function."""
        threshold = 10
        relevant_post = posts_reddit[0]
        irrelevant_post = posts_reddit[1]

        self.assertTrue(is_relevant_post(relevant_post, threshold))
        self.assertFalse(is_relevant_post(irrelevant_post, threshold))

    def test_relevant_title_keywordbased(self):
        """Test the relevant_title function."""
        self.assertTrue(
            relevant_title("Is it a good idea to replace monoliths with Microservices?")
        )
        self.assertFalse(relevant_title("How to implement Microservices in SQL"))

    def test_filter_discussions_with_too_few_comments(self):
        """Test the filter_discussions_with_too_few_comments function."""

        comments_30 = [
            Comment("ID" + str(comment_counter), date.today(), "Comment content")
            for comment_counter in range(30)
        ]
        discussion_30_comments = Discussion(
            "ID1", "source", date.today(), "Title", "Content", comments_30
        )

        comments_10 = [
            Comment("ID" + str(comment_counter), date.today(), "Comment content")
            for comment_counter in range(10)
        ]
        discussion_10_comments = Discussion(
            "ID2", "source", date.today(), "Title", "Content", comments_10
        )

        filtered_discussions = filter_discussions_with_too_few_comments(
            [discussion_30_comments, discussion_10_comments], min_comments=25
        )

        self.assertEqual(len(filtered_discussions), 1)




if __name__ == "__main__":
    unittest.main()
