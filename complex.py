# Let's create an Instagram-like feed with two posts
post1 = {
    "author": "Alice",
    "likes": 10,
    "tags": ["morning", "coffee", "happy"]
}

post2 = {
    "author": "Bob",
    "likes": 5,
    "tags": ["sunset", "beach"]
}

# The feed is a list of posts
feed = [post1, post2]

# Print initial feed
print("Initial feed:", feed)

# Alice's post gets 5 more likes
feed[0]["likes"] = feed[0]["likes"] + 5
print("Alice's likes updated to:", feed[0]["likes"])

# Bob adds a new tag to his post
feed[1]["tags"].append("vacation")
print("Bob's tags updated to:", feed[1]["tags"])

# A new post from Charlie
post3 = {
    "author": "Charlie",
    "likes": 0,
    "tags": ["new", "excited"]
}
feed.append(post3)  # Add Charlie's post to the feed
print("New feed after adding Charlie:", feed)

# Update Charlie's likes
feed[2]["likes"] = feed[2]["likes"] + 20
print("Charlie's likes updated to:", feed[2]["likes"])

# Let's print all authors in the feed
authors = [feed[0]["author"], feed[1]["author"], feed[2]["author"]]
print("Authors in the feed:", authors)

# Combine all tags from all posts into a single list
all_tags = feed[0]["tags"] + feed[1]["tags"] + feed[2]["tags"]
print("All tags from all posts:", all_tags)
