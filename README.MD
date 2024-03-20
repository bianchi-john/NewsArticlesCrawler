# News Articles Crawler

This repository contains a set of Python scripts for crawling news articles from various mastheads, extracting information such as text, title, author, and publication date. Below is a brief overview of the files included:

## Files:

- **cleanDataset.py:** *(Optional)* A script for cleaning the dataset, if necessary.
- **cleanUrls.py:** *(Optional)* A script for cleaning URLs, if necessary.
- **dataframe.csv:** *(Optional)* Initial dataset.
- **dataframeWithLinksAndTextClean.csv:** *(Optional)* Dataset with cleaned links and text.
- **dataframeWithLinksClean.csv:** *(Optional)* Dataset with cleaned links.
- **dataframeWithLinks.csv:** *(Optional)* Dataset with links.
- **FinalResult/:** A directory containing the final result(s).
  - **JohnDataset.csv:** Example dataset resulting from the crawling process.
- **getDataset.py:** A script to retrieve URLs of newspapers. *Note: This script relies on an external dataset, which is not included due to copyright restrictions.*
- **getUrls.py:** A script to extract links to individual news items.
- **getText.py:** A script to extract article information (text, title, author, publication date) using the [newspaper](https://pypi.org/project/newspaper/) library.

## Usage:

1. If needed, clean the dataset using `cleanDataset.py` and `cleanUrls.py`.
2. Run `getDataset.py` to obtain the URLs of the newspapers. (Skip this step if URLs are obtained manually.)
3. Execute `getUrls.py` to collect links to individual news items.
4. Run `getText.py` to extract article information and save them in a specific dataframe.

## Note:

- The `getDataset.py` script retrieves newspaper URLs from an external dataset, which cannot be included here due to copyright restrictions. You may need to manually input or obtain the URLs.
- Ensure you have installed the necessary dependencies, particularly the `newspaper` library, which can be installed via pip: `pip install newspaper3k`.

Feel free to customize and extend these scripts to suit your specific requirements. If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or contribute to the repository.
