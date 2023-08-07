facebook_posts = [
        {"likes": 10, "comments": 2},
        {"likes": 10, "comments": 7, "shares":1},
        {"likes": 10, "comments": 8, "shares":3},
        {"shares": 278, "comments": 1},
        {"shares": 26, "comments": 5},
        {"likes": 10, "comments": 24},
]

total_likes = 0
for post in facebook_posts:
        try:
                total_likes = total_likes + post["likes"]
        except KeyError:
                pass
print(total_likes)
               