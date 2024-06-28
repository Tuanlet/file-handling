import streamlit as st
import pandas as pd

st.subheader('UPloading the CSV file')

df = st.file_uploader("Upload the CSV file : ", type = ['csv', 'xlsx'])

if df is not None: 
    st.dataframe(df)

st.subheader('Loading the CSV file')
df = pd.read_csv('C:\\Users\\aska5\\pythonworks,\\Products.csv')
if df is not None:
    st.table(df.head())

st.subheader('Dealing with images')
st.image('\\Users\\aska5\\pythonworks,\\img.png')

img_file = img = st.file_uploader("upload image file: ", type = ['png', 'jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader('Working with videos')
vid_file = img = st.file_uploader("upload video file: ", type = ['mkv', 'mp4'])
if vid_file is not None:
    st,video(vid_file, start_time = 5)


st.subheader('Working with Audio')
aud_file = img = st.file_uploader("upload audio file: ", type = ['wav', 'mp3'])
if aud_file is not None:
    st,audio(aud_file)