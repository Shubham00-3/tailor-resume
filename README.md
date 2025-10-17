# 🎯 Resume Tailor AI

> **AI-powered resume optimization tool** that intelligently tailors your resume to match any job description using LangGraph and Groq API.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3.1-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)


---

## 📖 Overview

**Resume Tailor AI** is a full-stack application that uses advanced AI to analyze job descriptions and automatically optimize your resume to match the requirements. Built with FastAPI, LangGraph, and React, it provides a seamless experience for job seekers looking to improve their application success rate.


---

## ✨ Features

### 🤖 **AI-Powered Analysis**
- **Smart Keyword Extraction** - Automatically identifies key skills and requirements from job descriptions
- **Skill Matching** - Compares your resume against job requirements
- **Resume Rewriting** - AI-optimized content that highlights relevant experience
- **Professional Summaries** - Generates compelling 3-4 sentence professional summaries

### 🎨 **Modern Frontend**
- **Drag & Drop Upload** - Upload resume files (PDF, DOCX, TXT) with drag-and-drop
- **Clean UI/UX** - Beautiful, intuitive interface built with React and Tailwind CSS
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Real-time Feedback** - Character counts, validation, and status indicators
- **Copy to Clipboard** - One-click copy for tailored resumes
- **File Format Support** - Automatic text extraction from PDF and DOCX files

### 🔧 **Production Ready**
- **RESTful API** - Well-documented FastAPI backend
- **Error Handling** - Comprehensive error messages and logging
- **Docker Support** - Fully containerized for easy deployment
- **CORS Enabled** - Ready for frontend integration

---

## 🏗️ Architecture

```
┌─────────────────────┐
│   React Frontend    │
│   (Vite + Tailwind) │
│   Port: 3000        │
└──────────┬──────────┘
           │ HTTP/Axios
           ▼
┌─────────────────────┐
│  FastAPI Backend    │
│     Port: 8000      │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│  LangGraph Pipeline │
│  ┌───────────────┐  │
│  │ Node A: Extract│ │
│  │ JD Keywords   │  │
│  └───────┬───────┘  │
│          ▼          │
│  ┌───────────────┐  │
│  │ Node B: Match │  │
│  │ Skills        │  │
│  └───────┬───────┘  │
│          ▼          │
│  ┌───────────────┐  │
│  │ Node C: Rewrite│ │
│  │ Resume        │  │
│  └───────────────┘  │
└─────────┬───────────┘
          │
┌─────────▼───────────┐
│     Groq API        │
│ (llama-3.3-70b)     │
└─────────────────────┘
```

---

## 🚀 Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Workflow orchestration for LLM applications
- **[Groq API](https://console.groq.com/)** - Ultra-fast LLM inference (llama-3.3-70b-versatile)
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation using Python type annotations
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server

### Frontend
- **[React](https://react.dev/)** - UI library for building user interfaces
- **[Vite](https://vitejs.dev/)** - Next-generation frontend build tool
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Axios](https://axios-http.com/)** - Promise-based HTTP client

### DevOps
- **Docker** - Containerization
- **Render** - Backend deployment (recommended)
- **Vercel/Netlify** - Frontend deployment (recommended)

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **npm** or **yarn**
- **Git** - [Download](https://git-scm.com/)
- **Groq API Key** - [Get free key](https://console.groq.com/keys)

---

## 🛠️ Installation & Setup

### **Option 1: Quick Start (Automated)**

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shubham00-3/tailor-resume.git
cd tailor-resume
```

#### 2️⃣ Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Configure environment variables
copy .env.example .env
# Edit .env and add your GROQ_API_KEY

# Start backend server
uvicorn app.main:app --reload
```

Backend runs at: **http://localhost:8000**

#### 3️⃣ Frontend Setup (New Terminal)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs at: **http://localhost:3000**

---

### **Option 2: Using Setup Scripts (Windows)**

#### Backend:
```powershell
.\setup.ps1
.\run.ps1
```

#### Frontend:
```powershell
cd frontend
npm install
npm run dev
```

---

### **Option 3: Docker**

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or using Docker directly
docker build -t resume-tailor-ai .
docker run -p 8000:8000 -e GROQ_API_KEY=your_key_here resume-tailor-ai
```

---

## ⚙️ Environment Variables

### Backend (`.env`)

```env
# Required
GROQ_API_KEY=gsk_your_actual_groq_api_key_here

# Optional
MODEL_NAME=llama-3.3-70b-versatile
PORT=8000
LOG_LEVEL=INFO
```

**Get your Groq API Key:** https://console.groq.com/keys

### Frontend (`.env` - Optional)

```env
VITE_API_URL=http://localhost:8000
```

For production, set this to your deployed backend URL.

---

## 💻 Usage

### **1. Start Both Servers**

**Terminal 1 - Backend:**
```bash
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### **2. Open the Application**

Navigate to: http://localhost:3000

### **3. Tailor Your Resume**

1. **Paste your resume** in the left textarea
2. **Paste the job description** in the right textarea
3. Click **"Tailor Resume"** button
4. Wait 10-30 seconds for AI processing
5. **View results:**
   - ✅ Optimized resume
   - 📝 Professional summary
   - 🎯 Matched skills
   - ⚠️ Skills to develop
6. **Copy** your tailored resume to clipboard

---

## 📡 API Documentation

### **Health Check**

```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

### **Tailor Resume**

```http
POST /tailor
Content-Type: application/json
```

**Request Body:**
```json
{
  "resume_text": "Your full resume text here...",
  "job_description": "The job description text here..."
}
```

**Response:**
```json
{
  "tailored_resume": "Optimized resume content...",
  "summary": "Professional summary highlighting key qualifications...",
  "matched_skills": ["Python", "FastAPI", "PostgreSQL"],
  "missing_skills": ["Docker", "Kubernetes", "AWS"]
}
```

**Interactive API Docs:** http://localhost:8000/docs

---

## 📁 Project Structure

```
tailor-resume/
├── app/                          # Backend application
│   ├── graph/
│   │   ├── nodes.py             # LangGraph nodes (Extract, Match, Rewrite)
│   │   └── pipeline.py          # Workflow orchestration
│   ├── utils/
│   │   └── logger.py            # Logging configuration
│   ├── main.py                  # FastAPI app & endpoints
│   └── schemas.py               # Pydantic models
│
├── frontend/                     # Frontend application
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx       # App header
│   │   │   ├── InputSection.jsx # Resume/JD inputs
│   │   │   ├── ResultsSection.jsx # Results display
│   │   │   ├── LoadingSpinner.jsx # Loading animation
│   │   │   └── ErrorAlert.jsx   # Error handling
│   │   ├── services/
│   │   │   └── api.js           # Axios API client
│   │   ├── App.jsx              # Main component
│   │   ├── main.jsx             # Entry point
│   │   └── index.css            # Tailwind styles
│   ├── public/                  # Static assets
│   ├── index.html               # HTML template
│   ├── vite.config.js          # Vite configuration
│   ├── tailwind.config.js      # Tailwind configuration
│   └── package.json            # Dependencies
│
├── tests/                       # Backend tests
│   └── test_main.py
│
├── .env.example                 # Environment template
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── docker-compose.yml          # Docker Compose
├── setup.ps1                   # Windows setup script
├── run.ps1                     # Windows run script
├── test_setup.py               # Setup verification
└── example_usage.py            # API usage examples
```

---

## 🌐 Deployment

### **Backend Deployment (Render)**

1. **Push to GitHub** (already done ✅)

2. **Create Web Service on Render:**
   - Go to [render.com](https://render.com)
   - New → Web Service
   - Connect your GitHub repository
   - Configure:
     - **Name:** `resume-tailor-api`
     - **Runtime:** Docker
     - **Branch:** main

3. **Add Environment Variable:**
   - `GROQ_API_KEY` = your actual key

4. **Deploy!** 🚀

Your backend will be available at: `https://resume-tailor-api.onrender.com`

### **Frontend Deployment (Vercel)**

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel
   ```

3. **Set Environment Variable:**
   - `VITE_API_URL` = your Render backend URL

### **Frontend Deployment (Netlify)**

1. **Install Netlify CLI:**
   ```bash
   npm i -g netlify-cli
   ```

2. **Build and Deploy:**
   ```bash
   cd frontend
   npm run build
   netlify deploy --prod
   ```

3. **Set Environment Variable:**
   - `VITE_API_URL` = your Render backend URL

---

## 🧪 Testing

### **Backend Tests**

```bash
# Verify setup
python test_setup.py

# Run test suite
pytest tests/ -v

# Test API manually
python example_usage.py
```

### **Frontend Tests**

```bash
cd frontend
npm run lint
```

### **API Testing**

**Using cURL:**
```bash
curl http://localhost:8000/health
```

**Using PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health"
```

---

## 🔧 Development

### **Backend Development**

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn app.main:app --reload --log-level debug

# Check logs
tail -f logs/app.log
```

### **Frontend Development**

```bash
cd frontend

# Install dependencies
npm install

# Start dev server with HMR
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

---

## 🐛 Troubleshooting

### **"Unable to connect to server"**
- Ensure backend is running: `uvicorn app.main:app --reload`
- Check if port 8000 is available
- Verify `VITE_API_URL` in frontend `.env`

### **"GROQ_API_KEY not found"**
- Create `.env` file in root directory
- Add `GROQ_API_KEY=gsk_your_key_here`
- Restart the backend server

### **"Model decommissioned" error**
- Update `MODEL_NAME` in `.env` to `llama-3.3-70b-versatile`
- Groq regularly updates available models

### **Frontend shows blank page**
- Check browser console for errors
- Ensure backend is running on port 8000
- Verify all environment variables are set

### **CORS errors**
- Backend has CORS enabled by default
- For production, update `allow_origins` in `app/main.py`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---


## 🙏 Acknowledgments

- **[FastAPI](https://fastapi.tiangolo.com/)** - For the amazing web framework
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - For workflow orchestration
- **[Groq](https://groq.com/)** - For ultra-fast LLM inference
- **[React](https://react.dev/)** - For the powerful UI library
- **[Tailwind CSS](https://tailwindcss.com/)** - For the utility-first CSS framework

---

## 📞 Contact & Support

- **GitHub:** [@Shubham00-3](https://github.com/Shubham00-3)
- **Repository:** [tailor-resume](https://github.com/Shubham00-3/tailor-resume)
- **Issues:** [Report a bug](https://github.com/Shubham00-3/tailor-resume/issues)

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ on GitHub!

---

<div align="center">

**Built with ❤️ using FastAPI, React, LangGraph, and Groq API**

[Report Bug](https://github.com/Shubham00-3/tailor-resume/issues) · [Request Feature](https://github.com/Shubham00-3/tailor-resume/issues)

</div>



