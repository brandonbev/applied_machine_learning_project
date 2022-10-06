import streamlit as st

from utils.handler import error_handler


@error_handler
def main():
    (
        data,
        eda,
        pre_processing,
        feature_engineering,
        feature_selection,
        modeling,
        evaluation,
    ) = st.tabs(
        tabs=[
            "Data",
            "EDA",
            "Pre-Processing",
            "Feature Engineering",
            "Feature Selection",
            "Modeling",
            "Evaluation",
        ]
    )

    with data:
        st.markdown("Further description of data, how it was collected, etc.")

    with eda:
        st.markdown("Initial EDA, findings, methods, thoughts.")

    with pre_processing:
        st.markdown("Any sort of data cleanup or wrangling.")

    with feature_engineering:
        st.markdown("Engineering new features, manipulating original features, etc.")

    with feature_selection:
        st.markdown("What features were selected, how, and why.")

    with modeling:
        st.markdown("Creating models to predict soccer scores.")

    with evaluation:
        st.markdown("Final model evaluation.")


if __name__ == "__main__":
    main()
