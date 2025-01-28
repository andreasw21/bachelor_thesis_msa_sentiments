from datetime import date
import unittest
from src.Filter.filter_hackernews import my_hn_filter
from src.HackerNewsApi.hn_story_type import HN_Story


posts = [
    HN_Story(
        id="1",
        title="Relevant Post: Microservices are better then monoliths",
        score=15,
        content="Some content from microservices.",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="2",
        title="Irrelevant Post: YouTube Video",
        score=5,
        content="https://youtube.com/some-video",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="3",
        title="Another Relevant Post: monoliths suck",
        score=20,
        content="Some content from tech domain.",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="4",
        title="Irrelevant GitHub Repository",
        score=10,
        content="https://github.com/some-repo",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="5",
        title="Yet Another Relevant Post  because all advantages are great",
        score=25,
        content="Interesting content about programming.",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="6",
        title="low score",
        score=0,
        content="Interesting content about programming.",
        created=date.today(),
        num_comments=10,
    ),
    HN_Story(
        id="7",
        title="low score",
        score=0,
        content="Interesting content about programming.",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="8",
        title="low score",
        score=0,
        content="Interesting content about programming.",
        created=date.today(),
        num_comments=10,
    ),
    HN_Story(
        id="9",
        title="low score",
        score=0,
        content="Interesting content about programming.",
        created=date.today(),
        num_comments=100,
    ),
    HN_Story(
        id="10",
        title="low score",
        score=0,
        content="Interesting content about programming.",
        created=date.today(),
        num_comments=10,
    ),
]


class TestMyHNFilter(unittest.TestCase):

    def test_filter_hn_posts(self):
        """Test the my_hn_filter function and verify remaining posts."""
        expected_remaining_ids = ["1", "3", "5"]
        # Act
        result = my_hn_filter(posts)

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
