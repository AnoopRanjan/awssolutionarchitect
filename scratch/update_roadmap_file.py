import re

mapping = {
    1: ("PAr1DY82ymE", "AWS re:Invent 2024 - Anatomy of an AWS Region (ARC204)", "AWS Events (Official re:Invent)", "56m (Official Architecture Session)"),
    2: ("YQsK4MtsELU", "AWS re:Invent: Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1)", "Amazon Web Services (Official re:Invent)", "1h 12m (Official Masterclass Course)"),
    3: ("2uc1vaEsPXU", "AWS re:Invent 2021 - Powering next-gen Amazon EC2: Deep dive on the Nitro System", "AWS Events (Official re:Invent)", "58m (Official Compute Deep Dive)"),
    4: ("Ya4WFO9P0i8", "AWS re:Invent 2022 - Layered VPC security and inspection (NET311)", "AWS Events (Official re:Invent)", "52m (Official Security Deep Dive)"),
    5: ("6iO6wtDOKGM", "AWS re:Invent 2023 - Enhance your app's security & availability with Elastic Load Balancing (NET318)", "AWS Events (Official re:Invent)", "54m (Official ELB Deep Dive)"),
    6: ("nlGyIa3UQYU", "AWS re:Invent 2023 - Strategies for automated scaling, remediation, and smart self-healing (ENT107)", "AWS Events (Official re:Invent)", "51m (Official Auto Scaling Deep Dive)"),
    7: ("Ozc5Yu_IcaI", "Deploy Java Web Application in AWS Elastic Beanstalk | AWS Tutorial for Beginners", "Edureka (Hands-on Java Deployment)", "45m (Hands-On Implementation)"),
    8: ("NXehLy7IiPM", "AWS re:Invent 2024 - Dive deep on Amazon S3 (STG302)", "AWS Events (Official re:Invent)", "59m (Official Storage Masterclass)"),
    9: ("WZGG8RkvApY", "AWS re:Invent 2023 - Amazon S3 security and access control best practices (STG315)", "AWS Events (Official re:Invent)", "53m (Official Security Deep Dive)"),
    10: ("m03ICK5ZsA0", "AWS re:Invent 2024 - Simple Elastic File Systems: A Deep Dive into Amazon EFS (STG344)", "AWS Events (Official re:Invent)", "58m (Official Storage Deep Dive)"),
    11: ("7qaSfmnFiI0", "AWS re:Invent 2024 - Amazon VPC: Advanced design and what's new (NET301)", "AWS Events (Official re:Invent)", "57m (Official Networking Deep Dive)"),
    12: ("9Nikqn_02Oc", "AWS re:Invent: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)", "AWS Events (Official re:Invent)", "58m (Official Network Architecture)"),
    13: ("mczl5zhQcYQ", "AWS re:Invent 2022 - Amazon Route 53: What's in a domain name? A lot! (NET206)", "AWS Events (Official re:Invent)", "55m (Official DNS Deep Dive)"),
    14: ("lLnKaPqL3u0", "AWS re:Invent 2024 - Amazon CloudFront: Enhancing web performance one HTTP request at a time (CDN308)", "AWS Events (Official re:Invent)", "56m (Official CDN & Edge Deep Dive)"),
    15: ("TJxC-B9Q9tQ", "AWS re:Invent: Deep Dive on Amazon Relational Database Service (RDS) (DAT302)", "Amazon Web Services (Official re:Invent)", "1h 01m (Official Database Deep Dive)"),
    16: ("kVVdHezNTpw", "AWS re:Invent 2024 - Deep dive into Amazon Aurora and its innovations (DAT405)", "AWS Events (Official re:Invent)", "1h 00m (Official Aurora Masterclass)"),
    17: ("VFsGJIeuR_Y", "AWS re:Invent 2020: Deep dive into Amazon RDS Proxy for scaling applications", "AWS Events (Official re:Invent)", "48m (Official Connection Scaling Deep Dive)"),
    18: ("xfxBhvGpoa0", "AWS re:Invent 2021 - DynamoDB deep dive: Advanced design patterns (Rick Houlihan)", "AWS Events (Official re:Invent)", "1h 05m (Official Single-Table Masterclass)"),
    19: ("l5otnYulOt8", "AWS re:Invent 2024 - Deep dive into Amazon ECS resilience and availability (SVS409)", "AWS Events (Official re:Invent)", "55m (Official Container Deep Dive)"),
    20: ("cipDJwDWWbY", "AWS re:Invent 2021 - Deep dive on Amazon EKS", "AWS Events (Official re:Invent)", "1h 00m (Official Kubernetes Architecture)"),
    21: ("ZbnAithBNYY", "AWS re:Invent 2022 - AWS Lambda SnapStart: Fast cold starts for your Java functions (SVS320)", "AWS Events (Official re:Invent)", "48m (Official Serverless Java Masterclass)"),
    22: ("GvyyJQ5m7x0", "AWS re:Invent 2024 - Scaling and securing private workloads using Amazon API Gateway (SVS318)", "AWS Events (Official re:Invent)", "52m (Official API Gateway Deep Dive)"),
    23: ("8zysQqxgj0I", "AWS re:Invent 2020: Scalable serverless event-driven architectures with SNS, SQS & Lambda", "AWS Events (Official re:Invent)", "50m (Official Messaging Architecture)"),
    24: ("GWa2N3xe73M", "AWS re:Invent 2023 - Using AWS Lambda to process Amazon SQS and Amazon SNS messages (SVS212)", "AWS Events (Official re:Invent)", "49m (Official Pub/Sub Integration)"),
    25: ("dy7UXS7ur14", "AWS re:Invent 2024 - Event-driven architectures at scale: Manage millions of events (API307)", "AWS Events (Official re:Invent)", "56m (Official EventBridge Masterclass)"),
    26: ("lDEbFPKGozA", "Understanding the SAGA pattern with AWS Step Functions - With Demo", "FooBar Serverless (Enterprise Architecture)", "42m (Distributed Transactions Masterclass)"),
    27: ("HjoQllOWRmM", "AWS re:Invent 2023 - Serverless data streaming: Amazon Kinesis Data Streams and AWS Lambda (COM308)", "AWS Events (Official re:Invent)", "54m (Official Streaming Deep Dive)"),
    28: ("_YYBdsuUq2M", "AWS re:Invent: ElastiCache Deep Dive: Best Practices and Usage Patterns (DAT305)", "Amazon Web Services (Official re:Invent)", "58m (Official Caching Deep Dive)"),
    29: ("9vr3oMODIUE", "AWS re:Invent 2022 - Protecting secrets, keys, and data: Cryptography for the long term (SEC403)", "AWS Events (Official re:Invent)", "57m (Official Security & Cryptography)"),
    30: ("E_xm8W_BEFk", "AWS re:Invent 2025 - A day in the life of an AWS WAF administrator (NET317)", "AWS Events (Official re:Invent)", "53m (Official Edge Security Masterclass)"),
    31: ("qXLsx4r37_0", "AWS re:Invent 2020: AWS X-Ray & Amazon CloudWatch: Increasing visibility for ECS & Fargate", "AWS Events (Official re:Invent)", "46m (Official Observability Deep Dive)"),
    32: ("Wzawix9bMAE", "AWS re:Invent 2023 - Advanced AWS CDK: Lessons learned from 4 years of use (COM302)", "AWS Events (Official re:Invent)", "55m (Official Infrastructure as Code Deep Dive)"),
    33: ("PnWTWjmbNp0", "AWS re:Invent 2025 - Building resilient multi-Region applications with Capital One (ARC404)", "AWS Events (Official re:Invent)", "59m (Enterprise Multi-Region Resilience)"),
    34: ("nOKvA8HykW8", "AWS re:Invent 2022 - The well-architected way (ARC210)", "AWS Events (Official re:Invent)", "52m (Official Architectural Excellence)"),
    35: ("c3Cn4xYfxJY", "AWS Solutions Architect Associate Certification (SAA-C03) – Full Course to PASS the Exam", "freeCodeCamp.org & Andrew Brown (Official ExamPro AWS Masterclass)", "13h 26m (Complete SAA-C03 Blueprint & Exam Pitch)")
}

with open('data/roadmap.py', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to update each day dictionary in content
# Split content into days or use regex matching day blocks
day_blocks = re.split(r'(\s*\{\s*"day":\s*\d+,)', content)
# day_blocks[0] is preamble before Day 1
new_content = [day_blocks[0]]

for i in range(1, len(day_blocks), 2):
    header = day_blocks[i]
    body = day_blocks[i+1]
    day_match = re.search(r'"day":\s*(\d+)', header)
    if day_match:
        day_num = int(day_match.group(1))
        vid, vtitle, vinst, vdur = mapping[day_num]
        vembed = f"https://www.youtube-nocookie.com/embed/{vid}"
        vurl = f"https://www.youtube.com/watch?v={vid}"

        # Replace video fields in body
        body = re.sub(r'"video_id":\s*"[^"]*"', f'"video_id": "{vid}"', body)
        body = re.sub(r'"video_title":\s*"[^"]*"', f'"video_title": "{vtitle}"', body)
        body = re.sub(r'"video_instructor":\s*"[^"]*"', f'"video_instructor": "{vinst}"', body)
        body = re.sub(r'"video_duration":\s*"[^"]*"', f'"video_duration": "{vdur}"', body)
        body = re.sub(r'"video_embed":\s*"[^"]*"', f'"video_embed": "{vembed}"', body)
        body = re.sub(r'"video_url":\s*"[^"]*"', f'"video_url": "{vurl}"', body)

    new_content.append(header)
    new_content.append(body)

updated_content = "".join(new_content)

with open('data/roadmap.py', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Successfully updated all 35 days in data/roadmap.py!")
