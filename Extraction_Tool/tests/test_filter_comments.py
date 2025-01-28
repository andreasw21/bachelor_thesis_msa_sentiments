import unittest
from datetime import date
from src.discussion_dataclasses import Comment, Discussion
from src.Filter.filter_comments import (
    filter_comments,
    filter_by_keyword,
    skip_short_comments,
)


class TestCommentFilters(unittest.TestCase):

    def setUp(self):
        """Set up some initial data for testing."""

        self.comments = [
            Comment(
                "ID1",
                date.today(),
                "I like microservice architecture too, because they are scalable.",
            ),
            Comment("ID2", date.today(), "weird"),
            Comment(
                "ID3",
                date.today(),
                "I don't think that your ideas are useful at all!",
            ),
            Comment("ID4", date.today(), "cool picture!"),
            Comment("ID5", date.today(), "Microservices as strategies?"),
        ]

        self.discussion = Discussion(
            "ID1", "source", date.today(), "Title", "Content", self.comments
        )

    def test_skip_short_comments(self):
        """Test the skip_short_comments function."""
        long_enough_comments = skip_short_comments(self.comments, min_words=4)

        expected_comment_amount = 2

        self.assertEqual(len(long_enough_comments), expected_comment_amount)

    def test_filter_by_keyword(self):
        """Test the filter_by_keyword function, which filters out all comments that don't contain the keyword."""
        relevant_comments = filter_by_keyword(self.comments, keyword="microservice")

        expected_comment_amount = 2

        self.assertEqual(len(relevant_comments), expected_comment_amount)

    def test_filter_comments(self):
        """Test the filter_comments function."""
        filtered_comments = filter_comments(self.comments, keyword="microservice")

        expected_comment_amount = 1

        self.assertEqual(len(filtered_comments), expected_comment_amount)


if __name__ == "__main__":
    unittest.main()
