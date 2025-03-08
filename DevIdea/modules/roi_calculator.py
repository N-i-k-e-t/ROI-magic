import streamlit as st
import plotly.graph_objects as go
from utils.calculations import calculate_roi
from utils.data_generator import get_available_cities, get_city_metrics
from utils.ai_insights import AIPropertyAnalyst

def roi_calculator_section():
    st.header("Real Estate ROI Calculator")

    # Initialize AI Analyst
    ai_analyst = AIPropertyAnalyst()

    # Location Selection
    cities = get_available_cities()
    city_metrics = get_city_metrics()

    col1, col2 = st.columns(2)

    with col1:
        selected_city = st.selectbox("Select City", options=list(cities.keys()))
        city_areas = cities[selected_city]
        selected_area = st.selectbox("Select Area", options=city_areas)

        # Use city-specific metrics for default values
        default_price_per_sqft = city_metrics[selected_city]['avg_price']
        default_appreciation = city_metrics[selected_city]['appreciation']
        default_rental_yield = city_metrics[selected_city]['rental_yield']

        # Property details
        property_size = st.number_input("Property Size (sq ft)", min_value=100, value=1000, step=100)
        purchase_price = st.number_input(
            "Purchase Price (₹)", 
            min_value=0, 
            value=int(property_size * default_price_per_sqft), 
            step=100000
        )

    with col2:
        down_payment = st.number_input(
            "Down Payment (₹)", 
            min_value=0, 
            value=int(purchase_price * 0.20),  # 20% default down payment
            step=100000
        )
        loan_amount = st.number_input(
            "Loan Amount (₹)", 
            min_value=0, 
            value=int(purchase_price - down_payment),
            step=100000
        )
        interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=8.5, step=0.1)

    col3, col4 = st.columns(2)

    with col3:
        # Use city-specific rental yield for default rental income
        default_monthly_rent = int((purchase_price * default_rental_yield / 100) / 12)
        rental_income = st.number_input(
            "Monthly Rental Income (₹)", 
            min_value=0, 
            value=default_monthly_rent,
            step=1000
        )
        expenses = st.number_input(
            "Monthly Expenses (₹)", 
            min_value=0, 
            value=int(rental_income * 0.2),  # 20% of rental income as default expenses
            step=1000
        )

    with col4:
        appreciation_rate = st.number_input(
            "Annual Appreciation Rate (%)", 
            min_value=0.0, 
            value=default_appreciation,
            step=0.1
        )
        holding_period = st.number_input("Holding Period (Years)", min_value=1, value=5, step=1)

    # Get AI Insights for the location
    with st.expander("📊 AI Market Insights", expanded=True):
        location_insights = ai_analyst.get_location_insights(selected_city, selected_area)

        st.markdown(f"""
        ### Location Analysis for {selected_area}, {selected_city}

        #### 🌟 Key Advantages
        {location_insights['advantages']}

        #### 🏗️ Development Projects
        {location_insights['developments']}

        #### 📈 Return Potential
        {location_insights['potential']}

        #### ⚠️ Investment Risks
        {location_insights['risks']}
        """)

    # Display market metrics
    st.info(f"""
        📍 Market Metrics for {selected_area}, {selected_city}:
        - Average Price: ₹{default_price_per_sqft:,}/sq ft
        - Historical Appreciation: {default_appreciation}% per year
        - Typical Rental Yield: {default_rental_yield}%
    """)

    if st.button("Calculate ROI"):
        results = calculate_roi(
            purchase_price, down_payment, loan_amount, interest_rate,
            rental_income, expenses, appreciation_rate, holding_period
        )

        # Get AI Investment Recommendations
        property_data = {
            'city': selected_city,
            'area': selected_area,
            'price': purchase_price,
            'size': property_size,
            'rental': rental_income
        }
        investment_insights = ai_analyst.get_investment_recommendations(property_data)

        # Display Results
        st.subheader("Investment Analysis")

        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

        with metrics_col1:
            st.metric("Monthly Mortgage", f"₹{results['Monthly Mortgage']:,.2f}")
            st.metric("Annual Cash Flow", f"₹{results['Annual Cash Flow']:,.2f}")

        with metrics_col2:
            st.metric("Total Return", f"₹{results['Total Return']:,.2f}")
            st.metric("Final Property Value", f"₹{results['Final Property Value']:,.2f}")

        with metrics_col3:
            st.metric("ROI", f"{results['ROI']:.2f}%")
            st.metric("Cash on Cash Return", f"{results['Cash on Cash Return']:.2f}%")

        # Display AI Investment Recommendations
        st.subheader("AI Investment Recommendations")
        st.markdown(f"""
        #### 📊 Investment Summary
        {investment_insights['summary']}

        #### ✅ Advantages
        {investment_insights['pros']}

        #### ⚠️ Considerations
        {investment_insights['cons']}

        #### 🎯 Recommended Action
        {investment_insights['action']}
        """)

        # Create ROI Breakdown Chart
        fig = go.Figure()

        fig.add_trace(go.Waterfall(
            name="ROI Breakdown",
            orientation="v",
            measure=["relative", "relative", "relative", "total"],
            x=["Down Payment", "Total Cash Flow", "Appreciation", "Total Return"],
            text=[f"₹{-down_payment:,.0f}",
                  f"₹{results['Total Cash Flow']:,.0f}",
                  f"₹{(results['Final Property Value'] - purchase_price):,.0f}",
                  f"₹{results['Total Return']:,.0f}"],
            y=[-down_payment, 
               results['Total Cash Flow'],
               results['Final Property Value'] - purchase_price,
               results['Total Return']],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        ))

        fig.update_layout(
            title="ROI Breakdown Analysis",
            showlegend=False,
            height=500,
        )

        st.plotly_chart(fig, use_container_width=True)