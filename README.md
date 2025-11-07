# 📰 News Headlines App – CI/CD Pipeline using Jenkins

## 📖 Project Overview
This is a simple Flask web app that displays the latest top headlines from the News API.
It demonstrates a complete CI/CD pipeline using **Jenkins**:
1. Code hosted on GitHub
2. Jenkins pulls code automatically
3. Installs dependencies
4. Runs tests
5. Deploys the Flask app automatically

---

## 🧩 Tech Stack
- **Python 3.9+**
- **Flask** (Web framework)
- **Requests** (API calls)
- **Jenkins** (CI/CD pipeline)
- **GitHub** (Source control)
- **NewsAPI.org** (Fetches headlines)

---

## ⚙️ Setup Instructions

### 1️⃣ Get a NewsAPI Key
Create a free account and get your API key:  
👉 [https://newsapi.org/register](https://newsapi.org/register)

---

### 2️⃣ Set the Environment Variable
Before running the app, set your News API key:

**Windows PowerShell:**
```powershell
setx NEWSAPI_KEY "your_api_key_here"
