import streamlit as st
import pandas as pd
df= pd.read_csv(r"C:\Users\anirudh\Desktop\MACHINE LEARNING\Heart-disease-prediction\framingham.csv")
st.write('''
hello everyone
         ''')
# st.dataframe(df)
# st.table(df.iloc[0:5])
st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
st.metric('My metric', 42, 2)
x=st.radio('select your age:',[20,50])

if x==20:
    st.write('young')
else:
    st.write('old')

# a = st.sidebar.radio('Select one:', [1, 2])
# with st.sidebar:
#    st.radio('Select one:', [1, 2])
y=st.button('Click me')
if y:
    st.write('submit')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
# st.download_button('Download file',data=csv)
st.camera_input("Take a picture")
st.color_picker('Pick a color')

