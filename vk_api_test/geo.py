import requests, json

result = requests.get("https://api.vk.com/method/wall.get?owner_id=7980360&count=100&v=5.60")
text = result.text
json_result = json.loads(text)
posts = json_result["response"]
posts=posts["items"]
for post in posts:
	if "geo" in post.keys():
		place = post["geo"]["place"]
		if "title" in place.keys():
			print(place["title"])