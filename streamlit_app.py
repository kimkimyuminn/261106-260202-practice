import streamlit as st

st.set_page_config(
    page_title="나를 소개합니다",
    page_icon="🌿",
    layout="wide",
)

# 이 값들을 바꾸면 자기소개 내용을 손쉽게 수정할 수 있습니다.
PROFILE_NAME = "김유민"
PROFILE_TAGLINE = "좋아하는 것을 발견하고, 경험 속에서 배우는 사람"
PROFILE_INTRO = (
    "나를 설명하는 문장을 적어보세요. 관심사와 성격, 요즘 중요하게 생각하는 것을 "
    "편안한 말투로 소개하면 좋습니다."
)

PROFILE_DETAILS = [
    ("관심 키워드", "과외 수업 준비하기"),
    ("나를 설명하는 단어", "낙천적 · 긍정"),
    ("요즘의 관심사", "드라마 보기"),
]

FAVORITES = [
    ("드라마", [("가금채", "좋아하는 이유나 기억에 남는 장면")]),
    ("영화", [("인생은 아름다워", "좋아하는 이유나 오래 남은 대사")]),
    ("책", [("톰 소여의 모험", "인상 깊었던 문장이나 읽고 난 생각")]),
    ("음악", [("토리켈리의 25th", "이 음악을 즐겨 듣는 순간")]),
    ("음식", [("삼계탕", "좋아하게 된 계기나 추천하는 조합")]),
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
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 0.7rem;
        border-bottom: 0;
        margin: 1.75rem 0 2rem;
    }

    button[data-baseweb="tab"] {
        min-height: 3.8rem;
        justify-content: flex-start;
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid var(--line);
        border-radius: 6px;
        color: var(--ink);
        font-size: 1rem;
        font-weight: 650;
        padding: 0.9rem 1rem;
        transition: background-color 160ms ease, border-color 160ms ease, color 160ms ease;
    }

    button[data-baseweb="tab"]::before {
        color: var(--coral);
        font-size: 0.72rem;
        font-weight: 700;
        margin-right: 0.7rem;
    }

    button[data-baseweb="tab"]:nth-child(1)::before { content: "01"; }
    button[data-baseweb="tab"]:nth-child(2)::before { content: "02"; }
    button[data-baseweb="tab"]:nth-child(3)::before { content: "03"; }
    button[data-baseweb="tab"]:nth-child(4)::before { content: "04"; }

    button[data-baseweb="tab"]:hover {
        background: var(--white);
        border-color: var(--green);
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: var(--green);
        border-color: var(--green);
        color: var(--white);
    }

    button[data-baseweb="tab"][aria-selected="true"]::before {
        color: #e8c9b9;
    }

    [data-testid="stCaptionContainer"] { color: var(--muted); }

    @media (max-width: 700px) {
        .hero { grid-template-columns: 1fr; gap: 1.5rem; padding-top: 1rem; }
        .hero h1 { font-size: 2.25rem; }
        div[data-baseweb="tab-list"] {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.55rem;
        }
        button[data-baseweb="tab"] {
            min-height: 3.4rem;
            font-size: 0.88rem;
            padding: 0.7rem;
        }
        button[data-baseweb="tab"]::before { margin-right: 0.45rem; }
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
