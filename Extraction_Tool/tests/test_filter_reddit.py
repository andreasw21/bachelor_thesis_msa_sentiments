from datetime import date
import unittest
from src.Filter.filter_reddit import (
    my_reddit_filter,
    hasRelevantFlairs,
    isRelevantSubreddit,
)
from src.RedditApi.reddit_post_type import (
    RedditPost,
)

posts = [
    RedditPost(
        id="1",
        title="Relevant Post because microservices are better then monoliths",
        created=date.today(),
        score=35,
        subreddit="microservices",
        content="Some content",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="2",
        title="Irrelevant Post as to demonstrate that this post will not be in the results",
        created=date.today(),
        score=5,
        subreddit="nintendo",
        content="Another content",
        flairs=["meme"],
        num_comments=100,
    ),
    RedditPost(
        id="3",
        title="Advantages and Disadvantages of microservices",
        created=date.today(),
        score=20,
        subreddit="tech",
        content="More content",
        flairs=["discussion", "meme"],
        num_comments=100,
    ),
    RedditPost(
        id="4",
        title="Humorous Post",
        created=date.today(),
        score=10,
        subreddit="programming",
        content="Some funny content",
        flairs=["humor", "meme", "nintendo"],
        num_comments=100,
    ),
    RedditPost(
        id="5",
        title="Microservices vs Monoliths",
        created=date.today(),
        score=40,
        subreddit="programming",
        content="bla bla",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="6",
        title="Microservices tutorial",
        created=date.today(),
        score=10,
        subreddit="programming",
        content="bla bla",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="7",
        title="low score",
        created=date.today(),
        score=-10,
        subreddit="programming",
        content="bla bla",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="8",
        title="low score",
        created=date.today(),
        score=-10,
        subreddit="programming",
        content="bla bla",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="9",
        title="low score",
        created=date.today(),
        score=-10,
        subreddit="programming",
        content="bla bla",
        flairs=[],
        num_comments=100,
    ),
    RedditPost(
        id="10",
        title="low score",
        created=date.today(),
        score=-10,
        subreddit="programming",
        content="bla bla",
        flairs=[],
        num_comments=100,
    ),
]


class TestMyRedditFilter(unittest.TestCase):

    def test_relevant_subbreddit(self):
        """Test the my_reddit_filter function with relevant posts."""

        # Act
        post1_is_relevant = isRelevantSubreddit(posts[0])
        post2_is_relevant = isRelevantSubreddit(posts[1])
        post3_is_relevant = isRelevantSubreddit(posts[2])
        post4_is_relevant = isRelevantSubreddit(posts[3])
        # Assert
        self.assertTrue(post1_is_relevant)
        self.assertFalse(post2_is_relevant)
        self.assertTrue(post3_is_relevant)
        self.assertTrue(post4_is_relevant)

    def test_relevant_flairs(self):
        """Test the my_reddit_filter function with relevant posts."""

        # Act
        post1_is_relevant = hasRelevantFlairs(posts[0])
        post2_is_relevant = hasRelevantFlairs(posts[1])
        post3_is_relevant = hasRelevantFlairs(posts[2])
        post4_is_relevant = hasRelevantFlairs(posts[3])
        # Assert
        self.assertTrue(post1_is_relevant)
        self.assertFalse(post2_is_relevant)
        self.assertFalse(post3_is_relevant)
        self.assertFalse(post4_is_relevant)

    def test_filter_redditposts(self):
        """Test the my_reddit_filter function and verify remaining posts."""
        # Assert
        expected_remaining_ids = ["1", "5"]
        # Act
        result = my_reddit_filter(posts)
        print(result[0].id)
        # Assert
        self.assertEqual(
            len(result),
            len(expected_remaining_ids),
            "The number of filtered posts is incorrect.",
        )

        remaining_ids = [post.id for post in result]
        for expected_id in expected_remaining_ids:
            self.assertIn(
                expected_id,
                remaining_ids,
                f"Post ID {expected_id} should be in the filtered results.",
            )

    if __name__ == "__main__":
        unittest.main()
