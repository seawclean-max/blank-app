import streamlit as st

st.title("🎈 你好，欢迎来到小应用")
st.write("在下面输入名字，再点「打招呼」。这是页面上唯一的小互动。")

name = st.text_input("你的名字", placeholder="例如：Jon")

if st.button("打招呼"):
    if name.strip():
        st.success(f"你好，{name.strip()}！很高兴见到你。")
    else:
        st.info("先在上面写一个名字，再点按钮。")
