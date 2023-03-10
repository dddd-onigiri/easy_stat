import streamlit as st

st.set_page_config(page_title="ブラウザ統計", layout="wide")

st.title("ブラウザ統計")
st.caption("Created by Daiki Ito")
st.write("")
st.subheader("ブラウザで統計を行うことができるウェブアプリです。")
st.write("iPad等で分析を行うことができます")
st.write("")

st.write("実装済み検定")
st.write("・相関分析")
st.write("・ｔ検定（対応なし）")
st.write("・ｔ検定（対応あり）")
st.write("")
st.write("")
st.write("2023/03/11")
st.write("　相関分析を実装しました。")
st.write("")
st.write("2023/03/06")
st.write("　ｔ検定（対応あり・なし）を統合しました。")

st.write("")
st.write("")
st.write('ご意見・ご要望は→', 'https://forms.gle/G5sMYm7dNpz2FQtU9', 'まで')
st.write('© 2022-2023 Daiki Ito. All Rights Reserved.')
