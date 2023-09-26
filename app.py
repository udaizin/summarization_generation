# 以下を「app.py」に書き込み
import streamlit as st
from model import summarization_predict

st.set_option("deprecation.showfileUploaderEncoding", False)

st.sidebar.title("ニュース記事の見出し作成アプリ")
st.sidebar.write("ニュース記事の内容をもとに適切な見出しを作成します。")

st.sidebar.write("")

st.sidebar.write("右の枠にニュースの中身を入力してくだいさい。")

content = st.text_area(
    'ニュースの中身',  max_chars=3000
)

button = st.button("見出し生成開始")
if button and content is not None:
    with st.spinner("推定中..."):
        summaries = summarization_predict(content)
        st.text_area(
            'ニュースの見出し候補',
            value=f'候補①:{summaries[0]}\n候補②:{summaries[1]}\n候補③:{summaries[2]}\n',
            height=300
        )
