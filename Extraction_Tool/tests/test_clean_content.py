import unittest
from datetime import datetime, date

from src import DataManipulation
from src.DataManipulation.clean_content import (
    remove_extra_spaces,
    remove_special_characters,
    to_lower_case,
)
from src.discussion_dataclasses import Comment


class TestCleanContent(unittest.TestCase):

    def test_remove_single_quotes(self):
        """Tests that single quotes around a word are removed."""

        # arrange
        text_with_single_quotes = "'text'"
        text_with_single_quotes_and_spaces = "'  text '"
        text_without_quotes = "text"

        # act
        cleaned_text1 = DataManipulation.remove_single_quotes(text_with_single_quotes)
        cleaned_text2 = DataManipulation.remove_single_quotes(
            text_with_single_quotes_and_spaces
        )
        cleaned_text3 = DataManipulation.remove_single_quotes(text_without_quotes)

        # assert
        self.assertEqual(cleaned_text1, "text")
        self.assertEqual(cleaned_text2, "  text ")
        self.assertEqual(cleaned_text3, "text")

    def test_remove_block_tag(self):
        """Tests that block tags and their content are removed."""

        # Arrange
        text_with_block_tags = "<div>content 123</div>Keep this content"
        block_tag_pattern = (r"<div>", r"</div>")

        # Act
        cleaned_text = DataManipulation.remove_block_tag(
            block_tag_pattern, text_with_block_tags
        )

        # Assert
        self.assertEqual(cleaned_text.strip(), "Keep this content")

    def test_remove_single_tag(self):
        """Tests that single tags are removed from the text."""

        # Arrange
        text_with_single_tags = "Keep-<br>this<br>-content"
        single_tag_pattern = r"<br>"

        # Act
        cleaned_text = DataManipulation.remove_single_tag(
            single_tag_pattern, text_with_single_tags
        )

        # Assert
        self.assertEqual(cleaned_text.strip(), "Keep-this-content")

    def test_clean_removes_block_and_single_tags(self):
        """Tests that clean function removes block and single tags from the content."""

        # Arrange
        content_with_tags = (
            "Ke<br>ep this<div> thi's<br> div <br>'con</div>content Keep this content"
        )

        # Act
        cleaned_content = DataManipulation.clean(content_with_tags)

        # Assert
        expected_cleaned_content = "Keep this content Keep this content"
        self.assertEqual(cleaned_content.strip(), expected_cleaned_content)

    def test_remove_extra_spaces(self):

        # Arrange
        text_multiple_spaces = "This  is   a    test."
        text_leading_training_spaces = "   Leading and trailing spaces.   "
        text_single_spaces = "Single space between words."
        text_empty = ""
        # Act
        result_from_text_multiple_spaces = remove_extra_spaces(text_multiple_spaces)
        result_from_text_leading_training_spaces = remove_extra_spaces(
            text_leading_training_spaces
        )
        result_from_text_single_spaces = remove_extra_spaces(text_single_spaces)
        result_from_text_empty = remove_extra_spaces(text_empty)
        # Assert
        self.assertEqual(result_from_text_multiple_spaces, "This is a test.")
        self.assertEqual(
            result_from_text_leading_training_spaces, "Leading and trailing spaces."
        )
        self.assertEqual(result_from_text_single_spaces, text_single_spaces)
        self.assertEqual(result_from_text_empty, text_empty)

    def test_to_lower_case(self):

        # Arrange
        comment_caps_starting_letters = Comment("id", date.today(), "This Is A Test.")
        comment_caps_inside_words = Comment("id", date.today(), "ThIs is A tESt.")
        comment_all_caps = Comment("id", date.today(), "THIS IS A TEST.")
        comment_no_caps = Comment("id", date.today(), "this is a test.")
        # Act
        result_from_comment_caps_starting_letters = to_lower_case(
            comment_caps_starting_letters
        )
        result_from_comment_caps_inside_words = to_lower_case(comment_caps_inside_words)
        result_from_comment_all_caps = to_lower_case(comment_all_caps)
        result_from_comment_no_caps = to_lower_case(comment_no_caps)
        # Assert
        self.assertEqual(
            result_from_comment_caps_starting_letters.content, "this is a test."
        )
        self.assertEqual(
            result_from_comment_caps_inside_words.content, "this is a test."
        )
        self.assertEqual(result_from_comment_all_caps.content, "this is a test.")
        self.assertEqual(result_from_comment_no_caps.content, "this is a test.")

    def test_remove_special_characters(self):
        # Arrange
        input_text_with_special_chars = (
            "@#$$%Special characters **&&&&&shouldn't be here! "
        )

        input_text_no_special_chars = "Only letters and numbers 1234567890."

        # Act
        result_from_text_with_special_chars = remove_special_characters(
            input_text_with_special_chars
        )
        result_from_text_no_special_chars = remove_special_characters(
            input_text_no_special_chars
        )
        # Assert
        self.assertEqual(
            result_from_text_with_special_chars, "Special characters shouldn't be here!"
        )
        self.assertEqual(
            result_from_text_no_special_chars, "Only letters and numbers 1234567890."
        )


'''  def test_clean_discussions_removes_deleted_comments(self):
        """Test that deleted comments are removed from discussions."""

        # Arrange
        comments = [
            Comment("1", date.today(), "This is not good!"),
            Comment("2", date.today(), "[deleted]"),
            Comment("3", date.today(), "This is not good![deleted]"),
        ]

        discussions = [
            Discussion("1", comments),
        ]

        # Act
        cleaned_discussions = DataManipulation.clean_discussions(discussions)

        # Optionally, check the number of comments left
        self.assertEqual(len(cleaned_discussions[0].comments), 2)  # 2 comments remains
        self.assertNotEqual(
            cleaned_discussions[0].comments[1].content, "This is not good!"
        )
        self.assertNotEqual(
            cleaned_discussions[0].comments[2].content, "This is not good![deleted]."
        )
'''

"""
    def test_remove_citations(self):
       Tests that single tags are removed from the text.

        # Arrange
        comments = [
            Comment("1", date.today(), "I like all trees, because they are beautiful."),
            Comment(
                "2",
                date.today(),
                "I like all trees, but your explanation is not useful.",
            ),
            Comment(
                "3",
                date.today(),
                "I <i>like</i> all trees, but your explanation is not useful.",
            ),
            Comment(
                "4",
                date.today(),
                "<i>I like all trees</i> is what the OP says. However, he is wrong.",
            ),
        ]

        # Act
        cleaned_comments = DataManipulation.remove_citations(comments)

        # Assert
        self.assertEqual(
            cleaned_comments[0].content, "I like all trees, because they are beautiful."
        )
        self.assertEqual(
            cleaned_comments[1].content,
            "I like all trees, but your explanation is not useful.",
        )
        self.assertEqual(
            cleaned_comments[2].content,
            "I <i>like</i> all trees, but your explanation is not useful.",
        )
        self.assertEqual(
            cleaned_comments[3].content, " is what the OP says. However, he is wrong."
        )


  def test_remove_urls(self):
       Test the remove_urls function with various inputs.
        test_cases = [
            (
                "Visit our website at http://example.com for more info.",
                "Visit our website at for more info.",
            ),
            (
                "Check this: http://example.com and also this one: https://another-example.com.",
                "Check this: and also this one: .",
            ),
            (
                "This is a simple text without any URLs.",
                "This is a simple text without any URLs.",
            ),
            ("http://example.com https://another.com", ""),
        ]

        for i, (input_content, expected_output) in enumerate(test_cases):
            with self.subTest(test_case=i):
                self.assertEqual(
                    DataManipulation.remove_urls(input_content), expected_output
                )

"""


if __name__ == "__main__":
    unittest.main()
