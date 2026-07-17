# pages/1_Fund_Information.py

import streamlit as st

st.set_page_config(
    page_title="Fund Information",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Fund Information")

fund_information = {
    "KKP PLUS": {
        "category": "Fixed Income",
        "risk": "Low",
        "description": (
            "A fixed-income portfolio intended to provide liquidity "
            "and relatively stable returns."
        ),
        "management_fee": "0.50%",
    },

    "Global Equity Fund": {
        "category": "Global Equity",
        "risk": "High",
        "description": (
            "A portfolio investing across international equity markets."
        ),
        "management_fee": "1.20%",
    },

    "Technology Fund": {
        "category": "Sector Equity",
        "risk": "High",
        "description": (
            "A concentrated portfolio of technology-related companies."
        ),
        "management_fee": "1.50%",
    },
}

selected_fund = st.selectbox(
    "Select a fund",
    options=list(fund_information.keys()),
    key="fund_information_selector"
)

fund = fund_information[selected_fund]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Fund category", fund["category"])

with col2:
    st.metric("Risk level", fund["risk"])

with col3:
    st.metric("Management fee", fund["management_fee"])

st.subheader("Fund overview")
st.write(fund["description"])
