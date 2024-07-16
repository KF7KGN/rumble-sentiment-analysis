import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape comments from a Rumble video
def scrape_comments(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing the comments
    comments = soup.find_all("div", class_="comment-text-content")

    comment_list = []
    for comment in comments:
        comment_list.append(comment.get_text().strip())

    return comment_list

# URL of the Rumble video to scrape
video_url = "https://rumble.com/vxxxx-sample-video.html"  # Replace with actual video URL

# Scrape comments and store in a DataFrame
comments = scrape_comments(video_url)
df = pd.DataFrame(comments, columns=["Comment"])

# Save the DataFrame to a CSV file
df.to_csv("comments.csv", index=False)
