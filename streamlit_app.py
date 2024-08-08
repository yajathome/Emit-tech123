import streamlit as st
a="KA 06 1234"
b="72.5"
st.html("<h1 style='font-size:100px;text-align:center;background-color:#04336b;border-radius:20px;'>Emi-tech</h1>")
st.subheader("Number Plate")
st.write(a)
st.divider()
st.subheader("Aqi level")
st.write(b)
st.markdown('''<style>
                .st-emotion-cache-1sno8jx p{
                    word-break: break-word;
                    font-size: 90px;
                    }
                .st-emotion-cache-1v1dp7g p {
                    word-break: break-word;
                    font-size: 90px;
                    }
            </style>''',unsafe_allow_html=True)
