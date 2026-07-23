# 📋 To-Do List App

A modern To-Do List web application built using **Python**, **Streamlit**, **SQLite**, and **OOP** principles.

## ✨ Features

- 👤 User Registration & Login
- 🔒 Secure Password Hashing (bcrypt)
- 📧 Forgot Password using Email OTP
- 🔑 Change Password
- ➕ Add Tasks
- ✏️ Edit Tasks
- 🗑 Delete Tasks
- ✅ Mark Tasks as Completed
- 🔍 Search Tasks
- 📊 Task Statistics Dashboard
- 📅 Due Date & Time
- 🏷 Task Categories
- ⚡ Priority Levels

---

## 🛠 Tech Stack

- Python
- Streamlit
- SQLite
- bcrypt
- python-dotenv
- SMTP (Gmail)

---

## 📂 Project Structure

```
To-Do_List_App/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── todo.db
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

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-ToDo-List.git
```

Go to the project folder:

```bash
cd python-ToDo-List
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your_google_app_password
```

---

## 📸 Features

- Secure User Authentication
- Email OTP Verification
- Password Reset
- Task Management
- Search Functionality
- Progress Tracking
- Responsive Streamlit Interface

---

## 👨‍💻 Author

**Mayank Sejwar**

B.Tech Artificial Intelligence & Data Science  
Madhav Institute of Technology & Science (MITS), Gwalior

---

## 📄 License

This project is created for educational and portfolio purposes.