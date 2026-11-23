import urllib.request
import json
import re

candidates = [
    # Topic 2: ELB
    ("Topic 2 (ELB NET401)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpCQV3vKEDqIDCE6hjAgGNJXqPA1hY6EBrsvpGSUBxWzooogYXKydSK5ePfoX9x7XhN-cWyfIkcJ1MtCdNTBlZewldSvAbLLecjsILQkYzOFrVQKKXwOukXXAiJ4v7pMZk"),
    ("Topic 2 (ELB NET318)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR7iaXJuwLpOisg7-JnQKAO3LQu0ghbDRpB_LDVR3R4BwVnlzKwlCoTZkRrWqcCZjihYNMazMBuwOdBGXxqVlNV3exfkyRe0Y3zK8vFhWb0-IEbBdgRaT4aEs3Vpj-Vdx0"),
    # Topic 3: VPC
    ("Topic 3 (VPC NET301)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyvbQgvJQaoPmN0BkNut-RaGp9tfJLuHNT2Hz2Nn4txj6GKMujuVN2LMk_acn50CrPGNz_ZCcrBzHorY-RSwFjotF0EEgTFLa0zCah3nmpzDuGfw6crcs2EJaxZzy9VFD0"),
    ("Topic 3 (VPC NET306)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7BFzbIA1Aiae4CDsHGvFv0hDk2WTPM5EihVYw0noUfns-cSyWmzHn_fAIxDYzFoKuROFNA703sQf3HsS3s5n_vEA8V2XZrRTRBgAc2Zr-192SzV9WDCEfCq_k4ji6h8iS"),
    # Topic 4: S3
    ("Topic 4 (S3 STG302)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyZyp7DMZpUShd-6iUfg5hmFfso6kfyqni_ae4HCzmO1RMAxjc2kUlvZEvd6KW9WEl1iJG7NcqlPRwg2bEPpZ8F8dFHk9hMDYN4wFZW1eO18NTh-sXpspozBthMf8jVT11"),
    ("Topic 4 (S3 STG314)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjvko0obnzbgvIwxCtXiO6y4086i5bAUerk72c_yZhP4-VBP5cIg_A1-LN9HtHXaf7XJNANGBIi9-H3B2vEAAI1js7hpaAnqdPps8cHV-rJZ-7i3t4D4rz_B-zcSAN5vSd"),
    # Topic 5: Aurora / RDS
    ("Topic 5 (Aurora DAT405)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjUXiR--qiT9dg9IJtod0h2l_5qp0HvcDMZskc9Q4g_lddOxhp7MMn_MmcT0gDmiarvPYGtcQv_W9voEk_uEF5XDQedScjkx9yRhk7i1qvA30PEixLvOG4WiGiIu1Og8B7"),
    ("Topic 5 (Aurora DAT408)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrk_06V1N-iDugAPZHS8bSmSKkGnGyBSpM6pObtSRIjipjMSQ2BmY2rRzbA4a0rocQULqqLSGmDF42Awc0RaThRMgcm500pcQdhUqIvJeSun-UtZuQLDO4P2_Aj9eTq_Rl"),
    # Topic 6: DynamoDB
    ("Topic 6 (DynamoDB Rick Houlihan)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG45Gf0p9ZfYyCSyPLBMbrAFTQVTk7Q8WDvj4FNPZtlg2tOp5IvaCZjSUUyqLiPR8d680QeR4q5jpL16hAfrIu340qslopX3aD_z2aDsT0w88KfCjt4XVuR0tJP4vMlrHHZ"),
    # Topic 7: ECS / Fargate
    ("Topic 7 (ECS SVS409)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF78o_OZA-0Lex6VaST_2TgpQZLduRHsP_6GWXcLip4N0F898_fhSoV-frXOww2SQsWqkdmYWpRsugHThW6gKPuvcIwQ4SzkIP1mxJDtPyN7Jnpp9oYNqfh7-3U_oBNAaY="),
    # Topic 8: Lambda SnapStart
    ("Topic 8 (SnapStart SVS320)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEq2pXFCshK7a0f1xMT_oDUnC_zdzJHYQYvtOFgGuHLSkmNGfdzod5X1GLmJ15T2uReKANyA6oxu-3vHFsI6D1pbhAAgpIwr7BI95HhNwgugMG8ysdmYiIOwVrcwbt-YP0="),
    # Topic 9: Event-Driven EventBridge
    ("Topic 9 (EDA API307)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBTxlJ_h7xr8NUEhcOiPRdEF56Iyx7kT9b1jEfCFl6LYXPK-oCj7pYI761SpTrE7s_4QvSy4lyeNhfL_ldAEaF07jiA5w4UjxI4H3khBCbq0k0OqjCsLjdOaRLSDJQ0sE1"),
    ("Topic 9 (EDA COM301)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaF5caprFOpn8RabOKWJpzYIBlOQePT7585b1zq5OF_sJ94l-Mpqy0mAfzTz0VRvNZVRxBcKfrzCQ5WD6jUsqSMlCI4defZnPQKFXfi8SAGpu-je4GzwXOCvAFGL68XoR0"),
    # Topic 10: Well-Architected Framework
    ("Topic 10 (Well-Architected ARC210)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYK0CT8fkKScIpfn-Bp_V0a8QVHIkG1k5JGjHXPZmUt4tnEUppgymjFuGm-YanI_IcBaQnBiOzAcgb1M4GHKCSN3kjl-5a0EtGO-rsEh-Bq92PVIN5CpIHcEOqXSJN_Lx4")
]

for label, u in candidates:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        dest = res.geturl()
        m = re.search(r'[?&]v=([^&]+)', dest)
        if m:
            vid = m.group(1)
            o_req = urllib.request.Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json", headers={'User-Agent': 'Mozilla/5.0'})
            o_res = urllib.request.urlopen(o_req, timeout=5)
            data = json.loads(o_res.read())
            print(f"[{label}] vid={vid} | Title: {data.get('title')} | Author: {data.get('author_name')}")
        else:
            print(f"[{label}] no video id in {dest}")
    except Exception as e:
        print(f"[{label}] ERR: {e}")
