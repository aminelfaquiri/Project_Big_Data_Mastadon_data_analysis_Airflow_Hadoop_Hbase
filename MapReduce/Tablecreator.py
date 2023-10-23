#!/usr/bin/env python3

import happybase

# Connect to HBase :
connection = happybase.Connection()

#table.put(b'row5', {b'amin:a': b'hello'})

# creat Table user :
#if 'user' not in connection.tables():
 #   connection.create_table(
 #       'user',
 #       {
 #           'user_info': dict(),   # Column family 'user_info'
  #      }
  #   )

#if 'external_links' not in connection.tables():
 #   connection.create_table(
 #       'external_links',
 #       {
 #           'website': dict(),  # Column family 'user_info'
 #       }
 #  )

#if 'content_lang' not in connection.tables():
 #   connection.create_table(
 #       'content_lang',
 #       {
 #           'language': dict(),  # Column family 'user_info'
 #       }
 #   )

#if 'post_attachment' not in connection.tables():
  #  connection.create_table(
   #     'post_attachment',
   #     {
   #         'attachment': dict(),  # Column family 'user_info'
   #     }
   # )

if 'tags' not in connection.tables():
    connection.create_table(
        'tags',
        {
            'top_tags': dict(),  # Column family 'user_info'
        }
    )

if 'mentions' not in connection.tables():
    connection.create_table(
        'mentions',
        {
            'top_mentions': dict(),  # Column family 'user_info'
        }
    )

connection.close()
