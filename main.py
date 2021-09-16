import os

from flask import Flask, render_template
from data import db_session
from RegistrationForm import RegistrationForm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Olympiad'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form, message="Такой пользователь уже есть")
        user = User()
        user.email = form.email.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.patronymic = form.patronymic.data
        user.city = form.city.data
        user.grade = form.grade.data
        user.reason = form.reason.data
        user.benefit = form.benefit.data
        session.add(user)
        session.commit()
    return render_template('index.html', title='Регистрация', form=form)

def main():
    db_session.global_init("db/Olympiad.sqlite")

if __name__ == '__main__':
    main()
