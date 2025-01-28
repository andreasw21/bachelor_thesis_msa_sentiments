from Analyze_Sentiment_Results.tool_accuracy_analyzer import (
    calculate_precision_recall_f1,
    display_metrics,
    save_metrics_to_file,
)
from Analyze_Sentiment_Results.analyze_sentiment_results import (
    create_sentiment_report,
    save_sentiment_report,
)


def generate_analysis_reports(tool: str, approach: str, prediction_csv):
    # Calculate precision, recall, and F1 score

    path = f"./Labelled_Discussions/{tool}/Improved/{approach}"
    #   path = f"./Labelled_Discussions/All_Tools_Combined/strat3"
    metrics = calculate_precision_recall_f1(
        f"{path}/{prediction_csv}", delimiter=";", label_col=4, pred_col=5
    )

    # Display and save metrics
    display_metrics(metrics)
    save_metrics_to_file(
        metrics,
        f"{path}/tool_accuracy_report.txt",
    )

    # Generate sentiment report
    directory = f"{path}"
    report = create_sentiment_report(directory, sentiment_column_index=5)

    # Display and save sentiment report
    print(report)
    save_sentiment_report(directory, report)
