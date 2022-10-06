import streamlit as st

from utils.handler import error_handler


@error_handler
def main():
    st.markdown("# Sources")

    st.markdown(
        """
    Here's a list of sources:

    1. Source One
    2. Source Two
    3. Source Three

    """
    )


if __name__ == "__main__":
    main()
