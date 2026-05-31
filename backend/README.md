# ⚙️ Raksha AI - Backend Service

This is the Python-based REST API backend for **Raksha AI**. It serves as the single source of truth, orchestrating user authentication, road hazard reporting, AI-based image classification, emergency SOS workflows, routing risk-profiling, and command dashboard summaries.

---

## 🏛️ Architecture & Modules

The backend is built using **Flask** and follows a Service-Oriented pattern:

```
backend/
├── main.py                    # Consolidates all routes and initializes the app
├── config.py                  # Parses env configurations (secret keys, max uploads)
├── models/                    # Encapsulates business/model execution logic
│   ├── RiskModel.py           # Evaluates tabular risk scores and route-profiling indices
│   ├── RoadModel.py           # Loads sklearn class for predicting road hazard parameters
│   └── SosModel.py            # Prepares alert triggers and contacts emergency networks
├── services/                  # Handles IO and core operations
│   ├── ai_bridge.py           # Simulates job scheduling for async image classification
│   ├── auth_service.py        # Validates credentials and parses JWT Bearer tokens
│   ├── firebase_service.py    # Integrates Firebase cloud syncing status checks
│   ├── localization_service.py# Translates API response strings dynamically into 6 languages
│   ├── maps_service.py        # Interfaces coordinates with hospital geofences and reverse geocoding
│   ├── reports_service.py     # CRUD operations for hazard reports
│   └── sos_service.py         # Appends and lists emergency SOS alerts
├── routers/                   # ⚠️ Deprecated Prototype Routers
│   └── README.md              # Legacy files (not used; consolidated in main.py)
└── uploads/                   # Local storage folder for uploaded hazard pictures
```

---

## 🌐 API Localization

The backend supports dynamic localization for English (`en`), Hindi (`hi`), Tamil (`ta`), Telugu (`te`), Kannada (`kn`), and Malayalam (`ml`). 

The `LocalizationService` resolves the desired language using the following priority:
1. The `language` query parameter (e.g., `GET /roads/issues?language=hi`).
2. The `Accept-Language` header (e.g., `Accept-Language: ta-IN,ta;q=0.9`).
3. Defaults to `en` if not specified or not supported.

All response payloads generated through the service use a localized response format:
```json
{
  "success": true,
  "message": "रिपोर्ट सफलतापूर्वक जमा की गई",
  "language": "hi",
  "data": {
    "report_id": "1717182900"
  }
}
```

---

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.10+
- Virtual environment (`venv`)

### 1️⃣ Virtual Environment & Dependencies
Navigate to the `backend/` directory:
```bash
python -m venv .venv
```
Activate the environment:
- **Windows (PowerShell)**: `.venv\Scripts\Activate.ps1`
- **Windows (CMD)**: `.venv\Scripts\activate.bat`
- **Linux/macOS**: `source .venv/bin/activate`

Install the required packages:
```bash
pip install -r Requirements.txt
```

### 2️⃣ Environment Variables
The backend configures itself using environment variables. Create a `.env` file at the project root or set these values in your shell:
```bash
PORT=5000
HOST=0.0.0.0
SECRET_KEY=dev-secret-key-change-me
UPLOAD_DIR=uploads
```

### 3️⃣ Running the Server
Start the Flask development server:
```bash
python main.py
```
The console will print out:
`* Running on http://0.0.0.0:5000`

---

## 🧪 Running Tests

The backend contains integration and unit tests validating auth tokens, report submissions, risk evaluations, and SOS pings.

Run the tests from the `backend/` folder:
```bash
python -m unittest discover -s ../tests -p "*.py"
```
Or run a specific test file:
```bash
python -m unittest ../tests/test_backend_routes.py
```
