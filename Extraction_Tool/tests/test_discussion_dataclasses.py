import unittest
from datetime import date

from src import discussion_dataclasses


class TestDiscussion(unittest.TestCase):

    def test_discussion_empty_comments(self):
        """Test creation of Discussion object without comments."""

        comments = []

        discussion = discussion_dataclasses.Discussion(
            id="12345",
            source="My Favorite Social Media",
            creation_date=date(2012, 10, 12),
            title="I like microservices",
            content="I like microservices, because they are great",
            comments=comments,
        )

        self.assertEqual(discussion.id, "12345")
        self.assertEqual(discussion.source, "My Favorite Social Media")
        self.assertEqual(discussion.creation_date, date(2012, 10, 12))
        self.assertEqual(discussion.title, "I like microservices")
        self.assertEqual(
            discussion.content, "I like microservices, because they are great"
        )
        self.assertEqual(discussion.comments, comments)

    def test_discussion_with_comments(self):
        """Test creation of Discussion object with comments."""

        comment1 = discussion_dataclasses.Comment(
            id="1", creation_date=date(2010, 11, 12), content="comment 1"
        )
        comment2 = discussion_dataclasses.Comment(
            id="2", creation_date=date(2011, 12, 10), content="comment 2"
        )
        comments = [comment1, comment2]

        discussion = discussion_dataclasses.Discussion(
            id="123456",
            source="My Favorite Social Media",
            creation_date=date(2023, 9, 21),
            title="Discussion with useful comments",
            content="This discussion has two very interesting comments.",
            comments=comments,
        )

        # Überprüfe, ob die Kommentare korrekt zugewiesen wurden
        self.assertEqual(len(discussion.comments), 2)
        self.assertEqual(discussion.comments[0].content, "comment 1")
        self.assertEqual(discussion.comments[1].content, "comment 2")


if __name__ == "__main__":
    unittest.main()
