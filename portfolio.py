import streamlit as st

# Page config
st.set_page_config(page_title="Manas Srivastava | Profile", page_icon="💼", layout="wide")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio("Go to",
                           ["🏠 Home", "🛠️ Skills", "💼 Internship", "🎯 Interests", "📈 Projects", "🏆 Achievements",
                            "📄 Resume", "📬 Contact"])

# Sidebar info
st.sidebar.markdown("---")

# Image handling - Using file uploader (dynamic approach)
uploaded_image = st.sidebar.file_uploader("Choose an image...", type="jpg")
if uploaded_image is not None:
    st.sidebar.image(uploaded_image, width=100)
else:
    # Provide a default image from an online URL if no image is uploaded
    st.sidebar.image("https://example.com/default-image.jpg", width=100)

st.sidebar.markdown("**Manas Srivastava**")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/manas-srivastava-28010125b/)")
st.sidebar.markdown("[📧 Email](mailto:manasknitsultanpur@gmail.com)")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f7fb;
        }
        .title-style {
            font-size: 48px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle-style {
            font-size: 26px;
            font-weight: 500;
            color: #555;
            text-align: center;
            margin-bottom: 40px;
        }
        .section-title {
            font-size: 30px;
            color: #1f3b57;
            margin-top: 30px;
            border-bottom: 2px solid #ddd;
        }
        .box {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #999;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            margin-bottom: 10px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        .contact-form button {
            background-color: #003366;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# === PAGE CONTENT BASED ON SIDEBAR SELECTION === #

if section == "🏠 Home":
    st.markdown('<div class="title-style">👋 Hello, I\'m Manas Srivastava</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-style">Aspiring Data Enthusiast | Tech Enthusiast | Problem Solver</div>',
                unsafe_allow_html=True)

    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <p>👋 Hello, I’m <strong>Manas Srivastava</strong> – a passionate data enthusiast constantly exploring the world of data to uncover insights and drive meaningful decisions. With a keen interest in data science, machine learning, and analytics, I strive to leverage the power of data to solve complex problems and make impactful contributions.</p>

<p>🔍 I specialize in transforming raw data into valuable insights, using advanced tools like <strong>Python, SQL, and various analytics platforms</strong>. My goal is to bridge the gap between data and actionable business strategy, helping businesses make data-driven decisions that lead to growth and innovation.</p>

<p>💡 I'm always up for learning new skills, experimenting with emerging technologies, and staying updated on the latest trends in AI, machine learning, and analytics. I believe in the power of continuous learning and collaboration, which drives me to constantly improve and explore new horizons.</p>

<p>🎯 Here’s a glimpse of my key strengths:</p>
<ul>
    <li>⚙️ <strong>Data Analysis & Visualization:</strong> Transforming complex data into easy-to-understand visual stories.</li>
    <li>🧠 <strong>Machine Learning & Predictive Analytics:</strong> Building models to forecast trends and solve business challenges.</li>
    <li>💻 <strong>Automation & Process Optimization:</strong> Using Python and other tools to automate repetitive tasks and optimize workflows.</li>
    <li>📊 <strong>Data-Driven Decision Making:</strong> Helping businesses unlock actionable insights that fuel growth and improve customer targeting.</li>
</ul>

<p>Let’s connect and explore how data can help create business opportunities and drive growth. Feel free to explore more about my skills, projects, and achievements!</p>

    """, unsafe_allow_html=True)

elif section == "🛠️ Skills":
    st.markdown('<div class="section-title">Skills & Tools</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <ul>
                <li><strong>Languages:</strong> Python, SQL</li>
                <li><strong>Tools:</strong> Excel, Power BI, Tableau, Jupyter Notebooks</li>
                <li><strong>Libraries:</strong> Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn</li>
                <li><strong>Soft Skills:</strong> Communication, Problem Solving, Teamwork, Time Management</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

elif section == "💼 Internship":
    st.markdown('<div class="section-title">Current Internship</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <p><strong>Role:</strong> Data Analyst Intern</p>
            <p><strong>Company:</strong> Infosys Springboard</p>
            <p><strong>Project:</strong> Analyzing SaaS subscription sales in the market to uncover trends and opportunities.</p>
            <p><strong>Objective:</strong> Delivered insights and business recommendations to improve SaaS product strategy, customer targeting, and subscription growth.</p>
        </div>
    """, unsafe_allow_html=True)

elif section == "🎯 Interests":
    st.markdown('<div class="section-title">My Interests</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <p>📊 Data Science & Analytics</p>
            <p>📈 Business Insights & Strategy</p>
            <p>🧠 Machine Learning</p>
            <p>🎨 Designing Interactive Dashboards</p>
            <p>📚 Reading about AI and Technology trends</p>
            <p>📚 Exploration and creativity </p>
        </div>
    """, unsafe_allow_html=True)

elif section == "📈 Projects":
    st.markdown('<div class="section-title">My Projects</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <ul>
                <li><strong>Sales Forecasting Model:</strong> Developed a machine learning model to predict sales for a retail company, helping them optimize inventory.</li>
                <li><strong>Customer Segmentation:</strong> Used clustering techniques to segment customers based on purchasing behavior, leading to targeted marketing strategies.</li>
                <li><strong>Interactive Dashboard for Market Trends:</strong> Created a dynamic Tableau dashboard to visualize SaaS subscription trends across different regions.</li>
            </ul>
            <p>📂 You can view these projects and more in detail through my GitHub: <a href="https://github.com/manas0540" target="_blank"><strong>Click here to explore my GitHub Portfolio</strong></a></p>
        </div>
    """, unsafe_allow_html=True)

elif section == "🏆 Achievements":
    st.markdown('<div class="section-title">Achievements</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <p><strong>TCS CodeVita Season 12:</strong> Ranked 4,500 out of thousands of participants. A great achievement showcasing my problem-solving skills in coding challenges.</p>
            <p><strong>McKinsey Forward Program (8 Weeks):</strong> Completed a prestigious career accelerator focused on problem-solving, effective communication, and digital transformation in a business context.</p>
        </div>
    """, unsafe_allow_html=True)

elif section == "📄 Resume":
    st.markdown('<div class="section-title">My Resume</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <p>You can view or download my latest resume:</p>
            <a href="https://drive.google.com/file/d/1r_61hnF0i1S-qbqYxlyal19UCjftaW1r/view?usp=sharing" target="_blank">
            <button style="background-color:#003366;color:white;padding:10px 20px;border:none;border-radius:8px;">
            Download Resume
            </button></a>
            <p>If you prefer, you can also view the resume online:</p>
            <a href="https://drive.google.com/file/d/1r_61hnF0i1S-qbqYxlyal19UCjftaW1r/view?usp=sharing" target="_blank">
            View Resume</a>
        </div>
    """, unsafe_allow_html=True)

elif section == "📬 Contact":
    st.markdown('<div class="section-title">Get in Touch</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="box">
            <p>📧 Email: <a href="mailto:manasknitsultanpur@gmail.com">manasknitsultanpur@gmail.com</a></p>
            <p>🔗 LinkedIn: <a href="https://www.linkedin.com/in/manas-srivastava-28010125b/" target="_blank">linkedin.com/in/manas-srivastava-28010125b/</a></p>
            <p>🌐 Portfolio: <a href="https://linktr.ee/manass09" target="_blank">linktr.ee/manass09</a> (all things at one place)</p>
        </div>
    """, unsafe_allow_html=True)

    # Contact form
    st.markdown('<div class="section-title">Contact Form</div>', unsafe_allow_html=True)
    with st.form(key='contact_form', clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send Message")
        if submit_button:
            st.success("Thank you for reaching out! I will get back to you shortly.")
