import streamlit as st

st.title("Streamlit pertama")
with st.form(key="my_form"):
    nama = st.text_input("Masukkan nama Anda")
    jenis_kelamin = st.selectbox("Pilih jenis kelamin", ["Laki-laki", "Perempuan"])
    submit_button = st.form_submit_button(label="kirim")