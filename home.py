# home.py — Streamlit Portfolio (clean + consistent cards)

import base64
import os
from textwrap import dedent

import streamlit as st

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Anssoumane Sissokho — Portfolio",
    page_icon="📊",
    layout="wide",
)

# ---------------------------
# Small helpers
# ---------------------------
def img_b64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def mime_from_ext(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext in [".png"]:
        return "png"
    if ext in [".jpg", ".jpeg", ".webp"]:
        return "jpeg"
    return "png"

# Global CSS (typography + pills + socials)
st.markdown(dedent("""
<style>
.stApp { background:#ffffff; color:#111; }

/* round profile photo */
.profile-img { width:100%; max-width:420px; border-radius:50%;
  box-shadow:0 10px 28px rgba(0,0,0,0.12); }

/* header type */
.hello { color:#6b6b6b; font-size:16px; margin-bottom:6px; }
.name  { font-size:52px; line-height:1.1; margin:0 0 6px 0; font-weight:800; }
.role  { font-size:24px; color:#6b6b6b; font-weight:700; margin-bottom:18px; }

/* pill buttons */
.pills { display:flex; gap:16px; margin:22px 0 6px 0; flex-wrap:wrap; justify-content:center; }
.pill-btn { display:inline-block; width:190px; text-align:center; padding:12px 20px;
  border:2px solid #111; border-radius:999px; background:#fff; color:#111 !important;
  font-weight:700; text-decoration:none; transition:all .2s ease; }
.pill-btn:hover { background:#111; color:#fff !important; }
.pill-btn.dark { background:#111; color:#fff !important; }
.pill-btn.dark:hover { background:#000; }

/* socials */
.socials { display:flex; gap:24px; margin-top:14px; justify-content:center; }
.socials img { width:30px; height:30px; display:block; }

/* portfolio cards (uniform & centered) */
.pf-card { box-sizing:border-box; border:1px solid #ddd; border-radius:16px; background:#fff;
  padding:16px; height:360px; display:flex; flex-direction:column; justify-content:space-between;
  align-items:center; text-align:center; }
.pf-img { max-width:100%; max-height:160px; object-fit:contain; border-radius:12px; display:block; }
.pf-title { font-weight:800; font-size:18px; margin:8px 0 4px; }
.pf-desc { color:#555; font-size:14px; margin:0 6px 10px; }
.pf-btnrow { display:flex; gap:10px; flex-wrap:wrap; justify-content:center; }
.pf-pill { border:2px solid #111; border-radius:999px; padding:8px 14px; text-decoration:none;
  color:#111; font-weight:700; }
.pf-pill:hover { background:#111; color:#fff; }

/*
.social-icon {
  width: 40px;
  height: 40px;
  object-fit: contain;
}*/

</style>
"""), unsafe_allow_html=True)

# ---------------------------
# Header (photo left, centered text + flags in buttons)
# ---------------------------
photo_b64    = img_b64("assets/photo_website.jpg")
linkedin_b64 = img_b64("assets/linkedin.png")
github_b64   = img_b64("assets/github.png")
medium_b64   = img_b64("assets/medium_logo.gif")
flag_fr_b64  = img_b64("assets/flag-fr.png")
flag_uk_b64  = img_b64("assets/flag-uk.png")

with st.container():
    left, right = st.columns([1, 2], gap="large")

    with left:
        st.markdown(
            f"<img src='data:image/png;base64,{photo_b64}' class='profile-img' alt='Profile'/>",
            unsafe_allow_html=True
        )

    html_right = f"""
<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100%; text-align:center;">
  <div class='hello'>Hello, I'm</div>
  <div class='name'>Anssoumane Sissokho</div>
  <div class='role'>Data Product Owner</div>

  <div class="pills">
    <a class='pill-btn' href='assets/CV_Anssoumane_SISSOKHO_FR.pdf' download>
      <img src='data:image/png;base64,{flag_fr_b64}' style='width:18px;height:18px;vertical-align:middle;margin-right:6px;'/>
      CV
    </a>
    <a class='pill-btn' href='assets/CV_DPO_Anssoumane_SISSOKHO_EN.pdf' download>
      <img src='data:image/png;base64,{flag_uk_b64}' style='width:18px;height:18px;vertical-align:middle;margin-right:6px;'/>
      Résumé
    </a>
    <a class='pill-btn dark' href='mailto:anssoumane.sissokho@gmail.com'>Contact Info</a>
  </div>

  <div class="socials">
  <a href='https://www.linkedin.com/in/anssoumane-sissokho/' target='_blank'>
    <img src='data:image/png;base64,{linkedin_b64}' alt='LinkedIn' class="social-icon"/>
  </a>
  <a href='https://github.com/anssoumane14' target='_blank'>
    <img src='data:image/png;base64,{github_b64}' alt='GitHub' class="social-icon"/>
  </a>
  <a href='https://medium.com/@anssoumane.sissokho' target='_blank'>
    <img src='data:image/png;base64,{medium_b64}' alt='Medium' class="social-icon"/>
  </a>
</div>

</div>
"""

    with right:
        st.markdown(dedent(html_right), unsafe_allow_html=True)

# white space under header
st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------
# One simple card helper (uniform size, centered)
# ---------------------------
def portfolio_card(
    title: str,
    img_path: str | None = None,
    description: str = "",
    buttons: list[tuple[str, str]] | None = None,  # [(label, url), ...]
    height: int = 360,
    image_max_height: int = 160,
):
    img_html = ""
    if img_path:
        mime = mime_from_ext(img_path)
        b64  = img_b64(img_path)
        img_html = (
            f"<img class='pf-img' style='max-height:{image_max_height}px;' "
            f"src='data:image/{mime};base64,{b64}'/>"
        )

    btns_html = ""
    if buttons:
        btns_html = "".join(
            f"<a class='pf-pill' href='{url}' target='_blank'>{label}</a>"
            for (label, url) in buttons
        )

    st.markdown(dedent(f"""
    <div class="pf-card" style="height:{height}px">
      {img_html}
      <div class="pf-title">{title}</div>
      <div class="pf-desc">{description}</div>
      <div class="pf-btnrow">{btns_html}</div>
    </div>
    """), unsafe_allow_html=True)

# ---------------------------
# Tabs
# ---------------------------
exp_tab, proj_tab, art_tab, edu_tab, contact_tab = st.tabs(
    ["Experience", "Projects", "Articles", "Education", "Contact"]
)

# Experience (logos → smaller image area, slightly shorter cards)
with exp_tab:
    st.subheader("Experience")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        portfolio_card(
            title="L’Oréal — Data Product Owner",
            img_path="assets/loreal-logo.png",
            description="Industrialized end‑to‑end Power BI with GCP/BigQuery, RLS, and a non‑prod → test → prod pipeline.",
            buttons=[("See more", "#")],
            height=320,
            image_max_height=120,
        )
    with c2:
        portfolio_card(
            title="Alter’Actions — Strategic Consultant",
            img_path="assets/alteractions-logo.png",
            description="Designed a new equipment rental activity for an NGO: interviews, benchmark, SWOT, and recommendations.",
            buttons=[("See more", "#")],
            height=320,
            image_max_height=120,
        )

# Projects (screenshots → taller cards)
with proj_tab:
    st.subheader("Projects")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        portfolio_card(
            title="Telecom Customer Churn Analysis",
            img_path="assets/churn_project_img.webp",
            description="Churn analysis + segmentation to drive retention actions.",
            buttons=[("Read more", "https://github.com/"),
                     ("GitHub", "https://github.com/anssoumane14/Telecom-Customer-Churn")],
            height=380,
            image_max_height=160,
        )
    with c2:
        portfolio_card(
            title="Nba Analytics",
            img_path="assets/nba.png",
            description="Nba analytics app.",
            buttons=[("Read more", "#"),
                     ("GitHub", "https://github.com/anssoumane14/nba_analytics")],
            height=380,
            image_max_height=160,
        )
    

# Articles
with art_tab:
    st.subheader("Articles")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        portfolio_card(
            title="How to Implement a Star Schema",
            img_path="assets/star-schema.png",
            description="A step‑by‑step guide to clean star schemas for Power BI/SQL beginners.",
            buttons=[("Read article", "https://medium.com/@anssoumane.sissokho/star-schema-tutorial")],
            height=340,
            image_max_height=140,
        )
    with c2:
        portfolio_card(
            title="Scraping the NBA Universe",
            img_path="assets/nba.png",
            description="Extract Basketball‑Reference data with Python and build a mini analysis pipeline.",
            buttons=[("Read article", "https://medium.com/@anssoumane.sissokho/nba-scraping-tutorial")],
            height=340,
            image_max_height=140,
        )

# Education
with edu_tab:
    st.subheader("Education")
    c1, c2 = st.columns(2, gap="large")
    with c1 : 
        portfolio_card(
            title="Master's — Computer Science & Business Strategy",
            img_path="assets/upc.jpg",
            description="Université Paris Cité — Data engineering, BI, digital strategy.",
            buttons=[("See more", "#")],
            height=300,
            image_max_height=120,
        )

    with c2 : 
        portfolio_card(
            title="Bachelor's — Economics",
            img_path="assets/sorbonne.png",
            description="Université Paris 1 Panthéon Sorbonne — Theory, statistics, econometrics.",
            buttons=[("See more", "#")],
            height=300,
            image_max_height=120,
        )

# Contact
with contact_tab:
    st.subheader("Get in Touch — Don't Be Shy")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Email**")
        st.link_button("anssoumane.sissokho@gmail.com", "mailto:anssoumane.sissokho@gmail.com")
    with col2:
        st.write("**Phone**")
        st.write("+33 6 01 86 45 46")
