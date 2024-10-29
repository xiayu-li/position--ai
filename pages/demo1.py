import streamlit as st
from  langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from  langchain.prompts import  PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
# st.title("AI demo小程序!!!!")
model = ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="7651a1fbab6fe9ee0526d4f9e9cc20bb.TAg4eZgUODyOZCfp"
)
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
prompt = PromptTemplate.from_template("你叫柳如烟,你现在扮演的是一个女朋友的角色,你需要和你的男朋友对话,不需要回答其它的,你男朋友说的话是{input}")
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory
)

st.title("女朋友柳如烟")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
problem = st.chat_input("你的柳如烟正在等待你的回应")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role":"user","content":problem})
        result = chain.invoke({"input":problem})
    with st.chat_message("assistant"):
        st.write(result['text'])
        st.session_state.cache.append({"role":"assistant","content":result['text']})