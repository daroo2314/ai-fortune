# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.balloons()
st.title("Jenny's AI fortune teller")

content = st.text_input('Please enter your date of birth"(yyyy-mm-dd)"')
st.text('If the answer you want is not correct, please press the button again.')
result = chat_model.predict("생년월일이" + content+ "인데 오늘의 운세를 말해줘 '당신의 오늘의 운세는'으로 시작하는 문장으로 영어로 번역해서 답해줘")
# print(result)

if st.button("Tell me please"):
   with st.spinner('Reading the fortune...'):
      result = chat_model.predict(content)
      st.write(result) 
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRabYvzb-gX147vBNH-entQ4v6hkwnydLPsC0qepYtIua0eNBhmpEc_REG1WEcckFlVYmI&usqp=CAU')
#st.link_button("Go to Roar Festival", "http://daroousa.com/en/bbs/board.php?bo_table=en_w4_c&wr_id=1")
