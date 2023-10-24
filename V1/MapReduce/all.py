#!/usr/bin/env python3

import sys
import json
import re
import happybase
from datetime import datetime

# Connect to HBase
connection = happybase.Connection()
table_user = connection.table('user')
table_content_lang = connection.table('content_lang')
table_post_attachment = connection.table('post_attachment')
table_external_links = connection.table('external_links')
table_tags = connection.table('tags')
table_mentions = connection.table('mentions')

# Regular expression pattern to match URLs
url_pattern = re.compile(r'http[s]?://([a-zA-Z0-9.-]+)')

# Initialize variables
current_user_id = None
current_language = None
current_post_id = None
current_url = None
current_tag = None
current_mention = None

processed_user_ids = set()
tag_counts = {}
mention_counts = {}
unique_posts = {}

def put_in_hbase(table, row_key, column_family, column, value):
    table.put(
        row_key.encode('utf-8'),
        {
            f'{column_family}:{column}'.encode('utf-8'): str(value).encode('utf-8'),
        }
    )

def put_in_hbase_content_lang(language, language_count):
    table_content_lang.put(
        language.encode('utf-8'),
        {
            b'language:lang_count': str(language_count).encode('utf-8'),
        }
    )

for line in sys.stdin:
    try:
        data = json.loads(line)

        # Mapper for User Data
        user_id = data['account']['id']
        followers_count = data['account']['followers_count']
        user_created_at = data['account']['created_at']
        user_created_at = datetime.strptime(user_created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
        favorites_count = data['favourites_count']
        reblogs_count = data['reblogs_count']
        engagement_rate = (favorites_count + reblogs_count) / (followers_count if followers_count > 0 else 1)
        print(f"{user_id}\t{followers_count}\t{user_created_at}\t{engagement_rate}")

        # Mapper for Content Language
        language = data.get("language", "Unknown")
        print(f"{language}\t1")

        # Mapper for Post Attachment
        media_attachments = data.get("media_attachments", [])
        post_id = data.get("id", "")
        has_media = 1 if len(media_attachments) > 0 else 0
        print(f"{post_id}\t{has_media}")

        # Mapper for External Links
        content = data.get("content", "")
        urls = re.findall(url_pattern, content)
        for url in urls:
            print(f"{url}\t1")

        # Mapper for Tags and Mentions
        if "tags" in data:
            for tag in data["tags"]:
                print(f"#{tag}\t1")

        if "mentions" in data:
            if len(data["mentions"]) > 0:
                for mention in data["mentions"]:
                    print(f"{mention}\t1")
    except:
        continue

# ... Rest of the script as before ...

# Close the HBase connection
connection.close()
