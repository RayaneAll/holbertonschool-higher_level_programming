#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the HTTP status code of the response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        # Loop through the posts and print their titles
        for post in posts:
            print(post["title"])
    else:
        print("Error while fetching posts.")


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Open a CSV file in write mode and save the posts
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            writer.writerows(posts)  # Write the post data
        print("Posts have been saved in posts.csv")
    else:
        print("Error while fetching posts.")
