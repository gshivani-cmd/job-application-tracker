# Job Application Tracker

A full-stack web application built with Python and Flask to help job seekers organize, manage, and track their internship and job applications in one place.

## Features

- **Dashboard:** View total applications, awaiting responses, interviews, and selections.
- **Application Management:** Add, edit, and delete job applications.
- **Search:** Find applications by company name or job role.
- **Status Filtering:** Filter applications according to their current status.
- **Application Tracking:** Store company names, job roles, application dates, deadlines, statuses, and job links.
- **Interactive Interface:** Responsive dashboard styling with hover effects and status badges.
- **Dark Mode:** Switch between light and dark themes with the theme preference saved in the browser.
- **Notifications:** Automatically dismiss success messages after a few seconds.
- **Local Database:** Store application records using SQLite.

## Tech Stack

- **Programming Language:** Python
- **Backend Framework:** Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Version Control:** Git and GitHub
- **Development Environment:** Visual Studio Code

## Project Structure

```text
job-application-tracker/
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   ├── index.html
│   └── edit_application.html
└── static/
    ├── style.css
    └── script.js
```

## Installation and Setup

### Prerequisites

- Python installed on your computer
- Git installed on your computer

### 1. Clone the repository

```bash
git clone https://github.com/gshivani-cmd/job-application-tracker.git
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

Open the following address in your browser:

http://127.0.0.1:5000

## Database

The application uses SQLite to store job application records locally. The database is initialized by the application, and the local database file is excluded from version control.

## Key Learning Outcomes

- Built a web application using Python and Flask.
- Implemented create, read, update, and delete (CRUD) operations.
- Worked with SQLite and parameterized SQL queries.
- Implemented search and status filtering.
- Used SQL queries to calculate dashboard statistics.
- Integrated JavaScript for dark mode, theme persistence, and automatic notification dismissal.
- Organized project files and dependencies using a virtual environment and `requirements.txt`.
- Used Git and GitHub for version control.

## Future Improvements

- Add user authentication and individual user accounts.
- Add deadline reminders and application follow-up notifications.
- Deploy the application to a hosting platform.
- Add automated tests for application routes and database operations.

## Author

**G. Shivani**

GitHub: https://github.com/gshivani-cmd
