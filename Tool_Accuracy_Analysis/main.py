from Analyze_Sentiment_Results.generate_analysis import (
    generate_analysis_reports,
)
from Postprocess_Senti4SD.senti4SD_postprocessing import (
    classify_with_senti4SD_and_postprocess,
)


if __name__ == "__main__":

    generate_analysis_reports("ChatGPT", "Different_prompts", "2015-2017.csv")
# classify_with_senti4SD_and_postprocess()
