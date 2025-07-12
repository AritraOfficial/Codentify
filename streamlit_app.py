import streamlit as st
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AI Code Reviewer", layout="wide", page_icon='🔍')

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    st.error("API key missing in .env!")
    st.stop()


with open("prompt_template.json", "r") as f:
    prompt_template = json.load(f)["prompt"]

tabs = st.tabs(["🔎 Code Review", "📘 Project Overview"])

# ==============================================
# TAB 1: CODE REVIEW
# ==============================================
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'> Codentify </h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>💬 Smart AI-Powered Code Reviewer & Improver - web app that reviews, analyzes, and improves your code ...</h4>", unsafe_allow_html=True)
  
    st.markdown("### ⚙️ Review Settings")
    col1, col2, col3 = st.columns(3)
    with col1:
        language_choice = st.selectbox("💬 Programming Language - You Want the Review", ["Python", "JavaScript", "Java", "C++", "C#", "Go", "TypeScript"])
    with col2:
        review_type = st.selectbox("🔍 Select Review Focus", ["General Review", "Bug Detection", "Performance Optimization", "Security Issues", "Code Refactoring"])
    with col3:
        explanation_type = st.selectbox("🧠 Explanation Style", ["Detailed", "Concise", "Line-by-Line", "Bullet Points"])

    st.subheader("📝 Paste or Upload Your Code")
    uploaded_file = st.file_uploader("📁 Upload code", type=["py", "js", "jsx", "java", "ts", "cpp", "cs"])
    code_input = st.text_area("", height=300, placeholder="Paste your code here...")

    if uploaded_file:
        code_input = uploaded_file.read().decode("utf-8")

    submit = st.button("🚀 Run Code Review")

    def build_prompt(template, code, review_type, explanation_type, language):
        return (
            template
            .replace("{{REVIEW_TYPE}}", review_type)
            .replace("{{EXPLANATION_STYLE}}", explanation_type)
            .replace("{{CODE}}", code)
            .replace("{{LANGUAGE}}", language)
        )

    def review_code_with_llm(prompt):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
    
        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}]
        }
        try:
            res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"]
            else:
                return f"❌ Error {res.status_code}: {res.text}"
        except Exception as e:
            return f"❌ Exception: {e}"
        
    if submit:
        if not code_input.strip():
            st.warning("⚠️ Please enter or upload code first.")
        else:
            with st.spinner("🧠 Reviewing your code..."):
                prompt = build_prompt(prompt_template, code_input, review_type, explanation_type, language_choice)
                result = review_code_with_llm(prompt)

            st.markdown('<div class="review-heading">🔍 Review Summary</div>', unsafe_allow_html=True)
            if "```" in result:
                explanation = result.split("```")[0]
                st.markdown(f'<div class="review-box">{explanation}</div>', unsafe_allow_html=True)
                corrected_code = result.split("```")[1].split("```")[0]
                st.subheader("✅ Suggested Code")
                st.code(corrected_code, language=language_choice.lower())
            else:
                st.markdown(result)

    st.markdown("""
<div class="footer-container">
    <div class="footer-links">
        <a href="https://arim-official.netlify.app/" target="_blank">
            🌐 Portfolio
        </a>
        <a href="https://www.linkedin.com/in/aritramukherjeeofficial/" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="20" height="20" style="vertical-align:middle; margin-right:6px;"> LinkedIn
        </a>
        <a href="https://github.com/AritraOfficial" target="_blank">
  <img src="https://img.icons8.com/ios-glyphs/30/ffffff/github.png" width="20" height="20" style="vertical-align:middle; margin-right:6px;"> GitHub
</a>
        <a href="mailto:aritra.work.official@gmail.com" target="_blank">
            ✉️ Mail
        </a>
    </div>
    <div class="footer-credit">
        🤖 AI Code Reviewer | Built by AriM. Official | Built with Streamlit | Powered by Mistral-7B via OpenRouter
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================================
# TAB 2: PROJECT OVERVIEW
# ==============================================
with tabs[1]:
    st.title("📘 Project Overview")

    st.markdown("""
### 🔹 About the Project
This is a professional AI Code Reviewer app powered by OpenRouter's free LLMs. It analyzes source code, identifies bugs or inefficiencies, and offers improvement suggestions using dynamic prompt engineering.

### 🔹 Supported Languages - In Which Language You Want the Review!
- Python
- JavaScript
- Java
- C++
- C#
- Go
- TypeScript

### 🔹 Supported File Formats
`.py`, `.js`, `.jsx`, `.java`, `.ts`, `.cpp`, `.cs`

### 🔹 Key Features
- Paste or upload code
- Review using LLMs
- Explanation + corrected version
- Dynamic multi-language prompt
- Two-tab layout (Review + Overview)
- Modern UI with footer and layout styling

### 🔹 Technologies Used
- Python, Streamlit, OpenRouter
- Mistral-7B Instruct LLM
- dotenv, JSON-based prompting
- CSS-based UI enhancements
""")
    st.markdown("""
<div class="footer-container">
    <div class="footer-links">
        <a href="https://arim-official.netlify.app/" target="_blank">
            🌐 Portfolio
        </a>
        <a href="https://www.linkedin.com/in/aritramukherjeeofficial/" target="_blank">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="20" height="20" style="vertical-align:middle; margin-right:6px;"> LinkedIn
        </a>
        <a href="https://github.com/AritraOfficial" target="_blank">
  <img src="https://img.icons8.com/ios-glyphs/30/ffffff/github.png" width="20" height="20" style="vertical-align:middle; margin-right:6px;"> GitHub
</a>
        <a href="mailto:aritra.work.official@gmail.com" target="_blank">
            ✉️ Mail
        </a>
    </div>
    <div class="footer-credit">
        🤖 AI Code Reviewer | Built by AriM. Official | Built with Streamlit | Powered by Mistral-7B via OpenRouter
    </div>
</div>
""", unsafe_allow_html=True)


