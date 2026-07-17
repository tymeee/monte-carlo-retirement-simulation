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
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )


    st.plotly_chart(pie_fig, width = "stretch",config={"responsive":True,"displayModeBar":False})
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Bonds/Treasury Bills")
    
if fund == "KKP Cash":
    st.title("KKP Cash")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="1.29%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="2.01"
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

    historicaldata["cash"] = pd.to_numeric(
        historicaldata["cash"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "cash"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="cash",
        title="Historical Price",
        labels={
        "cash": "KKP Cash price",
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
        "พันธบัตรธนาคารแห่งประเทศไทย (CBF26907A)",
        "JAPAN TREASURY DISC BILL (JP1743701S35)",
        "พันธบัตรธนาคารแห่งประเทศไทย (CBF26824A)",
        "พันธบัตรธนาคารแห่งประเทศไทย (CBF26817A)",
        "JAPAN TREASURY DISC BILL (JP1743781S53)",
        "Other"
    ]
    alloc_amt = [
        0.0977,
        0.0757,
        0.054,
        0.05,
        0.0474,
        0.6752
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Money Market Assets")

if fund == "KFAFIX":
    st.title("KFAFIX-A")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="3.41%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="-0.22"
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

    historicaldata["kfa"] = pd.to_numeric(
        historicaldata["kfa"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "kfa"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="kfa",
        title="Historical Price",
        labels={
        "kfa": "KFAFIX-A price",
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
        "Doha Bank Deposit Account",
        "Gulf Development Bond (ครั้งที่ 1/2568 ชุดที่ 2)",
        "พันธบัตรธนาคารแห่งประเทศไทยงวดที่ 3/364/69",
        "PIMCO GIS Income Fund",
        "พันธบัตรรัฐบาลส่งเสริมความยั่งยืน ใน ปีงบประมาณ พ.ศ. 2568 ครั้งที่1",
        "Other"
    ]
    alloc_amt = [
        0.0833,
        0.0577,
        0.0471,
        0.0452,
        0.0389,
        0.7278
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Corporate Debt Instruments")

if fund == "UGISFX":
    st.title("UGISFX-N")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="1.26%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="1.47"
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

    historicaldata["ugi"] = pd.to_numeric(
        historicaldata["ugi"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "ugi"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="ugi",
        title="Historical Price",
        labels={
        "ugi": "UGISFX-N price",
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
        "PIMCO GIS Income Fund (Class I)",
        "Other"
    ]
    alloc_amt = [
        0.9654,
        0.0346
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Bonds")

if fund == "ESGQG":
    st.title("ES-GQG")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="12.33%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="0.79"
    )

    c3.metric(
        label="Risk Level",
        value="High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["gqg"] = pd.to_numeric(
        historicaldata["gqg"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "gqg"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="gqg",
        title="Historical Price",
        labels={
        "gqg": "ES-GQG price",
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
        "Wellington Global Quality Growth Fund",
        "Other"
    ]
    alloc_amt = [
        0.9773,
        0.0227
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Equity")


if fund == "ESGTECH":
    st.title("ES-GTECH")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="44.53%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="2.06"
    )

    c3.metric(
        label="Risk Level",
        value="Very High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["gtech"] = pd.to_numeric(
        historicaldata["gtech"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "gtech"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="gtech",
        title="Historical Price",
        labels={
        "gtech": "ES-GTECH price",
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
        "Polar Capital Global Technology Fund USD Class I Dist (POLGTIU)",
        "Other"
    ]
    alloc_amt = [
        0.9796,
        0.0204
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Technology Sector Equity")

if fund == "ESEAE":
    st.title("ES-EAE")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="27.46%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="1.57"
    )

    c3.metric(
        label="Risk Level",
        value="High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["eae"] = pd.to_numeric(
        historicaldata["eae"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "eae"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="eae",
        title="Historical Price",
        labels={
        "eae": "ES-EAE price",
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
        "Baillie Gifford Worldwide Emerging Markets Leading Companies Fund",
        "Other"
    ]
    alloc_amt = [
        0.9588,
        0.0412
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Emerging Market Equity")    

if fund == "KTPRECIOUS":
    st.title("KT-PRECIOUS")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="163.05%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="1.23"
    )

    c3.metric(
        label="Risk Level",
        value="Very High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["ktp"] = pd.to_numeric(
        historicaldata["ktp"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "ktp"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="ktp",
        title="Historical Price",
        labels={
        "ktp": "KT-PRECIOUS price",
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
        "Franklin Templeton Investment Funds - Franklin Gold and Precious Metals Fund A SGD",
        "Other"
    ]
    alloc_amt = [
        0.9742,
        0.0258
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Commodities (Gold/Precious Metals)")

if fund == "KKPGNPH":
    st.title("KKP GNP-H")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="14.43%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="0.7"
    )

    c3.metric(
        label="Risk Level",
        value="High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["gnph"] = pd.to_numeric(
        historicaldata["gnph"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "gnph"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="gnph",
        title="Historical Price",
        labels={
        "gnph": "KKP GNP-H price",
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
        "CAPITAL GROUP NEW PERSPECTIVE FUND LUX",
        "BAY",
        "STANDARD CHARTERED BANK (THAI) PUBLIC CO.,LTD.",
        "KIATNAKIN PHATRA ASSET MANAGEMENT COMPANY LIMITED",
        "Other"
    ]
    alloc_amt = [
        0.9657,
        0.0171,
        0.0108,
        0.0024,
        0.004
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Equity")

if fund == "KTHEALTHCAREA":
    st.title("KT-HEALTHCARE-A")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="16.05%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="1.87"
    )

    c3.metric(
        label="Risk Level",
        value="Very High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["healthcare"] = pd.to_numeric(
        historicaldata["healthcare"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "healthcare"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="healthcare",
        title="Historical Price",
        labels={
        "healthcare": "KT-HEALTHCARE-A price",
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
        "Janus Global Life Sciences Fund",
        "Other"
    ]
    alloc_amt = [
        0.9851,
        0.0149
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Healthcare Sector Equity")


if fund == "KFGPROPA":
    st.title("KFGPROP-A")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="3.58%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="0.6"
    )

    c3.metric(
        label="Risk Level",
        value="Very High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["prop"] = pd.to_numeric(
        historicaldata["prop"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "prop"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="prop",
        title="Historical Price",
        labels={
        "prop": "KFGPROP-A price",
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
        "Janus Capital International Ltd",
        "Other"
    ]
    alloc_amt = [
        0.9578,
        0.0422
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Property/Real Estate Sector Equity")

if fund == "ESGCORE":
    st.title("ES-GCORE")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="18.04%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="1.23"
    )

    c3.metric(
        label="Risk Level",
        value="High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["gcore"] = pd.to_numeric(
        historicaldata["gcore"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "gcore"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="gcore",
        title="Historical Price",
        labels={
        "gcore": "ES-GCORE price",
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
        "Goldman Sachs - SICAV I - GS Global CORE Eq Ptf",
        "Other"
    ]
    alloc_amt = [
        0.9742,
        0.0258
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="Global Equity")

if fund == "SCBS&P500A":
    st.title("SCBS&P500A")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        label="1 year return (2025)",
        value="12.07%"
    )

    c2.metric(
        label="1 year Sharpe Ratio (2025)",
        value="1.2"
    )

    c3.metric(
        label="Risk Level",
        value="High"
    )

    st.write("Historical Price Data (Since End of 2024)")

    historicaldata["Date"] = pd.to_datetime(
        historicaldata["Date"],
        errors="coerce"
    )

    historicaldata["sp500"] = pd.to_numeric(
        historicaldata["sp500"],
        errors="coerce"
    )

    plot_data = (
        historicaldata
        .dropna(subset=["Date", "sp500"])
        .sort_values("Date")
    )

    fig = px.line(
        plot_data,
        x="Date",
        y="sp500",
        title="Historical Price",
        labels={
        "sp500": "SCBS&P500A price",
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
        "ISHARES CORE S&P 500 ETF",
        "JP MORGAN US RESEARCH ENHANCED INDEX EQUITY ACTIVE UCITS ETF"
        "Other"
    ]
    alloc_amt = [
        0.9881,
        0.0098,
        0.0021
    ]
    pie_fig = px.pie(Holdings,values=alloc_amt,names = Holdings, title = "Top 5 Fund Holdings")
    pie_fig.update_traces(
        textposition="inside",
        textinfo="percent",
        textfont=dict(
            size=13,
            color="#F5F8FF"
        ),
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Allocation: %{percent}"
            "<extra></extra>"
        ),
        marker=dict(
            line=dict(
                color="#071121",
                width=2
            )
        )
      )
    pie_fig.update_layout(
        title=dict(
            text="Top 5 Fund Holdings",
            x=0.02,
            xanchor="left",
            font=dict(
                size=20,
                color="#F1F6FF"
            )
        ),

        height=520,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial, sans-serif",
            color="#D9E5F5"
        ),

    # Put legend below chart so it cannot get cut off
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=-0.08,
            yanchor="top",
            font=dict(
                size=12,
                color="#D9E5F5"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),

        margin=dict(
            l=25,
            r=25,
            t=75,
            b=100
        )
      )
    st.plotly_chart(pie_fig, use_container_width = True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Main Asset Class", value="S&P500 and American Equity")
