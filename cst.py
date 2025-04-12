import streamlit as st
import pandas as pd
from datetime import datetime
from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

# Load Ollama LLM
llm = OllamaLLM(model='gemma3:1b')

# Prompt templates
response_prompt = PromptTemplate(
    input_variables=['user_query'],
    template="""
You are a customer support bot.
Do not use any special symbols; keep it brief and simple.
Only reply according to the response format; any other output is not allowed.
You have 4 tasks:
- Determine the user emotion from [Neutral, Frustrated, Confused, Annoyed, Anxious, Urgent].
- Provide a summary of the issue for the tech support team.
- Decide the priority from [Low, Medium, High, Critical].
- Suggest a possible solution that might resolve the issue.

Query: {user_query}

Response format:
"
Sentiment: 
Summary:
Priority: 
Solution: 
"
"""
)

cleaning_prompt = PromptTemplate(
    input_variables=['message'],
    template="""
Clean the following message so that it is formatted with the following four fields: Sentiment, Summary, Priority, and Solution.
Remove any unnecessary spaces or special symbols and ensure it adheres strictly to the format.

Message: {message}

Cleaned text:
"""
)

# Chains
sentiment_analyser = response_prompt | llm
answer_cleaner = cleaning_prompt | llm

# Initialize session state to hold analysis result, if not already present.
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = {}

st.set_page_config(page_title="Support Sentiment Analyzer", page_icon="🧠")
st.title("💬 Smart Support Assistant")
st.markdown("Analyze user queries to determine sentiment, summary, priority, and solution using a local LLM.")

user_query = st.text_area("Enter user query:")

# When the Analyze button is clicked, perform analysis and store result in session state.
if st.button("Analyze", key="analyze_button"):
    if user_query.strip() != "":
        with st.spinner("Analyzing..."):
            raw_answer = sentiment_analyser.invoke(user_query)
            cleaned_answer = answer_cleaner.invoke(raw_answer)

            # Save analysis result text and parsed parts
            st.session_state.analysis_result["raw"] = cleaned_answer

            if "Sentiment:" in cleaned_answer:
                parts = {
                    line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip()
                    for line in cleaned_answer.splitlines()
                    if ":" in line
                }
                st.session_state.analysis_result.update({
                    "Sentiment": parts.get('Sentiment', '-'),
                    "Summary": parts.get('Summary', '-'),
                    "Priority": parts.get('Priority', '-'),
                    "Solution": parts.get('Solution', '-'),
                    "User Query": user_query
                })
                st.session_state.analysis_done = True
    else:
        st.error("Please enter a valid query.")

# Display analysis result if available
if st.session_state.analysis_done:
    st.subheader("📊 Analysis Result")
    st.text_area("Cleaned Response", st.session_state.analysis_result.get("raw", ""), height=200)

    st.markdown("### 🧾 Breakdown")
    st.write(f"Sentiment: {st.session_state.analysis_result.get('Sentiment', '-')}")
    st.write(f"Summary: {st.session_state.analysis_result.get('Summary', '-')}")
    st.write(f"Priority: {st.session_state.analysis_result.get('Priority', '-')}")
    st.write(f"Solution: {st.session_state.analysis_result.get('Solution', '-')}")

    # Ask for user satisfaction
    satisfaction = st.radio("Are you satisfied with the solution?", ["Yes", "No"], key="satisfaction_radio")

    if satisfaction == "No":
        st.warning("A support ticket will be generated.")

        with st.form("ticket_form"):
            st.write("Click the button below to generate a support ticket.")
            submit_ticket = st.form_submit_button("Generate Ticket")
            if submit_ticket:
                # Try to load the existing ticket CSV if it exists
                try:
                    df = pd.read_csv("ticket.csv")
                    # Use the number of existing rows to create a unique ticket id starting from T1101.
                    next_id = 1101 + len(df)
                except FileNotFoundError:
                    df = pd.DataFrame(columns=["Ticket ID", "Timestamp", "User Query", "Sentiment", "Summary", "Priority", "Solution"])
                    next_id = 1101

                ticket_id = f"T{next_id}"
                ticket_data = {
                    "Ticket ID": ticket_id,
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "User Query": st.session_state.analysis_result.get("User Query", ""),
                    "Sentiment": st.session_state.analysis_result.get("Sentiment", "-"),
                    "Summary": st.session_state.analysis_result.get("Summary", "-"),
                    "Priority": st.session_state.analysis_result.get("Priority", "-"),
                    "Solution": st.session_state.analysis_result.get("Solution", "-"),
                }

                df = pd.concat([df, pd.DataFrame([ticket_data])], ignore_index=True)
                df.to_csv("ticket.csv", index=False)

                st.success(f"✅ Ticket {ticket_id} has been generated and saved to ticket.csv.")