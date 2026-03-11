import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(page_title="RTU PADIOS SYSTEM", layout="wide")

# --------------------------------------------------
# PROGRAM LIST
# --------------------------------------------------

programs = [
"BS Civil Engineering",
"BS Mechanical Engineering",
"BS Computer Science",
"BS Information Technology",
"BS Business Administration"
]

# --------------------------------------------------
# UI STYLE
# --------------------------------------------------

st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
background-color:#f4f6fa;
}

.card{
background-color:white;
padding:25px;
border-radius:12px;
border-top:5px solid #FDB913;
text-align:center;
box-shadow:0px 3px 8px rgba(0,0,0,0.1);
}

.course-card{
background-color:white;
padding:15px;
border-radius:10px;
border-left:6px solid #0038A8;
margin-bottom:10px;
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

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.sidebar.button(" Home", use_container_width=True):
    st.session_state.page = "Home"

if st.sidebar.button(" Course Offer", use_container_width=True):
    st.session_state.page = "Course"

if st.sidebar.button(" Requirements", use_container_width=True):
    st.session_state.page = "Requirements"

if st.sidebar.button(" Admission Date", use_container_width=True):
    st.session_state.page = "Admission"

if st.sidebar.button(" Maps", use_container_width=True):
    st.session_state.page = "Maps"

page = st.session_state.page

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
     "Is RTU a state university?",
     "Do students need to wear a uniform?"]
)
if faq == "When is the entrance exam?":
    st.sidebar.info("Entrance exam usually happens from April to May.")
elif faq == "Is RTU a state university?":
    st.sidebar.info("Yes, Rizal Technological University (RTU) is a public state university in the Philippines.")
elif faq == "Do students need to wear a uniform?":
    st.sidebar.info("RTU implement a single design uniform for all program")



# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "Home":

    st.markdown('<h1 style="color:#0038A8;">RTU PADIOS SYSTEM INQUIRY</h1>', unsafe_allow_html=True)
    st.subheader("The Unofficial Student Inquiry Portal")

    st.info("Welcome to PADIOS SYSTEM INQUIRY- your guide to Rizal Technological University admissions.")

    st.write("""Empowering future **BluePad Knights** with instant access to academic opportunities at **Rizal Technological University**.""")

    st.divider()

    # TARGET AUDIENCE
    st.subheader(" TARGET AUDIENCE")

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

    # SYSTEM FUNCTIONS
    st.subheader(" SYSTEM FUNCTION")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Inputs")

        st.selectbox("Program Interest", programs)

        st.radio(
        "Application Status",
        ["Freshman","Transferee","Returnee"]
        )

        st.select_slider(
        "Campus Preference",
        ["Pasig","Mandaluyong"]
        )

    with col2:

        st.markdown("### Outputs")

        st.checkbox("Filtered Program List")
        st.checkbox("Requirement Checklist")
        st.checkbox("Admission Status / Dates")
        st.checkbox("Interactive Maps")

    st.divider()

    # QUICK FACTS
    st.subheader(" RTU Quick Facts")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Colleges","5")
    col2.metric("Programs","15+")
    col3.metric("Campuses","2")
    col4.metric("Students","15,000+")
    st.progress(70)
    st.caption("System prototype completion")
    st.divider()


# --------------------------------------------------
# COURSE OFFER
# --------------------------------------------------
elif page == "Course":

    st.title("📚 COURSE OFFERINGS")

    college = st.selectbox(
        "Select College",
        [
            "Engineering and Architecture",
            "Business and Accountancy",
            "Arts and Sciences",
            "Education",
            "Computer Studies"
        ]
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

    st.divider()

# ENROLLMENT CHART
    st.subheader(" Program Enrollment Comparison")

    data = pd.DataFrame({
        "Program":[
        "Civil Engineering",
        "Mechanical Engineering",
        "Computer Science",
        "Information Technology",
        "Business Administration"
        ],
        "Pasig":[320,210,450,500,300],
        "Mandaluyong":[280,180,400,420,350]
    })

    chart_data = data.set_index("Program")

    tab1,tab2 = st.tabs(["Chart","Data"])

    tab1.bar_chart(chart_data)
    tab2.dataframe(data)

    

# --------------------------------------------------
# REQUIREMENTS PAGE
# --------------------------------------------------

elif page == "Requirements":

    st.title("📄 ADMISSION REQUIREMENTS")

    tab1,tab2 = st.tabs(["Freshmen","Transferees"])

    with tab1:
        st.write("""
• Form 138 – Grade 12 Report Card  
• PSA Birth Certificate  
• Good Moral Character Certificate  
• 2x2 ID Pictures
""")

    with tab2:
        st.write("""
• Transcript of Records  
• Honorable Dismissal  
• Course Description
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
# ADMISSION PAGE
# --------------------------------------------------

elif page == "Admission":

    st.title("📅 ADMISSION TIMELINE")

    df = pd.DataFrame({
        "Activity":[
        "Online Application Filing",
        "Entrance Exam",
        "Release of Results",
        "Medical Exam",
        "Enrollment"
        ],
        "Date":[
        "January-March",
        "April-May",
        "June",
        "July",
        "August"
        ],
        "Status":[
        "🟢 Open",
        "🟡 Incoming",
        "⚪ Pending",
        "⚪ Pending",
        "⚪ Pending"
        ]
    })

    st.dataframe(df)

# --------------------------------------------------
# MAP PAGE
# --------------------------------------------------

elif page == "Maps":

    st.title("📍 RTU CAMPUS LOCATIONS")

    campus = pd.DataFrame({
        "Campus":["Pasig Campus","Mandaluyong Campus"],
        "lat":[14.5764,14.5832],
        "lon":[121.0851,121.0409]
    })

    layer = pdk.Layer(
        "ScatterplotLayer",
        campus,
        get_position='[lon, lat]',
        get_radius=300,
        get_fill_color=[0,56,168],
        pickable=True
    )

    view = pdk.ViewState(
        latitude=14.58,
        longitude=121.06,
        zoom=12
    )

    st.pydeck_chart(
        pdk.Deck(
            layers=[layer],
            initial_view_state=view,
            tooltip={"text":"{Campus}"}
        )
    )

    st.success("Blue markers represent RTU campuses.")