from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import date

router = APIRouter(prefix="/blackrock/challenge/v1")


# ---------- Models ----------

class Period(BaseModel):
    startDate: date
    endDate: date
    ceiling: float


class Transaction(BaseModel):
    date: date
    amount: float


class ValidationRequest(BaseModel):
    q: List[Period]
    p: List[Period]
    k: List[Period]
    transactions: List[Transaction]


# ---------- Helper Functions ----------

def find_ceiling(transaction_date, q_periods, p_periods):
    total_ceiling = 0

    for period in q_periods:
        if period.startDate <= transaction_date <= period.endDate:
            total_ceiling += period.ceiling

    for period in p_periods:
        if period.startDate <= transaction_date <= period.endDate:
            total_ceiling += period.ceiling

    return total_ceiling


def in_k_period(transaction_date, k_periods):
    for period in k_periods:
        if period.startDate <= transaction_date <= period.endDate:
            return True
    return False


# ---------- Reusable Core Validation ----------

def validate_core(q, p, k, transactions):
    valid = []
    invalid = []
    seen = set()

    for txn in transactions:

        if txn.amount < 0:
            invalid.append(txn)
            continue

        key = (txn.date, txn.amount)
        if key in seen:
            invalid.append(txn)
            continue

        seen.add(key)

        ceiling = find_ceiling(txn.date, q, p)

        if txn.amount > ceiling:
            invalid.append(txn)
            continue

        remaining = ceiling - txn.amount

        valid.append({
            "date": txn.date,
            "amount": txn.amount,
            "ceiling": ceiling,
            "remanent": remaining,
            "inKPeriod": in_k_period(txn.date, k)
        })

    return valid, invalid


# ---------- Endpoint ----------

@router.post("/transactions:validate")
def validate_transactions(data: ValidationRequest):
    valid, invalid = validate_core(
        data.q, data.p, data.k, data.transactions
    )

    return {
        "valid": valid,
        "invalid": invalid
    }