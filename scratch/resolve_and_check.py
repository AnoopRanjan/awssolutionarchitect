import urllib.request
import json
import re

urls = [
    ("Briefing 2024 ARC201", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAtFKVvTVu9ZaA8AIfxZ4QuqTECC5UEqBh5mCaGT6vCuEJ7RMxx4_pUMoQ-Mo2ejblVFkekfF0HCGdJfGysAg2ckhXkfybfyqh7P3MbdRiHQd2aFN3WmT2uz2re7UjyTbB"),
    ("Briefing 2023 ARC206", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiJ3dFSK4btvYo55d4pHQRQW8oWmFZHZ6bzg-NZmsG2UGkdIwGV2OJyWH3jCUXR3gDsL9RvGTjeN7JgidrCTJJyypwGSOmHbqBrRTprB4zQNdAXwRa4TiK7wLmAiXWh5aY"),
    ("Briefing 2019 ARC211", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvaO1IuOZIEBjUdEfur4XrDzlszE1gVTzhgB9Jzlhz4FArk6W-nzv7CTHc8-WPiXQN8EJDMo0hc-FkhWIK9jt50L8EFmG7DWoJ8QP6eTjUUKCdAInBieMpMiNB9AL_oAT0")
]

for label, u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        dest = res.geturl()
        print(f"[{label}] -> {dest}")
        # Extract v parameter
        m = re.search(r'[?&]v=([^&]+)', dest)
        if m:
            vid = m.group(1)
            o_req = urllib.request.Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json", headers={'User-Agent': 'Mozilla/5.0'})
            o_res = urllib.request.urlopen(o_req, timeout=5)
            data = json.loads(o_res.read())
            print(f"    OK: vid={vid} | {data.get('title')} | Author: {data.get('author_name')}")
    except Exception as e:
        print(f"[{label}] ERR: {e}")
