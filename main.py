import os
import mysql.connector
from flask import Flask, render_template, request, flash, redirect, url_for
from logging import FileHandler, WARNING

app = Flask(__name__)

app.secret_key = os.urandom(24)


from flask import request, jsonify
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyBK48Ys3UfJrIU1X1dOuYboXd0APpFhaIw")
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route('/ask', methods=['POST'])
def ask_bot():
    data = request.json
    question = data.get('question', '')

    try:
        response = model.generate_content(
            f"You are a cricket expert assistant. Answer this question: {question}"
        )
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'response': f"Sorry, I couldn't process that request. Error: {str(e)}"})


def db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",  # Change this to your MySQL username
        password="root",  # Change this to your MySQL password
        database="newsinfo",
        charset = "utf8"
    )




@app.route('/')
def home():
    return render_template('Homepage.html')


@app.route('/about')
def about():
    return render_template('Aboutus.html')



@app.route('/contact')
def contact():
    return render_template('Contactus.html')



@app.route('/adminhome')
def adminhome():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matches")
    matches = cursor.fetchall()
    conn.close()
    return render_template('Adminhome.html', matches=matches)


@app.route('/add_match', methods=['POST'])
def add_match():
    if request.method == "POST":
        team1 = request.form['team1']
        team2 = request.form['team2']
        match_date = request.form['match_date']
        venue = request.form['venue']

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO matches (team1, team2, match_date, venue) VALUES (%s, %s, %s, %s)",
                       (team1, team2, match_date, venue))
        conn.commit()
        conn.close()

        flash("Match Added Successfully!", "success")
        return redirect(url_for('adminhome'))


@app.route('/delete_match/<int:match_id>', methods=['GET'])
def delete_match(match_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM matches WHERE match_id=%s", (match_id,))
    conn.commit()
    conn.close()
    flash("Match Deleted Successfully!", "success")
    return redirect(url_for('adminhome'))


@app.route('/update_match/<int:match_id>', methods=['POST'])
def update_match(match_id):
    status = request.form['status']
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE matches SET status=%s WHERE match_id=%s", (status, match_id))
    conn.commit()
    conn.close()
    flash("Match Updated Successfully!", "success")
    return redirect(url_for('adminhome'))


@app.route('/update_score', methods=['POST'])
def update_score():
    match_id = request.form['match_id']
    team = request.form['team']
    runs = request.form['runs']
    wickets = request.form['wickets']
    overs = request.form['overs']

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO scores (match_id, team, runs, wickets, overs) VALUES (%s, %s, %s, %s, %s)",
                   (match_id, team, runs, wickets, overs))
    conn.commit()
    conn.close()
    flash("Score Updated Successfully!", "success")
    return redirect(url_for('adminhome'))


@app.route('/view_scores')
def view_scores():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores")
    scores = cursor.fetchall()
    conn.close()
    return render_template('view_scores.html', scores=scores)


@app.route('/categorynews')
def categorynews():
    return render_template('Categorynews.html')


@app.route('/uploadnews')
def uploadnews():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("select MAX(Newsid) from newsdetails")
    data = cursor.fetchone()
    rid = data[0]
    if rid == None:
        rid = "1"
        print(rid)
    else:
        rid = rid + 1
    conn.close()
    return render_template('uploadnews.html', Newsid=rid)


@app.route('/Register')
def Register():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("select MAX(Regid) from Register")
    data = cursor.fetchone()
    rid = data[0]
    if rid == None:
        rid = "1"
        print(rid)
    else:
        rid = rid + 1
        flash("Registration Successfully!", "success")  # Flash success message
    conn.close()
    return render_template('Register.html', Regid=rid)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        try:
            Regid = request.form['Regid']
            rname = request.form['rname']
            contact = request.form['contact']
            email = request.form['email']
            Address = request.form['Address']
            city = request.form['city']
            role = request.form['role']
            uname = request.form['uname']
            password = request.form['password']

            conn = db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO register (rname, contact, email, Address, city, role, uname, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                (rname, contact, email, Address, city, role, uname, password))
            conn.commit()
            conn.close()

            flash("Data Inserted Successfully")
            return redirect(url_for('Register'))
        except Exception as e:
            print(e)
        return render_template('Register.html')


@app.route('/insertnews', methods=['POST'])
def insertnews():
    if request.method == "POST":
        Newsid = request.form['Newsid']
        newshead = request.form['newshead']
        upload = request.form['dateinfo']
        category = request.form['category']
        Description = request.form['Description']

        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO newsdetails (Newsid, newshead, upload, category, Description) VALUES(%s, %s, %s, %s, %s)",
            (Newsid, newshead, upload, category, Description))
        conn.commit()
        conn.close()

        flash("News Detail Upload Successfully!", "success")  # Flash success message
        return render_template('Adminhome.html')


@app.route('/checklogin', methods=['POST'])
def checklogin():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        utype = request.form['utype']
        print(utype)
        if username == 'Admin' and password == 'Admin' and utype == 'Admin':
            return redirect(url_for('adminhome'))
        if utype == "User":
            conn = db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT rname, password FROM register WHERE uname = %s AND password = %s",
                (username, password))
            account = cursor.fetchone()
            conn.close()

            if account:
                flash("Login Successfully!", "success")  # Flash success message
                return redirect(url_for('userhome'))
            else:
                flash("Login Failed!", "success")  # Flash success message
                return render_template('login.html')


@app.route('/userhome')
def userhome():
    conn = db_connection()
    cursor = conn.cursor()

    # Get all matches
    cursor.execute("SELECT * FROM matches")
    matches = cursor.fetchall()

    # Get all scores
    cursor.execute("SELECT * FROM scores")
    scores = cursor.fetchall()

    # Create a dictionary to easily match scores with matches
    scores_dict = {}
    for score in scores:
        match_id = score[0]
        team = score[1]
        if match_id not in scores_dict:
            scores_dict[match_id] = {}
        scores_dict[match_id][team] = {
            'runs': score[2],
            'wickets': score[3],
            'overs': score[4]
        }

    conn.close()
    return render_template('Userhome.html', matches=matches, scores_dict=scores_dict)


@app.route('/viewnews')
def viewnews():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM newsdetails")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('viewnews.html', postlist=result)


@app.route('/viewnewsuser')
def viewnewsuser():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM newsdetails")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('viewnewsuser.html', postlist=result)


@app.route('/getcategory', methods=['POST'])
def getcategory():
    conn = db_connection()
    cursor = conn.cursor()
    Sports = request.form['category']
    print("category: " + Sports)
    cursor.execute("SELECT * FROM newsdetails WHERE category = %s", (Sports,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('viewnews1.html', postlist=data)


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/Logout')
def Logout():
    return render_template('Login.html')

@app.route('/logout')
def logout():
    session.clear()  # If you're using sessions
    return redirect(url_for('login'))



if __name__ == "__main__":
    # app.run(host='localhost', port=5000)
    app.run()

# pip install Flask-Session