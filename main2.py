# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.balloons()
st.title('AI fortune teller')

content = st.text_input('Please enter your date of birth or your zodiac sign of birth.')
st.text("**If it's not the answer you want, press the button again.**")
# result = chat_model.predict(content + "국악가사를 써줘")
# print(result)

if st.button("Tell me today's horoscope"):
   with st.spinner('frotune-telling...'):
      result = chat_model.predict('date of birth or zodiac sign of birth' + content + '의 별자리 오늘 운세 영문으로')
      st.write(result) 
st.image('http://daroousa.com/en/theme/basic/img/w4/w4_1_1.png')
st.link_button("Go to Roar Festival", "http://daroousa.com/en/bbs/board.php?bo_table=en_w4_c&wr_id=1")
