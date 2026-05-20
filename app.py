import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="맛집 찾기 앱",
    page_icon="🍜",
    layout="centered"
)

# 샘플 데이터
restaurants = [
    {
        "이름": "홍콩반점",
        "지역": "서울",
        "메뉴": "중식",
        "평점": 4.3
    },
    {
        "이름": "교촌치킨",
        "지역": "인천",
        "메뉴": "치킨",
        "평점": 4.5
    },
    {
        "이름": "이삭토스트",
        "지역": "부산",
        "메뉴": "토스트",
        "평점": 4.1
    },
    {
        "이름": "한솥도시락",
        "지역": "대전",
        "메뉴": "도시락",
        "평점": 4.0
    }
]

# 데이터프레임 생성
df = pd.DataFrame(restaurants)

# 제목
st.title("🍜 맛집 찾기 앱")

st.write("지역과 메뉴로 맛집을 검색해보세요.")

# 검색 UI
region = st.selectbox(
    "지역 선택",
    ["전체"] + sorted(df["지역"].unique().tolist())
)

menu = st.text_input("메뉴 검색", placeholder="예: 치킨")

# 필터링
filtered_df = df.copy()

if region != "전체":
    filtered_df = filtered_df[
        filtered_df["지역"] == region
    ]

if menu:
    filtered_df = filtered_df[
        filtered_df["메뉴"].str.contains(menu, case=False)
    ]

# 결과 출력
st.subheader("검색 결과")

if len(filtered_df) == 0:
    st.warning("검색 결과가 없습니다.")
else:
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# 하단 정보
st.caption("간단한 Streamlit 맛집 앱 예제")
