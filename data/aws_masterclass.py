"""
AWS Solutions Architect Transformation Masterclass module.
Tailored for transforming a simple Java Developer into an Enterprise AWS Solutions Architect in 35 days.
Features official Amazon Web Services & AWS Events video masterclasses, architectural briefing,
and the 5 core cloud modernization pillars.
"""

AWS_MASTER_COURSE = {
    "title": "AWS Certified Solutions Architect & Enterprise Modernization Masterclass",
    "subtitle": "Bridging Java Enterprise Applications to High-Availability Cloud Architecture on AWS",
    "primary_video_id": "7m_q1cRePO8",
    "primary_video_title": "AWS re:Invent: Architecture Best Practices & Global Cloud Resilience",
    "instructor": "Amazon Web Services (Official AWS Events & Architecture Team)",
    "duration": "3h 15m (Comprehensive Masterclass)",
    "embed_url": "https://www.youtube-nocookie.com/embed/7m_q1cRePO8",
    "watch_url": "https://www.youtube.com/watch?v=7m_q1cRePO8",
    "description": (
        "An intensive, master-level architectural blueprint designed to elevate simple Java developers into "
        "AWS Solutions Architects. Covers cloud-native application transformation: moving from monolithic Spring Boot "
        "and local databases to resilient, multi-AZ compute (EC2, ALB, ASG), Amazon Aurora, DynamoDB single-table design, "
        "ECS Fargate containers, Lambda SnapStart serverless microservices, and decoupled event-driven architectures (SQS, SNS, EventBridge)."
    ),
    "modules": [
        {
            "num": 1,
            "title": "From Localhost JAR to Multi-AZ Resilient Compute",
            "desc": "Translating Spring Boot, Tomcat, and JVM execution to EC2, Elastic Load Balancing, and Auto Scaling."
        },
        {
            "num": 2,
            "title": "Enterprise Networking & Security Perimeter",
            "desc": "Designing secure multi-tier VPCs, private subnets, Transit Gateways, Route 53, and IAM zero-trust."
        },
        {
            "num": 3,
            "title": "High-Throughput Cloud Databases & Caching",
            "desc": "Migrating from single-node MySQL/PostgreSQL to Amazon Aurora, DynamoDB NoSQL, and ElastiCache Redis."
        },
        {
            "num": 4,
            "title": "Containerization & Serverless Java with SnapStart",
            "desc": "Packaging Java microservices into Docker containers on ECS Fargate / EKS and sub-100ms Lambda functions."
        },
        {
            "num": 5,
            "title": "Event-Driven Decoupling & Well-Architected Framework",
            "desc": "Asynchronous messaging with SQS, SNS, and EventBridge, AWS CDK in Java, and SAA-C03/SAP-C02 exam mastery."
        }
    ]
}

# Alias for backward compatibility if imported as FDE_MASTER_COURSE
FDE_MASTER_COURSE = AWS_MASTER_COURSE

AWS_BRIEFING_10MIN = {
    "title": "Executive Architecture Briefing: Scaling on AWS for the First 10 Million Users",
    "video_id": "gB5bY1V_P-Y",
    "video_title": "AWS re:Invent: Scaling on AWS From Single Server to Global Scale",
    "instructor": "Amazon Web Services (Official AWS Events)",
    "duration": "14m 20s (Executive Briefing)",
    "embed_url": "https://www.youtube-nocookie.com/embed/gB5bY1V_P-Y",
    "watch_url": "https://www.youtube.com/watch?v=gB5bY1V_P-Y",
    "summary": (
        "A fast-paced executive walk-through showing how a basic monolithic application (such as a Java Spring Boot backend "
        "with single-node MySQL) evolves stage-by-stage into a fault-tolerant, horizontally auto-scaled, multi-AZ system "
        "using S3, CloudFront CDN, RDS Aurora with Read Replicas, ElastiCache Redis, and SQS event workers."
    )
}

# Alias for backward compatibility
FDE_BRIEFING_10MIN = AWS_BRIEFING_10MIN

PROJECT_EXPLORATION_PILLARS = [
    {
        "id": "pillar-1",
        "title": "Elastic Compute & Resilient Java Infrastructure",
        "icon": "bi-cpu-fill",
        "color": "sky",
        "services": ["EC2", "ALB", "ASG", "Elastic Beanstalk"],
        "description": "Shift from fixed-capacity servers to dynamic, self-healing compute clusters that scale automatically based on JVM metrics and traffic demands."
    },
    {
        "id": "pillar-2",
        "title": "Enterprise VPC Networking & Global Delivery",
        "icon": "bi-diagram-3-fill",
        "color": "indigo",
        "services": ["VPC", "Transit Gateway", "Route 53", "CloudFront"],
        "description": "Architect isolated multi-tier networks with public and private subnets, secure NAT Gateways, global DNS latency routing, and edge caching."
    },
    {
        "id": "pillar-3",
        "title": "Modern Cloud Databases & In-Memory Caching",
        "icon": "bi-database-fill-check",
        "color": "emerald",
        "services": ["Amazon Aurora", "DynamoDB", "RDS Proxy", "ElastiCache"],
        "description": "Replace single-instance SQL databases with high-throughput Aurora clusters, single-table NoSQL modeling, and sub-millisecond Redis caches."
    },
    {
        "id": "pillar-4",
        "title": "Containers, Kubernetes & Serverless Java",
        "icon": "bi-box-seam-fill",
        "color": "purple",
        "services": ["ECS Fargate", "EKS", "Lambda SnapStart", "API Gateway"],
        "description": "Containerize Spring Boot applications into serverless Fargate tasks or orchestrate with EKS, and deploy sub-100ms Java Lambda functions."
    },
    {
        "id": "pillar-5",
        "title": "Event-Driven Decoupling & Well-Architected Security",
        "icon": "bi-shield-lock-fill",
        "color": "amber",
        "services": ["SQS", "SNS", "EventBridge", "KMS", "CDK in Java"],
        "description": "Decouple synchronous Java HTTP calls with asynchronous event buses, enforce zero-trust with KMS encryption, and write IaC in pure Java."
    }
]

AWS_PILLARS = PROJECT_EXPLORATION_PILLARS
