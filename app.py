import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="RTU PADIOS SYSTEM", layout="wide")

# --------------------------------------------------
# BLUE & GOLD THEME (Plain Sidebar)
# --------------------------------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
background-color:#f5f5f5;
color:#000000;
}

/* Sidebar plain - remove background color */
[data-testid="stSidebar"]{
background-color:inherit;
color:#000000;
}
[data-testid="stSidebar"] *{
color:#000000;
}

/* Titles */
.main-title{
font-size:48px;
font-weight:800;
color:#0038A8;
}
.subtitle{
font-size:20px;
color:#333333;
}

/* Audience Cards */
.card{
background-color:#ffffff;
padding:25px;
border-radius:12px;
border-top:4px solid #FDB913;
margin-bottom:15px;
text-align:center;
}

/* Course Cards */
.course-card{
background-color:#ffffff;
padding:15px;
border-radius:10px;
border-left:6px solid #0038A8;
margin-bottom:8px;
}

/* Search Results */
.search-result{
background-color:#FDB913;
color:#0038A8;
padding:6px 10px;
margin-bottom:4px;
border-radius:5px;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/f/f5/RTU_Logo.jpg",
    width=120
)
st.sidebar.title("RTU SEARCH NAVIGATION")
page = st.sidebar.radio(
    "Select Section",
    ["Home", "Course Offer", "Requirements", "Admission Date", "Maps"]
)

# --------------------------------------------------
# SEARCH BAR
# --------------------------------------------------
st.sidebar.markdown("### 🔎 Search Program")
query = st.sidebar.text_input("", key="search_input")

programs = [
    "BS Civil Engineering","BS Mechanical Engineering","BS Architecture","BS Electronics Engineering",
    "BS Accountancy","BS Business Administration","BS Office Administration",
    "BS Psychology","BS Biology","AB Political Science",
    "BEEd","BSEd Math","BSEd English","BSEd Science",
    "BS Computer Science","BS Information Technology"
]

if query:
    results = [p for p in programs if query.lower() in p.lower()]
    if results:
        st.sidebar.markdown("### Results:")
        for r in results:
            st.sidebar.markdown(f'<div class="search-result">{r}</div>', unsafe_allow_html=True)
    else:
        st.sidebar.warning("No results found")

# --------------------------------------------------
# BLUE KNIGHT FAQ BOT
# --------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("Blue Knight Bot")
faq = st.sidebar.selectbox(
    "Ask a question",
    ["Select Question",
     "When is the entrance exam?",
     "Is RTU is a state university?",
     "Is there a uniform?"]
)
if faq == " is the entrance exam?":
    st.sidebar.info("Entrance exam usually happens from April to May.")
elif faq == "Is RTU is a state university?":
    st.sidebar.info("Yes, Rizal Technological University (RTU) is a public state university in the Philippines.")
elif faq == "Is there a uniform?":
    st.sidebar.info("RTU had one single design uniform for all program")

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if page == "Home":
    st.markdown('<h1 style="color:#0038A8;">RTU PADIOS SYSTEM INQUIRY</h1>', unsafe_allow_html=True)
    st.subheader("The Unofficial Student Inquiry Portal")
    st.info("Welcome to RTU PADIOS – your guide to Rizal Technological University admissions.")
    st.write("""
Empowering future **BluePad Knights** with instant access to academic opportunities
at **Rizal Technological University**.
""")
    st.divider()
    st.subheader("🎯 Target Audience")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
<div class="card">
<h3>🌟 Dreamers</h3>
<p>Prospective students exploring degree programs and future careers.</p>
</div>
""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
<div class="card">
<h3>🔄 Shifters</h3>
<p>Transferees and returnees looking for new academic opportunities.</p>
</div>
""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
<div class="card">
<h3>👨‍👩‍👧 Supporters</h3>
<p>Parents and guardians helping students choose the right program.</p>
</div>
""", unsafe_allow_html=True)
    st.divider()
    st.subheader("⚙ System Functions")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Inputs")
        st.selectbox("Program Interest", programs)
        st.radio("Application Status", ["Freshman", "Transferee", "Returnee"])
        st.select_slider("Campus Preference", ["Pasig", "Mandaluyong"])
    with col2:
        st.markdown("### Outputs")
        st.checkbox("Filtered Program List")
        st.checkbox("Requirement Checklist")
        st.checkbox("Admission Status / Dates")
        st.checkbox("Interactive Maps")
    st.divider()
    st.subheader("📊 RTU Quick Facts")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Colleges", "5")
    c2.metric("Programs", "15+")
    c3.metric("Campuses", "2")
    c4.metric("Students", "15,000+")
    st.progress(70)
    st.caption("System prototype completion")

# --------------------------------------------------
# COURSE OFFER
# --------------------------------------------------
elif page == "Course Offer":
    st.title("📚 COURSE OFFERINGS")
    college = st.selectbox(
        "Select College",
        ["Engineering and Architecture", "Business and Accountancy", "Arts and Sciences", "Education", "Computer Studies"]
    )
    if college == "Engineering and Architecture":
        st.markdown("""
<div class="course-card">🎓 BS Civil Engineering</div>
<div class="course-card">🎓 BS Mechanical Engineering</div>
<div class="course-card">🎓 BS Architecture</div>
<div class="course-card">🎓 BS Electronics Engineering</div>
""", unsafe_allow_html=True)
    elif college == "Business and Accountancy":
        st.markdown("""
<div class="course-card">🎓 BS Accountancy</div>
<div class="course-card">🎓 BS Business Administration</div>
<div class="course-card">🎓 BS Office Administration</div>
""", unsafe_allow_html=True)
    elif college == "Arts and Sciences":
        st.markdown("""
<div class="course-card">🎓 BS Psychology</div>
<div class="course-card">🎓 BS Biology</div>
<div class="course-card">🎓 AB Political Science</div>
""", unsafe_allow_html=True)
    elif college == "Education":
        st.markdown("""
<div class="course-card">🎓 BEEd</div>
<div class="course-card">🎓 BSEd Math</div>
<div class="course-card">🎓 BSEd English</div>
<div class="course-card">🎓 BSEd Science</div>
""", unsafe_allow_html=True)
    elif college == "Computer Studies":
        st.markdown("""
<div class="course-card">🎓 BS Computer Science</div>
<div class="course-card">🎓 BS Information Technology</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# REQUIREMENTS
# --------------------------------------------------
elif page == "Requirements":
    st.title("📄 ADMISSION REQUIREMENTS")
    tab1, tab2 = st.tabs(["Freshmen", "Transferees"])
    with tab1:
        st.info("Required Documents")
        st.write("""
• Form 138 – Grade 12 Report Card  
• PSA Birth Certificate  
• Good Moral Character Certificate  
• 2x2 ID Pictures
""")
        st.file_uploader("Upload Sample Requirement")
    with tab2:
        st.warning("Required Documents")
        st.write("""
• Transcript of Records (TOR)  
• Honorable Dismissal  
• Course Description for crediting
""")

# --------------------------------------------------
# ADMISSION DATE
# --------------------------------------------------
elif page == "Admission Date":
    st.title("📅 ADMISSION TIMELINE")
    df = pd.DataFrame({
        "Activity": ["Online Application Filing","Entrance Exam","Release of Results","Medical Exam","Enrollment"],
        "Date": ["January-March","April-May","June","July","August"],
        "Status": ["🟢 Open","🟡 Incoming","⚪ Pending","⚪ Pending","⚪ Pending"]
    })
    st.dataframe(df)
    st.metric("Applications Received", "1,245", "+10%")

# --------------------------------------------------
# MAPS
# --------------------------------------------------
elif page == "Maps":
    st.title("RTU CAMPUS MAPS")
    campus = pd.DataFrame({
        "Campus": ["Pasig Campus", "Mandaluyong Campus"],
        "lat": [14.5764, 14.5832],
        "lon": [121.0851, 121.0409]
    })
    layer = pdk.Layer(
        "ScatterplotLayer",
        campus,
        get_position='[lon, lat]',
        get_radius=250,
        get_fill_color=[253,185,19],  # Gold
        pickable=True
    )
    view = pdk.ViewState(latitude=14.58, longitude=121.06, zoom=12)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view, tooltip={"text":"{Campus}"}))
    st.map(campus)