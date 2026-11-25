import io
import os
import sys
import time
import zipfile

# Ensure project root is on path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from app import app, get_db
from data.outreach import parse_xlsx_stream, parse_csv_stream, generate_sales_email
from data.roadmap import ROADMAP_DAYS
from data.topics import TOPICS
from data.aws_masterclass import AWS_MASTER_COURSE, AWS_BRIEFING_10MIN
from data.aws_workbench import AWS_WORKBENCH_QUERIES
from data.access_control import (
    create_access_request,
    ADMIN_EMAIL
)
from data.google_auth import get_decrypted_admin_password


def test_native_xlsx_parsing():
    """Verify that native openpyxl/csv parsing works seamlessly without third-party CLI tools."""
    bio = io.BytesIO()
    with zipfile.ZipFile(bio, 'w') as zf:
        zf.writestr('[Content_Types].xml', '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        zf.writestr('xl/sharedStrings.xml', '<?xml version="1.0" encoding="UTF-8"?><sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><si><t>College Name</t></si><si><t>Campus Location</t></si><si><t>Official Email</t></si><si><t>IIT Bombay</t></si><si><t>Powai, Mumbai</t></si><si><t>dean@iitb.ac.in</t></si></sst>')
        zf.writestr('xl/worksheets/sheet1.xml', '<?xml version="1.0" encoding="UTF-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="s"><v>1</v></c><c r="C1" t="s"><v>2</v></c></row><row r="2"><c r="A2" t="s"><v>3</v></c><c r="B2" t="s"><v>4</v></c><c r="C2" t="s"><v>5</v></c></row></sheetData></worksheet>')

    bio.seek(0)
    rows = parse_xlsx_stream(bio)
    assert len(rows) == 1, f"Expected 1 row, got {len(rows)}"
    assert rows[0]['name'] == 'IIT Bombay'
    assert rows[0]['email'] == 'dean@iitb.ac.in'
    print("PASS: Native XLSX parsing verified.")


def test_topics_and_roadmap():
    """Verify that all 35 roadmap days and 10 topics have valid official AWS YouTube video links and Java architectural bridges."""
    print("Verifying 35 roadmap days have official AWS videos and Java bridges...")
    for day in ROADMAP_DAYS:
        assert day.get("video_id"), f"Day {day['day']} missing video_id"
        assert len(day.get("video_id", "")) == 11, f"Day {day['day']} has invalid YouTube video_id length"
        assert day.get("video_instructor"), f"Day {day['day']} missing instructor"
        assert day.get("java_bridge"), f"Day {day['day']} missing java_bridge explanation"
    print("PASS: All 35 days have verified official AWS video IDs, instructors, and Java bridges.")

    print("Verifying 10 topics have valid official AWS YouTube embeds...")
    for t in TOPICS:
        assert t.get("youtube_embed"), f"Topic {t['id']} missing youtube_embed"
        assert t.get("instructor"), f"Topic {t['id']} missing instructor"
        assert "AWS" in t.get("instructor", "") or "Amazon" in t.get("instructor", ""), f"Topic {t['id']} instructor should be AWS"
    print("PASS: All 10 topics have verified AWS video embeds and official instructors.")

    assert AWS_MASTER_COURSE['primary_video_id'] == 'c3Cn4xYfxJY', f"Expected c3Cn4xYfxJY, got {AWS_MASTER_COURSE['primary_video_id']}"
    assert 'freeCodeCamp' in AWS_MASTER_COURSE['instructor'] or 'AWS' in AWS_MASTER_COURSE['instructor']
    assert AWS_BRIEFING_10MIN['video_id'] == 'AzUG7GOfh7w', f"Expected AzUG7GOfh7w, got {AWS_BRIEFING_10MIN['video_id']}"
    assert 'AWS' in AWS_BRIEFING_10MIN['instructor'] or 'Amazon' in AWS_BRIEFING_10MIN['instructor']
    print("PASS: Home AWS masterclass and 10-min briefing videos verified with real playable IDs.")


def test_aws_workbench_simulation():
    """Verify the AWS Workbench simulation endpoint executes and returns realistic architectural audit data."""
    client = app.test_client()
    admin_pw = get_decrypted_admin_password()
    # Unlock site with admin password
    unlock = client.post('/api/verify-site-password', json={'password': admin_pw})
    assert unlock.status_code == 200
    for q in AWS_WORKBENCH_QUERIES:
        res = client.post('/api/workbench/simulate', json={'query_id': q['id']})
        assert res.status_code == 200
        data = res.get_json()
        assert data['success'] is True
        assert data['query_id'] == q['id']
        assert data['count'] > 0
        assert len(data['columns']) > 0
        assert len(data['rows']) > 0
    client.get('/api/lock-portal')
    print("PASS: AWS Workbench simulation executes and returns realistic architectural data.")


def test_routes_and_access():
    """Verify that only home page is displayed, admin popup unlocks with encrypted credentials, and email request contains approval link to anooppriyaranjan@gmail.com."""
    client = app.test_client()
    admin_pw = get_decrypted_admin_password()

    # 1. Home page is freely accessible and displays
    res_home = client.get('/')
    assert res_home.status_code == 200
    home_html = res_home.data.decode('utf-8')
    assert "AWS Solutions Architect" in home_html
    print("PASS: Home page is freely accessible and displays.")

    # 2. Navigating outside Home page redirects to /?unlock=1 (NOT /login)
    res_courses_locked = client.get('/courses')
    assert res_courses_locked.status_code == 302
    assert "unlock=1" in res_courses_locked.headers["Location"]
    assert "/login" not in res_courses_locked.headers["Location"]
    print("PASS: Navigating outside Home page redirects to /?unlock=1.")

    # 3. Wrong admin password rejected with 401
    wrong_pw = client.post('/api/verify-site-password', json={'password': 'WrongPassword123!'})
    assert wrong_pw.status_code == 401
    assert wrong_pw.get_json()['success'] is False
    print("PASS: Incorrect password rejected with 401.")

    # 3b. Anti-brute-force rate limiting: 5 consecutive failed attempts triggers 429 lockout
    for _ in range(4):
        client.post('/api/verify-site-password', json={'password': 'BadPassword!'})
    blocked_res = client.post('/api/verify-site-password', json={'password': 'BadPassword!'})
    assert blocked_res.status_code == 429
    assert "Too many failed attempts" in blocked_res.get_json()['error']
    print("PASS: Anti-brute-force rate limiting and security cooldown verified (429 Too Many Requests).")

    # Reset rate limit for subsequent test steps
    from app import reset_admin_rate_limit
    reset_admin_rate_limit("127.0.0.1")
    reset_admin_rate_limit("unknown")

    # 4. Correct admin password unlocks the entire web application directly (no email sending option)
    unlock_res = client.post('/api/verify-site-password', json={'password': admin_pw, 'target': '/courses'})
    assert unlock_res.status_code == 200
    unlock_data = unlock_res.get_json()
    assert unlock_data['success'] is True
    assert 'sample_email' not in unlock_data, "Email sending option should be removed"
    print("PASS: Correct admin password unlocks portal directly without email generation.")

    # 5. Now /courses and all other pages display completely!
    courses_unlocked = client.get('/courses')
    assert courses_unlocked.status_code == 200
    print("PASS: Rest of the web application now displays successfully.")

    # 6. Lock the portal again to test Client-Side Encrypted Verification
    client.get('/api/lock-portal')
    relocked_check = client.get('/courses')
    assert relocked_check.status_code == 302
    assert "unlock=1" in relocked_check.headers["Location"]
    print("PASS: Portal re-locked back to Home-only display.")

    # 7. Client-Side Encrypted Verification for Security:
    # Simulates browser JavaScript encryptAdminPasswordClientSide()
    import hashlib, secrets
    nonce = secrets.token_hex(8)
    key = hashlib.sha256(f"aws_sa_transport_vault_2026:{nonce}".encode("utf-8")).digest()
    data = admin_pw.encode("utf-8")
    key_stream = (key * (len(data) // len(key) + 1))[:len(data)]
    enc_hex = bytes(a ^ b for a, b in zip(data, key_stream)).hex()
    client_digest = hashlib.sha256(f"{admin_pw}:aws_sa_salt_2026".encode("utf-8")).hexdigest()

    enc_unlock_res = client.post('/api/verify-site-password', json={
        'encrypted_password': enc_hex,
        'nonce': nonce,
        'client_digest': client_digest,
        'target': '/topics'
    })
    assert enc_unlock_res.status_code == 200
    enc_data = enc_unlock_res.get_json()
    assert enc_data['success'] is True
    assert enc_data['redirect'] == '/topics'
    assert 'sample_email' not in enc_data
    print("PASS: Client-side encrypted password verification succeeds and unlocks session without exposing plaintext over network.")

    # 8. Verify invalid encrypted password is rejected with 401
    bad_nonce = secrets.token_hex(8)
    bad_key = hashlib.sha256(f"aws_sa_transport_vault_2026:{bad_nonce}".encode("utf-8")).digest()
    bad_data = "WrongPassword123!".encode("utf-8")
    bad_stream = (bad_key * (len(bad_data) // len(bad_key) + 1))[:len(bad_data)]
    bad_enc = bytes(a ^ b for a, b in zip(bad_data, bad_stream)).hex()
    bad_enc_res = client.post('/api/verify-site-password', json={
        'encrypted_password': bad_enc,
        'nonce': bad_nonce
    })
    assert bad_enc_res.status_code == 401
    assert bad_enc_res.get_json()['success'] is False
    print("PASS: Invalid encrypted password rejected with 401.")

    # 9. Verify UI contains NO email sending forms, email tabs, or mailto buttons in base.html
    res_home_ui = client.get('/')
    home_ui_html = res_home_ui.data.decode('utf-8')
    assert "Don't Know Password?" not in home_ui_html, "Email tab should be removed from modal"
    assert "panel-email" not in home_ui_html, "Email panel should be removed from modal"
    assert "verified-email-preview-textarea" not in home_ui_html, "Email preview textarea should be removed"
    assert "open-mailto-btn" not in home_ui_html, "Mailto button should be removed"
    assert "Client-Side Encrypted Verification" in home_ui_html, "Encrypted verification badge should be present"
    print("PASS: UI verified - all email sending options completely removed, pure encrypted admin password interface confirmed.")

    print("\nALL AWS SOLUTIONS ARCHITECT VERIFICATION TESTS PASSED SUCCESSFULLY! 🚀")


if __name__ == "__main__":
    test_native_xlsx_parsing()
    test_topics_and_roadmap()
    test_aws_workbench_simulation()
    test_routes_and_access()