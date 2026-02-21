from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

# Import models + validation logic from validation module
from app.validation import Period, Transaction, validate_core

router = APIRouter(prefix="/blackrock/challenge/v1")


# -------- Models --------

class ReturnsRequest(BaseModel):
    q: List[Period]
    p: List[Period]
    k: List[Period]
    transactions: List[Transaction]
    inflation: float
    wage: float
    age: int


# -------- Helper --------

def in_period(txn_date, period):
    return period.startDate <= txn_date <= period.endDate


# -------- Core Calculation --------

def calculate_returns(data: ReturnsRequest, is_nps: bool):

    # Validate first
    valid_transactions, _ = validate_core(
        data.q, data.p, data.k, data.transactions
    )

    total_transaction_amount = 0
    total_ceiling = 0
    savings_by_dates = []

    for k_period in data.k:

        invested = 0

        for txn in valid_transactions:
            if in_period(txn["date"], k_period):
                invested += txn["amount"]

        base_return_rate = 0.08 if is_nps else 0.06
        adjusted_return = base_return_rate - (data.inflation / 100)

        profit = invested * adjusted_return
        tax_benefit = invested * 0.1 if is_nps else 0

        savings_by_dates.append({
            "startDate": k_period.startDate,
            "endDate": k_period.endDate,
            "investedAmount": invested,
            "profit": round(profit, 2),
            "taxBenefit": round(tax_benefit, 2)
        })

        total_transaction_amount += invested
        total_ceiling += k_period.ceiling

    return {
        "totalTransactionAmount": total_transaction_amount,
        "totalCeiling": total_ceiling,
        "savingsByDates": savings_by_dates
    }


# -------- Endpoints --------

@router.post("/returns:nps")
def returns_nps(data: ReturnsRequest):
    return calculate_returns(data, is_nps=True)


@router.post("/returns:index")
def returns_index(data: ReturnsRequest):
    return calculate_returns(data, is_nps=False)