import re
import csv
import subprocess

from Postprocess_Senti4SD.add_column import add_column_to_csv


def run_senti4sd(input_file, output_file):
    """
    Executes the Senti4SD sentiment analysis.
    Notes:
        - this only works if you set up Senti4SD according to https://github.com/collab-uniba/Senti4SD/tree/master
        - this only works on Linux as Senti4SD's classificationTask.sh file uses Linux commands, I used WSL for this (https://learn.microsoft.com/de-de/windows/wsl/install)
    """
    try:
        subprocess.run(
            ["sh", "Senti4SD/classificationTask.sh", input_file, output_file],
            check=True,
        )
        print(f"Senti4SD has analyzed the sentiment in {input_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Senti4SD  sentiment analysis: {e}")
        raise


def sort_and_process_csv(input_csv: str):
    """
    Takes a CSV as Senti4Sd outputs it and sorts it by the timestamp and maps sentiment values from words (negative,neutral,positive) to numbers(-1,0,1).
    """

    def extract_timestamp_number(timestamp):
        match = re.search(r"\d+", timestamp)
        return int(match.group()) if match else float("inf")

    def map_sentiment_label(sentiment):
        sentiment_mapping = {"positive": 1, "neutral": 0, "negative": -1}
        return sentiment_mapping.get(sentiment.lower(), sentiment)

    try:
        with open(input_csv, mode="r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = list(reader)

        sorted_data = sorted(data, key=lambda row: extract_timestamp_number(row[0]))

        sorted_data = [[map_sentiment_label(row[1])] + row[2:] for row in sorted_data]

        print("CSV sorting and processing complete.")
        return sorted_data
    except Exception as e:
        print(f"Error processing CSV: {e}")
        raise


def classify_with_senti4SD_and_postprocess():
    input_csv = "Postprocess_Senti4SD/100_short_easter_and_chatgpt.csv"
    senti4sd_predictions_csv = "Postprocess_Senti4SD/senti4SD_predictions.csv"
    final_output_csv = "Postprocess_Senti4SD/senti4sd_final_output.csv"

    # print("Starting Senti4SD analysis...")
    # run_senti4sd(input_csv, senti4sd_predictions_csv)

    print("Sorting and processing the sentiment predictions...")
    processed_data = sort_and_process_csv(senti4sd_predictions_csv)

    print("Combining original data with sentiment predictions...")
    add_column_to_csv(input_csv, processed_data, final_output_csv, "Senti4SD Sentiment")

    print(f"Process complete! Results saved in {final_output_csv}.")
