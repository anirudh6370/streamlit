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