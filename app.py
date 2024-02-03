import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from config import OPENAI_API_KEY

st.set_page_config(page_title="Rap Soul", page_icon=":shushing_face:", layout="wide")

# Utils 
def moye():
        audio_file = open('./assets/moye-moye.mp3', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/ogg')
        st.write(":gray[Sorry! Autoplay feature isn't supported in Streamlit yet!!] :confused:")

# Header
with st.container():
    st.header("Rap battle between Good Soul :angel: and Bad Soul :imp:")
    st.write("##")
    st.write(":gray[Disclaimer: Good soul always wins!!!] :clap:")

title = st.text_input('Type any query to start the battle!', '')

# Battleground
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2, gap="large")
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    output_parser = StrOutputParser()
    chk = 0

    with left_column:
        st.subheader("Bad soul :imp:")
        if (title != ''):
            with st.spinner('Cooking the Rap!!!'):
                prompt = ChatPromptTemplate.from_template("Give a negative and insultful Rap to {topic} [Rap Battle] (Keep it consice)")
                chain = prompt | model | output_parser

                temp = chain.invoke({"topic": title})
                print(temp)
                st.write(temp)   
                
    
    with right_column:
        st.subheader("Good Soul :angel:")

        if (title != '' and temp != '') :
            with st.spinner('Replying!!!'):
                prompt = ChatPromptTemplate.from_template("Give a positive and motivational reply as a Rap to {topic} [Rap Battle] (Keep it consice)")
                chain = prompt | model | output_parser

                reply = chain.invoke({"topic": temp})
                print(reply)
                st.write(reply)
                st.success("Good Soul :angel: has won the battle!!! :clap:")
                chk = 1
    
    with left_column:
        if (chk):
            st.error("Bad Soul :imp: has lost the battle!!!")
            moye()
