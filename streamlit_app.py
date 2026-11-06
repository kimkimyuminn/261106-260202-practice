import streamlit as st

st.set_page_config(
    page_title="나를 소개합니다",
    page_icon="🌿",
    layout="wide",
)

# 이 값들을 바꾸면 자기소개 내용을 손쉽게 수정할 수 있습니다.
PROFILE_NAME = "이름을 입력하세요"
PROFILE_TAGLINE = "좋아하는 것을 발견하고, 경험 속에서 배우는 사람"
PROFILE_INTRO = (
    "나를 설명하는 문장을 적어보세요. 관심사와 성격, 요즘 중요하게 생각하는 것을 "
    "편안한 말투로 소개하면 좋습니다."
)

PROFILE_DETAILS = [
    ("관심 키워드", "관심 있는 주제를 적어보세요"),
    ("나를 설명하는 단어", "나를 잘 나타내는 단어를 적어보세요"),
    ("요즘의 관심사", "요즘 자주 생각하거나 찾아보는 것을 적어보세요"),
]

FAVORITES = [
    ("드라마", [("드라마 제목", "좋아하는 이유나 기억에 남는 장면")]),
    ("영화", [("영화 제목", "좋아하는 이유나 오래 남은 대사")]),
    ("책", [("책 제목 · 작가", "인상 깊었던 문장이나 읽고 난 생각")]),
    ("음악", [("곡 또는 아티스트", "이 음악을 즐겨 듣는 순간")]),
    ("음식", [("좋아하는 음식", "좋아하게 된 계기나 추천하는 조합")]),
]

SCHOOL_ACTIVITIES = [
    {"title": "활동 이름", "body": "참여한 이유, 맡은 역할, 기억에 남는 순간을 적어보세요."},
]

PRACTICES = [
    {"title": "실습 주제", "body": "실습에서 해본 일과 새롭게 익힌 점을 적어보세요."},
]

REFLECTIONS = [
    {
        "title": "오늘의 성찰",
        "date": "날짜를 입력하세요",
        "body": "오늘 배운 점, 잘한 점, 다음에 다르게 해보고 싶은 점을 적어보세요.",
    },
]

FUTURE_LEARNING = [
    {"title": "배우고 싶은 것", "body": "앞으로 더 알아가고 싶은 분야나 기술을 적어보세요."},
]

GROWTH_METHODS = [
    {"title": "작은 실천", "body": "꾸준히 이어가고 싶은 습관이나 나를 돌보는 방법을 적어보세요."},
]

st.markdown(
    """
    <style>
    :root {
        --paper: #f4f7f5;
        --ink: #20342e;
        --muted: #64736d;
        --line: #d7e1dc;
        --green: #537c6c;
        --coral: #b66c55;
        --white: #ffffff;
    }

    .stApp {
        background-color: var(--paper);
        background-image:
            linear-gradient(rgba(49, 79, 66, 0.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(49, 79, 66, 0.025) 1px, transparent 1px);
        background-size: 36px 36px;
        color: var(--ink);
    }

    [data-testid="stHeader"] { background: transparent; }
    .block-container {
        max-width: 1080px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: var(--ink);
        font-family: "Noto Serif KR", "Batang", Georgia, serif;
        letter-spacing: 0;
    }

    .hero {
        display: grid;
        grid-template-columns: minmax(0, 1.5fr) minmax(220px, 0.7fr);
        gap: 3rem;
        align-items: end;
        padding: 2rem 0 2.5rem;
        border-bottom: 1px solid var(--line);
    }

    .eyebrow, .hero-note-label, .section-label, .category-label {
        color: var(--green);
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.08em;
    }

    .hero h1 {
        margin: 1rem 0 0.75rem;
        font-size: clamp(2.25rem, 3.2rem, 3.2rem);
        line-height: 1.35;
        font-weight: 500;
    }

    .hero h1 span { color: var(--green); }
    .hero-lead { color: var(--muted); font-size: 1.05rem; }

    .hero-note {
        border-left: 2px solid var(--coral);
        padding: 0.25rem 0 0.25rem 1.25rem;
    }

    .hero-note p {
        color: var(--muted);
        line-height: 1.8;
        margin: 0.65rem 0 0;
    }

    .section-label { margin: 0 0 0.5rem; }
    .category-label { margin: 1.5rem 0 0.5rem; }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.82);
        border-color: var(--line);
        border-radius: 6px;
        box-shadow: none;
    }

    div[data-baseweb="tab-list"] {
        gap: 1.5rem;
        border-bottom: 1px solid var(--line);
    }

    button[data-baseweb="tab"] {
        color: var(--muted);
        font-size: 0.98rem;
        padding: 0.8rem 0.15rem;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: var(--ink);
        border-bottom-color: var(--green);
    }

    [data-testid="stCaptionContainer"] { color: var(--muted); }

    @media (max-width: 700px) {
        .hero { grid-template-columns: 1fr; gap: 1.5rem; padding-top: 1rem; }
        .hero h1 { font-size: 2.25rem; }
        div[data-baseweb="tab-list"] { gap: 0.7rem; }
        button[data-baseweb="tab"] { font-size: 0.88rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="hero">
        <div>
            <div class="eyebrow">PERSONAL PROFILE &nbsp; / &nbsp; ABOUT ME</div>
            <h1>안녕하세요,<br><span>{PROFILE_NAME}</span>입니다.</h1>
            <p class="hero-lead">{PROFILE_TAGLINE}</p>
        </div>
        <div class="hero-note">
            <div class="hero-note-label">A LITTLE ABOUT ME</div>
            <p>{PROFILE_INTRO}</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


def render_entries(entries):
    for entry in entries:
        with st.container(border=True):
            if entry.get("date"):
                st.caption(entry["date"])
            st.markdown(f"#### {entry['title']}")
            st.write(entry["body"])


profile_tab, favorites_tab, records_tab, growth_tab = st.tabs(
    ["프로필", "좋아하는 것", "활동과 기록", "앞으로의 성장"]
)

with profile_tab:
    st.markdown('<p class="section-label">01 / PROFILE</p>', unsafe_allow_html=True)
    st.subheader("나에 대해")
    st.write(PROFILE_INTRO)

    detail_columns = st.columns(3)
    for column, (label, value) in zip(detail_columns, PROFILE_DETAILS):
        with column:
            with st.container(border=True):
                st.caption(label)
                st.markdown(f"#### {value}")

with favorites_tab:
    st.markdown('<p class="section-label">02 / FAVORITES</p>', unsafe_allow_html=True)
    st.subheader("내가 좋아하는 것")
    st.write("작은 취향들이 모여 지금의 나를 만듭니다.")

    for start in range(0, len(FAVORITES), 2):
        columns = st.columns(2)
        for column, (category, items) in zip(columns, FAVORITES[start:start + 2]):
            with column:
                st.markdown(f'<p class="category-label">{category}</p>', unsafe_allow_html=True)
                for title, note in items:
                    with st.container(border=True):
                        st.markdown(f"#### {title}")
                        st.write(note)

with records_tab:
    st.markdown('<p class="section-label">03 / EXPERIENCES</p>', unsafe_allow_html=True)
    st.subheader("학교 활동")
    render_entries(SCHOOL_ACTIVITIES)

    st.divider()
    st.subheader("실습")
    render_entries(PRACTICES)

    st.divider()
    st.subheader("성찰 일기")
    render_entries(REFLECTIONS)

with growth_tab:
    st.markdown('<p class="section-label">04 / WHAT IS NEXT</p>', unsafe_allow_html=True)
    st.subheader("앞으로 배우고 싶은 것")
    render_entries(FUTURE_LEARNING)

    st.divider()
    st.subheader("나를 계발하는 방법")
    render_entries(GROWTH_METHODS)

st.markdown(
    "<p style='text-align:center; color:#64736d; padding-top:2rem;'>천천히 채워가는 나의 기록</p>",
    unsafe_allow_html=True,
)
