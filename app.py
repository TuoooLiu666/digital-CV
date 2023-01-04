from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tuo Liu"
PAGE_ICON = ":v:"
NAME = "Tuo Liu"
DESCRIPTION = """
Ph.D. student major in Environmental Health Sciences, minor in Biostatistics, at the University of Arizona,
studying and practising metabolomics.
"""

EMAIL = "tuoooliu@arizona.edu"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/tuo-l-491782194/",
    "GitHub": "https://github.com/TuoooLiu666",
    "Website": "https://tuo-liu.netlify.app"
}

PROJECTS = {
    "🏆 Expense Tracker - A web app with NoSQL database, Streamlit, and Python": "https://tuoooliu666-expense-tracker-app-t5a7ro.streamlit.app/",
    "🏆 Arizona Pesticide Use - A web app built with Flexboard, Shiny, and R": "https://tuoliu.shinyapps.io/Metabolomics_QC-EDA_APP/",
    "🏆 Exploring Neighborhoods - Chinese Restaurants in Toronto, Python": "https://www.linkedin.com/pulse/exploring-neighborhoods-chinese-restaurants-toronto-tuo-liu/?trackingId=tM10bHWKQ56%2Bknl2IqrG2g%3D%3D",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    
    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 Years expereince extracting publishable insights from experiment& survey data
- ✔️ Solid understanding of statistical grond and biostatistical applications
- ✔️ Strong hands on experience and knowledge in R & Python
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: R, Python, SQL
- 📊 Data Visulization: ggplot2, Shiny, Streamlit
- 📚 Modeling: Generalized linear regression
- 🗄️ Databases: MySQL
"""
)

# --- DS BACKGROUND ---
st.write('\n')
st.subheader("Statistical Background")
st.write(
    """
- ► Theory of Probability
- ► Theory of Statistics
- ► Longitudinal and Mixed Effects Models
- ► Advanced Statistical Regression Analysis
- ► Experiment Design and Analysis
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Research Assistant/Associate | University of Arizona**")
st.write("08/2021 - Present")
st.write(
    """
- ► Built a metabolomics data (high-dimensional data) analysis pipeline
- ► Built a Shiny application for metabolomics data quality assessment
- ► Authored/Co-authored scientific publications
"""
)

# --- JOB 2


# --- Education ---
# PhD
st.write('\n')
st.subheader("Education")
st.write("---")


st.write(":school:", "**Ph.D. in Environmental Health Sciences | University of Arizona**")
st.write(
    """
- :pencil: Major: Environmental Health Sciences
- :pencil: Minor: Biostatistics
"""
)
st.write("08/2021 - Present")


# MS
st.write("🏫", "**M.S. in Environmental Health Sciences | University of Michigan**")
st.write("09/2018 - 05/2020")




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")