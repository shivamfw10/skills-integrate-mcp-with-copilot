# Mergington High School Activities API 🏫

A complete FastAPI application that allows students to view and sign up for extracurricular activities at Mergington High School.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation & Running

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   
   **Option A - Using the startup script (Recommended):**
   ```bash
   python start_server.py
   ```
   
   **Option B - Direct execution:**
   ```bash
   cd src
   python app.py
   ```
   
   **Option C - Using uvicorn directly:**
   ```bash
   cd src
   uvicorn app:app --host 127.0.0.1 --port 8000 --reload
   ```

4. **Access the application:**
   - **Web Interface:** http://localhost:8000
   - **API Documentation:** http://localhost:8000/docs
   - **Alternative API Docs:** http://localhost:8000/redoc

## 🎯 Features

- ✅ **View Activities:** Browse all available extracurricular activities
- ✅ **Sign Up:** Students can sign up for activities using their email
- ✅ **Capacity Management:** Prevents signups when activities are full
- ✅ **Duplicate Prevention:** Stops students from signing up twice
- ✅ **Unregister:** Students can unregister from activities
- ✅ **Web Interface:** User-friendly web interface
- ✅ **Real-time Updates:** Participant lists update immediately
- ✅ **API Documentation:** Complete OpenAPI/Swagger docs

## 📋 Available Activities

The system comes pre-loaded with these activities:

- **Chess Club** - Fridays, 3:30-5:00 PM (12 spots)
- **Programming Class** - Tuesdays & Thursdays, 3:30-4:30 PM (20 spots)
- **Gym Class** - Mon/Wed/Fri, 2:00-3:00 PM (30 spots)
- **Soccer Team** - Tuesdays & Thursdays, 4:00-5:30 PM (22 spots)
- **Basketball Team** - Wednesdays & Fridays, 3:30-5:00 PM (15 spots)
- **Art Club** - Thursdays, 3:30-5:00 PM (15 spots)
- **Drama Club** - Mondays & Wednesdays, 4:00-5:30 PM (20 spots)
- **Math Club** - Tuesdays, 3:30-4:30 PM (10 spots)
- **Debate Team** - Fridays, 4:00-5:30 PM (12 spots)

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/activities` | Get all activities with participant counts |
| `POST` | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity |
| `DELETE` | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister from an activity |
| `GET` | `/` | Web interface (redirects to `/static/index.html`) |
| `GET` | `/docs` | Interactive API documentation |

## 🧪 Testing

You can test the API using the included test script:

```bash
python test_api.py
```

Or test manually using curl:

```bash
# Get all activities
curl http://localhost:8000/activities

# Sign up for Chess Club
curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=test@mergington.edu"

# Unregister from Chess Club  
curl -X DELETE "http://localhost:8000/activities/Chess%20Club/unregister?email=test@mergington.edu"
```

## 📁 Project Structure

```
├── src/
│   ├── app.py              # Main FastAPI application
│   ├── static/
│   │   ├── index.html      # Web interface
│   │   ├── app.js         # Frontend JavaScript
│   │   └── styles.css     # Styling
│   └── README.md          # Technical documentation
├── requirements.txt        # Python dependencies
├── start_server.py        # Easy startup script
├── test_api.py           # API testing script
└── README.md             # This file
```

## 💾 Data Storage

The application uses **in-memory storage**, which means:
- ✅ Fast performance
- ✅ No database setup required  
- ⚠️  Data resets when server restarts
- ⚠️  Not suitable for production use

For production deployment, consider integrating with a database like PostgreSQL, SQLite, or MongoDB.

## 🎨 Web Interface Features

The web interface provides:
- 📋 Live activity listings with participant counts
- ✉️ Easy signup form with email validation  
- 🗑️ One-click unregister buttons
- ✅ Success/error message feedback
- 📱 Responsive design for mobile devices

## 🔒 Validation & Error Handling

The API includes comprehensive validation:
- ✅ Activity existence checking
- ✅ Capacity limit enforcement  
- ✅ Duplicate signup prevention
- ✅ Email format validation (frontend)
- ✅ Proper HTTP status codes
- ✅ Descriptive error messages

## 🚀 Next Steps for Production

To make this production-ready, consider:

1. **Database Integration:** Replace in-memory storage
2. **User Authentication:** Add login/registration system
3. **Admin Panel:** Activity management interface
4. **Email Notifications:** Signup confirmations
5. **Advanced Features:** Waitlists, recurring events, etc.
6. **Testing:** Comprehensive test suite
7. **Deployment:** Docker containerization

---

**Made with ❤️ for Mergington High School students**