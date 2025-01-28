import csv


def add_column_to_csv(input_csv, processed_data, output_csv, new_column_name):
    try:
        with open(input_csv, mode="r", newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile, delimiter=";")
            headers = next(reader)
            rows = list(reader)

        headers.append(new_column_name)
        updated_rows = [row + [processed_data[i][0]] for i, row in enumerate(rows)]

        with open(output_csv, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile, delimiter=";")
            writer.writerow(headers)
            writer.writerows(updated_rows)

        print(f"Column '{new_column_name}' added to {output_csv}.")
    except Exception as e:
        print(f"Error: {e}")
