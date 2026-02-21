Here is your **final short, precise, single-file README.md** ready to submit:

---

# BlackRock Challenge – Backend API

FastAPI-based backend implementing:

* Transaction validation
* Returns calculation (NPS & Index)
* Performance reporting
* Dockerized deployment

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── validation.py
 ├── returns.py
 └── performance.py
```

---

## 🚀 Run Locally

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 5477
```

Swagger UI:

```
http://localhost:5477/docs
```

---

## 🐳 Run with Docker

### Pull & Run (Recommended)

```bash
docker pull chandresh2407/blackrock_challenge_chandresh_pachauri
docker run -p 5477:5477 chandresh2407/blackrock_challenge_chandresh_pachauri
```

Swagger:

```
http://localhost:5477/docs
```

### Build Locally

```bash
docker build -t blackrock_challenge .
docker run -p 5477:5477 blackrock_challenge
```

---

## 📌 API Endpoints

### Validate Transactions

`POST /blackrock/challenge/v1/transactions:validate`

* Rejects negative, duplicate, and ceiling-exceeding transactions
* Calculates remaining ceiling
* Identifies K-period membership

---

### Returns Calculation

**NPS Returns**
`POST /blackrock/challenge/v1/returns:nps`

* Base return: 8%
* Tax benefit: 10% of invested amount

**Index Returns**
`POST /blackrock/challenge/v1/returns:index`

* Base return: 6%
* No tax benefit

Responses include total investment, savings breakdown, profit, and effective returns (after inflation).

---

### Performance Report

`GET /blackrock/challenge/v1/performance`

Returns execution time, memory usage (MB), and active threads.

---

## 👤 Author

**Chandresh Pachauri**

---
