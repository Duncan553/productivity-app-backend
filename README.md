# Productivity App Backend

A secure Flask REST API for tracking personal workouts. Users can register, log in, and manage their own workout entries. Built with Flask, SQLAlchemy, and session-based authentication.

---

## Installation

1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd productivity-app-backend
```

2. Install dependencies:
```bash
   pipenv install
   pipenv shell
```

3. Navigate to the server folder:
```bash
   cd server
```

4. Set up the database:
```bash
   flask db upgrade
```

5. Seed the database:
```bash
   python seed.py
```

---

## Running the App

```bash
python app.py
```

The API runs at `http://localhost:5555`

---

## API Endpoints

### Auth

| Method | Endpoint         | Description                      |
|--------|------------------|----------------------------------|
| POST   | `/signup`        | Register a new user              |
| POST   | `/login`         | Log in with username and password|
| DELETE | `/logout`        | Log out and clear session        |
| GET    | `/check_session` | Returns logged-in user or 401    |

### Workouts (Protected)

| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| GET    | `/workouts`        | Get your workouts (paginated) |
| POST   | `/workouts`        | Create a new workout          |
| PATCH  | `/workouts/<id>`   | Update one of your workouts   |
| DELETE | `/workouts/<id>`   | Delete one of your workouts   |

---

## Test Login (after seeding)

- **Username:** `trainer_joe`
- **Password:** `password123`
