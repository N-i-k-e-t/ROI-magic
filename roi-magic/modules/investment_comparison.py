import streamlit as st
import plotly.graph_objects as go
from utils.calculations import calculate_fd_returns, calculate_sip_returns
from utils.data_generator import generate_investment_comparison_data

def investment_comparison_section():
    st.header("Investment Comparison Tool")
    
    # Input parameters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        investment_amount = st.number_input("Investment Amount (₹)", min_value=0, value=1000000, step=100000)
    with col2:
        investment_period = st.number_input("Investment Period (Years)", min_value=1, value=5, step=1)
    with col3:
        monthly_investment = st.number_input("Monthly Investment (for SIP) (₹)", min_value=0, value=10000, step=1000)
    
    # Calculate returns for different investment types
    fd_returns = calculate_fd_returns(investment_amount, 6.0, investment_period)  # 6% FD rate
    sip_returns = calculate_sip_returns(monthly_investment, 12.0, investment_period)  # 12% SIP return
    
    # Display comparison
    st.subheader("Investment Returns Comparison")
    
    comparison_data = {
        "Fixed Deposit": {
            "Initial Investment": investment_amount,
            "Final Amount": fd_returns['Final Amount'],
            "Total Returns": fd_returns['Total Interest'],
            "ROI": fd_returns['ROI']
        },
        "SIP Investment": {
            "Initial Investment": monthly_investment * 12 * investment_period,
            "Final Amount": sip_returns['Final Amount'],
            "Total Returns": sip_returns['Total Interest'],
            "ROI": sip_returns['ROI']
        }
    }
    
    # Create comparison cards
    for investment_type, data in comparison_data.items():
        with st.container():
            st.markdown(f"### {investment_type}")
            cols = st.columns(4)
            
            cols[0].metric("Initial Investment", f"₹{data['Initial Investment']:,.2f}")
            cols[1].metric("Final Amount", f"₹{data['Final Amount']:,.2f}")
            cols[2].metric("Total Returns", f"₹{data['Total Returns']:,.2f}")
            cols[3].metric("ROI", f"{data['ROI']:.2f}%")
    
    # Create comparison chart
    comparison_df = generate_investment_comparison_data()
    
    fig = go.Figure()
    
    for column in ['Real_Estate', 'Fixed_Deposit', 'Mutual_Funds', 'Gold']:
        fig.add_trace(
            go.Scatter(
                x=comparison_df['Year'],
                y=comparison_df[column],
                name=column.replace('_', ' '),
                mode='lines+markers'
            )
        )
    
    fig.update_layout(
        title="Investment Growth Comparison (Base: ₹100)",
        xaxis_title="Years",
        yaxis_title="Value",
        height=500,
        legend_title="Investment Type"
    )
    
    st.plotly_chart(fig, use_container_width=True)
