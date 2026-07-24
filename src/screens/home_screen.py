import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from streamlit_extras.stylable_container import stylable_container
from src.ui.base_layout import style_base_layout, style_background_dashboard,style_background_home
def home_screen():

    header_home()
    style_background_home()
    style_base_layout()
    
    
    col1,col2 = st.columns(2,gap="large")

    with col1:
        with stylable_container(
            key="student_card",
            css_styles="""
            {
                background: #E0E3FF;
                border-radius: 25px;
                padding: 25px;
                text-align: center;
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            }
            """
        ):
            st.header("I am Student")
            st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
            if st.button("Student Portal",type = "primary",icon= ':material/arrow_outward:',icon_position='right'):
                st.session_state['login_type'] = 'student'
                st.rerun()  
    with col2:
        with stylable_container(
            key="teacher_card",
            css_styles="""
            {
                background: #E0E3FF;
                border-radius: 25px;
                padding: 25px;
                text-align: center;
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            }
            """
        ):
            st.header("I am Teacher")
            st.image("https://i.ibb.co/CsmQQV6X/mascot-teacher.png", width=140)
            if st.button('Teacher Portal', type = "primary",icon= ':material/arrow_outward:',icon_position='right'):
                st.session_state['login_type'] = 'teacher'
                st.rerun()
    footer_home()