# roadwatch.py
# Unified RoadWatch application (Raksha AI pivot)
# Flask-based backend with citizen monitoring, authority routing,
# transparency dashboard, RTI generator, and lifecycle tracking.

from flask import Flask, request, jsonify
import hashlib
import datetime
import random

app = Flask(__name__)

# -----------------------------
# Utility Functions
# -----------------------------

def make_hash(content: bytes, metadata: str) -> str:
    """Generate tamper-evident hash for uploaded evidence."""
    return hashlib.sha256(content + metadata.encode()).hexdigest()

def now_iso() -> str:
    """Return current timestamp in ISO format."""
    return datetime.datetime.now().isoformat()

# -----------------------------
# Citizen Monitoring
# -----------------------------

def analyze_pothole(image_bytes: bytes) -> dict:
    """Mock AI pothole detection with severity scoring."""
    diameter = random.randint(15, 120)  # cm
    depth = random.choice(["shallow", "moderate", "deep"])
    severity = "High" if depth == "deep" or diameter > 80 else "Medium"
    return {
        "diameter_cm": diameter,
        "depth_category": depth,
        "danger_radius_m": round(diameter * 0.5, 1),
        "severity": severity,
    }

@app.route("/report", methods=["POST"])
def report_issue():
    """Citizen submits road issue with image + metadata."""
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image_bytes = request.files["image"].read()
    metadata = request.form.get("metadata", "{}")
    analysis = analyze_pothole(image_bytes)
    report_hash = make_hash(image_bytes, metadata)
    report_id = hashlib.md5(report_hash.encode()).hexdigest()[:10]
    ISSUES[report_id] = {"stage": "Reported", "last_update": now_iso()}
    return jsonify({
        "report_id": report_id,
        "analysis": analysis,
        "hash": report_hash,
        "status": "Received"
    })

# -----------------------------
# Authority Routing
# -----------------------------

def identify_authority(lat: float, lon: float) -> str:
    """Determine responsible authority based on coordinates."""
    if 28.5 < lat < 29.0 and 77.0 < lon < 78.0:
        return "Municipal Corporation Meerut"
    elif lat > 29.0:
        return "PWD Uttar Pradesh"
    return "NHAI"

@app.route("/route", methods=["POST"])
def route_to_authority():
    data = request.get_json(force=True)
    lat, lon = data.get("lat"), data.get("lon")
    if lat is None or lon is None:
        return jsonify({"error": "Missing coordinates"}), 400
    return jsonify({"authority": identify_authority(lat, lon)})

# -----------------------------
# Transparency Dashboard
# -----------------------------

def budget_vs_issues(district: str) -> dict:
    budgets = {"Meerut": 4.2e7, "Delhi": 6.8e7, "Lucknow": 5.1e7}
    issues = random.randint(400, 900)
    resolved = random.randint(100, issues)
    return {
        "district": district,
        "budget_allocated": budgets.get(district, 3.0e7),
        "issues_reported": issues,
        "resolved": resolved,
        "resolution_rate": round(resolved / issues * 100, 2)
    }

@app.route("/dashboard/<district>")
def dashboard(district):
    return jsonify(budget_vs_issues(district))

# -----------------------------
# RTI Draft Generator
# -----------------------------

def generate_rti(report_id: str, authority: str, description: str) -> str:
    today = datetime.date.today().strftime("%d-%m-%Y")
    return f"""
To,
The Public Information Officer,
{authority}

Subject: Request for information under the Right to Information Act, 2005

Respected Sir/Madam,

I am a citizen reporting a persistent road issue (Report ID: {report_id})
located under your jurisdiction. Kindly provide details of repair orders,
contractor name, and expenditure incurred for this location.

Date of request: {today}
Description: {description}

Yours faithfully,
RoadWatch Citizen
"""

@app.route("/rti", methods=["POST"])
def rti_draft():
    data = request.get_json(force=True)
    draft = generate_rti(
        data.get("report_id", "N/A"),
        data.get("authority", "Unknown Authority"),
        data.get("description", "No description provided")
    )
    return jsonify({"rti_draft": draft})

# -----------------------------
# Issue Lifecycle Tracker
# -----------------------------

ISSUES = {}

@app.route("/status/<report_id>")
def status(report_id):
    return jsonify(ISSUES.get(report_id, {"stage": "Unknown"}))

@app.route("/update_status", methods=["POST"])
def update_status():
    data = request.get_json(force=True)
    report_id, stage = data.get("report_id"), data.get("stage")
    if not report_id or not stage:
        return jsonify({"error": "Missing report_id or stage"}), 400
    ISSUES[report_id] = {"stage": stage, "last_update": now_iso()}
    return jsonify({"updated": True, "report_id": report_id, "stage": stage})

# -----------------------------
# Multilingual Stub
# -----------------------------

@app.route("/translate", methods=["POST"])
def translate_report():
    data = request.get_json(force=True)
    lang = data.get("lang", "en")
    translations = {
        "hi": "इस सड़क पर बड़ा गड्ढा है",
        "en": "There is a large pothole on this road"
    }
    return jsonify({"translated": translations.get(lang, data.get("text", ""))})

# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# -----------------------------
# 8️⃣ Government API Integrations
# -----------------------------

import requests

def forward_to_cpgrams(report):
    """Forward issue to CPGRAMS (mock integration)."""
    url = "https://grievances.india.gov.in/api/submit"  # Example endpoint
    payload = {
        "issue": report.get("description", ""),
        "location": report.get("location", ""),
        "citizen": report.get("citizen_id", "anonymous")
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def forward_to_nhai(report):
    """Forward issue to NHAI iDEAS portal (mock integration)."""
    url = "https://nhai.gov.in/ideas/api/report"
    payload = {
        "issue": report.get("description", ""),
        "gps": report.get("gps", {}),
        "severity": report.get("severity", "")
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.route("/forward", methods=["POST"])
def forward_issue():
    """Forward citizen report to government portals."""
    report = request.get_json(force=True)
    authority = report.get("authority", "NHAI")
    if authority == "NHAI":
        result = forward_to_nhai(report)
    else:
        result = forward_to_cpgrams(report)
    return jsonify({"forwarded_to": authority, "result": result})

# -----------------------------
# 9️⃣ Escalation Engine
# -----------------------------

def escalate_issue(report_id, days_since_report):
    if days_since_report > 30:
        return "RTI draft + social media escalation"
    elif days_since_report > 7:
        return "Escalated to District Collector"
    return "No escalation"

@app.route("/escalate/<report_id>")
def escalate(report_id):
    issue = ISSUES.get(report_id)
    if not issue:
        return jsonify({"error": "Report not found"}), 404
    last_update = datetime.datetime.fromisoformat(issue["last_update"])
    days = (datetime.datetime.now() - last_update).days
    action = escalate_issue(report_id, days)
    return jsonify({"report_id": report_id, "escalation_action": action})
