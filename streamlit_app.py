import streamlit as st
import cv2
st.set_page_config(layout="wide")
st.html("<h1 style='font-size:100px;text-align:center;background-color:#04336b;border-radius:20px;'>Emi-tech</h1>")
st.subheader("Number Plate")
st.write("ka 60 1234")
st.divider()
st.subheader("Aqi level")
st.write(72.5)
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
a=st.button("picture")
if a:
  cam = cv2.VideoCapture(0)
  if not cam.isOpened():
      print("Error: Could not open camera.")
      exit()
  result, image = cam.read()
  if result:
      cv2.imshow("GeeksForGeeks", image)
      cv2.imwrite("GeeksForGeeks.png", image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
  else:
      print("No image detected. Please try again.")
