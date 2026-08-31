"""
Central configuration for the Adaptive AI-Based Risk-Aware Key Rotation Framework.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
ENCRYPTED_DIR = os.path.join(BASE_DIR, "encrypted")
KEYS_DIR = os.path.join(BASE_DIR, "keys")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

for d in (UPLOAD_DIR, ENCRYPTED_DIR, KEYS_DIR, LOGS_DIR):
    os.makedirs(d, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"

# --- Crypto ---
KEY_SIZE = 32       # 256-bit key
NONCE_SIZE = 12      # 96-bit nonce for ChaCha20-Poly1305

# --- Risk engine ---
RISK_THRESHOLD = 30  # score above this triggers rotation

RISK_WEIGHTS = {
    "encryption_risk": 10,   # baseline risk simply for holding an encrypted secret
    "file_type_risk": {
        "high": 20,   # e.g. .exe, .zip, .sql, .env, .pem
        "medium": 12,  # e.g. .docx, .xlsx, .pdf
        "low": 5,     # e.g. .txt, .csv, .png
    },
    "age_risk_per_day": 1,       # file age contribution, capped
    "age_risk_cap": 25,
    "key_age_risk_per_day": 1.5,  # key age contributes more (older key = weaker)
    "key_age_risk_cap": 30,
    "access_risk_per_download": 3,  # more downloads = more exposure
    "access_risk_cap": 15,
}

# session secret (demo only — in production load from env/secret manager)
SESSION_SECRET = os.environ.get("APP_SESSION_SECRET", "dev-secret-change-me-in-production")

# Demo mode: if True, the file-detail page is allowed to show truncated key
# material for educational/evaluation purposes. Production UIs should NOT do this.
DEMO_MODE_SHOW_KEY_EVIDENCE = True
