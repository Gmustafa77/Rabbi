import streamlit as st
from content import HUSBAND, WIFE, QUALITIES, TABLE, LETTER

st.set_page_config(page_title=f"{WIFE}, by {HUSBAND}", page_icon="❤️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Nunito+Sans:wght@400;600&display=swap');
html, body, [class*="css"], .stMarkdown p { font-family: 'Nunito Sans', sans-serif; }
h1, h2, h3, .serif { font-family: 'Cormorant Garamond', serif !important; }
.hero { padding: 2rem 0 .5rem; }
.hero h1 { font-size: clamp(3.5rem, 14vw, 6.5rem); color: #A4325B; margin: 0; line-height: .95; font-weight: 700; }
.hero p { font-size: 1.15rem; color: inherit; opacity: .75; margin: .8rem 0 0; }
.intro { color: inherit; font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; line-height: 1.35; margin: 1rem 0 1.2rem; }
.line { padding: .55rem 0; border-bottom: 1px solid rgba(128,128,128,.35); font-size: 1.05rem; }
.truth { border-left: 4px solid #A4325B; background: rgba(164,50,91,.12); color: inherit; padding: .9rem 1.2rem; margin-top: 1.4rem;
         font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; line-height: 1.35; }
.letter p { color: inherit; font-family: 'Cormorant Garamond', serif; font-size: 1.35rem; line-height: 1.6; max-width: 38rem; }
.sign { font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; color: #D4608A; margin-top: 1.5rem; }
#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""<div class="hero"><h1>{WIFE}</h1>
<p>Described by her husband, {HUSBAND}</p></div>""", unsafe_allow_html=True)

titles = [q[0] for q in QUALITIES]
if "pick" not in st.session_state:
    st.session_state.pick = titles[0]

def step(delta):
    i = titles.index(st.session_state.pick)
    st.session_state.pick = titles[(i + delta) % len(titles)]

tab1, tab2, tab3 = st.tabs(["Her qualities", "At a glance", f"{HUSBAND}'s letter"])

with tab1:
    st.selectbox("Choose a quality", titles, key="pick")
    title, intro, lines, truth = QUALITIES[titles.index(st.session_state.pick)]
    st.markdown(f"## {title}")
    st.markdown(f'<div class="intro">{intro}</div>', unsafe_allow_html=True)
    for l in lines:
        st.markdown(f'<div class="line">{l}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="truth">{truth}</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 2])
    c1.button("Previous", on_click=step, args=(-1,), use_container_width=True)
    c2.button("Next", on_click=step, args=(1,), use_container_width=True)
    c3.caption(f"{titles.index(st.session_state.pick) + 1} of {len(titles)}")

with tab2:
    st.markdown(f"## What {HUSBAND} treasures in {WIFE}")
    q = st.text_input("Search", placeholder="Try: honesty")
    rows = {k: v for k, v in TABLE.items() if q.lower() in (k + v).lower()}
    if rows:
        st.table({"Quality": list(rows.keys()), "What he appreciates": list(rows.values())})
    else:
        st.info("No match. Try a different word.")

with tab3:
    st.markdown('<div class="letter">' + "".join(f"<p>{p.format(w=WIFE)}</p>" for p in LETTER) + "</div>",
                unsafe_allow_html=True)
    st.markdown(f'<div class="sign">With love, {HUSBAND}</div>', unsafe_allow_html=True)
    if st.button(f"Send {WIFE} a hug"):
        st.balloons()