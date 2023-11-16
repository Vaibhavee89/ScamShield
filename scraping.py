import requests
from bs4 import BeautifulSoup
import csv

# Define a function to scrape the comments from a public Instagram post
def scrape_comments(post_url):
    response = requests.get(post_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the comments
    comments = soup.find_all("div", class_="RnEpo")

    # Create a list to store the scraped data
    scraped_data = []

    # Iterate over the comments and extract the relevant data
    for comment in comments:
        comment_text = comment.find("span", class_="_a9zs").text
        number_of_likes = comment.find("span", class_="Nm936").text
        number_of_replies = comment.find("span", class_="zV_Nj").text

        # Scrape the account information
        account_username = comment.find("a", class_="sqdOP").text
        account_profile_picture_url = comment.find("img", class_="sFHGO _8OOt3").get("src")
        account_biography = comment.find("div", class_="C4VMK").text
        account_number_of_followers = comment.find("span", class_="PQo_0").text
        account_number_following = comment.find("span", class_="zV_Nj").text
        account_number_of_posts = comment.find("span", class_="g47SY").text
        account_date_of_account_creation = comment.find("time").get("datetime")

        # Add the scraped data to the list
        scraped_data.append([comment_text, number_of_likes, number_of_replies, account_username, account_profile_picture_url, account_biography, account_number_of_followers, account_number_following, account_number_of_posts, account_date_of_account_creation])

    return scraped_data

# Define a function to store the scraped data in a CSV file
def store_data_in_csv(scraped_data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["comment_text", "number_of_likes", "number_of_replies", "account_username", "account_profile_picture_url", "account_biography", "account_number_of_followers", "account_number_following", "account_number_of_posts", "account_date_of_account_creation"])

        # Write the scraped data to the CSV file
        for row in scraped_data:
            writer.writerow(row)

# Get the URL of the Instagram post
post_url = "https://www.instagram.com/p/CySad13NP9-/"

# Scrape the comments from the Instagram post
scraped_data = scrape_comments(post_url)

# Store the scraped data in a CSV file
store_data_in_csv(scraped_data, "instagram_data1.csv")
