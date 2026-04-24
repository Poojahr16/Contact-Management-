# 📇 Contact Management System (Flask)

A simple and user-friendly **Contact Management System** built using **Flask** and **SQLite**.
This application allows users to register, log in, and manage their personal contacts efficiently.

---

## 🚀 Features

* 👤 User Registration & Login
* 🔐 Session-based Authentication
* 📇 Add, Edit, Delete Contacts
* 👥 User-specific Contact Storage
* 💾 SQLite Database Integration
* 🎨 Simple and Clean UI

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite
* **Frontend:** HTML, CSS (Jinja Templates)

---

## 📁 Project Structure

```
contact_manager/
│── app.py
│── database.db
│
├── templates/
│   │── base.html
│   │── login.html
│   │── register.html
│   │── dashboard.html
│   │── add_contact.html
│   │── edit_contact.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup



### Install Dependencies

```bash
pip install flask
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000/register
```

---

## 🧠 How It Works

* Users can **register and log in** to their account
* Each user gets a **separate contact list**
* Contacts can be:

  * ➕ Added
  * ✏️ Edited
  * ❌ Deleted

---

## 🔒 Security Note

⚠️ Currently, passwords are stored in plain text (for learning purpose).
For production use, implement password hashing:

```python
from werkzeug.security import generate_password_hash, check_password_hash
```

---

## 🚀 Future Improvements

* 🔍 Search Contacts
* 📱 Responsive UI (Bootstrap)
* ☁️ Deployment (Render / Railway)
* 🔐 Password Hashing
* 📊 Pagination

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

