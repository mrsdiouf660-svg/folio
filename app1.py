import streamlit as st
st.header ("collecter les points x, y, z,")
x= st.number_input("x")
y= st.number_input("y")
z= st.number_input("z")
if st.button("résultat"):
    somme =x+y+z
    st.write(somme)