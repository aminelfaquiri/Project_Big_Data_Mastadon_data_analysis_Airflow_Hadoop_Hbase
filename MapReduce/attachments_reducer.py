#!/usr/bin/env python3

import sys

# Initialize a dictionary to store unique post IDs
unique_posts = {}

for line in sys.stdin:
    try:
        post_id, has_media = line.strip().split("\t")
        # If the post ID is not in the dictionary, add it with the corresponding media status
        if post_id not in unique_posts:
            unique_posts[post_id] = has_media
    except:
        continue

# Iterate through the unique post IDs and their media status and print the results
for post_id, has_media in unique_posts.items():
    print(f"{post_id}\t{has_media}")
