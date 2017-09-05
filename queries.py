import database


@database.connection_handler
def get_mentors_and_schools(cursor):
    cursor.execute(""" SELECT CONCAT (mentors.last_name, ' ', mentors.first_name) AS mentor_name,
                       schools.name AS school_name, schools.country AS school_country
                       FROM mentors
                       LEFT JOIN schools ON mentors.id=schools.contact_person ORDER BY mentors.id """)
    return cursor.fetchall()


@database.connection_handler
def get_schools_and_mentors(cursor):
    cursor.execute(""" SELECT schools.name AS school_name, schools.country AS school_country,
                       CONCAT (mentors.last_name, ' ', mentors.first_name) AS mentor_name
                       FROM schools
                       LEFT JOIN mentors ON schools.contact_person=mentors.id ORDER BY mentors.id """)
    return cursor.fetchall()


@database.connection_handler
def get_mentors_by_country(cursor):
    cursor.execute(""" SELECT COUNT (city) AS count
                       FROM mentors WHERE city = 'Budapest' OR city = 'Miskolc' """)
    result = cursor.fetchall()
    result[0].update({'country': 'Hungary'})
    cursor.execute(""" SELECT COUNT (city) AS count
                       FROM mentors WHERE city = 'Krakow' """)
    result.append(cursor.fetchall()[0])
    result[1].update({'country': 'Poland'})
    return result


@database.connection_handler
def get_contacts(cursor):
    cursor.execute(""" SELECT schools.name AS school_name,
                       CONCAT (mentors.last_name, ' ', mentors.first_name) AS mentor_name
                       FROM schools
                       INNER JOIN mentors ON schools.contact_person=mentors.id
                       ORDER BY schools.name  """)
    return cursor.fetchall()


@database.connection_handler
def get_applicants(cursor):
    cursor.execute(""" SELECT applicants.first_name AS name, applicants.application_code,
                       applicants_mentors.creation_date AS date
                       FROM applicants
                       INNER JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                       WHERE applicants_mentors.creation_date >= '2016-01-01' """)
    return cursor.fetchall()


@database.connection_handler
def get_applicants_mentors(cursor):
    cursor.execute(""" SELECT applicants.first_name AS applicant_name, applicants.application_code,
                       CONCAT (mentors.last_name, ' ', mentors.first_name) AS mentor_name
                       FROM applicants
                       LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                       LEFT JOIN mentors ON applicants_mentors.mentor_id=mentors.id
                       ORDER BY applicants.id """)
    return cursor.fetchall()
