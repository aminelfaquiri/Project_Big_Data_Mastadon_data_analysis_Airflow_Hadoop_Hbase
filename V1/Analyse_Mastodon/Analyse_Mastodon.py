#!/usr/bin/env python3

def Analyse_Mastodon():
    import happybase

    # Connect to HBase :
    connection = happybase.Connection()

    # The Top 10 Account with folowers :

    table = connection.table('user')

    # Scan the table and retrieve all rows sorted by followers_count in descending order
    rows = table.scan(columns=['user_info:followers_count'], sorted_columns=True, reverse=True)

    # Retrieve the top 10 user IDs with the highest number of followers
    top_10_user_ids = [row for i, row in enumerate(rows) if i < 10]

    for id,follower in top_10_user_ids :
        print(id.decode('utf-8'),"=> ",int(follower[b'user_info:followers_count']))








