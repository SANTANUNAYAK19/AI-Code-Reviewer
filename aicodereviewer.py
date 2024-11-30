import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyArOEt0GNyxnd6-h1i4V-Ur0O7iiEh53V8")

sys_prompt = """You are a Python code reviewer. 
                Users will submit Python code for analysis.
                You are expected to:
                1. Identify bugs, errors, or areas for improvement.
                2. Suggest fixes or optimizations.
                3. Provide corrected code snippets.
                Ensure detailed and actionable feedback for the user."""

model = genai.GenerativeModel(model_name="gemini-1.5-flash", 
                              system_instruction=sys_prompt)

st.markdown("""
    <style>
        /* Netflix-like Main Header */
        .main-header {
            background-color: #141414; /* Dark Netflix background */
            color: #E50914; /* Netflix red for the title */
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            font-family: 'Arial', sans-serif;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
        }

        /* Sidebar styles */
        .sidebar-text {
            color: #E50914; /* Netflix red */
            font-size: 1.2rem;
            font-family: 'Arial', sans-serif;
        }

        /* Button styling with Netflix red */
        .stButton button {
            background-color: #E50914;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #bf0810;
            transform: scale(1.1);
        }

        /* Text area styling */
        .stTextArea textarea {
            background-color: white; /* Dark gray background */
            color: black;
            border: 2px solid #E50914;
            border-radius: 8px;
            padding: 0.8rem;
            font-size: 1rem;
            font-family: 'Courier New', monospace;
        }

        /* Feedback box with Netflix feel */
        .feedback-box {
            background-color: #1C1C1C;
            color: white;
            border: 2px solid #E50914;
            border-radius: 8px;
            padding: 1rem;
            font-size: 1rem;
            font-family: 'Courier New', monospace;
        }

        /* Footer design */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #141414;
            color: #E50914;
            text-align: center;
            padding: 0.5rem 0;
            font-size: 1rem;
            border-top: 2px solid #E50914;
        }
             /* Customizing the text area placeholder */
        .stTextArea textarea::placeholder {
            color: black !important; /* Set placeholder color to white */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">AI Code Reviewer</div>', unsafe_allow_html=True)

st.sidebar.title("Welcome to the AI Code Reviewer!")
st.sidebar.write("Paste your Python code in the text area, and the AI will provide feedback, bug reports, and suggestions.")
st.sidebar.write("Note: This tool is designed specifically for Python code.")

st.sidebar.markdown('<div class="sidebar-text">Instructions:</div>', unsafe_allow_html=True)
st.sidebar.write("1. Paste your Python code in the text area.")
st.sidebar.write("2. Click 'Review Code' to get feedback.")
st.sidebar.write("3. Review the AI's response for insights and suggestions.")


code_input = st.text_area("Enter your Python code:", height=300, placeholder="Paste your code here...")

btn_click = st.button("Review Code")

if btn_click:
    if code_input.strip() == "":
        st.warning("Please enter some Python code before submitting.")
    else:
        with st.spinner("Reviewing your code..."):
            try:
                response = model.generate_content(code_input)
                st.write(response.text)
            except Exception as e:
                st.error(f"Error in processing: {e}")

st.markdown('<div class="footer">App Developed by:-Santanu Prasad Nayak</div>', unsafe_allow_html=True)
