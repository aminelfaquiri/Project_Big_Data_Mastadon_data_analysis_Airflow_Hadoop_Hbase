#!/usr/bin/env python3

import happybase

# Connect to HBase :
connection = happybase.Connection()
tables = connection.get_tables()

# user =>  user_info => key : user_id, col :followers_count,engagement_rate,create_at
# external_links => website => key : url , col : links_count
# content_lang => language => key : langue ,col : lang_count
# post_attachment => attachment => key : post_id , col : has_media
# tags => top_tags => key :  tag, col : tag_count
# mentions => top_mentions  => key : mention , col : mention_count

# creat Table user :
if 'user' not in tables:
   connection.create_table(
       'user',
       {
           'user_info': dict(),   # Column family 'user_info'
       }
    )

if 'external_links' not in tables:
   connection.create_table(
       'external_links',
       {
           'website': dict(),  # Column family 'user_info'
       }
  )

if 'content_lang' not in tables:
   connection.create_table(
       'content_lang',
       {
           'language': dict(),  # Column family 'user_info'
       }
   )

if 'post_attachment' not in tables:
   connection.create_table(
       'post_attachment',
       {
           'attachment': dict(),  # Column family 'user_info'
       }
   )

if 'tags' not in tables:
    connection.create_table(
        'tags',
        {
            'top_tags': dict(),  # Column family 'user_info'
        }
    )

if 'mentions' not in tables:
    connection.create_table(
        'mentions',
        {
            'top_mentions': dict(),  # Column family 'user_info'
        }
    )

connection.close()
