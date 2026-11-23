import urllib.request
import json
import re

candidates = [
    ("Day 1 (Global Infra)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf9SvuYrpQWhO-NGk6fLIpvrAhRiUHrDJoeqAjY_EDMzuwitVBepXDPRC3KDcoJ6yQlqwu6LPGgDrLrsOdPi0pJE0iV2pdvCHPvBgsdDviTmNBT1jZ9qpDPFLnfk_m4GN6"),
    ("Day 3 (EC2 Nitro)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt257F_UNMNZ3ChWEynSq5Q8b5sQbe0cI6OEtiOLa369LwEpDDJCCbkrhQcOElfWtBr7-K8xo1wp2d3R1hQS2iz_VuO8pAV52RazByxpnt-jTQoR6qRgyWVMpagX98JNA="),
    ("Day 4 (Security Groups)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH47D_i5gvXijl9nSk2w7QFgYHSwv8FVkfZ3aab2RPweLYsMZ4UMn5y3HtynZdhC7gjXB5t2cBTbdAuFkdLylBWwcWQuBSLo-K6q_8ZQDG9RKWHUa_Msx6vOwB6RmInyQyh"),
    ("Day 6 (Auto Scaling)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGptyh3jOJvYDJMyJogl0LrUb8j0osYeGIoSIdzy8cjeIBAZO6neImDpOWQUm6qh-Q3qeIfyUhU90IvSdn4oGwuN05SQFesCMwALf0FuEW1GEWwT0jgcxuB5raeLPcpqSM="),
    ("Day 7 (Elastic Beanstalk)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnvbbMAwqKxn5RO9M9ziBo9vek89MDOrfMtGjBQTg6IQeg6Fups6TQhRrK7B3fEsX_v93BPLvLBkTXh50QJtVxJ_LzcfWIx36aIqY4Ffjxi8SGZsDniYTF-3BNcdzqDt-j"),
    ("Day 9 (S3 Security)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBCyVeANLsIbwE81tJ_fuJhsR_CMTdAlqVCigv6KZhS8zUIlmElXLdLmFJWxRkyqFtBA1r3ke7Rpdqu8ByTE3B5B-Y-oCxB6JOvDNrE3dNe6Fwn4yzlVY9vlRMC_iDLSAq"),
    ("Day 10 (EFS)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYw_pOmUshbcZJb4da6V0YCuk7D8YSQggkhpczBJCtuIaHmisTYtG2rVa_Ytv8_cII4nIzJ1WUnj1kiGB4eIfMQeC5zumpvRZD2ryREo918bIuPkjE7XKf8NA1tpQCRhd2"),
    ("Day 12 (Transit Gateway)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8XYQPp88H3GpVIkJ5Pg4dyxEvP2tgF-TDDwhTT9S2mLvki8x4MWkrm7tVBlvLfc9gFExjq3_FkYfopXzy7mufgaaNGX7k8jugFw8wZpaFjsdxUiQoH7gXjJHgWxPv-bxh"),
    ("Day 13 (Route 53)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7HdJqqTkPV0-ElKaCt21VtPLUyzIzrvP4vsUcY-axdS-goNxBrv306jSHF-DPRIV48iTL5PJzS6U4rNSsWkT0O8xjlyyoDKb9i9RzHPeTeC7q-32Qf6LxT_uyfS0P7IUj"),
    ("Day 14 (CloudFront)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs9M88DevfhJ_41H1BEKhWVg5e9US_FhnDa1uBqLjoMNhgrhro-bmc6DVVoH-_jnYPO9IkXvOPaqtmdxyO5Dor0h3dUYgBB25h6Q3veLfndgPon0Ix2S6IyAAKgXIz3pwV"),
    ("Day 15 (RDS)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsDw5gRQq1dKKF6rFkH09xYAxq_zlPYAwVqONJTXy2v6pnp-vpprKqd9WzGWIGkeEYM8hUodM2skFrECkMIQpDEw6vcChifAsnD0JHEvvqQGKRcQNyC9Bujyi7RBaNDF_P"),
    ("Day 17 (RDS Proxy)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpR42seUIU1uFDkdcytHmjMjsgLbh50KwqHY6nl6fjYOMA2Yq95u38iji-msQg55L2or3l7ESadysuitxvInwjyDZTzFroLNOXVNEAz0mX633LQ487Hm5Ppkcu6k6R2Ncz"),
    ("Day 20 (EKS)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHqHNLEMPngQw381qypN7QqJqXSL2QdAfcvwDAgdmLpBq_J4-Vjv3IkPCPCbMPAXUA_luaQpPWDIfiZHE_Jhle4bBn1iie_A5W1Bur1F7wa_1ChShj24kEsJ7p5yIU5g1a"),
    ("Day 22 (API Gateway)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy5Qnb8nfurAaZ1_lnoI-UkRLlasopX9TtdNjDPMF62H-kBYp6gZyCqOTSodHk09Vp1iULXzNlORsgV74TiUE1Nxl4MNZi3K85xu8oxU78pAOtKz5pCxW2DuL34D2KTeXM"),
    ("Day 23 (SQS)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGL0LLNSnYqXG5mntF3qTUlYvrGw_pKo3kRIzYVvgXb3L5RZDCfBqNsPL83CSPTgsZ20mJZHoC6rv5sdiEhLBhTF2UBhtGJbLXAn2p8jB-Zfc8gCJ1i1qqhSsU8uhf5RtX"),
    ("Day 24 (SNS)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3xlUEPpLlky6ZtoVYQun0CUK4kRzjjT8aIZkH15nSQCDjPyEfhzv5Io_ktDGDbLkuTrSudTtw9jRxCGCTVclNtK_vlQpez-VqD9bfcnXgYU54RX0zOMX_7BMVHV2_33QO"),
    ("Day 26 (Step Functions)", "https://www.youtube.com/watch?v=lDEbFPKGozA"),
    ("Day 27 (Kinesis)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZoPDEqkzu5Avy9zO19geOAxtAEXolzO4tn15YJdvkQ1bwgwcbwo-Ec0YJfk9DUl8mvguNtjAVHvedsQ60GC0mqzp13-G5p3RXznbldCEPDYNauUfcqPEC3Mdgx2unlo-"),
    ("Day 28 (ElastiCache)", "https://www.youtube.com/watch?v=_YYBdsuUq2M"),
    ("Day 29 (KMS)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH07WfGzj0sDUyeGfaB69KyzvooW81ERgccRfnaImfZNvj5diF3wZGEy-4PUE3T2_ZwPjDJ7u8k94pFGPqqJRnQ2F8NrkH5kgRLzVlxptLGUoA1QLRfBGeBXZBmQWmcETai"),
    ("Day 30 (WAF)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh9j4-rcZNVbcfBLJbfieoY9YJDvYKZYSX9xLIDPiIKraVVxaBS3LGEGgXBL3EMc5IG5v3c9IFBgJhThTcIrogjM3wyuVRHWoxsZnH3y-gOXCaQ1FB3_tfjbMX4dX2aXe5"),
    ("Day 31 (Observability)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBsneW5A0ldYAvM_qICkGSDh1dfyRJUA-vm_0L4e9BrWTuJHozSlbkk00aVLItMA4VL2dV9LVK1vhsfT-n0SGSBj8HPOsbSF6hlMedJd_tFoz1Eje-wA7uFwR3P16Ms4h8"),
    ("Day 32 (CDK)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUAX33J8-pT4yVZjQ4Vk5Wahx46r-PyC3T-6wmaREi-JXUWLlsZH_N3FruyNCgi3YSyrgljz7M5Jm1dG53zo8KSVTcMVEiY3Lhu-BKtIYIZonQTTSbai-FkJ5_RfAamCKs"),
    ("Day 33 (Disaster Recovery)", "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG01nyWAVwQ9Ify-3IwC4sROydlU6VKnjqRxjYVRfENRLyZ8Dqga_OHBZ4NWzsd5kRhNyTj0EnQ5c9uVkQHT7e7717mSk1RXFNwOcTuJCaAm-ABDqV_0HL44xj-9Tom2NZr")
]

results = {}
for label, u in candidates:
    try:
        dest = u
        if "grounding-api-redirect" in u:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=5)
            dest = res.geturl()
        m = re.search(r'[?&]v=([^&]+)', dest)
        if m:
            vid = m.group(1)
            o_req = urllib.request.Request(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json", headers={'User-Agent': 'Mozilla/5.0'})
            o_res = urllib.request.urlopen(o_req, timeout=5)
            data = json.loads(o_res.read())
            print(f"[{label}] OK vid={vid} | Title: {data.get('title')} | Author: {data.get('author_name')}")
            results[label] = {
                "vid": vid,
                "title": data.get('title'),
                "author": data.get('author_name')
            }
        else:
            print(f"[{label}] NO VID in {dest}")
    except Exception as e:
        print(f"[{label}] ERR: {e}")

with open('scratch/resolved_days.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Saved resolved_days.json")
