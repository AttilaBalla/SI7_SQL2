from flask import Flask, render_template, redirect, request, session
import csv
import queries


app = Flask(__name__)


@app.route('/')
def index():
    title = "Click on a button display query results"
    return render_template('form.html', title=title)


@app.route('/mentors')
def mentors():
    title = "Mentors and schools"
    order = ['mentor_name', 'school_name', 'school_country']
    data = queries.get_mentors_and_schools()
    return render_template('form.html', title=title, data=data, order=order)


@app.route('/all-school')
def all_school():
    title = "All schools"
    order = ['school_name', 'school_country', 'mentor_name']
    data = queries.get_schools_and_mentors()
    for row in data:
        if (row['mentor_name'] == ' '):
            row['mentor_name'] = '- no data -'
    return render_template('form.html', title=title, data=data, order=order)


@app.route('/mentors-by-country')
def mentors_by_country():
    title = "Mentors by country"
    order = ['country', 'count']
    data = queries.get_mentors_by_country()
    return render_template('form.html', title=title, data=data, order=order)


@app.route('/contacts')
def contacts():
    title = "Contacts"
    order = ['school_name', 'mentor_name']
    data = queries.get_contacts()
    return render_template('form.html', title=title, data=data, order=order)


@app.route('/applicants')
def applicants():
    title = "Recent Applicants"
    order = ['name', 'application_code', 'date']
    data = queries.get_applicants()
    return render_template('form.html', title=title, data=data, order=order)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    title = "Assigned Applicants"
    order = ['applicant_name', 'application_code', 'mentor_name']
    data = queries.get_applicants_mentors()
    for row in data:
        if (row['mentor_name'] == ' '):
            row['mentor_name'] = '- no data -'
    return render_template('form.html', title=title, data=data, order=order)


if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
