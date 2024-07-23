import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 검색창 
title = st.text_input("애니메이션")


# 입력창에서 데이터를 받아서 
for i in range(len(ani_list)):
    if title==ani_list[i]:
        st.image(img_list[i])

        st.download_button(
            label="Download image",
            data=img_list[i],
            file_name=title
        )