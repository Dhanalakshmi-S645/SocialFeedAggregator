# SocialFeedAggregator

SocialFeedAggregator is a full-stack web application that aggregates social media feeds into one unified platform. The project is structured into multiple components, including client, frontend, and backend directories.

---

## 🔧 Features

- 📰 Aggregate multiple social media feeds
- 👤 User authentication (login/signup)
- 💬 Like, comment, and interact with posts
- 📦 Modular structure with clear separation between frontend and backend
- 🛠 Built with MERN stack and Python (Django)

---

## 🗂 Project Structure
SocialFeedAggregator/
│
├── feeds/ # Feed processing logic
├── node_modules/ # Node.js dependencies
├── social-aggregator-client/ # Client-side logic (React or similar)
├── social-aggregator-frontend/ # Frontend UI files
├── social_aggregator/ # Django project (backend)
│
├── README.md # Project documentation
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
├── package.json # Node.js metadata
└── package-lock.json # Node.js dependency lock file
---

## ⚙️ Tech Stack

- **Frontend:** React.js
- **Backend:** Django (Python)
- **Database:** SQLite (for development)
- **Others:** Node.js, Express (if applicable), GitHub

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Dhanalakshmi-S645/SocialFeedAggregator.git
cd SocialFeedAggregator

*Set up Backend (Django)
  cd social_aggregator
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
*Set up Frontend (React)
  cd ../social-aggregator-frontend
    npm install
    npm start

