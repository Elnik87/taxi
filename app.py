import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<Contact %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        comment = request.form['comment']

        contact = Contact(name=name, last_name=last_name, phone=phone, comment=comment)
        try:
            db.session.add(contact)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"
    else:
        return render_template("contact.html")


@app.route('/admin/<int:id>/delete')
def delete(id):
    driver = Contact.query.get_or_404(id)
    try:
        db.session.delete(driver)
        db.session.commit()
        return redirect('/admin')
    except:
        return "Ошибка"


@app.route('/admin/<int:id>/create', methods=['POST', 'GET'])
def create(id):
    driver = Contact.query.get(id)

    if request.method == 'POST':
        driver.name = request.form['name']
        driver.last_name = request.form['last_name']
        driver.phone = request.form['phone']
        driver.comment = request.form['comment']
        try:
            db.session.commit()
            return redirect('/admin')
        except:
            return "Ошибка"

    return render_template("create.html", driver=driver)


@app.route('/klerjflsejtalsef;lasm;oete;rogmzxd;lfkeargj')
def admin():
    drivers = Contact.query.order_by(Contact.date.desc()).all()
    return render_template("admin.html", drivers=drivers)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Artem" and password == "12345":
            return redirect("/klerjflsejtalsef;lasm;oete;rogmzxd;lfkeargj")
        else:
            return redirect("/")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
