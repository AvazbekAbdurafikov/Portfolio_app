import streamlit as st
from sent_mail import send_mail
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    user_message =f"""\
Subject: New email From {user_email}

From: {user_email}
{raw_message}
    """

    button = st.form_submit_button("Submit")
    if button:
        send_mail(user_email, user_message)
        st.info("Your email was sent successfully")