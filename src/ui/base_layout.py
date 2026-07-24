import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp{
                background : #5865F2 !important;
            }
        </style>
    """,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp{
                background : #E0E3FF !important;
            }
        </style> 
    """,unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            /* Hide ToolBar*/
            #MainMenu, footer , header{
                visibility : hidden;
            }     
            .block-container{
                padding-top:1.5rem;
            }

            .main-title {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                color: white;
            }
            h1{
                font-family: 'Climate Crisis',sans-serif !important;
                font-size : 3.5rem !important;
                line-height : 1.1 !important;
                margin-bottom : 0rem !important;
            }
            h2{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size : 2rem !important;
                line-height : 0.9 !important;
                margin-bottom : 0rem !important;
            }
            h3,h4,p{
                font-family : 'Outfit',sans-serif;
            }
            /* Primary Button */
            .stButton > button[kind="primary"] {
                background: #5865F2 !important;
                color: white !important;
                transition : transform 0.25s ease-in-out !important;
                border: none !important;
                margin-top : 10px !important;
                padding : 10px 20px !important;
                border-radius: 1.5rem !important;
            }

            /* Secondary Button */
            .stButton > button[kind="secondary"] {
                background: #EB459E !important;
                color: white !important;
                border: none !important;
                margin-top : 10px !important;
                transition : transform 0.25s ease-in-out !important;
                padding : 10px 20px !important;
                border-radius: 1.5rem !important;
            }

            /* Tertiary Button */
            .stButton > button[kind="tertiary"] {
                background: black !important;
                color: #EB459E !important;
                transition : transform 0.25s ease-in-out !important;
                padding : 10px 20px !important;
                border: none !important;
                border-radius: 1.5rem !important;
            }

        </style>
    """,unsafe_allow_html=True)