import requests
import json

result = requests.get("https://api.vk.com/method/wall.get?domain=roctbb&count=1&v=5.60&access_token=c6e0a47af82b6ba4d7a17093b4bedb155178e14111adb7066c75766f6f21f7b495aba7a4f926a9c61f680")
json_result = json.loads(result.text)

posts = []
col = json_result["response"]["count"]

for offset in range(0,col,100):
    result = requests.get(
        "https://api.vk.com/method/wall.get?domain=roctbb&count=100&offset="+str(offset)+"&v=5.60")
    print(offset)
    json_result = json.loads(result.text)
    posts = posts + json_result["response"]["items"]

for post in posts:
    print(post["text"] + " - " + post["likes"]["count"])
