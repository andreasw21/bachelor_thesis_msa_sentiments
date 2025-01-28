import pandas as pd


def filter_sentences_in_column(input_csv, output_csv):

    df = pd.read_csv(input_csv, delimiter=";")

    if df.shape[1] < 4:
        print("Error: The CSV file has less than 4 columns.")
        return

    def filter_microservice_sentences(text):

        if isinstance(text, str):

            sentences = text.split(".")

            filtered_sentences = [
                s
                for s in sentences
                if "microservice" in s.lower() or "microservices" in s.lower()
            ]

            return ". ".join(filtered_sentences).strip()
        return text

    df.iloc[:, 3] = df.iloc[:, 3].apply(filter_microservice_sentences)

    df.to_csv(output_csv, index=False)
    print(f"Filtered data saved to {output_csv}")


filter_sentences_in_column("100_short_comments.csv", "short_and_msa.csv")
