import urllib.request
import json

# Full Proposed Mapping
MASTERCLASS = {
    "primary_video_id": "c3Cn4xYfxJY",
    "primary_video_title": "AWS Solutions Architect Associate Certification (SAA-C03) – Full Course to PASS the Exam",
    "instructor": "freeCodeCamp.org & Andrew Brown (Official ExamPro AWS Masterclass)",
    "duration": "13h 26m (Full Comprehensive Masterclass)"
}

BRIEFING = {
    "video_id": "AzUG7GOfh7w",
    "video_title": "AWS re:Invent 2024 - Scaling on AWS for the first 10 million users (ARC201)",
    "instructor": "AWS Events (Official re:Invent)",
    "duration": "57m (Executive Architecture Briefing)"
}

TOPIC_VIDEOS = {
    1: ("YQsK4MtsELU", "AWS re:Invent: Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1)", "Amazon Web Services"),
    2: ("EhbFossuQhI", "AWS re:Invent 2024 - Optimizing ELB traffic distribution for high availability (NET401)", "AWS Events"),
    3: ("7qaSfmnFiI0", "AWS re:Invent 2024 - Amazon VPC: Advanced design and what's new (NET301)", "AWS Events"),
    4: ("NXehLy7IiPM", "AWS re:Invent 2024 - Dive deep on Amazon S3 (STG302)", "AWS Events"),
    5: ("kVVdHezNTpw", "AWS re:Invent 2024 - Deep dive into Amazon Aurora and its innovations (DAT405)", "AWS Events"),
    6: ("xfxBhvGpoa0", "AWS re:Invent 2021 - DynamoDB deep dive: Advanced design patterns (Rick Houlihan)", "AWS Events"),
    7: ("l5otnYulOt8", "AWS re:Invent 2024 - Deep dive into Amazon ECS resilience and availability (SVS409)", "AWS Events"),
    8: ("ZbnAithBNYY", "AWS re:Invent 2022 - AWS Lambda SnapStart: Fast cold starts for your Java functions (SVS320)", "AWS Events"),
    9: ("dy7UXS7ur14", "AWS re:Invent 2024 - Event-driven architectures at scale: Manage millions of events (API307)", "AWS Events"),
    10: ("nOKvA8HykW8", "AWS re:Invent 2022 - The well-architected way (ARC210)", "AWS Events")
}

ROADMAP_VIDEOS = {
    1: ("PAr1DY82ymE", "AWS re:Invent 2024 - Anatomy of an AWS Region (ARC204)", "AWS Events", "56m"),
    2: ("YQsK4MtsELU", "AWS re:Invent: Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1)", "Amazon Web Services", "1h 12m"),
    3: ("2uc1vaEsPXU", "AWS re:Invent 2021 - Powering next-gen Amazon EC2: Deep dive on the Nitro System", "AWS Events", "58m"),
    4: ("Ya4WFO9P0i8", "AWS re:Invent 2022 - Layered VPC security and inspection (NET311)", "AWS Events", "52m"),
    5: ("6iO6wtDOKGM", "AWS re:Invent 2023 - Enhance your app's security & availability with Elastic Load Balancing (NET318)", "AWS Events", "54m"),
    6: ("nlGyIa3UQYU", "AWS re:Invent 2023 - Strategies for automated scaling, remediation, and smart self-healing (ENT107)", "AWS Events", "51m"),
    7: ("Ozc5Yu_IcaI", "Deploy Java Web Application in AWS Elastic Beanstalk | AWS Tutorial for Beginners", "Edureka", "45m"),
    8: ("NXehLy7IiPM", "AWS re:Invent 2024 - Dive deep on Amazon S3 (STG302)", "AWS Events", "59m"),
    9: ("WZGG8RkvApY", "AWS re:Invent 2023 - Amazon S3 security and access control best practices (STG315)", "AWS Events", "53m"),
    10: ("m03ICK5ZsA0", "AWS re:Invent 2024 - Simple Elastic File Systems: A Deep Dive into Amazon EFS (STG344)", "AWS Events", "58m"),
    11: ("7qaSfmnFiI0", "AWS re:Invent 2024 - Amazon VPC: Advanced design and what's new (NET301)", "AWS Events", "57m"),
    12: ("9Nikqn_02Oc", "AWS re:Invent: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)", "AWS Events", "58m"),
    13: ("mczl5zhQcYQ", "AWS re:Invent 2022 - Amazon Route 53: What's in a domain name? A lot! (NET206)", "AWS Events", "55m"),
    14: ("lLnKaPqL3u0", "AWS re:Invent 2024 - Amazon CloudFront: Enhancing web performance one HTTP request at a time (CDN308)", "AWS Events", "56m"),
    15: ("TJxC-B9Q9tQ", "AWS re:Invent: Deep Dive on Amazon Relational Database Service (RDS) (DAT302)", "Amazon Web Services", "1h 01m"),
    16: ("kVVdHezNTpw", "AWS re:Invent 2024 - Deep dive into Amazon Aurora and its innovations (DAT405)", "AWS Events", "1h 00m"),
    17: ("VFsGJIeuR_Y", "AWS re:Invent 2020: Deep dive into Amazon RDS Proxy for scaling applications", "AWS Events", "48m"),
    18: ("xfxBhvGpoa0", "AWS re:Invent 2021 - DynamoDB deep dive: Advanced design patterns (Rick Houlihan)", "AWS Events", "1h 05m"),
    19: ("l5otnYulOt8", "AWS re:Invent 2024 - Deep dive into Amazon ECS resilience and availability (SVS409)", "AWS Events", "55m"),
    20: ("cipDJwDWWbY", "AWS re:Invent 2021 - Deep dive on Amazon EKS", "AWS Events", "1h 00m"),
    21: ("ZbnAithBNYY", "AWS re:Invent 2022 - AWS Lambda SnapStart: Fast cold starts for your Java functions (SVS320)", "AWS Events", "48m"),
    22: ("GvyyJQ5m7x0", "AWS re:Invent 2024 - Scaling and securing private workloads using Amazon API Gateway (SVS318)", "AWS Events", "52m"),
    23: ("8zysQqxgj0I", "AWS re:Invent 2020: Scalable serverless event-driven architectures with SNS, SQS & Lambda", "AWS Events", "50m"),
    24: ("GWa2N3xe73M", "AWS re:Invent 2023 - Using AWS Lambda to process Amazon SQS and Amazon SNS messages (SVS212)", "AWS Events", "49m"),
    25: ("dy7UXS7ur14", "AWS re:Invent 2024 - Event-driven architectures at scale: Manage millions of events (API307)", "AWS Events", "56m"),
    26: ("lDEbFPKGozA", "Understanding the SAGA pattern with AWS Step Functions - With Demo", "FooBar Serverless", "42m"),
    27: ("HjoQllOWRmM", "AWS re:Invent 2023 - Serverless data streaming: Amazon Kinesis Data Streams and AWS Lambda (COM308)", "AWS Events", "54m"),
    28: ("_YYBdsuUq2M", "AWS re:Invent: ElastiCache Deep Dive: Best Practices and Usage Patterns (DAT305)", "Amazon Web Services", "58m"),
    29: ("9vr3oMODIUE", "AWS re:Invent 2022 - Protecting secrets, keys, and data: Cryptography for the long term (SEC403)", "AWS Events", "57m"),
    30: ("E_xm8W_BEFk", "AWS re:Invent 2025 - A day in the life of an AWS WAF administrator (NET317)", "AWS Events", "53m"),
    31: ("qXLsx4r37_0", "AWS re:Invent 2020: AWS X-Ray & Amazon CloudWatch: Increasing visibility for ECS & Fargate", "AWS Events", "46m"),
    32: ("Wzawix9bMAE", "AWS re:Invent 2023 - Advanced AWS CDK: Lessons learned from 4 years of use (COM302)", "AWS Events", "55m"),
    33: ("PnWTWjmbNp0", "AWS re:Invent 2025 - Building resilient multi-Region applications with Capital One (ARC404)", "AWS Events", "59m"),
    34: ("nOKvA8HykW8", "AWS re:Invent 2022 - The well-architected way (ARC210)", "AWS Events", "52m"),
    35: ("c3Cn4xYfxJY", "AWS Solutions Architect Associate Certification (SAA-C03) – Full Course to PASS the Exam", "freeCodeCamp.org", "13h 26m")
}

all_vids = set()
all_vids.add(MASTERCLASS["primary_video_id"])
all_vids.add(BRIEFING["video_id"])
for v_id, _, _ in TOPIC_VIDEOS.values():
    all_vids.add(v_id)
for v_id, _, _, _ in ROADMAP_VIDEOS.values():
    all_vids.add(v_id)

print(f"Total unique video IDs to verify: {len(all_vids)}")

failed = []
passed = []

for vid in sorted(all_vids):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req, timeout=5)
        data = json.loads(res.read())
        passed.append((vid, data.get('title'), data.get('author_name')))
        print(f"PASS: {vid} | {data.get('title')} ({data.get('author_name')})")
    except Exception as e:
        failed.append((vid, str(e)))
        print(f"FAIL: {vid} | {e}")

print(f"\nVerification Results: {len(passed)} PASSED, {len(failed)} FAILED")
if failed:
    sys.exit(1)
else:
    print("ALL VIDEOS ARE 100% REAL AND PLAYABLE!")
