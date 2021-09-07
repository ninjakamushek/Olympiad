from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    patronymic = StringField('Отчество')
    city = StringField('Город', validators=[DataRequired()])
    grade = IntegerField('Класс', validators=[DataRequired()])
    reason = StringField('Почему вы хотите участвовать на олимпиаде?', validators=[DataRequired()])
    benefit = StringField('Что вы собираетесь извлечь после(из) участия в олимпиаде?', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
