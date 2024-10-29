import  streamlit as st
st.title("AI大模型应用产品网")

c1,c2 = st.columns(2)
with c1:
    # st.image("logo.png", use_column_width=True)
    flag = st.button("基础版",use_container_width=True)
    if flag:
        st.switch_page("pages/demo1.py")
with c2:
    # st.image("logo.png", use_column_width=True)
    flag1 = st.button("最终版",use_container_width=True)
    if flag1:
        st.switch_page("pages/text.py")
