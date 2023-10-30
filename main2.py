# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()
st.balloons()
st.title('AI fortune teller')

content = st.text_input('묻고싶은 내용을 입력하세요')
st.text('원하는 답변이 아니면 버튼을 다시 눌러주세요')
# result = chat_model.predict(content + "국악가사를 써줘")
# print(result)

if st.button("답해줘"):
   with st.spinner('작성중...'):
      result = chat_model.predict(content)
      st.write(result) 
st.image('https://oasisbpartners.netlify.app/assets/images/resources/logo.png')
#st.link_button("Go to Roar Festival", "http://daroousa.com/en/bbs/board.php?bo_table=en_w4_c&wr_id=1")
