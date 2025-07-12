# 🤖 Codentify – AI Code Reviewer

**Codentify** is a smart AI-powered web app that reviews, analyzes, and improves your code using LLMs like Mistral-7B via OpenRouter...

A powerful and customizable AI-powered code reviewer web application built using **Python**, **Streamlit**, and **OpenRouter’s free LLMs (like Mistral-7B)**.

This app allows developers to paste or upload source code, select review focus and explanation style, and instantly receive a professional AI-generated review along with corrected code.

---

## 🚀 Features

- 🔍 **AI-Powered Code Review**: Analyze logic, bugs, performance, and security flaws
- 📥 **Upload or Paste Code**: Supports `.py`, `.js`, `.jsx`, `.java`, `.ts`, `.cpp`, `.cs`
- 🧠 **Select Review Focus**:
  - General Review
  - Bug Detection
  - Performance Optimization
  - Security Issues
  - Code Refactoring
- 💬 **Choose Explanation Style**:
  - Detailed
  - Concise
  - Line-by-Line
  - Bullet Points
- 🌐 **Supports Multiple Languages**:
  - Python, JavaScript, Java, C++, C#, Go, TypeScript
- ✨ **Dynamic Prompt Engineering** for maximum accuracy
- 📘 **Project Overview Tab**: Includes specs, tech stack, and documentation
- 🎨 **Professional UI**: Responsive layout, dark theme, clean footer with profile links

---

## 🛠 Tech Stack

| Layer          | Tool / Tech                              |
|----------------|-------------------------------------------|
| Frontend       | [Streamlit](https://streamlit.io)         |
| Backend Logic  | Python + REST API                         |
| AI Model       | [Mistral-7B (via OpenRouter)](https://openrouter.ai/models/mistralai/mistral-7b-instruct) |
| Prompting      | JSON-powered dynamic prompt template      |
| Styling        | Custom CSS (`style.css`)                  |
| Secrets Mgmt   | `.env` + `python-dotenv`                  |

---

## 📂 File Structure

├── main.py # Main Streamlit app
├── prompt_template.json # Dynamic LLM prompt template
├── style.css # Custom styles and footer
├── .env # OpenRouter API key (NOT shared)
├── requirements.txt # Install dependencies
└── README.md # You're here

yaml
Copy
Edit

---

## ⚙️ Installation & Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
2. Set Up the Environment
Create .env with your OpenRouter API key:

env
Copy
Edit
OPENROUTER_API_KEY=sk-xxxxxx-your-key
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Launch the App
bash
Copy
Edit
streamlit run main.py
📸 Screenshots
Coming soon — UI previews, before/after review comparison.

🔐 Free LLMs Used
This app uses Mistral-7B Instruct from OpenRouter, a fast and free-to-use model for code understanding and natural language generation.

You can switch to other free OpenRouter models by changing the model name in main.py.

🧠 How It Works
User selects:

Language preference

Type of review

Style of explanation

User pastes or uploads code

Code is validated against language choice

A dynamic prompt is constructed

LLM returns:

Problem analysis

Suggestions

Corrected version of code

✨ Example Output
python
Copy
Edit
🔹 Issues Found:
- Missing error handling
- Unused variable

🔹 Suggestions:
- Add try-except block
- Remove unused variable

✅ Corrected Code:
```python
def process(data):
    try:
        return data.lower()
    except Exception:
        return None
yaml
Copy
Edit

---

## 👤 Developer

**Aritra Mukherjee**  
📧 [aritra.work.official@gmail.com](mailto:aritra.work.official@gmail.com)

- 🔗 [LinkedIn](https://www.linkedin.com/in/aritramukherjeeofficial/)
- 💻 [GitHub](https://github.com/AritraOfficial)
- 🌐 [Portfolio](https://arim-official.netlify.app/)
- 📸 [Instagram](https://www.instagram.com/arim.official/)

---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Fork and improve the app!

Open a PR or contact me via LinkedIn or email.

---

## 📌 Disclaimer

This tool is powered by LLMs and should not be used for production-critical code reviews without human verification.

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io)
- [OpenRouter](https://openrouter.ai)
- [Mistral](https://mistral.ai)

---


## 📧 Contact 
For queries or collaborations, feel free to connect:  
<p align="center">
  <a href="https://www.linkedin.com/in/aritramukherjeeofficial/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://x.com/AritraMofficial" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
  </a>
  <a href="https://www.instagram.com/aritramukherjee_official/?__pwa=1" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
  </a>
  <a href="https://leetcode.com/u/aritram_official/" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-%23FFA116.svg?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode">
  </a>
  <a href="https://github.com/AritraOfficial" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://discord.com/channels/@me" target="_blank">
    <img src="https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
  <a href="mailto:aritra.work.official@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-%23D14836.svg?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
</p>