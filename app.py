#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, flash
import db_functions

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index_page():
    data = {
        "title": "Add message",
        "info": "Add a message!"
    }

    return render_template("index.html", data=data);

@app.route('/recreate')
def recreate_db():
    db_functions.recreate_db()
    flash("Database is recreated.")

    return redirect("/", code=302);

@app.route('/process', methods=["POST"])
def process_form():
    input_data = request.form;
    db_functions.add_to_database(input_data)
    flash("Added data")
    return redirect("/result", code=302);

@app.route('/result')
def result_page():
    data = {
        "title": "Read messages",
        "info": "This is your messages",
        "messages": db_functions.get_all_from_database()
    }

    return render_template("result.html", data=data);

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
