import streamlit as st
import plotly.express as px
from utils.data_generator import generate_market_data

def market_analysis_section():
    st.header("Market Analysis Dashboard")
    
    # Generate market data
    market_data = generate_market_data()
    
    # City selection
    selected_cities = st.multiselect(
        "Select Cities to Compare",
        options=market_data['City'].unique(),
        default=market_data['City'].unique()[:3]
    )
    
    # Filter data based on selection
    filtered_data = market_data[market_data['City'].isin(selected_cities)]
    
    # Price Trends
    st.subheader("Property Price Trends")
    fig_price = px.line(
        filtered_data,
        x='Date',
        y='Price_Per_SqFt',
        color='City',
        title='Property Price Trends (Price per Sq Ft)'
    )
    fig_price.update_layout(height=500)
    st.plotly_chart(fig_price, use_container_width=True)
    
    # Rental Yield Analysis
    st.subheader("Rental Yield Analysis")
    
    # Calculate average rental yield by city
    rental_yield_data = filtered_data.groupby('City')['Rental_Yield'].mean().reset_index()
    
    fig_rental = px.bar(
        rental_yield_data,
        x='City',
        y='Rental_Yield',
        title='Average Rental Yield by City',
        color='City'
    )
    fig_rental.update_layout(height=400)
    st.plotly_chart(fig_rental, use_container_width=True)
    
    # Market Statistics
    st.subheader("Market Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Price Statistics
        price_stats = filtered_data.groupby('City')['Price_Per_SqFt'].agg(['mean', 'min', 'max']).round(2)
        st.write("Price Statistics (₹ per Sq Ft)")
        st.dataframe(price_stats)
    
    with col2:
        # Rental Yield Statistics
        rental_stats = filtered_data.groupby('City')['Rental_Yield'].agg(['mean', 'min', 'max']).round(2)
        st.write("Rental Yield Statistics (%)")
        st.dataframe(rental_stats)
