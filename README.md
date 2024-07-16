# Sentiment Analysis of Rumble Comments

This project involves scraping comments from Rumble videos, performing sentiment analysis on the comments, and visualizing the results. The goal is to identify patterns in sentiment that might indicate false information.

## Prerequisites

- Python 3
- Virtual environment (venv)
- Libraries: requests, beautifulsoup4, pandas, textblob, nltk, jupyter, matplotlib, seaborn

## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/rumble-sentiment-analysis.git
    cd rumble-sentiment-analysis
    ```

2. **Set Up the Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install requests beautifulsoup4 pandas textblob nltk jupyter matplotlib seaborn
    ```

## Usage

1. **Run the Web Scraping Script**
    ```bash
    python scrape_comments.py
    ```

2. **Start Jupyter Notebook**
    ```bash
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
    ```

3. **Load and Analyze the Data**
    - Open `data_analysis.ipynb` in Jupyter Notebook.
    - Run the cells to load, clean, analyze, and visualize the data.

## License

This project is licensed under the MIT License.
