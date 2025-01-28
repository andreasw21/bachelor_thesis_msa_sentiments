# Tracking the adoption of microservices in developer communities through sentiment analysis

This project belongs to the Bachelor Thesis by Andreas Wallnöfer, Universität Wien, Bachelor Business Informatics.

This project tries to extraxt microservice related posts, use sentiment tools to evaluate sentiment towards MSA (the tools are excluded from this repo) and then analyze how accurately the tools perform against a ground truth of manual classified data.

Below is an overview of the folders and files included in this repository:

## Project Structure
Some folders contain another readme, describing more in detail how to use the contents.

### Folders

1. **`Discussions`**  
   Contains the extracted discussions, one file per discussion.

2. **`Extraction_Tool`**  
   Contains the tool that fetches MSA related discussions from Reddit & Hackernews, filters them, preprocesses them and saves them to CSV files.

3. **`Thesis_Documentation`**  
   Contains all presentation slides.

4. **`Tool_Accuracy`**  
   Includes scripts and data used for evaluating the accuracy of various the evaluated sentiment tools on the baseline data and also on the improved data

