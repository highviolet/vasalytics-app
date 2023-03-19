import streamlit as st
import utils
import plost


def make_mean_time_line_plot():
    df = utils.load_mean_per_year()
    df = df.T.melt(ignore_index=False).reset_index()
    plost.line_chart(
        df,
        x={"field": "year", "type": "ordinal", "title": None},
        y={"field": "value", "type": "quantitative", "title": "Tid", "mark": "point"},
        color={"field": "start_group", "title": "Startled"},
        title="Medeltid per startled",
        legend="right",
    )


def render_page():
    st.title("Vasalytics")
    make_mean_time_line_plot()


if __name__ == "__main__":
    render_page()
