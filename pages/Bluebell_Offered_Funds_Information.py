# pages/1_Fund_Information.py

import streamlit as st

st.set_page_config(
    page_title="Fund Information",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Fund Information")

def get_data():
    master_doc = pd.read_csv('master_investment_data.csv')
    return master_doc

available_fund =[ 
    "KKP Plus",
    "KKP Cash",
    "KFAFIX",
    "UGISFX",
    "ESGQG",
    "ESGTECH",
    "ESEAE",
    "KTPRECIOUS",
    "Rostrum Wisdom Grand Fund of Funds",
    "KKPGNPH",
    "KTHEALTHCAREA",
    "KFGPROPA",
    "SCBS&P500A",
    "ESGCORE"
]
fund = st.sidebar.radio( 
    "Fund Selection",
    available_fund)

if fund == "KKP Plus":
    col1, col2, col3 = st.columns(3)
                        
    
