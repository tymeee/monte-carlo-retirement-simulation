# pages/1_Fund_Information.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Fund Information",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Fund Information")
st.write("Disclaimer: Data was last updated on July 17 2026, future changes may not have been accounted for")

def get_data():
    master_doc = pd.read_csv("master_investment_data.csv")
    return master_doc
historicaldata = get_data()

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
    st.title("KKP Plus")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="1.49%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="3.71"
    )

    c3.metric(
        label="Risk Level",
        value="Low"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["plus"] = pd.to_numeric(
        historicaldata["plus"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "plus"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="plus",
        title="Historical Price",
        labels={
        "plus": "KKP Plus price",
        "Date": "Date"
        }
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Fund Price",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={"displayModeBar": False}
    )

    Holdings = [
        "Japan Treasury Disc Bill(JP1743701S35)",
        "พันธบัตรธนาคารแห่งประเทศไทย (CBF26O12A)",
        "พันธบัตรธนาคารแห่งประเทศไทย (CBF26817A)",
        "JAPAN TREASURY DISC BILL (JP1743801S59)",
        "พันธบัตรธนาคารแห่งประเทศไทย (CBF26720A)",
        "Other"
    ]
    alloc_amt = [
        0.058,
        0.055,
        0.0454,
        0.0417,
        0.0317,
        0.7628
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Fund Holdings")
    st.plotly_chart(pie_fig, use_container_width = True)
    c2.metric(label="Main Asset Class", value="Money Market Assets")
                        
    
