from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hammad Ahmad Zafar"
PAGE_ICON = ":wave:"
NAME = "Hammad Ahmad Zafar"
DESCRIPTION = """
Medical Scribe
"""
EMAIL = "hammadahmadzafar471@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCEIS4WF50yzfnzA5Xkw1fsw",
    "LinkedIn": "https://linkedin.com/in/hazafar",
    "GitHub": "https://github.com/DrBlack22",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Registered Medical Practitioner(RMP)": "Link to RMP project",
    "🏆 Electronic Health Record(EHR)": "Link to EHR project",
    "🏆 Hospital Management System(HMS)": "Link to HMS project",
    "🏆 Confidentiality and Adherence to HIPAA regulations": "Link to HIPAA project",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


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
- ✔️ Proven track record of accurately documenting patient encounters
- ✔️ Maintaining electronic medical records in various healthcare settings
- ✔️ Proficient in medical terminology and adept at facilitating communication
-    between healthcare providers to ensure seamless patient care delivery
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ⏺️ Proficient in electronic medical record (EMR) systems
- 🩺 Prescribing medication, assessing test results, symptoms, and conditions
- 🖥️ Beginner level proficiency in various programming languages(cpp, python, html)
- 👩‍💻 Time management, collaboration,  empathy and CRM 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**House Officer | CMH Nowshera**")
st.write("2020 - 2023")
st.write(
    """
- ► Performed medical assessments, diagnosed conditions, and developed treatment plans under the supervision of senior physicians as a house officer in a hospital setting
- ► Assisted in surgical procedures, conducted patient rounds, and managed medical documentation to ensure efficient and quality patient care during my tenure as a house officer
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Marketing Lead | Chohan Tech Solutions**")
st.write("06/2023 - 09/2023")
st.write(
    """
- ► Led cross-functional teams in the creation of compelling marketing campaigns, resulting in a significant increase in client engagement and conversion rates
- ► Cultivated and maintained strong relationships with key stakeholders and industry partners to expand market reach and drive revenue growth
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Skills and Certifications")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
