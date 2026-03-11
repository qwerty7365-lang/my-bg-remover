import streamlit as st
from rembg import remove
from PIL import Image
import io

# 페이지 설정
st.set_page_config(page_title="AI 배경 제거기", page_icon="✂️")

st.title("✂️ AI 이미지 배경 제거기")
st.write("이미지를 업로드하면 AI가 배경을 깨끗하게 지워드립니다!")

# 파일 업로더
uploaded_file = st.file_uploader("이미지를 선택하세요 (jpg, png, jpeg)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 이미지 불러오기
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("원본 이미지")
        st.image(image, use_container_width=True)
        
    with st.spinner("배경을 제거하는 중입니다... 잠시만 기다려 주세요."):
        # 배경 제거 처리
        result = remove(image)
        
        # 다운로드 버튼을 위한 이미지 변환
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
    with col2:
        st.subheader("제거 결과")
        st.image(result, use_container_width=True)
        
        # 다운로드 버튼
        st.download_button(
            label="결과 이미지 다운로드",
            data=byte_im,
            file_name="removed_bg.png",
            mime="image/png"
        )
