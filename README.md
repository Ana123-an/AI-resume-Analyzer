
# 🚀 AI Career Copilot

AI Career Copilot is a Flask-based web application that helps users analyze their resumes using OpenAI. Users can upload a PDF or DOCX resume or paste resume text directly, specify their target job role, and receive personalized feedback including relevant skills, missing skills, a learning roadmap, and interview questions.

---

## ✨ Features

- User Registration & Login
- Secure Session Authentication
- Upload PDF Resume
- Upload DOCX Resume
- Paste Resume Text
- AI-Powered Resume Analysis
- Relevant Skills Extraction
- Missing Skills Identification
- Personalized Learning Roadmap
- Interview Question Suggestions
- Resume Analysis History
- Logout Functionality

---

## 🛠 Tech Stack

### Backend
- Python 3
- Flask
- SQLAlchemy
- OpenAI API
- PyPDF2
- python-docx

### Database
- TiDB Cloud
- PyMySQL

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

---

## 📂 Project Structure

```text
AI-Career-Copilot/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Career-Copilot.git
```

Go to the project directory:

```bash
cd AI-Career-Copilot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure:

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=mysql+pymysql://USERNAME:PASSWORD@HOST:4000/test
```

Run the application:

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add screenshots of:

- Login Page
- Signup Page
- Dashboard
- Resume Upload
- AI Analysis
- History Page

---

## 🔒 Security

- Environment variables for secrets
- Password hashing
- Session authentication
- Secure database connection
- Input validation
- Error handling

---

## 📌 Future Enhancements

- Resume Score (ATS Score)
- Resume Improvement Suggestions
- Resume PDF Report
- Download AI Report
- Multiple Resume Versions
- Dark Mode
- Email Verification
- Password Reset
- Resume Keyword Optimizer
- Interview Preparation Chatbot

---

## 👩‍💻 Author

**Ananya Mishra**

- GitHub: https://github.com/Ana123-an
- LinkedIn: https://www.linkedin.com/in/ananya-mishra77/

---

## 📜 License

This project is developed for educational and portfolio purposes.
