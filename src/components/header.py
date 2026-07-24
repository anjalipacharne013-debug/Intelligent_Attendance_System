import streamlit as st


def header_home():
    left, center, right = st.columns([1, 2, 1])

    with center:
        l, img, r = st.columns([1.2, 1, 1.4])  # Increase left column to push image right

        with img:
            st.image("assets/logo.png", width=120)
        st.markdown("""
        <style>
            img{
            margin-bottom:-20px;}
        </style>
        <div style="display:flex;
                    flex-direction:column;
                    align-items:center;
                    justify-content:center;">
        """, unsafe_allow_html=True)

        st.markdown("""
            <h1 style="
                text-align:center;
                color:#E0E3FF;
                line-height:0.9;
                position:relative;
                margin-top:-20px;">
                SNAP<br>CLASS
            </h1>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
# import streamlit as st

# def header_home():
#     left, center, right = st.columns([1, 2, 1])

#     with center:
#         l, img, r = st.columns([1.2, 1, 0.8])  # Increase left column to push image right

#         with img:
#             st.image("assets/logo.png", width=120)
#         st.markdown("""
#         <div style="display:flex;
#                     flex-direction:column;
#                     align-items:center;
#                     justify-content:center;">
#         """, unsafe_allow_html=True)

#         st.markdown("""
#             <h1 style="
#                 text-align:center;
#                 color:#E0E3FF;
#                 margin-top:10px;
#                 margin-bottom:30px;
#                 line-height:1.1;
#                 position:relative;
#                 left:-5px;">
#                 SNAP<br>CLASS
#             </h1>
#             """, unsafe_allow_html=True)

#         st.markdown("</div>", unsafe_allow_html=True)