import os
from typing import List

from Common_Utils.read_file import get_all_file_paths, get_column_from_csv


def count_sentiment_score(sentiments: List[int], score: str) -> int:
    amount_sentiment = sum(
        1 for sentiment_entry in sentiments if sentiment_entry == score
    )
    return amount_sentiment


def calculate_percentage(amount: int, total: int) -> int:

    if total < 0:
        print(
            f"Error in calculate_percentage. Cannot use a negative total, total was {total}"
        )
        return 0

    if amount < 0:
        print(
            f"Error in calculate_percentage. Cannot use a negative total, total was {amount}"
        )
        return 0

    if total == 0:
        print("Error in calculate_percentage. Cannot divide by a total of 0")
        return 0

    percentage = amount * 100 / total
    return percentage


def get_sentiments_from_file(
    file_paths: List[str], sentiment_column_index: int
) -> List[str]:
    sentiments = []

    for file_path in file_paths:
        normalized_path = os.path.normpath("./" + file_path)

        # Extract column content for the specified column index
        sentiment_column = get_column_from_csv(
            normalized_path, ";", sentiment_column_index
        )
        sentiments.extend(sentiment_column)

    return sentiments


def create_sentiment_report(directory: str, sentiment_column_index=4) -> str:
    file_paths = get_all_file_paths(directory)

    sentiments = get_sentiments_from_file(file_paths, sentiment_column_index)

    total_entries = len(sentiments)

    amount_positive = count_sentiment_score(sentiments, "1")
    amount_negative = count_sentiment_score(sentiments, "-1")
    amount_neutral = count_sentiment_score(sentiments, "0")

    percentage_positive = calculate_percentage(amount_positive, total_entries)
    percentage_negative = calculate_percentage(amount_negative, total_entries)
    percentage_neutral = calculate_percentage(amount_neutral, total_entries)

    result_analysis_summary = (
        f"\nSentiment Analysis Summary for the files in {directory}: \n {file_paths}\n"
        + "-" * 30
        + "\n"
        + f"Total Entries: {total_entries}\n"
        + f"Positive Sentiments: {amount_positive} ({percentage_positive:.2f}%)\n"
        + f"Negative Sentiments: {amount_negative} ({percentage_negative:.2f}%)\n"
        + f"Neutral Sentiments:  {amount_neutral} ({percentage_neutral:.2f}%)\n"
        + "-" * 30
        + "\n"
    )

    return result_analysis_summary


def save_sentiment_report(directory: str, report: str):

    output_file = f"{directory}/sentiment_analysis_summary.txt"

    with open(output_file, "w") as file:
        file.write(report)
    print(f"Summary saved to {output_file}")
