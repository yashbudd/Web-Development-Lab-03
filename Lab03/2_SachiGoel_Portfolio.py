import streamlit as st
import sachi_info
import pandas as pd

def about_me_section():
    st.header('About Me')
    st.image(sachi_info.profile_picture, width = 200)
    st.write(sachi_info.about_me)
    st.write("---")

about_me_section()

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on Linkedin")
    linkedin_link=f'<a href="{sachi_info.my_linkedin_url}"><img src="{sachi_info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.text("Check out my projects")
    github_link=f'<a href="{sachi_info.my_github_url}"><img src="{sachi_info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    st.sidebar.text("Contact Me!")
    email_link=f'<a href="mailto:{sachi_info.my_email_address}"><img src="{sachi_info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_link, unsafe_allow_html=True)

links_section()

def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree** {education_data['Degree']}")
    st.write(f"**Graduation Date** {education_data['Graduation Date']}")
    st.write(f"**GPA** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Name",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True
    )
    st.write("---")
education_section(sachi_info.education_data, sachi_info.course_data)

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(sachi_info.experience_data)

def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander=st.expander(f"{project_name}")
        for bullet in project_description:
            expander.write(bullet)
    st.write("---")
project_section(sachi_info.projects_data)

def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{sachi_info.programming_icons.get(skill, '')}")
        st.progress(percentage)
    
    for spoken, proficency in spoken_data.items():
        st.write(f"{spoken} {sachi_info.spoken_icons.get(spoken, '')}: {proficency}")

    st.write("---")
skills_section(sachi_info.programming_data, sachi_info.spoken_data)

def activities_section(leadership_data, activity_data):
    st.header("Leadership & Community Engagement")
    tab1, tab2 = st.tabs(["Leadership", "Community Engagement"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Engagement")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullets in details:
                expander.write(bullets)

activities_section(sachi_info.leadership_data, sachi_info.activity_data)