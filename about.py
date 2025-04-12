import streamlit as st

# Page config
st.set_page_config(page_title="Manas Srivastava | Profile", page_icon="💼", layout="wide")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio("Go to", ["🏠 Home", "🛠️ Skills", "💼 Internship", "🎯 Interests", "📬 Contact"])

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=100)
st.sidebar.markdown("**Manas Srivastava**")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/your-profile)")
st.sidebar.markdown("[📧 Email](mailto:youremail@example.com)")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f7fb;
        }
        .title-style {
            font-size: 46px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle-style {
            font-size: 24px;
            font-weight: 500;
            color: #555;
            text-align: center;
            margin-bottom: 40px;
        }
        .section-title {
            font-size: 28px;
            color: #1f3b57;
            margin-top: 30px;
            border-bottom: 2px solid #ddd;
        }
        .box {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)

# === PAGE CONTENT BASED ON SIDEBAR SELECTION === #

if section == "🏠 Home":
    st.markdown('<div class="title-style">👋 Hello, I\'m Manas Srivastava</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-style">Aspiring Data Analyst | Tech Enthusiast | Problem Solver</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box">
        <p>Hi, I’m <strong>Manas Srivastava</strong>, currently working as a Data Analyst Intern focused on SaaS subscription sales in the Indian market.</p>
        <p>I enjoy extracting meaningful insights from data and using them to guide business decisions. I'm passionate about growing in the technical space and love turning complex data into simple stories.</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "🛠️ Skills":
    st.markdown('<div class="section-title">Skills & Tools</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box">
        <ul>
            <li><strong>Languages:</strong> Python, SQL</li>
            <li><strong>Tools:</strong> Excel, Power BI, Tableau, Jupyter Notebooks</li>
            <li><strong>Libraries:</strong> Pandas, NumPy, Matplotlib, Seaborn</li>
            <li><strong>Soft Skills:</strong> Communication, Problem Solving, Teamwork</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif section == "💼 Internship":
    st.markdown('<div class="section-title">Current Internship</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box">
        <p><strong>Role:</strong> Data Analyst Intern</p>
        <p><strong>Company:</strong> Infosys</p>
        <p><strong>Project:</strong> Analyzing SaaS subscription sales in the Indian market to uncover trends and opportunities.</p>
        <p>Preparing a final presentation for Infosys, focused on actionable insights derived from real data.</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "🎯 Interests":
    st.markdown('<div class="section-title">My Interests</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box">
        <p>📊 Data Science & Analytics</p>
        <p>📈 Business Insights & Strategy</p>
        <p>🧠 Beginner in Machine Learning</p>
        <p>🎨 Creating Engaging Dashboards</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "📬 Contact":
    st.markdown('<div class="section-title">Get in Touch</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="box">
        <p>📧 Email: <a href="manasknitsultanpur@gmail.com">manasknitsultanpur@gmail.com</a></p>
        <p>🔗 LinkedIn: <a href="https://www.linkedin.com/in/manas-srivastava-28010125b/" target="https://www.linkedin.com/in/manas-srivastava-28010125b/">linkedin.com/in/your-profile</a></p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Stay Positive ✨ | Made with ❤️ by Manas Srivastava</div>', unsafe_allow_html=True)
