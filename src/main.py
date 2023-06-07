import praw
from decouple import config

print(f"[*] Getting configuration secrets")
client_id=config("client_id")
client_secret=config("client_secret")
reddit_username=config("reddit_username")
reddit_password=config("reddit_password")

print(f"[*] Configuration Reddit client.")
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent="Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36",
)


print(f"[*] Looking up Reddit user \"{reddit_username}\".")
redditor = reddit.redditor(reddit_username)

print(f"[*] Getting newest 100 comments.")
comments = redditor.comments.new(limit=100)

count = 0

print(f"[*] Looping through comments...")
for comment in comments:
    #print(comment.body)
    # if hasattr(comment, "body" ):
    comment.delete()
    print(".", end='', flush=True)
    count = count + 1
        
print(f"[*] Done. {count} comments deleted.")
