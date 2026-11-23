import sys
import urllib.request
import json
import time

sys.path.append('.')
from data.aws_masterclass import AWS_MASTER_COURSE, AWS_BRIEFING_10MIN
from data.topics import TOPICS
from data.roadmap import ROADMAP_DAYS

def check_video(vid):
    if not vid or len(vid) < 5:
        return False, "Invalid ID"
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req, timeout=5)
        data = json.loads(res.read())
        return True, f"{data.get('title')} ({data.get('author_name')})"
    except Exception as e:
        return False, str(e)

print("=== CHECKING MASTERCLASS & BRIEFING ===")
mc_id = AWS_MASTER_COURSE.get('primary_video_id')
ok, msg = check_video(mc_id)
print(f"Masterclass ({mc_id}): {'[OK]' if ok else '[FAIL]'} - {msg}")

br_id = AWS_BRIEFING_10MIN.get('video_id')
ok, msg = check_video(br_id)
print(f"Briefing ({br_id}): {'[OK]' if ok else '[FAIL]'} - {msg}")

print("\n=== CHECKING TOPICS ===")
for t in TOPICS:
    v_id = t.get('youtube_embed', '').split('/')[-1]
    ok, msg = check_video(v_id)
    print(f"Topic {t['id']:2d} ({v_id}): {'[OK]' if ok else '[FAIL]'} - {msg}")

print("\n=== CHECKING ROADMAP DAYS ===")
for d in ROADMAP_DAYS:
    v_id = d.get('video_id')
    ok, msg = check_video(v_id)
    print(f"Day {d['day']:2d} ({v_id}): {'[OK]' if ok else '[FAIL]'} - {msg}")
