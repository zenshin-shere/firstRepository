
import urllib.request

topic = "ntfy1"
message = "Pythonからの通知テスト"

url = f"https://ntfy.sh/{topic}"
request = urllib.request.Request(
    url,
    data=message.encode("utf-8"),
    method="POST"
)

with urllib.request.urlopen(request, timeout=10) as response:
    print("通知送信:", response.status)
