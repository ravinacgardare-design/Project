import streamlit as st

st.title(" Recommendation Product ")
st.subheader("Bresed with streamlit")
st.text("Welcome to your first Recommendation Product")
st.write("choose your fav. Product")

product=st.selectbox("select your product :",["select","hp","dell","lenovo","boat","phone"])

st.write(f"your choose {product}. Excellent choise")

st.success("best")

if st.button("Press"):
    st.success("best of luck")


add_masala=st.checkbox("add suggestion")

if add_masala:
    st.write("masala added to your chai")

tea_type=st.radio("pick your chai base:",["milk", "water", "almond Mill"])
st.write(f"selected base {tea_type}")

flavour=st.selectbox("choose flavour:",["adrak","kesar","Tulsi"])
st.write(f"selected flavour {flavour}")

