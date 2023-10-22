#!/usr/bin/env python3

import sys

# Initialize variables to keep track of tag and mention counts
tag_counts = {}
mention_counts = {}

for line in sys.stdin:
    try:
        # Split the input into tag/mention and count
        item, count = line.strip().split("\t")
        count = int(count)

        if item.startswith("#"):
            # It's a tag, update tag counts
            if item in tag_counts:
                tag_counts[item] += count
            else:
                tag_counts[item] = count
        else:
            # It's a user mention, update mention counts
            if item in mention_counts:
                mention_counts[item] += count
            else:
                mention_counts[item] = count
    except:
        continue

# Print the most frequently used tags :
print("Most frequently used tags:")
for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"tags\t{tag}\t{count}")

# Print the most frequently mentioned users :
print("\nMost frequently mentioned users:")
for mention, count in sorted(mention_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"mention\t{mention}\t{count}")