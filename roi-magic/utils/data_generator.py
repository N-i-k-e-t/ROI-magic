import pandas as pd
import numpy as np

def get_available_cities():
    """Return list of available cities with their areas"""
    return {
        'Mumbai': ['Andheri', 'Bandra', 'Colaba', 'Juhu', 'Powai'],
        'Delhi': ['Dwarka', 'Rohini', 'South Delhi', 'Noida', 'Gurgaon'],
        'Bangalore': ['Whitefield', 'Electronic City', 'Indiranagar', 'Koramangala', 'HSR Layout'],
        'Hyderabad': ['Gachibowli', 'HITEC City', 'Banjara Hills', 'Jubilee Hills', 'Madhapur'],
        'Chennai': ['Anna Nagar', 'T Nagar', 'Adyar', 'Velachery', 'OMR']
    }

def get_city_metrics():
    """Return predefined metrics for each city"""
    return {
        'Mumbai': {'avg_price': 15000, 'appreciation': 8.5, 'rental_yield': 3.5},
        'Delhi': {'avg_price': 12000, 'appreciation': 7.5, 'rental_yield': 3.0},
        'Bangalore': {'avg_price': 9000, 'appreciation': 9.0, 'rental_yield': 4.0},
        'Hyderabad': {'avg_price': 7000, 'appreciation': 10.0, 'rental_yield': 4.5},
        'Chennai': {'avg_price': 8000, 'appreciation': 8.0, 'rental_yield': 3.8}
    }

def generate_market_data():
    """Generate mock market data for analysis"""
    cities = get_available_cities().keys()
    dates = pd.date_range(start='2018-01-01', end='2023-12-31', freq='M')
    city_metrics = get_city_metrics()

    data = []
    for city in cities:
        base_price = city_metrics[city]['avg_price']
        growth_rate = city_metrics[city]['appreciation'] / 100
        rental_yield_base = city_metrics[city]['rental_yield']
        volatility = 0.03  # Monthly volatility

        for date in dates:
            time_factor = (date - dates[0]).days / 365
            price = base_price * (1 + growth_rate) ** time_factor
            price *= (1 + np.random.normal(0, volatility))

            data.append({
                'Date': date,
                'City': city,
                'Price_Per_SqFt': round(price, 2),
                'Rental_Yield': round(rental_yield_base + np.random.normal(0, 0.2), 2)
            })

    return pd.DataFrame(data)

def generate_investment_comparison_data():
    """Generate mock investment comparison data"""
    years = range(1, 11)

    data = []
    for year in years:
        data.append({
            'Year': year,
            'Real_Estate': 100 * (1.12 ** year),  # 12% annual return
            'Fixed_Deposit': 100 * (1.06 ** year), # 6% annual return
            'Mutual_Funds': 100 * (1.15 ** year),  # 15% annual return
            'Gold': 100 * (1.08 ** year)           # 8% annual return
        })

    return pd.DataFrame(data)