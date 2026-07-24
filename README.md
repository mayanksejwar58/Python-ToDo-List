# 📋 To-Do List App

A modern **Task Management Web Application** built using **Python**, **Streamlit**, and **Supabase** with secure authentication and cloud-based data storage.

---

## 🚀 Features

- 👤 User Registration
- 🔐 Secure Login
- 🔑 Password Hashing using bcrypt
- 📧 Forgot Password (OTP via Email)
- 🔒 Change Password
- ➕ Add Tasks
- ✏️ Edit Tasks
- 🗑 Delete Tasks
- ✅ Mark Tasks as Completed
- 🔍 Search Tasks
- 📅 Due Date & Time
- 🏷 Categories
- ⚡ Priority Levels
- 📊 Dashboard Statistics
- ☁️ Cloud Database (Supabase)

---

## 🛠 Tech Stack

- Python
- Streamlit
- Supabase (PostgreSQL)
- bcrypt
- python-dotenv
- SMTP (Gmail)

---

## 📂 Project Structure

```
To-Do_List_App
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── config.toml
│
├── database/
│   ├── auth.py
│   ├── database.py
│   ├── email_service.py
│   └── task_db.py
│
├── pages/
│   ├── login.py
│   ├── register.py
│   ├── dashboard.py
│   ├── forgot_password.py
│   └── change_password.py
│
├── models/
│   ├── task.py
│   └── user.py
│
└── services/
    └── task_manager.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/mayanksejwar58/Python-ToDo-List.git
```

Move into the project

```bash
cd Python-ToDo-List
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.streamlit/secrets.toml` file

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"

EMAIL_ADDRESS="YOUR_EMAIL"
EMAIL_PASSWORD="YOUR_GMAIL_APP_PASSWORD"
```

Run the application

```bash
streamlit run app.py
```

---

## 🌟 Highlights

- Object-Oriented Programming (OOP)
- Secure Authentication
- Cloud Database using Supabase
- Password Encryption with bcrypt
- Email OTP Verification
- Clean Streamlit UI
- Multi-user Support
- Persistent Cloud Storage

---

## 🚀 Future Improvements

- Dark Mode
- Task Notifications
- Calendar Integration
- AI Task Suggestions
- Mobile Responsive UI
- User Profile Management

---

## 👨‍💻 Author

**Mayank Sejwar**

B.Tech Artificial Intelligence & Data Science

Madhav Institute of Technology & Science (MITS), Gwalior

GitHub: https://github.com/mayanksejwar58

---

## 📄 License

This project is released under the MIT License.