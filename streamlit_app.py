import streamlit as st

# Page Setup
main_page = st.Page(
    page="views/main.py",
    title="Grow LSS",
    icon="🏠",
    default=True
)
define_page = st.Page(
    page="views/define.py",
    title="Define",
    icon="📖"
)
measure_page = st.Page(
    page="views/measure.py",
    title="Measure",
    icon="🧮"
)
analyze_page = st.Page(
    page="views/analyze.py",
    title="Analyze",
    icon="🔍"
)
improve_page = st.Page(
    page="views/improve.py",
    title="Improve",
    icon="📈"
)
control_page = st.Page(
    page="views/control.py",
    title="Control",
    icon="📊"
)

bi_page = st.Page(
    page="views/bi.py",
    title="BI",
    icon="📈"
)

pg = st.navigation(
    {
        "Página Inicial": [main_page],
        "DMAIC": [define_page, measure_page, analyze_page, improve_page, control_page],
        "BI": [bi_page]
    }
)

# Shared in all pages
st.logo("assets/grow_lss_logo.png")

# Sidebar for page selection
# with st.sidebar.selectbox('Pages', ["Main", "Define"]):


# Run the navigation
pg.run()
