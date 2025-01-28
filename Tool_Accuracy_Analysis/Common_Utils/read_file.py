from typing import List
import csv
import os


def get_column_from_csv(file_path, delimiter, column_index: int):
    values = []
    with open(file_path, "r", encoding="utf-8") as f:

        # Skip the header line
        next(f)

        for line_number, line in enumerate(f, start=1):
            row = line.strip().split(delimiter)

            if not row or all(field.strip() == "" for field in row):
                print(f"Skipping empty row {line_number} in {file_path}")
                continue

            # for debugging
            # print(f"Row {line_number} in {file_path}: {row[column_index]}")

            # Check if the row has enough columns
            if len(row) > column_index and row[column_index].strip() != "":
                values.append(row[column_index])
            else:

                display_path = (
                    "./" + file_path if not file_path.startswith("./") else file_path
                )
                print(
                    f"Warning: Row {line_number} in {display_path} does not have column {column_index} or is empty."
                )

    return values


def get_all_file_paths(directory: str):
    """
    Retrieves all file paths from the specified directory and its subdirectories.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):  # Only consider the CSV files
                full_path = os.path.join(root, file)
                file_paths.append(os.path.normpath(full_path))
    return file_paths
