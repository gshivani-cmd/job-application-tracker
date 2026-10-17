
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_connection, init_db

app = Flask(__name__)
app.secret_key = "dev-key-change-before-deployment"

STATUSES = [
    "Applied",
    "Assessment",
    "Interview",
    "Selected",
    "Rejected"
]

init_db()


@app.route("/")
def home():
    search_query = request.args.get("search", "").strip()
    selected_status = request.args.get("status", "").strip()

    connection = get_connection()

    statistics = connection.execute("""
        SELECT
            COUNT(*) AS total,
            SUM(CASE
                WHEN status IN ('Applied', 'Assessment')
                THEN 1 ELSE 0
            END) AS awaiting_response,
            SUM(CASE
                WHEN status = 'Interview'
                THEN 1 ELSE 0
            END) AS interviews,
            SUM(CASE
                WHEN status = 'Selected'
                THEN 1 ELSE 0
            END) AS selected
        FROM applications
    """).fetchone()

    sql = "SELECT * FROM applications"
    conditions = []
    parameters = []

    if search_query:
        conditions.append("(company LIKE ? OR role LIKE ?)")
        search_pattern = f"%{search_query}%"
        parameters.extend([search_pattern, search_pattern])

    if selected_status not in STATUSES:
        selected_status = ""

    if selected_status:
        conditions.append("status = ?")
        parameters.append(selected_status)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " ORDER BY id DESC"

    applications = connection.execute(
        sql, parameters
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        applications=applications,
        statuses=STATUSES,
        today=date.today().isoformat(),
        search_query=search_query,
        selected_status=selected_status,
        statistics=statistics
    )



@app.route("/add", methods=["POST"])
def add_application():
    company = request.form.get("company", "").strip()
    role = request.form.get("role", "").strip()
    application_date = request.form.get("application_date", "").strip()
    deadline = request.form.get("deadline", "").strip()
    job_url = request.form.get("job_url", "").strip()
    status = request.form.get("status", "Applied").strip()
    notes = request.form.get("notes", "").strip()

    if not company or not role or not application_date:
        flash("Please fill in all required fields.")
        return redirect(url_for("home"))

    try:
        date.fromisoformat(application_date)

        if deadline:
            date.fromisoformat(deadline)
    except ValueError:
        flash("Please enter valid dates.")
        return redirect(url_for("home"))

    if status not in STATUSES:
        flash("Please select a valid application status.")
        return redirect(url_for("home"))

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO applications
        (company, role, application_date, deadline, job_url, status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            company,
            role,
            application_date,
            deadline or None,
            job_url or None,
            status,
            notes or None
        )
    )

    connection.commit()
    connection.close()

    flash("Application saved successfully!")
    return redirect(url_for("home"))

@app.route("/edit/<int:application_id>", methods=["GET", "POST"])
def edit_application(application_id):
    connection = get_connection()

    application = connection.execute(
        "SELECT * FROM applications WHERE id = ?",
        (application_id,)
    ).fetchone()

    if application is None:
        connection.close()
        flash("Application not found.")
        return redirect(url_for("home"))

    if request.method == "POST":
        company = request.form.get("company", "").strip()
        role = request.form.get("role", "").strip()
        application_date = request.form.get("application_date", "").strip()
        deadline = request.form.get("deadline", "").strip()
        job_url = request.form.get("job_url", "").strip()
        status = request.form.get("status", "").strip()
        notes = request.form.get("notes", "").strip()

        if (
            not company
            or not role
            or not application_date
            or len(company) > 150
            or len(role) > 150
            or len(notes) > 2000
        ):
            connection.close()
            flash("Please check the required fields and field lengths.")
            return redirect(url_for(
                "edit_application",
                application_id=application_id
            ))

        try:
            date.fromisoformat(application_date)

            if deadline:
                date.fromisoformat(deadline)
        except ValueError:
            connection.close()
            flash("Please enter valid dates.")
            return redirect(url_for(
                "edit_application",
                application_id=application_id
            ))

        if status not in STATUSES:
            connection.close()
            flash("Please select a valid status.")
            return redirect(url_for(
                "edit_application",
                application_id=application_id
            ))

        connection.execute(
            """
            UPDATE applications
            SET company = ?,
                role = ?,
                application_date = ?,
                deadline = ?,
                job_url = ?,
                status = ?,
                notes = ?
            WHERE id = ?
            """,
            (
                company,
                role,
                application_date,
                deadline or None,
                job_url or None,
                status,
                notes or None,
                application_id
            )
        )

        connection.commit()
        connection.close()

        flash("Application updated successfully!")
        return redirect(url_for("home"))

    connection.close()

    return render_template(
        "edit_application.html",
        application=application,
        statuses=STATUSES
    )


@app.route("/delete/<int:application_id>", methods=["POST"])
def delete_application(application_id):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )

    connection.commit()
    connection.close()

    if cursor.rowcount:
        flash("Application deleted successfully!")
    else:
        flash("Application not found.")

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
