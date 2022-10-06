import streamlit as st

from utils.handler import error_handler


@error_handler
def main():
    st.markdown("# Welcome! 👋")

    st.markdown(
        """
    ## Overview

    This website provides a demonstration of the capabilities created
    for the course, DSBA 6156: Applied Machine Learning. In this demo,
    we offer a novel approach to predicting soccer match outcomes.

    ## Motivation



    ## Data



    ## Similar Works



    """
    )


if __name__ == "__main__":
    main()
