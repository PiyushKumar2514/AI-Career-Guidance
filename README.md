# 🎓 AI Career Guidance and Resume Analysis System

**Personalized AI-powered career counseling — Get career recommendations, skill gap analysis, resume feedback, learning roadmaps, and interview preparation all in one place.**

---

## 🧠 Problem & Solution

Traditional career counseling is often expensive, time-consuming, and not easily accessible to every student. Many students struggle to identify suitable career paths, required skills, and ways to improve their resumes.

This AI-powered Career Guidance System uses **Google Gemini API** to analyze a student's academic background, skills, interests, career goals, and resume details. The system generates personalized career recommendations, identifies skill gaps, provides learning roadmaps, and offers resume improvement suggestions instantly.

---

## 🛠️ Features

| Feature                   | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Career Recommendation** | Suggests suitable career paths based on skills, interests, and academic background. |
| **Skill Gap Analysis**    | Identifies missing skills required for the selected career.                         |
| **Learning Roadmap**      | Generates a personalized step-by-step learning plan.                                |
| **Resume Analysis**       | Reviews resumes and provides improvement suggestions.                               |
| **Interview Preparation** | Generates technical and HR interview questions.                                     |
| **Interactive Interface** | Easy-to-use web interface developed using Streamlit.                                |

---

## 💻 Tech Stack

| Component                  | Technology                             |
| -------------------------- | -------------------------------------- |
| **Programming Language**   | Python 3.12                            |
| **Frontend**               | Streamlit                              |
| **AI Model**               | Google Gemini API (`gemini-2.5-flash`) |
| **Environment Management** | python-dotenv (`.env`)                 |
| **Version Control**        | Git & GitHub                           |

---

## 📁 Project Structure

```text
AI_Career_Guidance/

├── app.py               # Main Streamlit Application
├── requirements.txt     # Project Dependencies
├── .env                 # Gemini API Key (Not uploaded to GitHub)
├── .gitignore           # Ignore secret and temporary files
└── README.md            # Project Documentation
```

---

## 🚀 Installation

### Requirements

* Python 3.12+
* pip package manager

### Setup

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/AI-Career-Guidance.git

cd AI-Career-Guidance
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure API Key**

Create a `.env` file:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

> ⚠️ **Security Warning:** Never upload your `.env` file or API key to GitHub.

---

## 🕹️ Usage

Run the application:

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🔧 Troubleshooting

| Issue               | Solution                                                    |
| ------------------- | ----------------------------------------------------------- |
| API Key Error       | Check `.env` file and ensure the Gemini API key is correct. |
| Module Not Found    | Run `pip install -r requirements.txt` again.                |
| Streamlit Not Found | Activate the virtual environment before running the app.    |
| API Rate Limit      | Wait a few moments and retry the request.                   |

---

## 📌 Future Scope

* Voice-based career counseling.
* PDF resume upload and analysis.
* Real-time job and internship recommendations.
* AI-powered mock interviews.
* Multilingual support.
* Mobile application deployment.

---

## 🧑‍💻 Author

**Piyush Kumar**

B.Tech Computer Science Engineering

AI Career Guidance and Resume Analysis System using Generative AI.
