from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import BaseModel
import sqlite3
import hashlib
import bcrypt

# Import ML predictor
try:
    from ml_model.predict import ml_predictor
    ML_ENABLED = True
    print("[ML] Models loaded successfully")
except Exception as e:
    ML_ENABLED = False
    print(f"[ML] Models not available: {e}")

# --- Configuration ---
SECRET_KEY = "your-very-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Security Helpers ---

def get_password_hash(password: str):
    pw_bytes = hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str):
    try:
        pw_bytes = hashlib.sha256(plain_password.encode('utf-8')).hexdigest().encode('utf-8')
        return bcrypt.checkpw(pw_bytes, hashed_password.encode('utf-8'))
    except Exception:
        return False

# --- JWT Helpers ---

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    conn = sqlite3.connect("finance_app.db")
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()

    if user is None:
        raise credentials_exception
    return dict(user)

# --- Database Initialization ---

def init_db():
    conn = sqlite3.connect("finance_app.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            hashed_password TEXT,
            name TEXT,
            status TEXT,
            balance REAL DEFAULT 0.0,
            financial_score REAL DEFAULT 50.0,
            xp INTEGER DEFAULT 0,
            latest_advice TEXT DEFAULT 'Keep tracking your expenses!',
            savings_goal REAL DEFAULT 5000.0,
            role TEXT DEFAULT 'general'
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            username TEXT,
            amount REAL,
            timestamp TEXT
        )
    """)

    hashed_pw = get_password_hash("password123")

    conn.execute("""
        INSERT OR IGNORE INTO users 
        (id, username, hashed_password, name, status, balance, financial_score, xp, latest_advice, savings_goal, role)
        VALUES (1, 'ali_farmer', ?, 'Ali', 'Gold Member', 45280.0, 72.0, 150,
                'Invest in seeds this season for better returns!', 10000.0, 'farmer')
    """, (hashed_pw,))

    conn.commit()
    conn.close()

init_db()

# --- Pydantic Models ---

class SpendRequest(BaseModel):
    amount: float

class XPRequest(BaseModel):
    points: int

class RedeemRequest(BaseModel):
    cost: int
    brand: str

# --- API Routes ---

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    conn = sqlite3.connect("finance_app.db")
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (form_data.username,)).fetchone()
    conn.close()

    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user/me")
async def read_user_profile(current_user: dict = Depends(get_current_user)):
    profile = current_user.copy()
    profile.pop("hashed_password", None)
    return profile

@app.get("/user/{username}")
async def get_user(username: str):
    conn = sqlite3.connect("finance_app.db")
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    u = dict(user)
    u.pop("hashed_password", None)
    return u

@app.post("/spend/{username}")
async def spend(username: str, req: SpendRequest):
    conn = sqlite3.connect("finance_app.db")
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")

    u = dict(user)
    if u["balance"] < req.amount:
        conn.close()
        return {"error": "Insufficient balance!"}

    new_balance = u["balance"] - req.amount
    new_score = max(0.0, u["financial_score"] - (req.amount / u["savings_goal"]) * 10)

    # Generate ML-powered advice
    if ML_ENABLED:
        advice = ml_predictor.generate_ml_advice(u, req.amount)
    else:
        advice = "Good job staying within budget!" if req.amount < u["savings_goal"] * 0.1 else \
                 "Consider if this expense is necessary."

    conn.execute(
        "UPDATE users SET balance = ?, financial_score = ?, latest_advice = ? WHERE username = ?",
        (new_balance, new_score, advice, username)
    )
    conn.execute(
        "INSERT INTO transactions (username, amount, timestamp) VALUES (?, ?, ?)",
        (username, req.amount, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

    return {"message": "Success", "advice": advice, "new_balance": new_balance}

@app.post("/add_xp/{username}")
async def add_xp(username: str, req: XPRequest):
    conn = sqlite3.connect("finance_app.db")
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")

    new_xp = dict(user)["xp"] + req.points
    conn.execute("UPDATE users SET xp = ? WHERE username = ?", (new_xp, username))
    conn.commit()
    conn.close()

    return {"message": "Success", "new_xp": new_xp}

@app.post("/redeem/{username}")
async def redeem(username: str, req: RedeemRequest):
    conn = sqlite3.connect("finance_app.db")
    conn.row_factory = sqlite3.Row
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user:
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")

    u = dict(user)
    if u["xp"] < req.cost:
        conn.close()
        return {"error": "Not enough XP!"}

    new_xp = u["xp"] - req.cost
    conn.execute("UPDATE users SET xp = ? WHERE username = ?", (new_xp, username))
    conn.commit()
    conn.close()

    return {"message": "Success", "brand": req.brand, "new_xp": new_xp}
