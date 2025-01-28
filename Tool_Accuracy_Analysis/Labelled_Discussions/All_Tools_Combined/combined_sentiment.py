import csv


input_file = "prediction_file_all_tools.csv"
output_file = "combined.csv"


with open(input_file, "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile, delimiter=";")

    fieldnames = [
        col
        for col in reader.fieldnames
        if col not in ("EASTERSentiment", "ChatGPTSentiment", "Senti4SDSentiment")
    ]
    fieldnames.append("CombinedSentiment")

    with open(output_file, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        for row in reader:
            try:
                easter_sentiment = int(row["EASTERSentiment"].strip())
                chatgpt_sentiment = int(row["ChatGPTSentiment"].strip())
                senti4sd_sentiment = int(row["Senti4SDSentiment"].strip())
            except ValueError:
                easter_sentiment = chatgpt_sentiment = senti4sd_sentiment = None

            # Caclulate sentiment from a combined aproach
            if easter_sentiment == -1:
                combined_sentiment = -1  # Trust EASTER if it says -1
            elif (
                easter_sentiment == 0
                and senti4sd_sentiment == -1
                and chatgpt_sentiment == -1
            ):
                combined_sentiment = -1

            elif (
                (easter_sentiment in (0, 1))
                and (senti4sd_sentiment in (0, 1))
                and chatgpt_sentiment == 1
            ):
                combined_sentiment = 1  # Trust ChatGPT if it says 1
            else:
                combined_sentiment = easter_sentiment  # Otherwise, trust EASTER

            new_row = {
                key: value
                for key, value in row.items()
                if key
                not in ("EASTERSentiment", "ChatGPTSentiment", "Senti4SDSentiment")
            }
            new_row["CombinedSentiment"] = combined_sentiment

            writer.writerow(new_row)

print(f"Processed data has been written to {output_file}.")


# produced current highscore
