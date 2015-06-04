import praw, os, re
from config import username, password

r = praw.Reddit(user_agent = "United 1.0")

r.login(username, password)
print"Logged in"


if not os.path.isfile("post_replied_to.txt"):
	post_replied_to = []
else:
	with open("post_replied_to.txt", "r") as f:
		post_replied_to = f.read()
		post_replied_to = post_replied_to.split("\n")
		post_replied_to = filter(None, post_replied_to)

subreddit = r.get_subreddit("pythonforengineers")

for submission in subreddit.get_hot(limit = 5):
	if submission.id not in post_replied_to:
		if re.search("i love python", submission.title, re.IGNORECASE):
			submission.add_comment("The Delta BOT says: me too")
			print "Replied to ", submission.title
			post_replied_to.append(submission.id)

	with open ("post_replied_to.txt", "w") as f:
		for post_id in post_replied_to:
			f.write(post_id + "\n")