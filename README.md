# 🤖 Codentify – AI Code Reviewer
<p align="center">
  <a href="https://codentify-arim-official.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/-🚀 Live%20Codentify-000000?style=for-the-badge&logo=firefox&logoColor=white&labelColor=00C853&color=000000" alt="Live Codentify">
  </a>
</p>


### **Codentify** is a smart AI-powered web app that reviews, analyzes, and improves your code using LLMs. A powerful and customizable AI-powered code reviewer web application built using **Python**, **Streamlit**, and **OpenRouter’s free LLMs (like Mistral-7B)**. 


` This app allows developers to paste or upload source code, select review focus and explanation style, and instantly receive a professional AI-generated review along with corrected code. `



## 📸 App View 
| Web View                          | APP's Specification              |
| --------------------------------- | -------------------------------- | 
<img width="1899" height="917" alt="image" src="https://github.com/user-attachments/assets/e34737a6-426c-41c9-ba7c-57ba195abd16" />|<img width="1901" height="1079" alt="image" src="https://github.com/user-attachments/assets/805cd621-4c3c-46c4-a6cd-be1d86345454" />|


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
| Backend Logic  | Python                                    |
| AI Model       | [Mistral-7B (via OpenRouter)](https://openrouter.ai/models/mistralai/mistral-7b-instruct) |
| Prompting      | JSON-powered dynamic prompt template      |
| Styling        | Custom CSS (`style.css`)                  |
| Secrets Mgmt   | `.env` + `python-dotenv`                  |

---

## 📂 File Structure
```
├── main.py # Main Streamlit app
├── prompt_template.json # Dynamic LLM prompt template
├── style.css # Custom styles and footer
├── .env # OpenRouter API key (NOT shared)
├── requirements.txt # Install dependencies
└── README.md # You're here
```
---

## ⚙️ Installation & Run

### 1. Clone the Repository

```bash
git clone https://github.com/AritraOfficial/Codentify.git
cd Codentify
```
2. Set Up the Environment
- Create .env with your OpenRouter API key:
```
OPENROUTER_API_KEY= sk-xxxxxx-your-key
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Launch the App
```bash
streamlit run main.py
```
---------------------------
## 📸 Computer's View

| Upload File                       | Ask Questions                    | Get Answers                       |
| --------------------------------- | -------------------------------- | --------------------------------- |
|<img width="1882" height="852" alt="image" src="https://github.com/user-attachments/assets/171868ae-e27d-4cb4-a230-713d4780e7ef" />|<img width="1859" height="796" alt="image" src="https://github.com/user-attachments/assets/bd6e3f2d-c36a-47d6-b85c-ffa6b01d63a6" />|<img width="1845" height="959" alt="image" src="https://github.com/user-attachments/assets/61214e8a-f7a0-4156-b0ed-67674343d764" />|
---------------------------


- 🔐 Free LLMs Used
```
 This app uses Mistral-7B Instruct from OpenRouter, a fast and free-to-use model for code understanding and natural language generation.
You can switch to other free OpenRouter models by changing the model name in main.py.
```
## 🧠 How It Works

1. User selects:
   - ✅ **Language preference**
   - 🔍 **Type of review**
   - 🧠 **Style of explanation**

2. User pastes or uploads code

3. Code is validated against the selected language

4. A dynamic prompt is constructed using all selections

5. The LLM returns:
   - ⚠️ **Problem analysis**
   - 💡 **Suggestions for improvement**
   - 🛠️ **Corrected version of the code**

---

## ✨ Example Output

```python
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
```

---

## 👤 Developer
**[Aritra Mukherjee](https://arim-official.netlify.app/)**  - ` AI Developer `

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
  <a href="https://arim-official.netlify.app/" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-Website-blueviolet?style=for-the-badge&logo=internet-explorer&logoColor=white" alt="Portfolio Website">
  </a>
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
