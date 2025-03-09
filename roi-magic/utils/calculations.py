import numpy as np

def pmt(rate, nper, pv):
    """
    Calculate the payment for a loan based on constant payments and a constant interest rate.

    Parameters:
    rate : float
        Interest rate per period
    nper : int
        Total number of payments
    pv : float
        Present value
    """
    if rate == 0:
        return -pv / nper
    return -rate * pv * (1 + rate)**nper / ((1 + rate)**nper - 1)

def calculate_roi(purchase_price, down_payment, loan_amount, interest_rate, rental_income, expenses, appreciation_rate, holding_period):
    """Calculate Real Estate ROI metrics"""

    # Monthly mortgage payment calculation
    monthly_rate = interest_rate / 12 / 100
    num_payments = holding_period * 12
    monthly_mortgage = pmt(monthly_rate, num_payments, loan_amount)

    # Annual calculations
    annual_rental_income = rental_income * 12
    annual_expenses = expenses * 12
    annual_mortgage = abs(monthly_mortgage) * 12

    # Cash flow calculations
    annual_cash_flow = annual_rental_income - annual_expenses - annual_mortgage
    total_cash_flow = annual_cash_flow * holding_period

    # Property value after appreciation
    final_value = purchase_price * (1 + appreciation_rate/100) ** holding_period

    # ROI Calculations
    total_investment = down_payment
    total_return = total_cash_flow + (final_value - purchase_price)
    roi = (total_return / total_investment) * 100

    return {
        'Monthly Mortgage': abs(monthly_mortgage),
        'Annual Cash Flow': annual_cash_flow,
        'Total Cash Flow': total_cash_flow,
        'Final Property Value': final_value,
        'Total Return': total_return,
        'ROI': roi,
        'Cash on Cash Return': (annual_cash_flow / down_payment) * 100
    }

def calculate_fd_returns(principal, rate, years):
    """Calculate Fixed Deposit returns"""
    amount = principal * (1 + rate/100) ** years
    return {
        'Final Amount': amount,
        'Total Interest': amount - principal,
        'ROI': ((amount - principal) / principal) * 100
    }

def calculate_sip_returns(monthly_investment, rate, years):
    """Calculate SIP returns"""
    monthly_rate = rate / 12 / 100
    months = years * 12

    amount = monthly_investment * ((1 + monthly_rate) ** months - 1) / monthly_rate * (1 + monthly_rate)
    total_investment = monthly_investment * months

    return {
        'Final Amount': amount,
        'Total Investment': total_investment,
        'Total Interest': amount - total_investment,
        'ROI': ((amount - total_investment) / total_investment) * 100
    }