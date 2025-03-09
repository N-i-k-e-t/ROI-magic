import streamlit as st
from modules.roi_calculator import roi_calculator_section
from modules.investment_comparison import investment_comparison_section
from modules.market_analysis import market_analysis_section
from pages.auth import auth_page

# Page configuration
st.set_page_config(
    page_title="InvestWise India - Real Estate ROI Analysis",
    page_icon="🏠",
    layout="wide"
)

# Load custom CSS
with open('assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Main app
def main():
    # Check authentication
    is_authenticated = auth_page()

    if not is_authenticated:
        return

    # Header
    st.title("🏠 InvestWise India")
    st.subheader("Real Estate ROI Analysis & Investment Comparison Platform")

    # User welcome message
    if "user_email" in st.session_state:
        st.sidebar.write(f"Welcome, {st.session_state['user_email']}!")

    # Navigation
    nav_option = st.sidebar.radio(
        "Navigate to:",
        ["ROI Calculator", "Investment Comparison", "Market Analysis"]
    )

    # Content based on navigation
    if nav_option == "ROI Calculator":
        roi_calculator_section()
    elif nav_option == "Investment Comparison":
        investment_comparison_section()
    else:
        market_analysis_section()

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Made with ❤️ by InvestWise India | Data for educational purposes only</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()