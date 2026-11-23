"""
Projects module: Contains comprehensive blueprints, ASCII architecture diagrams,
and step-by-step implementation guides for the 4 enterprise portfolio projects that
prove hands-on AWS Solutions Architect competence to hiring managers and CTOs.
Specifically crafted for transforming a Java developer into an enterprise cloud architect.
"""

PROJECTS = [
    {
        "id": "project-1",
        "title": "Project 1: Spring Boot Monolith to Event-Driven Serverless Microservices Migration",
        "subtitle": "Strangler Fig Pattern + API Gateway + Lambda SnapStart + EventBridge + DynamoDB",
        "category": "Cloud Migration & Serverless Architecture",
        "badge": "Core Portfolio 1",
        "summary": "Deconstruct a monolithic Java Spring Boot application using the Strangler Fig pattern. Route live customer traffic through Amazon API Gateway, extract domain services into sub-100ms Java Lambda functions with SnapStart, store high-velocity transactions in Amazon DynamoDB single-table design, and decouple downstream services using Amazon EventBridge.",
        "architecture_diagram": """
+---------------------------------------------------------------------------------------------------+
|                                       AWS CLOUD ARCHITECTURE                                      |
|                                                                                                   |
|  [ Client Web / Mobile ]                                                                          |
|             |                                                                                     |
|             v (HTTPS / TLS 1.3)                                                                   |
|  +---------------------------------------------------------------------------------------------+  |
|  |                            Amazon CloudFront (Edge Caching & WAF)                           |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 |                                                 |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  |                   Amazon API Gateway (HTTP API / Strangler Fig Routing)                     |  |
|  |   - Path /api/v1/legacy/*  --------->  Legacy Spring Boot Monolith on Amazon EC2 / ALB       |  |
|  |   - Path /api/v2/orders/*  --------->  Modern Serverless Java Lambda (SnapStart enabled)     |  |
|  +----------------------+-----------------------------------------------+----------------------+  |
|                         |                                               |                         |
|                         v (Migrated Route)                              v (Legacy Fallback)       |
|  +----------------------------------------------+      +---------------------------------------+  |
|  |    AWS Lambda (Java 21 + SnapStart / CRaC)   |      |  Legacy Java Monolith on EC2 / ALB   |  |
|  |  - Execution Time: 80ms                     |      |  - Single-Node MySQL Database         |  |
|  |  - Zero Cold Starts                          |      +---------------------------------------+  |
|  +----------------------+-----------------------+                                                 |
|                         |                                                                         |
|                         +---------------------------+                                             |
|                         | (Write Transaction)       | (Emit Domain Event)                         |
|                         v                           v                                             |
|  +------------------------------------+   +----------------------------------------------------+  |
|  |   Amazon DynamoDB (Single-Table)   |   |        Amazon EventBridge (Custom Event Bus)       |  |
|  |  - PK: CUSTOMER#<id>               |   |  - Rule: source = 'ecommerce.orders'               |  |
|  |  - SK: ORDER#<timestamp>           |   +-------+-------------------+--------------------+---+  |
|  |  - Single-Digit Millisecond Access |           |                   |                    |      |
|  +------------------------------------+           v                   v                    v      |
|                                           [ Billing Lambda ]   [ Inventory Queue ]  [ Email SNS ] |
+---------------------------------------------------------------------------------------------------+
""",
        "problem_statement": "The enterprise operated a 10-year-old monolithic Java Spring Boot application deployed on static EC2 instances with a shared MySQL database. The monolith suffered from deployment bottlenecks (a bug in reporting delayed checkout releases), slow cold starts, and database connection exhaustion during seasonal traffic spikes.",
        "solution_architecture": "Applied Martin Fowler's Strangler Fig pattern. Placed Amazon API Gateway in front of the existing system. Incrementally carved out the highest-velocity service (Order Processing) into an event-driven serverless architecture using Java 21 Lambda functions with SnapStart, Amazon DynamoDB for millisecond storage, and Amazon EventBridge for asynchronous pub/sub decoupling.",
        "technologies_used": [
            "AWS Lambda (Java 21 + SnapStart CRaC)",
            "Amazon API Gateway (HTTP APIs)",
            "Amazon DynamoDB (Single-Table Design)",
            "Amazon EventBridge (Custom Event Bus)",
            "Amazon CloudFront & AWS WAF",
            "AWS Secrets Manager & IAM Roles"
        ],
        "key_metrics": {
            "p99_latency": "Reduced from 2,800ms to 92ms",
            "cloud_cost": "Reduced infrastructure spend by 58%",
            "deployment_frequency": "Increased from bi-weekly to daily autonomous releases"
        },
        "resume_bullets": [
            "Architected and executed Strangler Fig cloud modernization for a legacy Spring Boot monolith, extracting core order processing into serverless Java Lambda microservices with AWS Lambda SnapStart, slashing p99 latency from 2.8s to 92ms.",
            "Modeled e-commerce domain entities into an Amazon DynamoDB single-table architecture, eliminating relational join bottlenecks and supporting 25,000+ peak writes/second with zero downtime.",
            "Decoupled order fulfillment and billing workflows using Amazon EventBridge custom event buses and Amazon SQS, eliminating cascading HTTP microservice failures."
        ]
    },
    {
        "id": "project-2",
        "title": "Project 2: Multi-Region High-Availability Banking Core on AWS",
        "subtitle": "Amazon Route 53 + ALB + ECS Fargate + Amazon Aurora Global Database + AWS KMS",
        "category": "Enterprise High Availability & Disaster Recovery",
        "badge": "Core Portfolio 2",
        "summary": "Architect a multi-region active-passive resilient core banking platform designed to withstand total AWS regional failures. Features Route 53 health failover, containerized Java banking microservices on Amazon ECS Fargate across multiple Availability Zones, Amazon Aurora Global Database with sub-second replication, and envelope encryption via AWS KMS.",
        "architecture_diagram": """
+---------------------------------------------------------------------------------------------------+
|                                 GLOBAL CLIENT ACCESS LAYER (DNS & CDN)                            |
|                                                                                                   |
|                            Amazon Route 53 (Latency & Health Failover Routing)                    |
|                                    /                                  \\                           |
|       (Primary: us-east-1)        /                                    \\   (Secondary DR: eu-west-1)
|                                  v                                      v                         |
|  +---------------------------------------------+      +----------------------------------------+  |
|  |           PRIMARY REGION (us-east-1)        |      |          SECONDARY DR (eu-west-1)      |  |
|  |                                             |      |                                        |  |
|  |  +---------------------------------------+  |      |  +----------------------------------+  |  |
|  |  | Application Load Balancer (Public SG) |  |      |  | Application Load Balancer        |  |  |
|  |  +-------------------+-------------------+  |      |  +----------------+-----------------+  |  |
|  |                      |                      |      |                   |                    |  |
|  |                      v                      |      |                   v                    |  |
|  |  +---------------------------------------+  |      |  +----------------------------------+  |  |
|  |  | Amazon ECS Fargate (Private Subnets)  |  |      |  | Amazon ECS Fargate (Warm Standby)|  |  |
|  |  | - Spring Boot Banking Microservices   |  |      |  | - Scaled to minimum capacity     |  |  |
|  |  | - Running across 3 Availability Zones |  |      |  | - Auto-scales upon DR activation |  |  |
|  |  +-------------------+-------------------+  |      |  +----------------+-----------------+  |  |
|  |                      |                      |      |                   |                    |  |
|  |                      v                      |      |                   v                    |  |
|  |  +---------------------------------------+  |      |  +----------------------------------+  |  |
|  |  | Amazon RDS Proxy (Connection Pool)   |  |      |  | Amazon RDS Proxy (Connection Pool)|  |  |
|  |  +-------------------+-------------------+  |      |  +----------------+-----------------+  |  |
|  |                      |                      |      |                   |                    |  |
|  |                      v                      |      |                   v                    |  |
|  |  +---------------------------------------+  |      |  +----------------------------------+  |  |
|  |  | Amazon Aurora PostgreSQL (Writer)     |  |=====>|  | Amazon Aurora Global DB (Reader) |  |  |
|  |  | - Encrypted with AWS KMS              |  | (1s) |  | - Read Replica across continents |  |  |
|  |  | - Multi-AZ Synchronous Standby        |  |      |  | - Promoted to Writer upon DR fail|  |  |
|  |  +---------------------------------------+  |      |  +----------------------------------+  |  |
|  +---------------------------------------------+      +----------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
""",
        "problem_statement": "A financial services institution required 99.99% availability for their transaction gateway. Regulatory mandates required Recovery Time Objective (RTO) under 60 seconds and Recovery Point Objective (RPO) under 1 second in the event of an entire data center or regional power grid catastrophe.",
        "solution_architecture": "Designed a multi-region Warm Standby architecture. Containerized Spring Boot banking services using Amazon ECS on AWS Fargate spanning 3 Availability Zones. Implemented Amazon Aurora Global Database with dedicated storage-level cross-region replication under 1 second. Configured Amazon Route 53 automated health checks to trigger zero-touch DNS failover.",
        "technologies_used": [
            "Amazon Aurora Global Database (PostgreSQL)",
            "Amazon ECS on AWS Fargate",
            "Amazon Route 53 (Failover & Latency Routing)",
            "Amazon RDS Proxy",
            "AWS Key Management Service (KMS Envelope Encryption)",
            "AWS Secrets Manager with Automated Rotation"
        ],
        "key_metrics": {
            "rpo": "Sub-second (RPO < 1s via Aurora storage engine)",
            "rto": "Under 45 seconds automated failover",
            "availability": "Achieved 99.99% multi-region uptime"
        },
        "resume_bullets": [
            "Designed and implemented an active-passive multi-region disaster recovery platform on AWS for enterprise banking microservices, achieving an RTO under 45 seconds and an RPO under 1 second.",
            "Engineered Amazon Aurora Global Database cross-region replication and deployed Amazon RDS Proxy, eliminating connection pooling exhaustion during regional failover drills.",
            "Automated infrastructure deployment and multi-region failover testing using AWS CloudFormation and Route 53 DNS health checking."
        ]
    },
    {
        "id": "project-3",
        "title": "Project 3: Real-Time Asynchronous E-Commerce Order Processing Pipeline",
        "subtitle": "Amazon SNS Fan-Out + SQS FIFO + AWS Step Functions Saga Pattern + ElastiCache Redis",
        "category": "Event-Driven Systems & Distributed Transactions",
        "badge": "Core Portfolio 3",
        "summary": "Build a high-throughput, fault-tolerant distributed order processing pipeline capable of handling 50,000+ orders per minute. Uses Amazon SNS for message fan-out, Amazon SQS FIFO for deduplication, AWS Step Functions for the Saga pattern (compensating transactions), and Amazon ElastiCache for sub-millisecond inventory caching.",
        "architecture_diagram": """
+---------------------------------------------------------------------------------------------------+
|                                  ORDER INGESTION & FAN-OUT PIPELINE                               |
|                                                                                                   |
|  [ Checkout API (Spring Boot on ECS) ]                                                            |
|                    |                                                                              |
|                    v (Publish OrderPlaced Event)                                                  |
|  +----------------------------------------------------+                                           |
|  |           Amazon SNS Topic (OrderPlaced)           |                                           |
|  +-----+--------------------+--------------------+----+                                           |
|        |                    |                    |                                                |
|        v (Fan-Out)          v (Fan-Out)          v (Fan-Out)                                      |
|  +-------------+      +-------------+      +-------------+                                        |
|  | SQS Queue   |      | SQS Queue   |      | SQS FIFO    |                                        |
|  | (Analytics) |      | (Email/SMS) |      | (Payment)   |                                        |
|  +-------------+      +-------------+      +------+------+                                        |
|                                                   |                                               |
|                                                   v                                               |
|  +---------------------------------------------------------------------------------------------+  |
|  |                 AWS Step Functions State Machine (Saga Pattern Coordinator)                 |  |
|  |                                                                                             |  |
|  |  +--------------------------+                                                               |  |
|  |  | Step 1: Check Inventory  |----(Success)----+                                             |  |
|  |  | (Amazon ElastiCache Redis|                 |                                             |  |
|  |  +--------------------------+                 v                                             |  |
|  |                                      +--------------------------+                           |  |
|  |                                      | Step 2: Authorize Card   |----(Success)----+         |  |
|  |                                      | (Payment Gateway)        |                 |         |  |
|  |                                      +------------+-------------+                 v         |  |
|  |                                                   | (Fail)              +-----------------+ |  |
|  |                                                   v                     | Step 3: Dispatch| |  |
|  |                                      +--------------------------+       | (Warehouse SQS) | |  |
|  |                                      | Compensate: Release Stock|       +-----------------+ |  |
|  |                                      | in ElastiCache Redis     |                           |  |
|  |                                      +--------------------------+                           |  |
|  +---------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
""",
        "problem_statement": "During high-traffic holiday sales events, the client's synchronous microservice architecture experienced distributed deadlocks and data inconsistency: when a payment failed midway, inventory had already been decremented without an automated rollback, causing thousands of angry customer support tickets.",
        "solution_architecture": "Re-architected the order checkout into an asynchronous, event-driven pipeline. Used Amazon SNS fan-out to deliver events simultaneously to analytics and notifications. Coordinated multi-service distributed transactions with an AWS Step Functions Saga State Machine that automatically triggers compensating transactions to restore inventory in ElastiCache Redis upon payment rejection.",
        "technologies_used": [
            "Amazon SNS (Pub/Sub Fan-Out)",
            "Amazon SQS (FIFO Queues & Dead Letter Queues)",
            "AWS Step Functions (Saga Pattern)",
            "Amazon ElastiCache for Redis",
            "AWS Lambda (Java 21)",
            "Amazon CloudWatch & AWS X-Ray"
        ],
        "key_metrics": {
            "throughput": "Processed 65,000 orders/minute peak without dropping a single event",
            "data_consistency": "100% automated compensation consistency with zero orphaned stock locks",
            "checkout_response": "Dropped from 4.2 seconds to 110ms asynchronous confirmation"
        },
        "resume_bullets": [
            "Architected a scalable event-driven order processing pipeline utilizing Amazon SNS, SQS FIFO, and AWS Step Functions, sustaining 65,000+ orders/minute peak with guaranteed exactly-once processing.",
            "Implemented the Saga Pattern with Step Functions state machines to orchestrate distributed transactions across microservices, eliminating inconsistent data states via automated compensating rollbacks.",
            "Integrated Amazon ElastiCache for Redis as an in-memory inventory reservation cache, reducing database read contention by 82%."
        ]
    },
    {
        "id": "project-4",
        "title": "Project 4: Enterprise Java Container Platform on Amazon EKS with AWS CDK",
        "subtitle": "Amazon EKS + IAM Roles for Service Accounts (IRSA) + AWS CDK in Java + Secrets Manager",
        "category": "Kubernetes & Infrastructure as Code",
        "badge": "Core Portfolio 4",
        "summary": "Build a production-ready, enterprise Kubernetes microservice platform on Amazon EKS entirely defined in type-safe Java code using AWS CDK. Features IAM Roles for Service Accounts (IRSA) for zero-trust pod security, Amazon RDS Proxy for HikariCP connection pooling, AWS Secrets Manager automated credential sync, and Karpenter autoscaling.",
        "architecture_diagram": """
+---------------------------------------------------------------------------------------------------+
|                            AWS CDK IN JAVA (INFRASTRUCTURE AS CODE)                               |
|                                                                                                   |
|  [ MyEksStack.java (software.amazon.awscdk) ]                                                     |
|                         |                                                                         |
|                         v (cdk synth -> cdk deploy)                                               |
|  +---------------------------------------------------------------------------------------------+  |
|  |                                    AMAZON EKS CLUSTER                                       |  |
|  |                                                                                             |  |
|  |  +---------------------------------------------------------------------------------------+  |  |
|  |  | Managed Node Groups (AWS Graviton3 / ARM64) + Karpenter Just-In-Time Autoscaler      |  |  |
|  |  |                                                                                       |  |  |
|  |  |  +-------------------------+                     +---------------------------------+  |  |  |
|  |  |  | Java Pod: Account Service|                     | Java Pod: Payment Service       |  |  |  |
|  |  |  | - ServiceAccount: acct-sa|                     | - ServiceAccount: pay-sa        |  |  |  |
|  |  |  +------------+------------+                     +----------------+----------------+  |  |  |
|  |  +---------------|---------------------------------------------------|-------------------+  |  |
|  +------------------|---------------------------------------------------|----------------------+  |
|                     | (OIDC Web Identity Federation)                    |                         |
|                     v                                                   v                         |
|  +--------------------------------------+             +----------------------------------------+  |
|  |  IAM Role: AccountServiceRole        |             |   IAM Role: PaymentServiceRole         |  |
|  |  - Policy: S3 ReadOnly on Statements |             |   - Policy: KMS Decrypt & Stripe Key   |  |
|  +--------------------------------------+             +----------------------------------------+  |
|                     |                                                   |                         |
|                     +---------------------------+-----------------------+                         |
|                                                 |                                                 |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  |                Amazon RDS Proxy (Shared Database Connection Multiplexer)                    |  |
|  |                - Authenticates via AWS Secrets Manager with Zero-Hardcoded Passwords       |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 |                                                 |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  |                       Amazon Aurora PostgreSQL (Multi-AZ Enterprise)                        |  |
|  +---------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
""",
        "problem_statement": "The enterprise engineering team struggled with brittle, unvalidated Kubernetes YAML manifests and insecure container deployments where AWS access keys were mounted as plaintext environment variables inside Pods. Relational database connections frequently crashed during Kubernetes horizontal pod autoscaling (HPA) events.",
        "solution_architecture": "Replaced raw YAML with a type-safe AWS CDK application written in pure Java (`software.amazon.awscdk`). Implemented Amazon EKS with IAM Roles for Service Accounts (IRSA), eliminating all static credentials inside containers. Integrated Amazon RDS Proxy to shield Amazon Aurora from connection spikes during Karpenter node autoscaling.",
        "technologies_used": [
            "Amazon EKS (Kubernetes 1.29+)",
            "AWS CDK in Java (software.amazon.awscdk)",
            "IAM Roles for Service Accounts (IRSA)",
            "Amazon RDS Proxy & Aurora PostgreSQL",
            "Karpenter Just-In-Time Kubernetes Autoscaler",
            "AWS Secrets Manager"
        ],
        "key_metrics": {
            "security_compliance": "100% elimination of static credentials; CIS Kubernetes Benchmark compliant",
            "provisioning_speed": "Entire multi-AZ cluster and 12 microservices provisioned in 8 minutes",
            "cluster_cost": "Reduced cluster compute bill by 42% via Graviton3 and Karpenter rightsizing"
        },
        "resume_bullets": [
            "Authored and deployed a production-grade Amazon EKS container infrastructure entirely in pure Java using AWS CDK, managing multi-AZ VPCs, Karpenter autoscaling, and Aurora databases.",
            "Enforced Zero Trust pod security by implementing IAM Roles for Service Accounts (IRSA) across 20+ Spring Boot microservices, eliminating all hardcoded AWS credentials.",
            "Integrated Amazon RDS Proxy between EKS pods and Amazon Aurora PostgreSQL, safely accommodating 10x microservice pod scaling events without database connection exhaustion."
        ]
    }
]


for p in PROJECTS:
    if "technologies_used" in p and "tech_stack" not in p:
        p["tech_stack"] = p["technologies_used"]


def get_project_by_id(project_id: str):
    """Fetches a project dictionary by its string id (e.g. 'project-1')."""
    for p in PROJECTS:
        if p["id"] == project_id:
            return p
    return None


def get_all_projects():
    """Returns all 4 enterprise portfolio projects."""
    return PROJECTS
