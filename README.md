# BlackRock Challenge – Backend API

This project implements the BlackRock Challenge backend system including:

- Transaction validation
- Returns calculation (NPS & Index)
- Performance reporting
- Dockerized deployment

---

## 🏗 Architecture Overview

The application is built using **FastAPI** with a clean modular structure:

```
app/
 ├── main.py
 ├── validation.py
 ├── returns.py
 └── performance.py
```

### Key Design Principles

- Single source of truth for data models
- Reusable validation logic
- Clear separation of concerns
- Lightweight and efficient design
- Docker-ready production structure

---

## 🚀 How to Run Locally

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Start the Server

```bash
python -m uvicorn app.main:app --reload --port 5477
```

Open Swagger UI:

```
http://localhost:5477/docs
```

---

## 🐳 Run with Docker

### 1️⃣ Build Docker Image

```bash
docker build -t blk-hacking-ind-chandresh-pachauri .
```

### 2️⃣ Run Docker Container

```bash
docker run -p 5477:5477 blk-hacking-ind-chandresh-pachauri
```

Access Swagger UI:

```
http://localhost:5477/docs
```

---

## 📌 API Endpoints

### 🔹 Transaction Validation

**POST**
```
/blackrock/challenge/v1/transactions:validate
```

Validation Rules:
- Negative transaction amounts are rejected
- Duplicate transactions are rejected
- Transactions exceeding ceiling are rejected
- Remaining ceiling is calculated
- K-period membership is identified

---

### 🔹 Returns Calculation

#### NPS Returns
```
POST /blackrock/challenge/v1/returns:nps
```

#### Index Returns
```
POST /blackrock/challenge/v1/returns:index
```

Returns include:
- Total transaction amount
- Total ceiling
- Savings breakdown by K periods
- Profit calculation
- Tax benefit (NPS only)

Assumptions:
- NPS base return rate: 8%
- Index base return rate: 6%
- Inflation reduces effective return
- Tax benefit = 10% of invested amount (NPS only)

---

### 🔹 Performance Report

**GET**
```
/blackrock/challenge/v1/performance
```

Returns:
- Execution time
- Memory usage (MB)
- Number of active threads

---

## 🧠 Implementation Notes

- Validation logic is reusable across endpoints.
- Only valid transactions are considered in returns calculation.
- Clear separation between routing and business logic.
- Docker image exposes port **5477** as required.

---

## 📦 Docker Image

Public Docker image:

```
https://hub.docker.com/r/chandresh2407/blackrock_challenge_chandresh_pachauri
```

---

## 👤 Author

Chandresh Pachauri