import csv
from typing import List
import os

from src.discussion_dataclasses import Discussion


def save_single_discussion_to_csv(
    discussion: Discussion, filename: str = "discussions.csv"
):
    """
    Saves a single discussion to a CSV file.
    """

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow(
            [
                "ID",
                "Source",
                "Creation Date",
                "Content",
                "Sentiment",
            ]
        )

        discussion_content = f"Title:{discussion.title}, Content: {discussion.content}"

        empty_sentiment = "0"

        initial_row = [
            discussion.id,
            discussion.source,
            discussion.creation_date,
            discussion_content,
            empty_sentiment,
        ]

        writer.writerow(initial_row)
        writer.writerow("")

        for comment in discussion.comments:
            comment_row = [
                comment.id,
                discussion.source,
                comment.creation_date,
                comment.content,
                empty_sentiment,
            ]
            writer.writerow(comment_row)

    print(f"Discussions saved to {filename}")


def save_to_csv(
    discussion_lists: List[Discussion],
) -> None:
    """
    Saves a list of discussions to separate CSV files organized by year.
    """

    for discussion in discussion_lists:
        creation_year = discussion.creation_date.year

        year_directory = f"Discussions/{creation_year}"

        os.makedirs(year_directory, exist_ok=True)

        save_single_discussion_to_csv(
            discussion,
            f"{year_directory}/{discussion.source}-{discussion.id}.csv",
        )

    print(f"Saved {len(discussion_lists)} discussions into CSV")


def save_to_csv_all_into_one_file(
    discussion_lists: List[Discussion], filename: str = "discussions.csv"
) -> None:
    """
    Saves a list of discussions to a single CSV file.

    """

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow(
            [
                "Discussion ID",
                "Source",
                "Creation Date",
                "Title",
                "Content",
                "Comment ID",
                "Comment Body",
                "Comment Author",
                "Comment Creation Date",
            ]
        )

        for discussion in discussion_lists:
            row = discussion.to_csv_rows()
            writer.writerow(row)

    print(f"Discussions saved to {filename}")


def save_to_txt(filename: str, content: str):
    """Saves content to a .txt file."""
    with open(filename, "w") as file:
        file.write(content)
    print(f"Content was saved to {filename}")
