"""
Interview Preparation module: Strategy, 20 deep scenario interview questions,
model answers, and elevator pitch tailored for transforming a simple Java Developer
into an elite Enterprise AWS Solutions Architect.
Covers AWS SAA-C03 (Associate) and SAP-C02 (Professional) core architectural trade-offs.
"""

POSITIONING_STRATEGY = {
    "headline": "Enterprise AWS Solutions Architect | Cloud Migration & Modernization Lead | Distributed Systems & Java Microservices Specialist",
    "value_proposition": (
        "I bridge the critical gap between deep software engineering reality and high-level enterprise cloud architecture. "
        "Because I built, profiled, and debugged Java Spring Boot applications, multi-threaded JVMs, and relational database queries, "
        "I design AWS architectures (Aurora, ECS Fargate, DynamoDB, Lambda SnapStart, EventBridge) that developers love to implement "
        "and that meet the strictest C-level requirements for security, reliability, performance, and cost optimization."
    ),
    "what_to_avoid": "Do NOT introduce yourself as just a developer who completed an AWS tutorial or memorized certification flashcards. Avoid claiming you only configure YAML without understanding system architecture.",
    "what_to_own": "Own your extensive software engineering background in Java as your greatest competitive advantage! Emphasize that the most dangerous cloud architects are the ones who never wrote production code, whereas you understand the real-world performance, thread-pooling, and latency impacts of cloud architectural choices.",
    "experience_framing_tip": "When asked 'How long have you worked with AWS?', respond with confidence: 'I have engineered enterprise Java applications for years, and over the past several years, I have architected and migrated those systems directly into AWS—designing multi-tier VPCs, Aurora clusters, containerized Fargate deployments, and event-driven serverless architectures.'"
}

ELEVATOR_PITCH = """I bring a powerful dual background as an enterprise software engineer rooted in Java microservices and a certified AWS Solutions Architect—which gives me a rare, grounded perspective on building cloud systems that actually scale.

Throughout my career, I've seen organizations struggle because cloud architects design theoretical diagrams that fall apart during high-concurrency production deployments—such as exhausting MySQL connection pools during auto-scaling or suffering from severe serverless cold starts. Because I understand the JVM, memory management, connection pooling, and multi-threading, I architect AWS solutions that prevent these bottlenecks before they reach production.

My architectural focus spans resilient multi-AZ and multi-region compute across EC2, ALB, and ECS Fargate; cloud-native databases with Amazon Aurora and DynamoDB single-table design; sub-100ms serverless architectures with Lambda SnapStart; and event-driven decoupling with Amazon EventBridge, SQS, and Step Functions.

As an Enterprise Solutions Architect, I don't just hand over diagrams—I design scalable, cost-optimized, Well-Architected platforms and partner closely with engineering teams to guide them through flawless cloud execution."""

INTERVIEW_QUESTIONS = [
    {
        "id": 1,
        "category": "Architectural Positioning",
        "question": "How does your software engineering background in Java help you succeed as an AWS Solutions Architect?",
        "model_answer": "Many cloud architects come from pure IT infrastructure or networking backgrounds and treat applications as black boxes. Because of my deep background in Java and Spring Boot, I understand exactly what happens inside the application runtime: how connection pooling (HikariCP) behaves under load, how JVM garbage collection impacts tail latency, and how synchronous HTTP microservice chains create cascading failure domains. When I architect an AWS solution using Amazon Aurora with RDS Proxy, ECS Fargate, or Lambda SnapStart, I design around application realities, ensuring that the cloud infrastructure and the software layer work in seamless harmony.",
        "key_points": ["Deep runtime awareness", "Application-infrastructure synergy", "Eliminating black-box architectural assumptions", "Credibility with engineering teams"]
    },
    {
        "id": 2,
        "category": "Relational Databases & Scalability",
        "question": "A Java microservice fleet running on ECS auto-scales from 10 to 100 instances during flash sales and immediately crashes the PostgreSQL database with 'Too many connections'. How do you architect a solution?",
        "model_answer": "This is a classic connection pool multiplication problem: each of the 100 Spring Boot instances initializes its own HikariCP pool of 20 connections, attempting to open 2,000 concurrent database sockets against a database configured for a maximum of 500 connections. I would solve this by introducing Amazon RDS Proxy between ECS and the PostgreSQL cluster. RDS Proxy sits within the VPC, maintains a shared pool of idle database connections, and multiplexes thousands of incoming application connections over a small, persistent set of database sockets. Furthermore, I would configure read-only traffic to route through the Aurora Reader Endpoint and audit HikariCP settings (`maximumPoolSize=5-10`). As a result, connection exhaustion is completely eliminated, and failover recovery time during an AZ outage is reduced by up to 66%.",
        "key_points": ["Connection pool multiplication diagnosis", "Amazon RDS Proxy multiplexing", "Aurora Reader endpoint separation", "HikariCP rightsizing", "66% failover time reduction"]
    },
    {
        "id": 3,
        "category": "Serverless Java Architecture",
        "question": "Our leadership wants to migrate our customer-facing REST APIs to AWS Lambda, but the team is concerned about multi-second JVM cold starts. How do you solve this as an architect?",
        "model_answer": "Traditionally, Java cold starts on Lambda took 3 to 6 seconds due to JVM class loading, bytecode verification, and framework initialization (like Spring component scanning). I would architect this using AWS Lambda SnapStart, which is based on Firecracker microVM snapshotting (CRaC - Coordinated Restore at Checkpoint). When a function version is published, AWS initializes the JVM, loads all classes, runs framework startup, and takes a snapshot of the encrypted microVM memory state. When a live request arrives, AWS restores the memory snapshot in under 100 milliseconds. For stateful dependencies, I implement CRaC resource hooks to refresh database connections and ensure cryptographic seed randomness post-restore. For ultra-low latency, I would pair this with Quarkus or Micronaut on Java 21 on Graviton.",
        "key_points": ["AWS Lambda SnapStart (CRaC)", "Firecracker microVM memory snapshotting", "Sub-100ms restoration latency", "CRaC hooks for sockets and randomness", "Framework selection (Quarkus / Spring Cloud Function)"]
    },
    {
        "id": 4,
        "category": "NoSQL Architecture",
        "question": "When would you architect a solution using Amazon DynamoDB with Single-Table Design instead of Amazon Aurora PostgreSQL?",
        "model_answer": "I recommend Amazon DynamoDB when the workload requires predictable single-digit millisecond latency at massive scale (tens of thousands to millions of requests per second), where horizontal scaling must happen automatically without manual sharding, and where access patterns are well-understood. Using Single-Table Design with composite partition and sort keys (`PK` and `SK`), I can satisfy 1:1, 1:N, and N:M relationships in a single round-trip query without relational joins. Conversely, I choose Amazon Aurora PostgreSQL when the business requires ad-hoc analytics, flexible reporting queries that cannot be predicted upfront, complex aggregations, or strict ACID compliance across multiple tables that cannot be modeled in a single transactional write.",
        "key_points": ["Predictable single-digit ms latency at any scale", "Single-Table design access pattern pre-computation", "Aurora for ad-hoc SQL, complex joins and analytics", "Cost predictability at high throughput"]
    },
    {
        "id": 5,
        "category": "High Availability & Multi-Region DR",
        "question": "Design an active-passive disaster recovery architecture on AWS for a core financial application with an RTO of 60 seconds and an RPO of 1 second.",
        "model_answer": "To meet an RPO under 1 second and RTO under 60 seconds, I architect a Warm Standby multi-region design across us-east-1 (Primary) and eu-west-1 (Secondary). At the database layer, I deploy Amazon Aurora Global Database: dedicated storage nodes replicate data across continents with typical replication lag under 1 second, meeting the RPO requirement. In the secondary region, I provision a minimal footprint of ECS Fargate tasks and an Application Load Balancer. At the global routing layer, Amazon Route 53 is configured with Failover Routing and health checks pinging the primary ALB `/actuator/health` endpoint. If the primary region fails, Route 53 shifts DNS traffic to the secondary region, Aurora Global DB is promoted to standalone writer in under 45 seconds via AWS CLI or Lambda, and ECS auto-scaling scales up to full production capacity, meeting the 60-second RTO.",
        "key_points": ["Aurora Global Database storage-level replication (RPO < 1s)", "Amazon Route 53 Failover routing with health checks", "Warm Standby scaled-down ECS Fargate fleet", "Automated secondary cluster promotion (RTO < 60s)"]
    },
    {
        "id": 6,
        "category": "Decoupled Integration",
        "question": "What is the difference between Amazon SQS, Amazon SNS, and Amazon EventBridge? How do you choose between them?",
        "model_answer": "All three are messaging services, but they serve distinct architectural patterns. Amazon SQS is a point-to-point pull/polling queue used to buffer work between producers and consumers (1 message to 1 worker) with guaranteed durability and worker decoupling. Amazon SNS is a push-based pub/sub topic used for 1-to-many fan-out (1 message to thousands of subscribers like SQS queues, SMS, email) with ultra-high throughput and microsecond latency. Amazon EventBridge is an enterprise event bus with intelligent content-based filtering, schema registry, and native integration with 20+ AWS services and third-party SaaS (like Salesforce/Datadog). I choose SQS for buffering and asynchronous worker jobs, SNS when fanning out high-volume events to multiple queues, and EventBridge when building complex event-driven routing rules based on JSON payload contents.",
        "key_points": ["SQS: Pull-based 1:1 queue buffering", "SNS: Push-based 1:Many fan-out topic", "EventBridge: Content-filtered enterprise event bus", "Architecture selection criteria"]
    },
    {
        "id": 7,
        "category": "Distributed Transactions",
        "question": "How do you implement the Saga Pattern in an AWS event-driven microservice architecture?",
        "model_answer": "In distributed microservices, traditional Two-Phase Commit (2PC) locks resources across databases and fails to scale. I implement the Saga Pattern using AWS Step Functions as an orchestrator. Step Functions coordinates forward transactions: Step 1 invokes a Lambda to reserve inventory in Redis/DynamoDB; Step 2 invokes a payment service; Step 3 notifies shipping via SQS. If Step 2 (payment) fails, Step Functions catches the error state and executes compensating transactions in reverse order—such as invoking a Lambda to release the reserved inventory and notifying the customer. Step Functions provides visual auditing, automated retry policies with exponential backoff, and guarantees that distributed transactions either complete successfully or roll back to a consistent state.",
        "key_points": ["Why 2PC fails in cloud distributed systems", "Orchestration-based Saga with AWS Step Functions", "Forward transactions vs compensating rollbacks", "Visual auditability and error catching"]
    },
    {
        "id": 8,
        "category": "Network Security & Zero Trust",
        "question": "Explain the difference between a Security Group and a Network ACL. What are the best practices for a multi-tier web application?",
        "model_answer": "Security Groups operate at the individual ENI (instance) level and are stateful: if traffic is allowed inbound, response traffic is automatically permitted outbound regardless of outbound rules. Network ACLs (NACLs) operate at the subnet boundary and are stateless: rules are evaluated in numbered order, and both inbound and outbound traffic must be explicitly permitted, including ephemeral ports (1024-65535). For a production multi-tier application, best practice uses Security Groups as the primary defense: ALB SG accepts 80/443 from internet; Application SG accepts 8080 ONLY from ALB SG; Database SG accepts 5432 ONLY from Application SG. NACLs act as a coarse subnet firewall to block specific malicious CIDR ranges or enforce strict compliance baselines across entire subnets.",
        "key_points": ["Stateful (SG) vs Stateless (NACL)", "ENI level vs Subnet boundary", "3-tier Security Group chaining", "Ephemeral ports requirement in NACLs"]
    },
    {
        "id": 9,
        "category": "Storage & Cost Optimization",
        "question": "An enterprise generates 50TB of PDF invoice files every month. How do you design a cost-optimized, compliant storage architecture on Amazon S3?",
        "model_answer": "I would implement an Amazon S3 Lifecycle policy to automatically optimize storage costs across the data lifecycle. For the first 30 days when invoices are frequently downloaded by customers, objects stay in S3 Standard. After 30 days, lifecycle rules transition them to S3 Intelligent-Tiering to capture automated tiering savings without operational overhead. After 90 days, invoices are transitioned to S3 Glacier Flexible Retrieval (costing ~$0.0036/GB/month vs $0.023 for Standard, an 84% savings). After 1 year, compliance archives move to S3 Glacier Deep Archive ($0.00099/GB/month, a 95% savings) with S3 Object Lock in Compliance mode to guarantee legal WORM (Write Once Read Many) immutability against accidental deletion for 7 years.",
        "key_points": ["S3 Lifecycle transitions (Standard -> Intelligent-Tiering -> Glacier -> Deep Archive)", "95% cost reduction calculation", "S3 Object Lock (WORM) for regulatory compliance", "Pre-signed URLs for zero-compute retrieval"]
    },
    {
        "id": 10,
        "category": "Containers & Kubernetes",
        "question": "How do you choose between Amazon ECS on AWS Fargate and Amazon EKS for deploying containerized Java microservices?",
        "model_answer": "I evaluate this across team expertise, operational overhead, and multi-cloud requirements. Amazon ECS on AWS Fargate is the sweet spot for teams that want AWS-native serverless container operations with zero Kubernetes cluster management: it integrates deeply with ALB, IAM, CloudWatch, and Secrets Manager with minimal cognitive load. I choose Amazon EKS when the enterprise has standardized on Kubernetes tooling (Helm, ArgoCD, Istio service mesh), requires multi-cloud portability, or runs complex stateful workloads requiring granular container scheduling. On EKS, I mandate IAM Roles for Service Accounts (IRSA) to ensure pods use least-privilege IAM credentials without hardcoded secrets.",
        "key_points": ["ECS Fargate for AWS-native serverless simplicity", "EKS for enterprise Kubernetes ecosystem standardization", "Operational overhead comparison", "IRSA for pod-level IAM security"]
    },
    {
        "id": 11,
        "category": "Secrets & Key Management",
        "question": "How do you achieve zero hardcoded secrets and automated credential rotation in a Java Spring Boot application on AWS?",
        "model_answer": "I use AWS Secrets Manager integrated with AWS KMS and the AWS Secrets Manager JDBC library. Database credentials (username, password, endpoint) are stored in Secrets Manager encrypted with a Customer Managed Key (CMK). Secrets Manager has automated rotation enabled, invoking an AWS-managed Lambda function every 30 days that generates a new database password, updates PostgreSQL, and updates the secret. Inside the Spring Boot application, instead of standard HikariCP URL/user/password properties, I use the `aws-secretsmanager-jdbc` driver wrapper. The wrapper fetches the credentials dynamically from Secrets Manager and caches them. When rotation occurs, the driver seamlessly retrieves the updated secret without restarting the JVM or redeploying code.",
        "key_points": ["AWS Secrets Manager with automated 30-day Lambda rotation", "AWS KMS Customer Managed Key encryption", "AWS Secrets Manager JDBC library wrapper", "Zero JVM restart during rotation"]
    },
    {
        "id": 12,
        "category": "Edge & API Acceleration",
        "question": "What is the difference between Amazon CloudFront and AWS Global Accelerator? When would you use each for a Java backend?",
        "model_answer": "Amazon CloudFront is a Content Delivery Network (CDN) operating at Layer 7 (HTTP/HTTPS) that caches static assets and dynamic responses at 450+ Edge Locations worldwide, terminating SSL close to users and providing WAF protection. AWS Global Accelerator operates at Layer 4 (TCP/UDP) and provides two static Anycast IP addresses that route traffic over the private AWS global network directly to the nearest healthy regional endpoint without caching content. I use CloudFront when my Java application serves web frontends, REST APIs, or media files that benefit from edge caching and HTTP/2 acceleration. I choose Global Accelerator for non-HTTP protocols (gaming, VoIP, IoT MQTT), or for HTTP applications that require static white-listed IP addresses for enterprise firewalls and rapid failover between regions under 10 seconds.",
        "key_points": ["CloudFront: Layer 7 HTTP/HTTPS edge caching CDN", "Global Accelerator: Layer 4 Anycast IP routing over AWS fiber", "Use cases: Web/API caching vs Static IP non-HTTP endpoints", "Sub-10 second multi-region failover"]
    },
    {
        "id": 13,
        "category": "Infrastructure as Code",
        "question": "Why should a Java engineering team choose AWS CDK in Java over writing raw CloudFormation YAML or Terraform?",
        "model_answer": "AWS CDK in Java allows software engineers to author infrastructure using the object-oriented language and IDE tools they already master. Raw CloudFormation YAML is verbose, lacks compile-time validation, and prone to copy-paste indentation bugs. With AWS CDK in Java (`software.amazon.awscdk`), developers get compile-time type safety, automated code completion in IntelliJ/Eclipse, and the ability to write unit tests for infrastructure using JUnit. Furthermore, CDK provides high-level 'L2' and 'L3' constructs with built-in security best practices: for example, creating an `ApplicationLoadBalancedFargateService` generates a VPC, ALB, target groups, security groups, and ECS task definitions in 25 lines of Java code.",
        "key_points": ["Type-safe Java object-oriented constructs", "Compile-time validation and JUnit testability", "L2/L3 constructs enforcing security defaults", "Eliminating 1,000+ lines of raw CloudFormation YAML"]
    },
    {
        "id": 14,
        "category": "Observability & Monitoring",
        "question": "How do you trace a slow request across a fleet of 5 distributed Java microservices deployed on AWS?",
        "model_answer": "I use AWS X-Ray combined with the AWS Distro for OpenTelemetry (ADOT). When a client sends a request to Amazon API Gateway or ALB, AWS injects an `X-Amzn-Trace-Id` HTTP header. As the request travels from Service A to Service B, Service C, and Amazon Aurora, the AWS X-Ray SDK for Java intercepts outgoing HTTP and JDBC calls, appending subsegments. In the AWS X-Ray console, this generates an interactive Service Map showing latency and error rates for every hop. If the payment service took 1.8 seconds due to a slow database lock in Aurora, the X-Ray trace displays the exact subsegment and SQL statement responsible, eliminating finger-pointing between microservice teams.",
        "key_points": ["`X-Amzn-Trace-Id` correlation header", "AWS X-Ray / AWS Distro for OpenTelemetry (ADOT)", "Interactive Service Map visualization", "Subsegment level latency breakdown"]
    },
    {
        "id": 15,
        "category": "VPC & Private Connectivity",
        "question": "How do Java applications running in private subnets access Amazon S3 and Amazon DynamoDB without paying for NAT Gateway data transfer?",
        "model_answer": "NAT Gateways charge both an hourly rate and a per-GB data processing fee, which becomes very expensive when microservices transfer terabytes of data to S3 or DynamoDB. The architectural solution is to provision VPC Gateway Endpoints for Amazon S3 and Amazon DynamoDB. Gateway Endpoints are completely free of charge. You configure them in your VPC and attach them to the route tables of your private subnets. Route tables automatically route prefix lists for S3 and DynamoDB directly across the internal AWS network backbone, bypassing the NAT Gateway entirely while keeping traffic off the public internet.",
        "key_points": ["VPC Gateway Endpoints (free for S3 & DynamoDB)", "Eliminating NAT Gateway data processing fees", "Route table prefix list attachment", "Keeping traffic on private AWS backbone"]
    },
    {
        "id": 16,
        "category": "Edge Security & WAF",
        "question": "How do you protect a Spring Boot public REST API against SQL injection and credential stuffing attacks on AWS?",
        "model_answer": "I place AWS WAF (Web Application Firewall) on the Application Load Balancer or Amazon CloudFront distribution. For SQL injection and Cross-Site Scripting, I enable AWS Managed Rules: the Core Rule Set (CRS) and the SQL Database Rule Set, which inspect HTTP bodies and query strings and block malicious payloads at the edge before they reach the JVM. For credential stuffing and brute-force attacks against `/api/auth/login`, I create a Rate-Based Rule configured to block any individual IP address that exceeds 100 requests per 5-minute window with an HTTP 403 Forbidden. I also enable AWS Shield Standard for automatic Layer 3/4 volumetric DDoS mitigation.",
        "key_points": ["AWS WAF on CloudFront / ALB", "AWS Managed Rules (Core Rule Set & SQLi)", "Rate-Based rules on sensitive login endpoints", "AWS Shield for Layer 3/4 DDoS defense"]
    },
    {
        "id": 17,
        "category": "Real-Time Streaming",
        "question": "When would you choose Amazon Kinesis Data Streams over Amazon SQS?",
        "model_answer": "Amazon SQS is designed for decoupled worker processing where individual messages are consumed and deleted by one worker in a queue (pull-and-delete model). Amazon Kinesis Data Streams is designed for real-time streaming data ingestion (such as IoT telemetry, clickstreams, financial ticks) where data is stored in shards and can be read simultaneously by multiple independent application consumers. Furthermore, Kinesis preserves strict shard-level ordering and allows consumers to replay data from up to 365 days in the past. If you need 10 different analytics and ML services to process the exact same event stream in real time, choose Kinesis. If you need task distribution and worker queuing, choose SQS.",
        "key_points": ["SQS: Pull-and-delete task queue for 1 consumer", "Kinesis: Append-only replayable streaming log for multiple consumers", "Shard ordering and historical replayability (up to 365 days)", "Real-time analytics vs job processing"]
    },
    {
        "id": 18,
        "category": "Cloud Migration",
        "question": "Explain the '6 Rs' of cloud migration and how you apply them when modernizing legacy enterprise Java applications.",
        "model_answer": "The 6 Rs framework guides cloud migration strategy: 1. Rehost (Lift-and-Shift to EC2 via AWS Application Migration Service); 2. Replatform (Lift-tinker-and-shift, such as moving Tomcat to Elastic Beanstalk or self-hosted MySQL to Amazon RDS); 3. Repurchase (Moving to SaaS, such as Jira/Salesforce); 4. Refactor/Rearchitect (Modernizing Java monoliths into serverless Lambda SnapStart and containerized ECS microservices); 5. Retain (Keeping legacy on-premise components until depreciation); 6. Retire (Decommissioning obsolete services). As an architect, I often use a phased approach: Replatform to RDS and ECS first to stabilize operations, then Refactor core domain components using the Strangler Fig pattern.",
        "key_points": ["6 Rs: Rehost, Replatform, Repurchase, Refactor, Retain, Retire", "Phased modernization roadmap", "Replatform to RDS/ECS as immediate quick win", "Refactor core domains for long-term cloud agility"]
    },
    {
        "id": 19,
        "category": "Well-Architected Review",
        "question": "How do you prepare for and conduct an AWS Well-Architected Framework review for a production workload?",
        "model_answer": "I use the AWS Well-Architected Tool in the management console, evaluating the workload against the 6 Pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability. Before the review, I gather architecture diagrams, CloudWatch dashboards, and CloudTrail audit logs. During the review, I facilitate structured discussions with developers, security leads, and product owners across key questions: 'How do you encrypt data at rest?', 'How do you withstand component failure?', 'How do you monitor JVM health?'. The tool generates a report identifying High-Risk Issues (HRIs) and Medium-Risk Issues (MRIs) with prescriptive remediation milestones.",
        "key_points": ["The 6 Pillars evaluation", "AWS Well-Architected Tool", "High-Risk Issues (HRIs) identification", "Cross-functional stakeholder collaboration", "Iterative remediation plan"]
    },
    {
        "id": 20,
        "category": "Cost Optimization",
        "question": "A company's AWS cloud bill has grown 300% in 6 months. What is your systematic architectural approach to reducing costs without compromising reliability?",
        "model_answer": "I execute a 4-step cost optimization framework: 1. Immediate Waste Elimination: Delete unattached EBS volumes, release idle Elastic IPs, and delete obsolete EBS snapshots using AWS Trusted Advisor and Cost Explorer. 2. Storage Rightsizing: Enable S3 Intelligent-Tiering across all buckets to automate archival transitions, and upgrade EBS gp2 volumes to gp3 (saving 20% on storage costs while gaining baseline 3000 IOPS). 3. Compute Rightsizing: Analyze AWS Compute Optimizer recommendations to downsize overprovisioned EC2 and ECS instances, and purchase Compute Savings Plans (up to 66% discount) for steady-state workloads. 4. Architecture Modernization: Convert idle dev/test EC2 environments to auto-shutdown schedules and replace idle polling workers with event-driven Lambda functions.",
        "key_points": ["Eliminating unattached EBS volumes and idle Elastic IPs", "Upgrading EBS gp2 to gp3 for immediate 20% savings", "S3 Intelligent-Tiering enablement", "AWS Compute Optimizer & Compute Savings Plans (up to 66% off)", "Automated dev/test off-hours shutdown"]
    }
]


def get_all_interview_questions():
    """Returns the complete list of 20 AWS Solutions Architect scenario questions."""
    return INTERVIEW_QUESTIONS


def get_questions_by_category(category: str):
    """Filters interview questions by category name."""
    return [q for q in INTERVIEW_QUESTIONS if q["category"].lower() == category.lower()]
