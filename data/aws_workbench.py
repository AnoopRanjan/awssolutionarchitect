"""
AWS Architecture, CLI & CloudFormation Workbench Simulator module.
Provides realistic interactive architectural simulations for AWS Solutions Architects:
- AWS CLI queries (EC2, S3, RDS, IAM)
- CloudFormation / CDK Java template generators
- IAM Policy evaluation
- DynamoDB Single-Table queries
- Step Functions Saga execution simulation
"""

AWS_WORKBENCH_QUERIES = [
    {
        "id": "aws-1",
        "title": "AWS CLI: Audit Multi-AZ Auto-Scaling Group & Target Health",
        "category": "Compute & High Availability",
        "command": "aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names prod-java-asg --query 'AutoScalingGroups[].{Instances:Instances[].{Id:InstanceId,AZ:AvailabilityZone,State:LifecycleState,Health:HealthStatus}}'",
        "description": "Inspects whether Spring Boot compute instances are evenly balanced across us-east-1a, us-east-1b, and us-east-1c with healthy status.",
        "expected_columns": ["InstanceId", "AvailabilityZone", "LifecycleState", "HealthStatus", "TargetGroupStatus"],
        "mock_rows": [
            {"InstanceId": "i-09a8b7c6d5e4f3a21", "AvailabilityZone": "us-east-1a", "LifecycleState": "InService", "HealthStatus": "Healthy", "TargetGroupStatus": "healthy (HTTP 200 /actuator/health)"},
            {"InstanceId": "i-01b2c3d4e5f6a7b82", "AvailabilityZone": "us-east-1b", "LifecycleState": "InService", "HealthStatus": "Healthy", "TargetGroupStatus": "healthy (HTTP 200 /actuator/health)"},
            {"InstanceId": "i-07c8d9e0f1a2b3c43", "AvailabilityZone": "us-east-1c", "LifecycleState": "InService", "HealthStatus": "Healthy", "TargetGroupStatus": "healthy (HTTP 200 /actuator/health)"}
        ]
    },
    {
        "id": "aws-2",
        "title": "AWS CLI: Audit S3 Enterprise Encryption & Public Access Blocks",
        "category": "Storage & Data Protection",
        "command": "aws s3api get-public-access-block --bucket enterprise-finance-vault-2026 && aws s3api get-bucket-encryption --bucket enterprise-finance-vault-2026",
        "description": "Audits compliance to verify that BlockPublicAccess is 100% active and SSE-KMS Customer Managed Key encryption is enforced.",
        "expected_columns": ["BucketName", "BlockPublicAcls", "IgnorePublicAcls", "BlockPublicPolicy", "RestrictPublicBuckets", "SSEAlgorithm", "KMSMasterKeyId"],
        "mock_rows": [
            {
                "BucketName": "enterprise-finance-vault-2026",
                "BlockPublicAcls": "true",
                "IgnorePublicAcls": "true",
                "BlockPublicPolicy": "true",
                "RestrictPublicBuckets": "true",
                "SSEAlgorithm": "aws:kms",
                "KMSMasterKeyId": "arn:aws:kms:us-east-1:123456789012:key/b8d7a6c5-4e3f-2a1b-0c9d-8e7f6a5b4c3d"
            }
        ]
    },
    {
        "id": "aws-3",
        "title": "DynamoDB: Single-Table Partition & Range Key Query",
        "category": "NoSQL Database",
        "command": "aws dynamodb query --table-name ECommercePlatform --key-condition-expression 'PK = :pk and begins_with(SK, :sk)' --expression-attribute-values '{\":pk\":{\"S\":\"CUSTOMER#1001\"},\":sk\":{\"S\":\"ORDER#2026\"}}'",
        "description": "Simulates single-digit millisecond query fetching customer order history without scanning or full-table joins.",
        "expected_columns": ["PK", "SK", "OrderDate", "TotalAmount", "OrderStatus", "ItemCount", "LatencyMs"],
        "mock_rows": [
            {"PK": "CUSTOMER#1001", "SK": "ORDER#2026-11-20T10:15:00Z", "OrderDate": "2026-11-20", "TotalAmount": "$249.99", "OrderStatus": "CONFIRMED", "ItemCount": 3, "LatencyMs": "4.2ms"},
            {"PK": "CUSTOMER#1001", "SK": "ORDER#2026-11-22T14:30:00Z", "OrderDate": "2026-11-22", "TotalAmount": "$1,120.00", "OrderStatus": "SHIPPED", "ItemCount": 5, "LatencyMs": "3.8ms"}
        ]
    },
    {
        "id": "aws-4",
        "title": "AWS Step Functions: Saga Distributed Transaction Simulation",
        "category": "Event-Driven & Microservices",
        "command": "aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:OrderSagaCoordinator --input '{\"orderId\":\"ORD-8821\",\"amount\":450.00}'",
        "description": "Executes multi-step Saga distributed transaction: reserves inventory, charges card, handles automated rollbacks.",
        "expected_columns": ["ExecutionArn", "Status", "Step1_Inventory", "Step2_Payment", "Step3_Fulfillment", "CompensatingAction"],
        "mock_rows": [
            {
                "ExecutionArn": "arn:aws:states:us-east-1:123456789012:execution:OrderSagaCoordinator:exec-9921",
                "Status": "SUCCEEDED",
                "Step1_Inventory": "Reserved in ElastiCache Redis (12ms)",
                "Step2_Payment": "Authorized via Stripe Gateway (180ms)",
                "Step3_Fulfillment": "Dispatched to Shipping SQS FIFO (15ms)",
                "CompensatingAction": "None (Clean Forward Transaction)"
            }
        ]
    }
]


def get_workbench_query_by_id(query_id: str):
    """Finds a workbench simulation query by id."""
    for q in AWS_WORKBENCH_QUERIES:
        if q["id"] == query_id:
            return q
    return None


def get_all_workbench_queries():
    """Returns all simulation queries."""
    return AWS_WORKBENCH_QUERIES
