## 🚀 Features

    📂 Upload documents, PDFs, and text snippets.
    🔄 Choose between RSVP mode (flashing words) or highlight mode.
    ⚡ Set your reading speed (WPM) and track progress.
    📊 Data-driven insights into reading habits and engagement.
    🔑 OAuth & JWT authentication for secure login.
    🧠 AI-assisted features (paid) for smarter reading assistance.

## 🏗 Tech Stack

### Frontend:

    React (Vite) ⚛️
    Tailwind CSS 🎨
    Redux (for state management) 🔄

### Backend:

    Django (Django Rest Framework) 🐍
    PostgreSQL (future database support) 🗄
    OAuth & JWT authentication 🔐
    AI integration (future paid feature) 🤖

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository

git clone https://github.com/your-username/spread.git
cd spread

### 2️⃣ Backend Setup (Django)

cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

API runs at: http://127.0.0.1:8000/api/


### 3️⃣ Frontend Setup (React)

cd frontend
npm install
npm run dev

Frontend runs at: http://localhost:5173/

## 📌 API Endpoints
Method	Endpoint	Description
POST	/api/auth/register	Register a new user
POST	/api/auth/login	Authenticate & receive JWT token
POST	/api/documents/upload	Upload a document
GET	/api/documents/list	Fetch all uploaded documents
POST	/api/reading/start	Start a reading session
POST	/api/reading/stop	Stop and save session progress
GET	/api/reading/{doc_id}/progress	Get user reading progress

## 💡 Future Enhancements

    AI-assisted phrase chunking for improved comprehension.
    Social features (reading challenges, leaderboards).
    Gamification to boost engagement.
    Personalized recommendations based on reading patterns.

## 🤝 Contributing

Want to contribute? PRs are welcome! 🚀

    Fork the repo.
    Create a new branch (feature-new-idea).
    Commit your changes.
    Submit a pull request!

## 🛠 License
This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.
