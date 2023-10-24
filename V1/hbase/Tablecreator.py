#!/usr/bin/env python3

def Tablecreator() :
    
    import happybase

    # Connect to HBase :
    connection = happybase.Connection()

    tables = connection.tables()

    # creat Table user :
    if b'user' not in tables:
        connection.create_table(
        'user',
        {
            'user_info': dict(),   # Column family 'user_info'
            }
        )

    if b'external_links' not in tables:
        connection.create_table(
            'external_links',
            {
                'website': dict(),  # Column family 'user_info'
            }
    )

    if b'content_lang' not in tables:
        connection.create_table(
            'content_lang',
            {
                'language': dict(),  # Column family 'user_info'
            }
        )

    if b'post_attachment' not in tables:
        connection.create_table(
            'post_attachment',
            {
                'attachment': dict(),  # Column family 'user_info'
            }
        )

    if b'tags' not in tables:
        connection.create_table(
            'tags',
            {
                'top_tags': dict(),  # Column family 'user_info'
            }
        )

    if b'mentions' not in tables:
        connection.create_table(
            'mentions',
            {
                'top_mentions': dict(),  # Column family 'user_info'
            }
        )

    connection.close()
