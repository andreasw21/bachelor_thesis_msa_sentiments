from sklearn.metrics import classification_report
from typing import Dict
from Common_Utils.read_file import get_column_from_csv


def calculate_precision_recall_f1(
    csv_file_path: str, delimiter: str = ";", label_col: int = 4, pred_col: int = 5
) -> Dict[str, Dict[str, float]]:
    # Load data from CSV and generate per-class metrics
    truth_values = get_column_from_csv(csv_file_path, delimiter, label_col)
    prediction_values = get_column_from_csv(csv_file_path, delimiter, pred_col)

    per_class_metrics = classification_report(
        truth_values, prediction_values, zero_division=0, output_dict=True
    )
    return per_class_metrics


def format_metrics(metrics: Dict[str, Dict[str, float]]) -> str:
    """Helper function to format metrics into a string."""
    output = [
        "The Tool's accuracy will be evaluated by comparing it to manual lables.\n \nStatistical Metrics:"
    ]
    for label, values in metrics.items():
        if (
            isinstance(values, dict) and "precision" in values
        ):  # Filter only class entries
            output.append(
                f"{label} - Precision: {values['precision']:.2f}, Recall: {values['recall']:.2f}, F1-Score: {values['f1-score']:.2f}"
            )
    return "\n".join(output)


def display_metrics(metrics: Dict[str, Dict[str, float]]) -> None:
    """Display metrics in the console."""
    print(format_metrics(metrics))


def save_metrics_to_file(
    metrics: Dict[str, Dict[str, float]], file_path: str = "metrics_report.txt"
) -> None:
    """Save formatted metrics to a file."""
    with open(file_path, "w") as file:
        file.write(format_metrics(metrics))
    print(f"Metrics saved to {file_path}")


if __name__ == "__main__":
    metrics = calculate_precision_recall_f1(
        "predictions.csv", delimiter=";", label_col=0, pred_col=2
    )
    display_metrics(metrics)
    save_metrics_to_file(metrics, "metrics_report.txt")
