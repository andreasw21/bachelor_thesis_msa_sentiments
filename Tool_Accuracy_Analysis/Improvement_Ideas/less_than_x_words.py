import csv

def filter_rows_by_word_count(input_csv, output_csv, word_limit):
    """
    The output_csv will be the same as the input_csv, but all the rows with content that has less then word_limit words will be deleted
    """
    try:
  
        with open(input_csv, mode="r", newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile, delimiter=";")
            headers = next(reader) 

      
            if "Content" not in headers:
                raise ValueError("'Content' column not found in the CSV file.")

            content_index = headers.index("Content")  


            filtered_rows = [
                row for row in reader if len(row[content_index].split()) < word_limit
            ]


        with open(output_csv, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile, delimiter=";")
            writer.writerow(headers)  
            writer.writerows(filtered_rows) 

        print(f"Filtered rows with less than {word_limit} words in 'Content' written to {output_csv}.")
    except Exception as e:
        print(f"Error: {e}")



word_limit=50
filter_rows_by_word_count("HackerNews-32250722.csv", f"hn_less_than_{word_limit}_words.csv", word_limit)
