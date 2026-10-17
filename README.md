# Job Application Tracker

A Python-based web application that helps job seekers organize and track their internship and job applications in one place.

## Features

- Add new job applications.
- Edit application details and update statuses.
- Delete applications.
- Search applications by company name or job role.
- Filter applications by status.
- View dashboard statistics for total applications, applications awaiting response, interviews, and selections.
- Store application records locally using SQLite.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Tools:** Visual Studio Code, Git, GitHub

## Project Structure

```text
job-application-tracker/
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    ├── index.html
    └── edit_application.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd job-application-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Database

The application automatically initializes a local SQLite database when it starts. Application data is stored locally and is not included in the GitHub repository.

## Learning Outcomes

- Developed a web application using Flask.
- Implemented CRUD operations with SQLite.
- Used parameterized SQL queries for database operations.
- Built search and status-filtering functionality.
- Created dynamic dashboard statistics using SQL aggregation.
- Organized a Python project using a virtual environment and dependency file.

## Future Improvements

- Add user authentication.
- Add application deadlines and reminders.
- Improve responsive styling and accessibility.
- Deploy the application securely.

## Author

G. Shivani