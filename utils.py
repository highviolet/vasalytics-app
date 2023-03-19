import streamlit as st
import pandas as pd
from pathlib import Path


@st.cache_data
def load_all() -> pd.DataFrame:
    path = Path("data") / "all.pkl"
    df = pd.read_pickle(path)
    return df


@st.cache_data
def load_mean_per_year() -> pd.DataFrame:
    path = Path("data") / "mean_by_year.pkl"
    df = pd.read_pickle(path)
    return df

@st.cache_data
def get_frame_for_year(year: int) -> pd.DataFrame:
    df = load_all()
    return df[df.year == year]

@st.cache_data
def get_years() -> list[int]:
    df = load_all()
    return sorted(df.year.unique(), reverse=True)
