# ☁️ AWS Solutions Architect: 35-Day Java Developer Transformation Portal

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask_3.0-lightgrey.svg)](https://palletsprojects.com/p/flask/)
[![AWS](https://img.shields.io/badge/Cloud-Amazon_Web_Services-orange.svg)](https://aws.amazon.com/)
[![AWS Certifications](https://img.shields.io/badge/Certifications-SAA--C03%20%7C%20SAP--C02-yellow.svg)](https://aws.amazon.com/certification/)
[![Deployment](https://img.shields.io/badge/Deployment-Vercel_Serverless_Ready-black.svg)](https://vercel.com)

A production-grade, responsive full-stack web application designed with a proven **pedagogical algorithm** to transform a simple **Java / Spring Boot Enterprise Developer** into an elite, certified **AWS Solutions Architect (SAA-C03 / SAP-C02)** in **35 days**. 

The portal features full training videos for core services inside AWS curated directly from official **Amazon Web Services (AWS)** YouTube channels, hands-on architectural labs, an interactive AWS CLI Workbench simulator, 4 enterprise portfolio projects with ASCII architecture diagrams, and a complete interview scenario defense studio.

---

## 📑 Table of Contents
1. [⚡ How to Run (Local & Vercel Serverless)](#-how-to-run-local--vercel-serverless)
2. [🧠 The Pedagogical Algorithm: Java to AWS Architecture](#-the-pedagogical-algorithm-java-to-aws-architecture)
3. [🔐 Security Architecture & Access Control Gate](#-security-architecture--access-control-gate)
4. [📅 35-Day Curriculum with Official AWS YouTube Masterclasses](#-35-day-curriculum-with-official-aws-youtube-masterclasses)
5. [🏛️ The 10 Core AWS Architecture Domains](#️-the-10-core-aws-architecture-domains)
6. [🏗️ 4 Enterprise Portfolio Projects (With Architecture Blueprints)](#️-4-enterprise-portfolio-projects-with-architecture-blueprints)
7. [💻 Interactive AWS Architecture & CLI Workbench](#-interactive-aws-architecture--cli-workbench)
8. [🎙️ Interview Studio & Positioning Pack](#️-interview-studio--positioning-pack)
9. [🎓 Campus & Institutional Outreach (Native XLSX Parser)](#-campus--institutional-outreach-native-xlsx-parser)
10. [📂 Project Directory Structure](#-project-directory-structure)

---

## ⚡ How to Run (Local & Vercel Serverless)

### Option A: Run Locally (Zero Config)
Run directly with standard Python 3 from the root directory:

```bash
python app.py
```

Then open your browser at:
👉 **[http://localhost:5000](http://localhost:5000)**

*(No batch files, no Docker daemon, and no Node.js/npm build steps required! Everything runs on pure Python with Flask and SQLite).*

To run the automated verification test suite:
```bash
python test_verification.py
```

---

### Option B: Deploy Instantly to Vercel (Serverless Ready)

The application includes native Vercel serverless support (`api/index.py` entrypoint and `vercel.json` configuration):

1. **Deploy via Git**:
   Push this directory to GitHub, GitLab, or Bitbucket:
   ```bash
   git init
   git add .
   git commit -m "Deploy AWS Solutions Architect Transformation Portal"
   git branch -M master
   git remote add origin <your-repo-url>
   git push -u origin master
   ```
2. **Deploy on Vercel**:
   - Log into [vercel.com](https://vercel.com) and click **"Add New Project"**.
   - Import your repository.
   - Leave build settings as default (Framework Preset: **Other**, Root Directory: `./`).
   - Click **Deploy**. Vercel will install `requirements.txt` and serve your serverless application globally in under 60 seconds.

> **Serverless Persistence Architecture**: The application automatically detects Vercel (`VERCEL=1`), directs SQLite database operations to the writable `/tmp/learning_portal.db` directory, and syncs progress via client-side `localStorage` to preserve checklist states across serverless cold starts.

---

## 🧠 The Pedagogical Algorithm: Java to AWS Architecture

The greatest obstacle Java developers face when stepping into cloud architecture is treating cloud services as abstract black boxes. This curriculum bridges familiar JVM, memory, connection pooling, and multi-threading primitives directly to high-availability AWS cloud counterparts:

```
+------------------------------------+          +----------------------------------------------+
|     TRADITIONAL JAVA BACKEND       |  =====>  |          AWS ARCHITECTURAL PRIMITIVE         |
+------------------------------------+          +----------------------------------------------+
| Localhost Tomcat / Spring Boot JAR |  =====>  | EC2 Graviton3 + ALB + Multi-AZ Auto-Scaling  |
| HikariCP Connection Pool Exhaustion|  =====>  | Amazon RDS Proxy + Aurora Read Replicas      |
| JPA / Hibernate Relational Joins   |  =====>  | Amazon DynamoDB Single-Table Design (PK/SK)  |
| 3-6s JVM Lambda Cold Starts        |  =====>  | AWS Lambda SnapStart (Firecracker CRaC)      |
| Synchronous HTTP REST Chains       |  =====>  | EventBridge + SQS FIFO + Step Functions Saga |
| Local application.properties Keys  |  =====>  | AWS Secrets Manager + KMS Envelope Encryption|
| Logback Appender to Local Disk     |  =====>  | CloudWatch Logs Insights + AWS X-Ray Tracing |
| Manual Shell Scripts / YAML        |  =====>  | AWS Cloud Development Kit (CDK) in Java      |
+------------------------------------+          +----------------------------------------------+
```

### Why Java Depth Makes Superior Cloud Architects:
- **Connection Multiplication Awareness**: An architect from an IT background might scale ECS tasks from 10 to 100 instances during flash sales without realizing each Spring Boot instance's HikariCP pool will attempt to open 2,000 database connections, crashing PostgreSQL. A Java-grounded architect immediately introduces **Amazon RDS Proxy** for connection multiplexing.
- **MicroVM Snapshotting (CRaC)**: By understanding classloading and JVM initialization, the architect leverages **AWS Lambda SnapStart**, eliminating cold starts by taking encrypted Firecracker memory snapshots restored in under 100ms.
- **Eliminating Cascading Failures**: By understanding thread starvation in blocking I/O, the architect decouples microservices asynchronously using **Amazon SQS FIFO** and **Amazon EventBridge**.

---

## 🔐 Security Architecture & Access Control Gate

The portal implements enterprise security controls:

```
                                  [ Incoming Web Request ]
                                             |
                         +-------------------+-------------------+
                         |                                       |
                 Request is for "/"?                   Request outside "/"?
                         |                                       |
                       [YES]                                   [NO]
                         |                                       |
             +-----------------------+              +-------------------------+
             | Display Home Page     |              | Is Session Unlocked?    |
             | (Freely Accessible)   |              +------------+------------+
             +-----------------------+                           |
                                                    +------------+------------+
                                                    |                         |
                                                  [YES]                      [NO]
                                                    |                         |
                                       +-----------------------+   +----------------------+
                                       | Display Requested     |   | Flash Admin Password |
                                       | Course / Project Page |   | Modal & Redirection  |
                                       +-----------------------+   +----------------------+
```

### 1. Mandatory Public Home Restriction
- Only the **Home Page (`/`)** is freely displayed.
- Navigating to any other route (`/courses`, `/roadmap`, `/topics`, `/projects`, `/aws-workbench`, `/interview-studio`, `/notes`) redirects to `/?unlock=1` and flashes the **Admin Security Password Modal** with an attention-grabbing pulse animation.

### 2. Admin Security Password
- **Encrypted & Hashed Storage**: The master admin password is never stored or disclosed in plaintext in the codebase or documentation. It is stored as an encrypted cryptographic vault ciphertext and verified via salted PBKDF2-HMAC-SHA256 constant-time comparison (with optional runtime `ADMIN_PASSWORD` environment variable override).
- **Zero Hints & Zero Placeholders**: The password input field displays strictly masked bullets (`••••••••••••`). No plaintext hints, placeholders, or clues are visible on the website.
- **Anti-Brute-Force Rate Limiting**: 5 consecutive failed attempts immediately locks out the client IP for 60 seconds, returning HTTP `429 Too Many Requests`.
- **Automatic Access Email Generation**: When the correct password is submitted, full access is granted, and the system automatically generates a formatted sample email text for the user to send to **`anooppriyaranjan@gmail.com`** requesting full registered candidate access.

### 3. Invisible Authorization Link for Senders
- If a candidate does not know the admin password, they can switch to the *"Don't Know Password?"* tab and submit their email address.
- The system generates a sample email addressed to **`anooppriyaranjan@gmail.com`**.
- The authorization approval link is **completely invisible to the sender** in the email draft to prevent unauthorized self-approval.
- The request is recorded in the password-protected **Admin Inbox (`/access/inbox`)**.
- When `anooppriyaranjan@gmail.com` clicks the approval link (`/access/allow/<token>`) in their inbox, full portal access is granted to that valid email ID.

---

## 📅 35-Day Curriculum with Official AWS YouTube Masterclasses

Every day features official video embeds from **Amazon Web Services (AWS)**, **AWS Events (re:Invent)**, **AWS Developers**, and **AWS Online Tech Talks**, accompanied by official AWS documentation links and the **Java Developer to AWS Architectural Bridge**:

| Phase | Days | Curriculum Phase | Primary AWS Services Covered | Official AWS Video ID |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | **Day 1** | Cloud Foundations & Global Infrastructure | Regions, AZs, Edge Locations, Points of Presence | `PAr1DY82ymE` |
| | **Day 2** | IAM Architecture & Zero Trust Security | IAM Roles, Policies, SCPs, Permission Boundaries | `YQsK4MtsELU` |
| | **Day 3** | Resilient Compute & Amazon EC2 Deep Dive | Nitro System, Graviton3, Spot Instances, Placement Groups | `2uc1vaEsPXU` |
| | **Day 4** | Security Groups, Network ACLs & EC2 Hardening | Stateful SGs vs Stateless NACLs, Layered VPC Security | `Ya4WFO9P0i8` |
| | **Day 5** | Elastic Load Balancing (ALB, NLB, GLB) | Weighted Target Groups, Path Routing, TLS Offloading | `6iO6wtDOKGM` |
| | **Day 6** | Auto Scaling Groups & Dynamic Scaling | Predictive Scaling, Target Tracking, Graceful Drain | `nlGyIa3UQYU` |
| | **Day 7** | Elastic Beanstalk & Cloud Deployment Automation | Spring Boot JAR Deployment, Blue/Green Deployments | `Ozc5Yu_IcaI` |
| **Phase 2** | **Day 8** | Amazon S3 Architecture & Storage Classes | S3 Standard, Intelligent-Tiering, Glacier Deep Archive | `NXehLy7IiPM` |
| | **Day 9** | S3 Security, Encryption & Lifecycle Management | SSE-KMS, S3 Object Lock (WORM), BlockPublicAccess | `WZGG8RkvApY` |
| | **Day 10** | High-Performance Block & File Storage | EBS gp3/io2 Block Express, EFS Multi-AZ Mounting | `m03ICK5ZsA0` |
| | **Day 11** | Amazon VPC Architecture & Subnet CIDR Design | Public/Private Subnets, Internet Gateways, NAT Gateways | `7qaSfmnFiI0` |
| | **Day 12** | Transit Gateway, VPC Peering & PrivateLink | Hub-and-Spoke VPC, Interface VPC Endpoints | `9Nikqn_02Oc` |
| | **Day 13** | Route 53 Global DNS & Traffic Routing | Latency Routing, Geolocation, Route 53 Health Checks | `mczl5zhQcYQ` |
| | **Day 14** | Amazon CloudFront CDN & Edge Acceleration | Edge Caching, Origin Shield, Lambda@Edge, CloudFront Functions | `lLnKaPqL3u0` |
| **Phase 3** | **Day 15** | Relational Database Scalability: Amazon RDS | Multi-AZ Failover, Read Replicas, Storage Autoscaling | `TJxC-B9Q9tQ` |
| | **Day 16** | Enterprise Database Modernization: Amazon Aurora | Aurora Global Database, Aurora Serverless v2, Storage Engine | `kVVdHezNTpw` |
| | **Day 17** | Connection Multiplexing: Amazon RDS Proxy | Solving HikariCP Connection Exhaustion, Instant Failover | `VFsGJIeuR_Y` |
| | **Day 18** | Amazon DynamoDB Single-Table Design | Partition Keys, Sort Keys, GSIs, Sub-10ms Queries | `xfxBhvGpoa0` |
| | **Day 19** | Containerization on AWS: Amazon ECS Fargate | Serverless Docker Containers, Task Definitions, ALB Target Groups | `l5otnYulOt8` |
| | **Day 20** | Enterprise Kubernetes: Amazon EKS Architecture | Managed Node Groups, Karpenter Autoscaling, IRSA | `cipDJwDWWbY` |
| | **Day 21** | Serverless Java: AWS Lambda & SnapStart | Firecracker microVM Memory Snapshotting (CRaC), Sub-100ms Cold Starts | `ZbnAithBNYY` |
| **Phase 4** | **Day 22** | API Management: Amazon API Gateway | REST & HTTP APIs, Cognito Authorizers, Request Throttling | `GvyyJQ5m7x0` |
| | **Day 23** | Message Queues: Amazon SQS FIFO & Dead-Letter Queues | Decoupling Workflows, FIFO Message Deduplication, DLQ Redrive | `8zysQqxgj0I` |
| | **Day 24** | Publish/Subscribe Fan-Out: Amazon SNS | Event Fan-out to Queues & Lambdas, Message Filtering | `GWa2N3xe73M` |
| | **Day 25** | Event-Driven Architectures: Amazon EventBridge | Custom Event Buses, Schema Registry, Content Filtering | `dy7UXS7ur14` |
| | **Day 26** | Distributed Workflow Orchestration: AWS Step Functions | Saga Pattern, Distributed Transactions, Automated Rollbacks | `lDEbFPKGozA` |
| | **Day 27** | Real-Time Streaming: Amazon Kinesis Data Streams | Sharded Streams, Kinesis Consumer Application, Data Ingestion | `HjoQllOWRmM` |
| | **Day 28** | In-Memory Caching: Amazon ElastiCache Redis | Cache-Aside, Write-Through, Redis Cluster High Availability | `_YYBdsuUq2M` |
| **Phase 5** | **Day 29** | Encryption & Key Management: AWS KMS & CloudHSM | Envelope Encryption, Customer Managed Keys (CMKs), Key Rotation | `9vr3oMODIUE` |
| | **Day 30** | Perimeter Protection: AWS WAF & AWS Shield | OWASP CRS Rules, Rate-Limiting, DDoS Mitigation | `E_xm8W_BEFk` |
| | **Day 31** | Observability: CloudWatch Logs Insights & AWS X-Ray | Distributed Microservice Tracing, Metric Filters, Alarms | `qXLsx4r37_0` |
| | **Day 32** | Infrastructure as Code: AWS CDK in Java | CloudFormation Synthesizer, TypeScript to Java CDK, L2/L3 Constructs | `Wzawix9bMAE` |
| | **Day 33** | High Availability & Multi-Region Disaster Recovery | Active-Active vs Pilot Light, RPO / RTO Tradeoffs | `PnWTWjmbNp0` |
| | **Day 34** | Well-Architected Framework: The 6 Pillars | Operational Excellence, Security, Reliability, Performance, Cost, Sustainability | `nOKvA8HykW8` |
| | **Day 35** | AWS Certified Solutions Architect Associate (SAA-C03) Capstone | Complete Exam Blueprint, Full Scenario Reviews & System Design Pitch | `c3Cn4xYfxJY` |

---

## 🏛️ The 10 Core AWS Architecture Domains

The portal breaks down AWS architecture into 10 fundamental mastery subjects:

1. **IAM & Zero-Trust Cloud Foundations**: IAM roles, policies, STS assume role, permission boundaries, AWS Organizations SCPs.
2. **Resilient Compute & Auto-Scaling**: Multi-AZ EC2 Graviton3 clusters, ALB path routing, dynamic target tracking auto-scaling.
3. **High-Performance Storage & Lifecycle**: S3 Intelligent-Tiering, SSE-KMS encryption, S3 Object Lock (WORM), EBS gp3/io2, EFS Multi-AZ.
4. **Enterprise VPC Networking & Hybrid Connectivity**: CIDR subnetting, NAT Gateways, Transit Gateways, Interface VPC Endpoints (PrivateLink), Route 53.
5. **Relational Databases & High Concurrency**: Amazon RDS Multi-AZ, Aurora Global Databases, and RDS Proxy connection multiplexing.
6. **NoSQL Database Architecture**: Amazon DynamoDB single-table design with composite keys (`PK`/`SK`) and global secondary indexes.
7. **Container Platforms & Kubernetes**: Amazon ECS Fargate serverless containers, Amazon EKS with Karpenter autoscaling and IAM Roles for Service Accounts (IRSA).
8. **Serverless Java & Fast In-Memory Caching**: AWS Lambda SnapStart with Firecracker memory snapshotting (CRaC) and Amazon ElastiCache Redis cluster caching.
9. **Asynchronous Decoupling & Event-Driven Systems**: Amazon EventBridge event buses, Amazon SQS FIFO deduplication, and AWS Step Functions Saga distributed orchestration.
10. **Enterprise Security, KMS, Observability & AWS CDK**: AWS Secrets Manager, KMS envelope encryption, AWS WAF, CloudWatch Insights, AWS X-Ray tracing, and AWS CDK in Java.

---

## 🏗️ 4 Enterprise Portfolio Projects (With Architecture Blueprints)

Each project provides comprehensive problem statements, solutions, tech stacks, ASCII blueprints, quantified impact metrics, and resume defense bullets:

### Project 1: Spring Boot Monolith to Event-Driven Serverless Microservices Migration
- **Architectural Pattern**: Martin Fowler's Strangler Fig Pattern + API Gateway + Java 21 Lambda SnapStart + EventBridge + DynamoDB.
- **ASCII Blueprint**:
```
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
```
- **Impact**: Reduced p99 latency from 2,800ms to 92ms; reduced infrastructure cost by 58%.

---

### Project 2: Multi-Region High-Availability Banking Core on AWS
- **Architectural Pattern**: Route 53 DNS Latency & Failover + ECS Fargate + Amazon Aurora Global Database + RDS Proxy + AWS KMS.
- **ASCII Blueprint**:
```
+---------------------------------------------------------------------------------------------------+
|                                 GLOBAL CLIENT ACCESS LAYER (DNS & CDN)                            |
|                                                                                                   |
|                            Amazon Route 53 (Latency & Health Failover Routing)                    |
|                                    /                                  \                           |
|       (Primary: us-east-1)        /                                    \   (Secondary DR: eu-west-1)
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
|  |  | - Storage replicated to 6 nodes       |  |Replic|  | - Replication latency < 1 second  |  |  |
|  |  | - KMS Envelope Encryption             |  |ation |  | - Can be promoted in < 1 minute  |  |  |
|  |  +---------------------------------------+  |      |  +----------------------------------+  |  |
|  +---------------------------------------------+      +----------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
```
- **Impact**: RTO < 60 seconds, RPO < 1 second; zero database connection exhaustion during failovers.

---

### Project 3: Event-Driven Order Processing with Step Functions Saga Orchestration
- **Architectural Pattern**: SQS FIFO + Step Functions Saga Coordinator + Compensating Rollback Transactions + ElastiCache Redis.
- **ASCII Blueprint**:
```
+---------------------------------------------------------------------------------------------------+
|                                 DISTRIBUTED SAGA TRANSACTION PIPELINE                             |
|                                                                                                   |
|  [ API Gateway ]  -->  [ Amazon SQS FIFO Queue ]  -->  [ AWS Step Functions (Saga Coordinator) ]  |
|                                                                   |                               |
|       +------------------------------------+----------------------+--------------------+          |
|       |                                    |                                           |          |
|       v (Step 1)                           v (Step 2)                                  v (Step 3) |
|  +--------------------------+     +--------------------------+     +--------------------------+   |
|  | Reserve Inventory Lambda |     | Process Payment Lambda   |     | Dispatch Shipment Lambda |   |
|  | - Atomically decrements  |     | - Invokes Stripe API     |     | - Notifies 3PL Logistics |   |
|  |   stock in ElastiCache   |     | - Handles 3D Secure      |     | - SQS Dispatch Message   |   |
|  +------------+-------------+     +------------+-------------+     +------------+-------------+   |
|               |                                |                                |                 |
|               v (On Inventory Failure)         v (On Payment Failure)           v (On Success)    |
|  +--------------------------+     +--------------------------+     +--------------------------+   |
|  | Cancel Order & Alert Cust|     | COMPENSATING TRANSACTION |     | Order Complete (HTTP 200)|   |
|  |                          |     | Release Reserved Stock   |     | DynamoDB Status: SHIPPED |   |
|  +--------------------------+     +--------------------------+     +--------------------------+   |
+---------------------------------------------------------------------------------------------------+
```
- **Impact**: 100% elimination of orphaned inventory holds; zero partial order inconsistencies across distributed microservices.

---

### Project 4: Enterprise Kubernetes Container Platform with AWS CDK in Java
- **Architectural Pattern**: AWS CDK in pure Java (`software.amazon.awscdk`) + Amazon EKS + Karpenter Autoscaler + IRSA + RDS Proxy.
- **ASCII Blueprint**:
```
+---------------------------------------------------------------------------------------------------+
|                            AWS CDK IN JAVA INFRASTRUCTURE DEFINITION                              |
|                         (package com.enterprise.infrastructure.cdk)                               |
|                                                                                                   |
|  +---------------------------------------------------------------------------------------------+  |
|  |                  EnterprisePlatformApp (AWS CDK Java App / CloudFormation)                  |  |
|  |    Stack 1: NetworkStack (VPC, 3 Public Subnets, 3 Private Subnets, Isolated DB Subnets)    |  |
|  |    Stack 2: DatabaseStack (Aurora Serverless v2 PostgreSQL + RDS Proxy + Secrets Manager)   |  |
|  |    Stack 3: EksClusterStack (Amazon EKS 1.29 + Karpenter Autoscaler + Bottlerocket OS)      |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 | (Synthesizes CloudFormation & Deploys)          |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  |                       Amazon EKS Multi-AZ Cluster (Production VPC)                           |  |
|  |                                                                                             |  |
|  |  +---------------------------------------------------------------------------------------+  |  |
|  |  |                   Karpenter Autoscaler (Sub-Minute JIT EC2 Provisioning)              |  |  |
|  |  |   - Mix of Graviton3 (c7g.xlarge) on-demand and spot compute instances                |  |  |
|  |  +---------------------------------------------------------------------------------------+  |  |
|  |                                                                                             |  |
|  |  +---------------------------+  +---------------------------+  +-------------------------+  |  |
|  |  | Pod: Account-Service      |  | Pod: Order-Service        |  | Pod: Payment-Service    |  |  |
|  |  | - Java 21 / Spring Boot 3 |  | - Java 21 / Spring Boot 3 |  | - Java 21 / Spring Boot |  |  |
|  |  | - IRSA: Read S3 Bucket    |  | - IRSA: Write EventBridge |  | - IRSA: Call Secrets Mgr|  |  |
|  |  +-------------+-------------+  +-------------+-------------+  +------------+------------+  |  |
|  +----------------|------------------------------|-----------------------------|---------------+  |
|                   |                              |                             |                  |
|                   v                              v                             v                  |
|  +---------------------------------------------------------------------------------------------+  |
|  |                Amazon RDS Proxy (Shared Database Connection Multiplexing Pool)              |  |
|  +----------------------------------------------+----------------------------------------------+  |
|                                                 | (Multiplexed Database Connections)              |
|                                                 v                                                 |
|  +---------------------------------------------------------------------------------------------+  |
|  |                  Amazon Aurora Serverless v2 PostgreSQL (Multi-AZ Cluster)                  |  |
|  +---------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------+
```
- **Impact**: 100% elimination of static credentials using IRSA; reduced cluster compute costs by 42% via Graviton3 and Karpenter rightsizing.

---

## 💻 Interactive AWS Architecture & CLI Workbench

Accessible at `/aws-workbench`:
- **Scenario `aws-1`**: *Audit Multi-AZ Auto-Scaling Group & Target Health* (`aws autoscaling describe-auto-scaling-groups`).
- **Scenario `aws-2`**: *Audit S3 Enterprise Encryption & Public Access Blocks* (`aws s3api get-public-access-block && aws s3api get-bucket-encryption`).
- **Scenario `aws-3`**: *DynamoDB Single-Table Partition & Range Key Query* (`aws dynamodb query --table-name ECommercePlatform`).
- **Scenario `aws-4`**: *Step Functions Saga Distributed Transaction Simulation* (`aws stepfunctions start-execution`).

Executes live against the simulated AWS Cloud Engine via `/api/workbench/simulate`, rendering structured tabular results.

---

## 🎙️ Interview Studio & Positioning Pack

Accessible at `/interview-studio`:
- **Verbatim 60-Second Elevator Pitch**:
  > *"I bring a powerful dual background as an enterprise software engineer rooted in Java microservices and a certified AWS Solutions Architect—giving me a grounded perspective on building cloud systems that actually scale. Because I understand the JVM, memory management, connection pooling, and multi-threading, I architect AWS solutions that prevent production bottlenecks like database connection pool exhaustion or severe serverless cold starts before they reach production..."*
- **20 Deep AWS Solutions Architect Scenario Questions**:
  1. *How does your software engineering background in Java help you succeed as an AWS Solutions Architect?*
  2. *A Java microservice fleet running on ECS auto-scales from 10 to 100 instances during flash sales and immediately crashes the PostgreSQL database with 'Too many connections'. How do you architect a solution?*
  3. *Our leadership wants to migrate our customer-facing REST APIs to AWS Lambda, but the team is concerned about multi-second JVM cold starts. How do you solve this as an architect?*
  4. *How would you architect a distributed transaction across three independent microservices (Order, Payment, Inventory) on AWS without two-phase commit (2PC)?*
  5. *How do you model a relational One-to-Many and Many-to-Many relationship in Amazon DynamoDB using single-table design?*
  ... and 15 more covering Multi-Region DR, S3 Lifecycle, VPC Peering, Transit Gateway, AWS KMS Envelope Encryption, and AWS CDK in Java.

---

## 🎓 Campus & Institutional Outreach (Native XLSX Parser)

Accessible at `/institutional-outreach`:
- **Zero-Dependency Native Stream Parser**: Built using Python's standard `zipfile` and `xml.etree.ElementTree` to parse `.xlsx` spreadsheets and `.csv` files directly in memory without requiring external CLI utilities or bloated runtime dependencies.
- **Cold Email Pitch Generator**: Instantly drafts campus training proposals addressed to college deans and corporate training heads.

---

## 📂 Project Directory Structure

```
c:\Games\Interview\FDE\
├── app.py                      # Main Flask application, routes, and security layer
├── learning_portal.db          # SQLite database for progress tracking and notes
├── requirements.txt            # Python dependencies (Flask, openpyxl, etc.)
├── test_verification.py        # Automated verification test suite (100% PASS)
├── vercel.json                 # Vercel serverless deployment configuration
├── api/
│   └── index.py                # Serverless WSGI entrypoint for Vercel
├── data/
│   ├── aws_masterclass.py      # Masterclass course metadata, 10-min briefing & pillars
│   ├── aws_workbench.py        # AWS CLI simulation queries & mock cloud engine data
│   ├── roadmap.py              # 35-Day curriculum with official AWS YouTube video IDs
│   ├── topics.py               # 10 Core AWS Architecture Domains with documentation links
│   ├── projects.py             # 4 Enterprise portfolio projects with ASCII blueprints
│   ├── interview_prep.py       # Elevator pitch, positioning strategy & 20 scenario Q&As
│   ├── access_control.py       # Password verification, encrypted tokens & approval flow
│   ├── google_auth.py          # Google SSO & admin verification engine
│   └── outreach.py             # Native XLSX/CSV stream parser & pitch email generator
├── templates/
│   ├── base.html               # Master layout, navigation, and Admin Password modal
│   ├── index.html              # Executive dashboard, AWS masterclass player & pillars
│   ├── courses.html            # Day-by-Day course hub with Java-to-AWS bridge callout
│   ├── day_detail.html         # Daily study guide (Morning AWS Docs, Afternoon Lab, Defense)
│   ├── roadmap.html            # 35-Day roadmap with phase filters and note persistence
│   ├── topics_list.html        # 10 Core AWS Architecture Domains with status dropdowns
│   ├── topic_detail.html       # Domain deep-dive with official video embeds & labs
│   ├── kql_lab.html            # Interactive AWS Architecture & CLI Workbench simulator
│   ├── projects.html           # 4 Enterprise portfolio blueprints with ASCII diagrams
│   ├── interview.html          # 20 Scenario questions & 60s elevator pitch studio
│   ├── notes.html              # Personal engineering journal & lab notes
│   ├── access_gate.html        # Access request modal
│   ├── access_inbox.html       # Password-protected admin inbox for anooppriyaranjan@gmail.com
│   └── access_allow.html       # One-click email approval confirmation screen
├── static/
│   ├── css/custom.css          # Clean styling, white-background card layout
│   └── js/main.js              # AJAX toggles, simulation runner, copy-to-clipboard
└── README.md                   # This comprehensive documentation file
```

---

## 🧪 Verification & Quality Assurance

To execute the automated end-to-end verification suite:

```bash
python test_verification.py
```

Expected output:
```
PASS: Native XLSX parsing verified.
Verifying 35 roadmap days have official AWS videos and Java bridges...
PASS: All 35 days have verified official AWS video IDs, instructors, and Java bridges.
Verifying 10 topics have valid official AWS YouTube embeds...
PASS: All 10 topics have verified AWS video embeds and official instructors.
PASS: Home AWS masterclass and 10-min briefing videos verified.
PASS: AWS Workbench simulation executes and returns realistic architectural data.
PASS: Home page is freely accessible and displays.
PASS: Navigating outside Home page redirects to /?unlock=1.
PASS: Incorrect password rejected with 401.
PASS: Anti-brute-force rate limiting and security cooldown verified (429 Too Many Requests).
PASS: Correct admin password unlocks portal AND creates sample email text for anooppriyaranjan@gmail.com requesting full access.
PASS: Rest of the web application now displays successfully.
PASS: Portal re-locked back to Home-only display.
PASS: Sample email text generated with invisible link for sender.
PASS: Approval correctly verified as pending before link is clicked.
PASS: Admin inbox is password protected with masked placeholder and no hints.
PASS: Admin inbox unlocked; received email request and approval link visible to anooppriyaranjan@gmail.com.
PASS: Clicking approval link in anooppriyaranjan@gmail.com inbox successfully grants access.
PASS: User of approved email now has full access to the rest of the web application.
PASS: Direct email check confirms approval from anooppriyaranjan@gmail.com.

ALL AWS SOLUTIONS ARCHITECT VERIFICATION TESTS PASSED SUCCESSFULLY! 🚀
```

---

## 📄 License
This application is created for cloud architects, enterprise software engineers, and hiring managers. All video masterclasses are the property of **Amazon Web Services (AWS)** and their respective official YouTube channels.
