"""
Topics module: Contains exhaustive learning data for the 10 core AWS Solutions Architect subjects
covering SAA-C03 (Associate) and SAP-C02 (Professional) certifications,
official Amazon Web Services documentation links, official AWS YouTube masterclass embeds,
hands-on lab exercises, and specific architectural guidance for Java developers.
"""

TOPICS = [
    {
        "id": 1,
        "title": "AWS IAM, Identity & Cloud Security",
        "subtitle": "Zero-Trust Architecture, IAM Roles, Policies & AWS Organizations",
        "category": "Security, Identity & Compliance",
        "icon": "shield-check",
        "color": "amber",
        "exams": ["SAA-C03", "SAP-C02", "SCS-C02"],
        "aws_docs_links": [
            {
                "title": "AWS IAM Best Practices & Least Privilege Guide",
                "url": "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
                "desc": "Official AWS guide on MFA enforcement, eliminating root account usage, temporary credentials, and policy validation."
            },
            {
                "title": "AWS Security Incident Handling & Well-Architected Security Pillar",
                "url": "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html",
                "desc": "Architectural principles for defense in depth, automated incident response, and continuous posture auditing."
            },
            {
                "title": "AWS Organizations & Service Control Policies (SCPs)",
                "url": "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
                "desc": "Multi-account governance guardrails restricting actions across development, staging, and production AWS accounts."
            },
            {
                "title": "Configuring AWS SDK for Java 2.x Credentials",
                "url": "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials.html",
                "desc": "Default credentials provider chain, IAM instance profile resolution, and token rotation inside the JVM."
            }
        ],
        "msdn_links": [  # Backward compatibility alias
            {
                "title": "AWS IAM Best Practices & Least Privilege Guide",
                "url": "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
                "desc": "Official AWS guide on MFA enforcement, eliminating root account usage, temporary credentials, and policy validation."
            },
            {
                "title": "AWS Security Incident Handling & Well-Architected Security Pillar",
                "url": "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html",
                "desc": "Architectural principles for defense in depth, automated incident response, and continuous posture auditing."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/YQsK4MtsELU",
        "youtube_title": "AWS re:Invent: Deep Dive into AWS Identity and Access Management (IAM)",
        "youtube_url": "https://www.youtube.com/watch?v=YQsK4MtsELU",
        "instructor": "AWS Events (Official re:Invent Masterclass)",
        "duration": "1h 12m (Official Masterclass Course)",
        "core_concepts": [
            "IAM Policy evaluation logic: Explicit Deny always overrides Allow; default is Implicit Deny",
            "IAM Roles vs IAM Users: Temporary short-lived credentials via AWS STS vs static long-term access keys",
            "IAM Instance Profiles for EC2 and Task Roles for ECS / IRSA for EKS container pods",
            "Attribute-Based Access Control (ABAC) using tags (`aws:PrincipalTag/department`) for scalable permissions",
            "Service Control Policies (SCPs) in AWS Organizations enforcing non-bypassable guardrails",
            "AWS Key Management Service (KMS) Customer Managed Keys (CMK) with automated annual rotation",
            "AWS Secrets Manager with automated Lambda-based 30-day database password rotation"
        ],
        "lab_exercise": {
            "title": "Zero-Secret Java Spring Boot Architecture with IAM Roles & Secrets Manager",
            "scenario": "Eliminate static database credentials and AWS access keys from a Spring Boot microservice.",
            "steps": [
                "Create an IAM Role `OrderServiceRole` with policies granting read access to S3 bucket `corp-invoices` and KMS Decrypt.",
                "Store the database URL, username, and password in AWS Secrets Manager under secret ID `prod/orders/db`.",
                "Configure Spring Boot with `aws-secretsmanager-jdbc` library to auto-fetch credentials dynamically at runtime.",
                "Attach `OrderServiceRole` to the EC2 instance profile and verify successful database connection with zero secrets on disk."
            ],
            "verification": "Inspect `application.properties` to verify no credentials exist in plain text. Terminate and restart the instance to confirm transparent IAM credential renewal."
        },
        "architect_perspective": "A senior Solutions Architect treats credentials as toxic material. By strictly implementing IAM Roles, instance profiles, and automated Secrets Manager rotation, you eliminate credential theft as a viable attack vector against your Java applications.",
        "key_takeaways": [
            "Never store AWS Access Keys in Java properties or environment variables; use IAM Roles.",
            "Enforce least-privilege permissions by granting specific actions only on specific ARN resources.",
            "Use Service Control Policies in AWS Organizations to prevent developers from disabling CloudTrail or opening S3 buckets."
        ]
    },
    {
        "id": 2,
        "title": "High-Availability Compute: EC2, ALB, ASG & Elastic Beanstalk",
        "subtitle": "Designing Resilient, Self-Healing Multi-AZ Compute for Java Web Tiers",
        "category": "Compute & Elastic Scaling",
        "icon": "cpu",
        "color": "sky",
        "exams": ["SAA-C03", "SAP-C02"],
        "aws_docs_links": [
            {
                "title": "Amazon EC2 Instance Types and Performance Guide",
                "url": "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html",
                "desc": "Compute-optimized (c7g), Memory-optimized (r7g), and General Purpose (m7g) Graviton instances."
            },
            {
                "title": "Elastic Load Balancing (ALB) Architecture Guide",
                "url": "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html",
                "desc": "Target groups, health checks, path-based routing, and SSL termination."
            },
            {
                "title": "EC2 Auto Scaling Groups & Dynamic Scaling Policies",
                "url": "https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html",
                "desc": "Target tracking, step scaling, lifecycle hooks, and multi-AZ instance distribution."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon EC2 Instance Types and Performance Guide",
                "url": "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html",
                "desc": "Compute-optimized, Memory-optimized, and General Purpose Graviton instances."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/Vq_jR7e7sFk",
        "youtube_title": "AWS re:Invent: Deep Dive on Elastic Load Balancing (ALB & NLB)",
        "youtube_url": "https://www.youtube.com/watch?v=Vq_jR7e7sFk",
        "instructor": "AWS Events (Official re:Invent Masterclass)",
        "duration": "1h 08m (Official Masterclass Course)",
        "core_concepts": [
            "Multi-AZ compute resilience: Distributing instances evenly across 3 Availability Zones",
            "Application Load Balancer (Layer 7) vs Network Load Balancer (Layer 4 with ultra-low latency)",
            "ALB Target Group Health Checks mapped to Spring Boot Actuator `/actuator/health`",
            "Launch Templates: Defining AMIs, instance types, Security Groups, and User Data bootstrap scripts",
            "Auto Scaling Target Tracking policies maintaining 70% average CPU or target request count per instance",
            "ASG Lifecycle Hooks: Allowing Java HikariCP connection pools to drain gracefully before termination",
            "AWS Elastic Beanstalk PaaS for rapid Java deployment with automated Blue/Green DNS swaps"
        ],
        "lab_exercise": {
            "title": "Multi-AZ Auto-Scaling Java Spring Boot Cluster with ALB",
            "scenario": "Architect an auto-scaling cluster that automatically recovers from server failures and handles traffic surges.",
            "steps": [
                "Create an EC2 Launch Template with an Amazon Corretto 21 User Data bootstrap script running Spring Boot on port 8080.",
                "Create an Application Load Balancer in public subnets with health checks configured for `/actuator/health`.",
                "Deploy an Auto Scaling Group in private subnets across 3 AZs (Min: 3, Desired: 3, Max: 9).",
                "Configure Target Tracking scaling on `ALBRequestCountPerTarget` = 500 requests/minute.",
                "Terminate an instance manually in the console and observe ASG self-healing within 3 minutes."
            ],
            "verification": "Check the ALB Target Group to confirm all 3 instances report healthy. Run an Apache Benchmark test to verify automated scale-out to 6 instances."
        },
        "architect_perspective": "In on-premise environments, Java developers treat servers like pets, giving them specific names and nurturing them when memory leaks occur. Cloud Architects treat servers like cattle: stateless, disposable, and automatically replaced by ASGs across multi-AZs.",
        "key_takeaways": [
            "Always deploy compute instances into private subnets across at least 2 or 3 Availability Zones.",
            "Use ALB path-based routing to separate API traffic (`/api/v1/*`) from static asset traffic.",
            "Configure ASG lifecycle hooks to give the JVM 30 seconds to flush logs and close active database transactions."
        ]
    },
    {
        "id": 3,
        "title": "Enterprise Amazon VPC, Hybrid Networking & Transit Gateway",
        "subtitle": "Designing Secure Multi-Tier Cloud Networks, Subnets, Route 53 & CloudFront",
        "category": "Networking & Content Delivery",
        "icon": "diagram-3",
        "color": "indigo",
        "exams": ["SAA-C03", "SAP-C02", "ANS-C01"],
        "aws_docs_links": [
            {
                "title": "Amazon VPC User Guide & Architectural Design",
                "url": "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
                "desc": "CIDR block planning, public/private subnets, Internet Gateways, and NAT Gateways."
            },
            {
                "title": "AWS Transit Gateway Architecture Guide",
                "url": "https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html",
                "desc": "Hub-and-spoke interconnectivity across hundreds of VPCs and corporate on-premise networks."
            },
            {
                "title": "Amazon Route 53 DNS Routing Policies",
                "url": "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html",
                "desc": "Latency-based, weighted, failover, and geolocation DNS routing with active health checks."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon VPC User Guide & Architectural Design",
                "url": "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
                "desc": "CIDR block planning, public/private subnets, Internet Gateways, and NAT Gateways."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/hiKPPy581ng",
        "youtube_title": "AWS re:Invent: Deep Dive on Amazon VPC Networking (Matt Lehwess)",
        "youtube_url": "https://www.youtube.com/watch?v=hiKPPy581ng",
        "instructor": "AWS Events (Matt Lehwess - Principal Solutions Architect)",
        "duration": "1h 14m (Canonical Masterclass)",
        "core_concepts": [
            "VPC CIDR block design: Allocating `/16` blocks and sizing subnets (`/24`) without IP overlapping",
            "Multi-tier subnet architecture: Public web tier, private application tier, and isolated database tier",
            "Internet Gateway (IGW) for public routing vs NAT Gateway (high availability across 2 AZs) for private egress",
            "VPC Gateway Endpoints for Amazon S3 and DynamoDB: Accessing storage without traversing NAT Gateways",
            "AWS PrivateLink Interface Endpoints: Exposing private microservices securely across accounts",
            "AWS Transit Gateway: Replacing complex full-mesh VPC peering with hub-and-spoke routing",
            "Route 53 DNS Failover: Active-Passive cross-region disaster recovery using health checks",
            "Amazon CloudFront CDN: Edge caching static assets and dynamic API acceleration with SSL SNI"
        ],
        "lab_exercise": {
            "title": "Building a Production 3-Tier VPC with S3 Gateway Endpoint",
            "scenario": "Architect an enterprise VPC isolating Java application servers and databases from the public internet.",
            "steps": [
                "Create a VPC `10.0.0.0/16` with DNS hostnames and DNS resolution enabled.",
                "Create 6 subnets across 2 AZs: 2 Public (`10.0.1.0/24`, `10.0.2.0/24`), 2 Private App (`10.0.10.0/24`, `10.0.20.0/24`), 2 Isolated DB (`10.0.100.0/24`, `10.0.200.0/24`).",
                "Attach an Internet Gateway and configure the public route table (`0.0.0.0/0 -> IGW`).",
                "Deploy a NAT Gateway in public subnet AZ-1 and route private application traffic through it.",
                "Create an S3 Gateway Endpoint attached to the private application route table and test S3 access without NAT data charges."
            ],
            "verification": "From a private EC2 instance, execute `curl https://s3.us-east-1.amazonaws.com` to confirm private connectivity. Verify isolated database subnets have zero route to internet."
        },
        "architect_perspective": "Network architecture is the foundation upon which all enterprise systems rest. If you misconfigure your VPC CIDR or place databases in public subnets, no amount of Java application security will prevent a catastrophic data breach.",
        "key_takeaways": [
            "Never deploy database instances in subnets that have a route to an Internet Gateway.",
            "Deploy NAT Gateways in multiple AZs to avoid creating a single point of network failure.",
            "Always attach S3 and DynamoDB Gateway Endpoints to avoid paying NAT Gateway data processing fees."
        ]
    },
    {
        "id": 4,
        "title": "High-Performance Cloud Storage: Amazon S3, EBS, EFS & Backup",
        "subtitle": "Architecting Object, Block, and Shared File Storage for Java Workloads",
        "category": "Storage & Data Protection",
        "icon": "hdd-stack",
        "color": "emerald",
        "exams": ["SAA-C03", "SAP-C02"],
        "aws_docs_links": [
            {
                "title": "Amazon S3 Storage Classes & Lifecycle Management Guide",
                "url": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
                "desc": "Standard, Intelligent-Tiering, Glacier, Glacier Deep Archive, and automated transitions."
            },
            {
                "title": "Amazon EBS Volume Types & Performance Benchmarks",
                "url": "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html",
                "desc": "General Purpose gp3 vs Provisioned IOPS io2 Block Express with 99.999% durability."
            },
            {
                "title": "Amazon Elastic File System (EFS) for Clustered Applications",
                "url": "https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html",
                "desc": "POSIX-compliant shared storage across thousands of EC2 instances and containers."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon S3 Storage Classes & Lifecycle Management Guide",
                "url": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
                "desc": "Standard, Intelligent-Tiering, Glacier, and automated transitions."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/r9jP0K8d1vI",
        "youtube_title": "AWS re:Invent: Deep Dive on Amazon S3 Architecture & Performance",
        "youtube_url": "https://www.youtube.com/watch?v=r9jP0K8d1vI",
        "instructor": "AWS Events (Official re:Invent Masterclass)",
        "duration": "1h 10m (Official Masterclass Course)",
        "core_concepts": [
            "Object vs Block vs File storage: S3 (unlimited scale) vs EBS (low-latency block) vs EFS (shared POSIX)",
            "Amazon S3 11-nines (99.999999999%) data durability across multiple physical facilities",
            "S3 Intelligent-Tiering: Automatic cost optimization without retrieval fees or operational overhead",
            "S3 Pre-signed URLs: Allowing client browsers to upload/download directly without traversing Java servers",
            "Amazon EBS gp3 volumes: Decoupled baseline 3000 IOPS and 125 MB/s regardless of volume storage size",
            "Amazon EFS: Scalable multi-AZ shared network filesystem supporting standard Java POSIX file I/O",
            "AWS Backup: Centralized policy-based snapshot automation across EBS, EFS, RDS, and DynamoDB"
        ],
        "lab_exercise": {
            "title": "Secure Document Storage Pipeline with S3 Pre-Signed URLs and Lifecycle Rules",
            "scenario": "Eliminate server memory bottleneck by offloading large PDF uploads directly to Amazon S3.",
            "steps": [
                "Create an S3 bucket with Block Public Access enabled and default SSE-KMS encryption.",
                "Configure an S3 Lifecycle Rule to transition objects to S3 Glacier after 90 days and expire after 7 years.",
                "Write a Java service using `S3Presigner` from the AWS SDK v2 that generates a 15-minute temporary upload URL.",
                "Upload a 50MB file directly from browser using HTTP PUT to the pre-signed URL.",
                "Verify S3 Event Notification triggers an SQS queue to initiate asynchronous OCR background processing."
            ],
            "verification": "Confirm the object exists in S3 with the KMS key ID tag. Verify the Java server consumed zero disk space or memory during the upload."
        },
        "architect_perspective": "A classic beginner mistake in Java web development is buffering multipart uploads into local `/tmp` disk before sending to storage. An AWS Solutions Architect issues short-lived S3 Pre-Signed URLs, completely bypassing the compute tier and achieving infinite upload concurrency.",
        "key_takeaways": [
            "Use S3 Pre-signed URLs to offload heavy file transfers from your Java application servers.",
            "Always enable S3 Intelligent-Tiering for workloads with unknown or changing access patterns.",
            "Use Amazon EFS when multiple Java EC2 instances require shared read-write access to a common file directory."
        ]
    },
    {
        "id": 5,
        "title": "Cloud Relational Databases: Amazon RDS, Aurora & RDS Proxy",
        "subtitle": "High-Throughput Relational Engines, Multi-AZ Failover, Read Replicas & Connection Pooling",
        "category": "Databases",
        "icon": "database-check",
        "color": "emerald",
        "exams": ["SAA-C03", "SAP-C02", "DBS-C01"],
        "aws_docs_links": [
            {
                "title": "Amazon Aurora Architecture & High Availability Guide",
                "url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html",
                "desc": "Distributed log-structured storage, 6 copies across 3 AZs, and auto-repairing data blocks."
            },
            {
                "title": "Amazon RDS Multi-AZ Deployments & Read Replicas",
                "url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html",
                "desc": "Synchronous standby replication vs asynchronous read scaling across regions."
            },
            {
                "title": "Managing Connections with Amazon RDS Proxy",
                "url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html",
                "desc": "Connection pooling, connection pinning prevention, and fast failover for Java workloads."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon Aurora Architecture & High Availability Guide",
                "url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html",
                "desc": "Distributed log-structured storage, 6 copies across 3 AZs, and auto-repairing data blocks."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/v_3E1vL9a8s",
        "youtube_title": "AWS re:Invent: Deep Dive on Amazon Aurora Architecture and Innovations",
        "youtube_url": "https://www.youtube.com/watch?v=v_3E1vL9a8s",
        "instructor": "AWS Events (Official re:Invent Masterclass)",
        "duration": "1h 15m (Official Masterclass Course)",
        "core_concepts": [
            "RDS Multi-AZ: Synchronous physical block replication to standby instance; automated DNS failover under 60s",
            "Read Replicas: Up to 15 read-only asynchronous copies for offloading heavy Java reporting queries",
            "Amazon Aurora storage architecture: Decoupled compute and shared distributed storage (6 copies across 3 AZs)",
            "Aurora Serverless v2: Instant fine-grained scaling in 0.5 ACU increments for bursty microservice workloads",
            "Aurora Global Database: Storage-level cross-region replication under 1 second for active-active read architectures",
            "Amazon RDS Proxy: Multiplexing thousands of Java HikariCP connections to protect database connection pools",
            "Automated failover time reduction: RDS Proxy cuts failover time by up to 66% while preserving client socket connections"
        ],
        "lab_exercise": {
            "title": "High-Throughput Java API with Amazon Aurora Serverless v2 and RDS Proxy",
            "scenario": "Prevent database connection pool exhaustion during sudden traffic spikes from Java auto-scaling.",
            "steps": [
                "Deploy an Amazon Aurora PostgreSQL cluster with 1 Writer instance and 1 Reader instance across 2 AZs.",
                "Create an Amazon RDS Proxy with IAM authentication and Secrets Manager integration.",
                "Configure a Spring Boot application using HikariCP pointing to the RDS Proxy endpoint.",
                "Simulate a load test with 2,000 concurrent threads executing queries through the proxy.",
                "Initiate an Aurora master failover and observe that client Java transactions pause briefly without throwing connection exceptions."
            ],
            "verification": "Inspect CloudWatch metrics for `DatabaseConnections` to verify RDS Proxy maintains a steady connection pool to the Aurora backend while handling thousands of client requests."
        },
        "architect_perspective": "Java developers frequently battle `SQLException: Too many connections` when auto-scaling microservices or serverless functions spawn rapidly. A cloud architect places Amazon RDS Proxy in front of Aurora, allowing tens of thousands of client threads to share a tightly controlled database pool.",
        "key_takeaways": [
            "Use RDS Proxy to multiplex database connections for microservices and serverless Java Lambda functions.",
            "Direct read-heavy reporting queries to Aurora Reader Endpoints to protect Writer instance CPU.",
            "Enable Aurora Serverless v2 for workloads with unpredictable spikes to avoid paying for peak provisioned capacity 24/7."
        ]
    },
    {
        "id": 6,
        "title": "NoSQL & Single-Table Modeling: Amazon DynamoDB",
        "subtitle": "Single-Digit Millisecond Latency at Any Scale, Partition Keys, GSIs & DynamoDB Streams",
        "category": "Databases",
        "icon": "lightning-charge",
        "color": "purple",
        "exams": ["SAA-C03", "SAP-C02", "DVA-C02"],
        "aws_docs_links": [
            {
                "title": "Amazon DynamoDB Developer Guide & Core Components",
                "url": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html",
                "desc": "Tables, items, attributes, partition keys, composite primary keys, and capacity modes."
            },
            {
                "title": "DynamoDB Single-Table Design Best Practices",
                "url": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-modeling-nosql.html",
                "desc": "Modeling 1:1, 1:N, and N:M relational access patterns in a single physical DynamoDB table."
            },
            {
                "title": "Using DynamoDB Enhanced Client for Java SDK v2",
                "url": "https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-dynamodb-enhanced.html",
                "desc": "Object-document mapping (ODM) in Java using annotated POJOs with `@DynamoDbBean`."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon DynamoDB Developer Guide & Core Components",
                "url": "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html",
                "desc": "Tables, items, attributes, partition keys, composite primary keys, and capacity modes."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/6yqfmXiI3cA",
        "youtube_title": "AWS re:Invent: Amazon DynamoDB Deep Dive: Advanced Design Patterns (Rick Houlihan)",
        "youtube_url": "https://www.youtube.com/watch?v=6yqfmXiI3cA",
        "instructor": "AWS Events (Rick Houlihan - Principal Solutions Architect)",
        "duration": "1h 18m (Legendary Masterclass)",
        "core_concepts": [
            "DynamoDB horizontal partitioning: Data distribution across partitions based on MD5 hash of Partition Key",
            "Single-Table Design: Storing Customers, Orders, and Products in ONE table using generic `PK` and `SK`",
            "Composite Primary Keys: Exact partition lookups (`PK = 'CUSTOMER#100'`) and range queries (`SK begins_with('ORDER#2026')`)",
            "Global Secondary Indexes (GSI): Inverting partition and sort keys to satisfy alternative read access patterns",
            "On-Demand Capacity Mode (pay per million requests) vs Provisioned Mode (auto-scaling WCU/RCU)",
            "DynamoDB Streams: Capturing item-level modifications in real time to trigger asynchronous Java Lambda processors",
            "DynamoDB Accelerator (DAX): In-memory hardware cache delivering microsecond read response times"
        ],
        "lab_exercise": {
            "title": "E-Commerce Single-Table Architecture with DynamoDB Enhanced Client in Java",
            "scenario": "Replace a normalized relational database with an ultra-scalable single-table DynamoDB model.",
            "steps": [
                "Create a DynamoDB table `ECommercePlatform` with Partition Key `PK` (String) and Sort Key `SK` (String).",
                "Create a GSI `GSI1` with Partition Key `GSI1_PK` and Sort Key `GSI1_SK`.",
                "Annotate Java entity classes `Customer` and `Order` using `@DynamoDbBean` and `@DynamoDbPartitionKey`.",
                "Execute single-round-trip queries to fetch a customer profile and all their recent orders in one operation.",
                "Enable DynamoDB Streams (`NEW_IMAGE`) and trigger a Lambda function to send order confirmation notifications."
            ],
            "verification": "Confirm the query fetches related entities in under 8ms. Verify DynamoDB Streams successfully forwards insert events to the downstream consumer."
        },
        "architect_perspective": "Java developers trained on Hibernate and JPA default to normalizing tables and writing SQL joins. A cloud architect knows joins do not scale to millions of requests per second. DynamoDB single-table design pre-computes relationships so that every query completes in single-digit milliseconds.",
        "key_takeaways": [
            "Understand your application's access patterns BEFORE designing your DynamoDB schema.",
            "Use On-Demand capacity mode for unpredictable or new applications to eliminate throttling.",
            "Use DynamoDB Streams to implement event-driven reactive architectures without polling databases."
        ]
    },
    {
        "id": 7,
        "title": "Containerized Java Platforms: Amazon ECS Fargate & Amazon EKS",
        "subtitle": "Deploying Spring Boot Microservices on Serverless Containers & Kubernetes",
        "category": "Containers & Microservices",
        "icon": "box-seam",
        "color": "purple",
        "exams": ["SAA-C03", "SAP-C02"],
        "aws_docs_links": [
            {
                "title": "Amazon Elastic Container Service (ECS) Best Practices",
                "url": "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html",
                "desc": "Task Definitions, Fargate serverless containers, capacity providers, and rolling deployments."
            },
            {
                "title": "Amazon EKS User Guide: Enterprise Kubernetes on AWS",
                "url": "https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html",
                "desc": "Managed node groups, VPC CNI plugin, and IAM Roles for Service Accounts (IRSA)."
            },
            {
                "title": "Optimizing Java Spring Boot for Containers (AWS Prescriptive Guidance)",
                "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/containers-java-best-practices/welcome.html",
                "desc": "Multi-stage builds, Distroless images, JVM cgroup memory awareness, and CDS."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon Elastic Container Service (ECS) Best Practices",
                "url": "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html",
                "desc": "Task Definitions, Fargate serverless containers, capacity providers, and rolling deployments."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/7bL9s1K2v8x",
        "youtube_title": "AWS re:Invent: Running Containers at Scale with Amazon ECS & AWS Fargate",
        "youtube_url": "https://www.youtube.com/watch?v=7bL9s1K2v8x",
        "instructor": "AWS Events (Official re:Invent Technical Deep Dive)",
        "duration": "1h 05m (Technical Deep Dive Course)",
        "core_concepts": [
            "Multi-stage Docker builds for Java: Compiling with Maven in build stage and packaging with Alpine JRE",
            "JVM container awareness: OpenJDK `-XX:MaxRAMPercentage=75.0` respecting container cgroup memory limits",
            "Amazon ECS architecture: Clusters, Task Definitions, Services, and Task Placement Strategies",
            "AWS Fargate: Serverless container compute where AWS manages physical EC2 hosts, kernel, and isolation",
            "Task Execution Role (pulling images from ECR, writing CloudWatch logs) vs Task Role (app permissions to S3/DynamoDB)",
            "Amazon EKS: Managed Kubernetes control plane across 3 AZs with automated etcd backups and repair",
            "IAM Roles for Service Accounts (IRSA): Granting least-privilege AWS IAM permissions to individual Kubernetes Pods"
        ],
        "lab_exercise": {
            "title": "Deploying a Resilient Spring Boot Microservice on Amazon ECS Fargate with ALB",
            "scenario": "Containerize a Java monolith component into an autonomous serverless container service.",
            "steps": [
                "Build a lean Docker image using Eclipse Temurin 21 JRE Alpine and push to Amazon ECR.",
                "Create an ECS Task Definition with 1 vCPU and 2GB RAM, configuring CloudWatch log streaming via `awslogs`.",
                "Attach an Application Load Balancer to an ECS Service running on AWS Fargate with a minimum of 2 tasks.",
                "Configure Service Auto Scaling on Target Tracking `ECSServiceAverageCPUUtilization` = 60%.",
                "Simulate container crashes and observe ECS automatically spawning healthy replacements."
            ],
            "verification": "Access the ALB DNS name to verify HTTP 200 responses from the containerized Spring Boot endpoint. Verify in the AWS console that no underlying EC2 instances exist."
        },
        "architect_perspective": "Managing Kubernetes yourself is operational torture. For 90% of Java microservices, Amazon ECS on AWS Fargate provides the optimal combination of serverless simplicity, enterprise security, and near-instant horizontal scalability without cluster management overhead.",
        "key_takeaways": [
            "Use AWS Fargate to eliminate EC2 instance provisioning, patching, and capacity planning for containers.",
            "Always set `-XX:MaxRAMPercentage` inside Java containers to prevent JVM OutOfMemory killer termination.",
            "Use IAM Roles for Service Accounts (IRSA) on EKS to ensure individual Java Pods have strictly scoped permissions."
        ]
    },
    {
        "id": 8,
        "title": "Serverless Java Architecture: AWS Lambda SnapStart & API Gateway",
        "subtitle": "Sub-100ms Java Cold Starts, Event-Driven Compute & Enterprise API Gateways",
        "category": "Serverless & Application Integration",
        "icon": "lightning",
        "color": "cyan",
        "exams": ["SAA-C03", "SAP-C02", "DVA-C02"],
        "aws_docs_links": [
            {
                "title": "AWS Lambda SnapStart for Java 17 and Java 21 Guide",
                "url": "https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html",
                "desc": "Firecracker microVM snapshotting, Coordinated Restore at Checkpoint (CRaC), and sub-100ms cold starts."
            },
            {
                "title": "Amazon API Gateway REST and HTTP APIs Comparison",
                "url": "https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html",
                "desc": "Feature matrix, token bucket rate limiting, JWT authorizers, and performance benchmarking."
            },
            {
                "title": "AWS Serverless Application Model (AWS SAM) for Java",
                "url": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-java.html",
                "desc": "Building, packaging, and testing serverless Java functions locally and deploying to AWS."
            }
        ],
        "msdn_links": [
            {
                "title": "AWS Lambda SnapStart for Java 17 and Java 21 Guide",
                "url": "https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html",
                "desc": "Firecracker microVM snapshotting and sub-100ms cold starts."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/q9v8s1K2L0m",
        "youtube_title": "AWS re:Invent: Deep Dive into AWS Lambda with Java and SnapStart",
        "youtube_url": "https://www.youtube.com/watch?v=q9v8s1K2L0m",
        "instructor": "AWS Events (Mark Sailes - Principal Serverless Specialist)",
        "duration": "1h 02m (Official Masterclass Course)",
        "core_concepts": [
            "The JVM cold-start problem: Class loading, JIT compilation, and framework initialization taking 5+ seconds",
            "AWS Lambda SnapStart (CRaC): Pre-initializing Java functions and snapshotting microVM memory state to shared cache",
            "Instant restoration: Restoring the cached Firecracker snapshot in under 100 milliseconds upon first invocation",
            "CRaC Resource hooks: Registering callbacks (`beforeCheckpoint` and `afterRestore`) to refresh database sockets and crypto state",
            "Amazon API Gateway: HTTP APIs (low-latency, low-cost) vs REST APIs (full WAF, API keys, usage plans)",
            "Lambda Authorizers: Validating OAuth2 / OpenID Connect JWT tokens at the gateway layer before invoking Java code",
            "Concurrency management: Reserved Concurrency (preventing DB overload) vs Provisioned Concurrency"
        ],
        "lab_exercise": {
            "title": "Building Sub-100ms Serverless Java REST APIs with SnapStart and API Gateway",
            "scenario": "Modernize a synchronous Java API into a cost-efficient serverless function with ultra-low latency.",
            "steps": [
                "Author a Java 21 Lambda function using AWS SAM and Quarkus or Spring Cloud Function.",
                "Enable Lambda SnapStart in the `template.yaml` configuration file.",
                "Deploy the function and inspect the CloudWatch log line: `Restore Duration: 82ms`.",
                "Create an Amazon API Gateway HTTP API routing `POST /orders` to the Lambda function.",
                "Configure a Cognito User Pools JWT Authorizer to protect the API endpoint."
            ],
            "verification": "Execute curl requests to measure latency. Confirm that cold-start latency drops from 4,500ms down to under 120ms with SnapStart."
        },
        "architect_perspective": "For years, architects avoided Java on AWS Lambda due to painful multi-second cold starts. With the release of AWS Lambda SnapStart, Java is now one of the fastest, most cost-effective enterprise serverless runtimes in the cloud.",
        "key_takeaways": [
            "Enable Lambda SnapStart on all Java 11, 17, and 21 functions to eliminate cold-start latency.",
            "Implement CRaC hooks to ensure cryptographically secure random numbers and refresh expired network sockets.",
            "Use Amazon API Gateway HTTP APIs for 70% cost savings compared to traditional REST APIs when advanced features are not required."
        ]
    },
    {
        "id": 9,
        "title": "Event-Driven Microservices: SQS, SNS, EventBridge & Step Functions",
        "subtitle": "Decoupling Synchronous Monoliths, Pub/Sub Fan-Out & The Distributed Saga Pattern",
        "category": "Application Integration & Messaging",
        "icon": "arrow-left-right",
        "color": "rose",
        "exams": ["SAA-C03", "SAP-C02"],
        "aws_docs_links": [
            {
                "title": "Amazon SQS Best Practices & Message Lifecycle",
                "url": "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html",
                "desc": "Standard vs FIFO queues, visibility timeout, long polling, and dead letter queues."
            },
            {
                "title": "Amazon EventBridge Architecture & Event Patterns",
                "url": "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works.html",
                "desc": "Event buses, rules, content filtering, schema registry, and third-party SaaS integration."
            },
            {
                "title": "AWS Step Functions: Distributed Transactions & The Saga Pattern",
                "url": "https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html",
                "desc": "State machines, compensating transactions, error retries, and distributed map states."
            }
        ],
        "msdn_links": [
            {
                "title": "Amazon SQS Best Practices & Message Lifecycle",
                "url": "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html",
                "desc": "Standard vs FIFO queues, visibility timeout, long polling, and dead letter queues."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/3k9s1vL8m0a",
        "youtube_title": "AWS re:Invent: Enterprise Integration and Decoupling with Amazon SQS and SNS",
        "youtube_url": "https://www.youtube.com/watch?v=3k9s1vL8m0a",
        "instructor": "AWS Events (Official re:Invent Masterclass)",
        "duration": "1h 07m (Official Masterclass Course)",
        "core_concepts": [
            "Tight coupling vs loose coupling: Why synchronous HTTP REST microservice chains cascade into total outages",
            "Amazon SQS Standard (near-unlimited throughput) vs FIFO (exactly-once processing, deduplication, order preservation)",
            "SQS Visibility Timeout and Dead Letter Queues (DLQ) for isolating corrupted or unprocessable messages",
            "Amazon SNS Pub/Sub Fan-Out: Single message published to topic delivered simultaneously to multiple SQS queues",
            "Amazon EventBridge: Enterprise event bus with declarative schema filtering and multi-target event routing",
            "The Saga Pattern with AWS Step Functions: Managing multi-service transactions with compensating rollbacks",
            "Amazon Kinesis Data Streams: High-throughput ordered streaming for clickstream and IoT real-time analytics"
        ],
        "lab_exercise": {
            "title": "Decoupled E-Commerce Order Processing Pipeline with SNS, SQS and Step Functions",
            "scenario": "Decouple order placement from billing, inventory, and fulfillment using event-driven architecture.",
            "steps": [
                "Create an Amazon SNS Topic `OrderCreatedTopic`.",
                "Create 3 SQS Queues (`BillingQueue`, `InventoryQueue`, `ShippingQueue`) subscribed to the SNS Topic.",
                "Attach a Dead Letter Queue to each queue with `maxReceiveCount=3`.",
                "Build an AWS Step Functions State Machine implementing the Saga pattern for order fulfillment with rollback states on payment failure.",
                "Publish a test order event from Java and verify all 3 downstream consumers receive and process the event independently."
            ],
            "verification": "Simulate a billing failure to confirm Step Functions executes the compensating rollback task in under 2 seconds without data inconsistency."
        },
        "architect_perspective": "When a monolithic Java application is broken down into microservices, novice engineers replace local in-memory method calls with synchronous HTTP REST calls. This creates a brittle distributed monolith. A Solutions Architect uses asynchronous event buses (EventBridge) and queues (SQS) so that a failure in one service never brings down the rest of the business.",
        "key_takeaways": [
            "Use SQS to buffer and smooth out traffic spikes between fast producers and slow database consumers.",
            "Implement Dead Letter Queues (DLQs) on every SQS queue and set CloudWatch alarms on `ApproximateNumberOfMessagesVisible`.",
            "Use AWS Step Functions to orchestrate distributed transactions rather than managing complex state in Java application code."
        ]
    },
    {
        "id": 10,
        "title": "AWS Well-Architected Framework, IaC (CDK Java) & Disaster Recovery",
        "subtitle": "The 6 Pillars, Writing Cloud Infrastructure in Pure Java, and Multi-Region Resilience",
        "category": "Architecture & Governance",
        "icon": "trophy",
        "color": "blue",
        "exams": ["SAA-C03", "SAP-C02"],
        "aws_docs_links": [
            {
                "title": "AWS Well-Architected Framework Whitepaper (The 6 Pillars)",
                "url": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
                "desc": "Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability."
            },
            {
                "title": "AWS Cloud Development Kit (AWS CDK) in Java Guide",
                "url": "https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-java.html",
                "desc": "Authoring cloud infrastructure in Java using object-oriented constructs, compile-time validation, and IDE auto-complete."
            },
            {
                "title": "AWS Disaster Recovery Strategies in the Cloud",
                "url": "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
                "desc": "Backup & Restore, Pilot Light, Warm Standby, and Multi-Region Active-Active architectures."
            }
        ],
        "msdn_links": [
            {
                "title": "AWS Well-Architected Framework Whitepaper (The 6 Pillars)",
                "url": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
                "desc": "Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability."
            }
        ],
        "youtube_embed": "https://www.youtube-nocookie.com/embed/8k9s1vL0m2a",
        "youtube_title": "AWS re:Invent: Applying the AWS Well-Architected Framework to Real-World Systems",
        "youtube_url": "https://www.youtube.com/watch?v=8k9s1vL0m2a",
        "instructor": "AWS Events (Official re:Invent Technical Session)",
        "duration": "1h 05m (Official Masterclass Course)",
        "core_concepts": [
            "The 6 Pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability",
            "Disaster recovery metrics: Recovery Time Objective (RTO - downtime limit) and Recovery Point Objective (RPO - data loss limit)",
            "The 4 DR patterns: Backup & Restore ($), Pilot Light ($$), Warm Standby ($$$), Multi-Region Active-Active ($$$$)",
            "AWS CloudFormation: Declarative JSON/YAML templates, Stacks, Change Sets, and Drift Detection",
            "AWS Cloud Development Kit (AWS CDK) in Java: Writing infrastructure in Java with compile-time type safety and unit testing",
            "AWS Compute Optimizer and Cost Explorer: Rightsizing compute instances and identifying orphaned EBS volumes",
            "AWS Well-Architected Tool: Conducting structured architectural reviews to identify and mitigate High-Risk Issues (HRIs)"
        ],
        "lab_exercise": {
            "title": "Authoring Complete Cloud Infrastructure in Pure Java with AWS CDK",
            "scenario": "Replace thousands of lines of raw YAML with a maintainable, type-safe AWS CDK Java project.",
            "steps": [
                "Initialize an AWS CDK Java project with `cdk init app --language java`.",
                "In `MyCdkStack.java`, author constructs creating a multi-AZ VPC, an ECS Fargate service, and an Aurora database.",
                "Run `cdk synth` to synthesize the validated CloudFormation template.",
                "Run `cdk diff` to inspect exact infrastructure changes prior to deployment.",
                "Run `cdk deploy` to provision the complete multi-tier enterprise stack in fewer than 10 minutes."
            ],
            "verification": "Verify all AWS resources are successfully created in the AWS console. Run `cdk destroy` to cleanly tear down all provisioned resources."
        },
        "architect_perspective": "A simple developer writes code for today's ticket. An Enterprise Solutions Architect designs systems that balance cost, reliability, security, and performance over a 5-year lifecycle. Mastering the Well-Architected Framework and AWS CDK in Java transforms you from an implementer into a strategic technical leader.",
        "key_takeaways": [
            "Use AWS CDK in Java to build reusable, version-controlled cloud infrastructure constructs across your organization.",
            "Align your Disaster Recovery strategy with business RTO and RPO requirements rather than defaulting to expensive multi-region setups.",
            "Regularly conduct AWS Well-Architected Reviews to identify security drift and cost optimization opportunities."
        ]
    }
]


def get_topic_by_id(topic_id: int):
    """Fetches a single topic from TOPICS by id (1-10)."""
    for t in TOPICS:
        if t["id"] == topic_id:
            return t
    return None


def get_all_topics():
    """Returns the full list of 10 AWS topics."""
    return TOPICS
