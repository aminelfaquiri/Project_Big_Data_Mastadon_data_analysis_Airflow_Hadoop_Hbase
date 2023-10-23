#!/usr/bin/env python3
import sys
import happybase

# Connect to HBase :
connection = happybase.Connection()
table = connection.table('user')


current_user_id = None
processed_user_ids = set()

for line in sys.stdin:
    line = line.strip()
    user_id, followers, created_at, engagement = line.split('\t')

    # Check if the current user ID is different from the previous one
    if current_user_id != user_id:
        # Output the record if it's a unique user ID
        if user_id not in processed_user_ids:
            # print(f"{user_id}\t{followers}\t{created_at}\t{engagement}")
            processed_user_ids.add(user_id)

            # put data into hbase :
            table.put(
                user_id.encode('utf-8'),
                {
                    b'user_info:followers_count': followers.encode('utf-8'),
                    b'user_info:engagement_rate': engagement.encode('utf-8'),
                    b'user_info:create_at': created_at.encode('utf-8')

                }
            )

    current_user_id = user_id

connection.close()



