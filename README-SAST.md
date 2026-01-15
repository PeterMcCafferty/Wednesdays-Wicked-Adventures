# SAST Security Testing

Static Application Security Testing (SAST) for Python code analysis.

## 🛠️ Tool Used

- **Bandit**: Static security analyzer for Python
- **Configuration**: `.bandit.yml` (excludes common false positives)

## 📋 What is tested

- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Insecure function usage (eval, exec)
- Hardcoded passwords in code
- Inadequate security configurations
- Cryptography issues

## 🚀 How to run

### Locally
```bash
# Install Bandit
pip install bandit

# Run full scan
bandit -c .bandit.yml -r . -f json -o bandit-results.json

# View results
python3 -c "import json; print(json.dumps(json.load(open('bandit-results.json')), indent=2))"