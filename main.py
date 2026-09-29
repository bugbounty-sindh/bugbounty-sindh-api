from fastapi import FastAPI, Query
import requests

app = FastAPI(title="BugBounty Sindh API")

@app.get("/")
def home():
    return {"status": "SindhSecretHunter API Live!", "from": "Mehar, Sindh"}

@app.get("/check/cors")
def check_cors(url: str):
    try:
        headers = {"Origin": "https://evil.com"}
        r = requests.get(url, headers=headers, timeout=5)
        acao = r.headers.get("Access-Control-Allow-Origin", "")
        vuln = acao == "*" or "evil.com" in acao
        return {"url": url, "vulnerable": vuln, "ACAO": acao}
    except Exception as e:
        return {"error": str(e)}

@app.get("/check/headers")
def check_headers(url: str):
    try:
        r = requests.get(url, timeout=5)
        missing = [h for h in ["X-Frame-Options", "Content-Security-Policy"] if h not in r.headers]
        return {"url": url, "missing": missing}
    except Exception as e:
        return {"error": str(e)}
