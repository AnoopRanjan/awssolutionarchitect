import sys
sys.path.append('.')
from data.aws_masterclass import AWS_MASTER_COURSE, AWS_BRIEFING_10MIN
from data.topics import TOPICS
from data.roadmap import ROADMAP_DAYS

print('--- MASTERCLASS ---')
print('Primary:', AWS_MASTER_COURSE.get('primary_video_id'), '|', AWS_MASTER_COURSE.get('primary_video_title'))
print('Briefing:', AWS_BRIEFING_10MIN.get('video_id'), '|', AWS_BRIEFING_10MIN.get('video_title'))

print('\n--- TOPICS ---')
for t in TOPICS:
    v_id = t.get('youtube_embed', '').split('/')[-1]
    print(f"Topic {t['id']:2d}: {v_id:15s} | {t.get('title')}")

print('\n--- ROADMAP DAYS ---')
for d in ROADMAP_DAYS:
    v_id = d.get('video_id')
    print(f"Day {d['day']:2d}: {str(v_id):15s} | {d.get('title')}")
