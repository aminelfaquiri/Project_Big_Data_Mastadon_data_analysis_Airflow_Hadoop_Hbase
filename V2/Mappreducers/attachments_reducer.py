#!/usr/bin/env python3

import sys
import happybase

# Connect to HBase :
connection = happybase.Connection()
table = connection.table('post_attachment')

def put_in_hbase(post_id,has_media) :
        table.put(
            post_id.encode('utf-8'),
            {
                b'attachment:has_media': str(has_media).encode('utf-8'),

            }
        )

# Initialize a dictionary to store unique post IDs :
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
    put_in_hbase(post_id,has_media) 
    #print(f"{post_id}\t{has_media}")


connection.close()