import streamlit as st

x = ['a','b','c']
y = [4,5.5,6]
data = {'tag':x,'valor':y}
media = sum(y)/len(y)

st.title('Exemplo')
coluna_1, coluna_2 = st.columns(2)

with coluna_1:
    st.bar_chart(data=data,x='tag',y='valor')
with coluna_2:
    st.metric(label='Média',value=media)