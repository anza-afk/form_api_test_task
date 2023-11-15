from fastapi import FastAPI

from db import db
from schema import RequestForm
from validators import validators

app = FastAPI()


@app.post('/get_form')
def api_data(model: RequestForm):
    request_form = model.model_dump()
    for form in db.all():
        # Проверкка вхождения всех полей из запроса в форму
        if all(key in form.keys() for key in request_form.keys()):
            # Валидация полей формы
            if all(
                validators[form.get(key)](value) for key, value
                in request_form.items() if form.get(key) != 'text'
            ):
                return form['name']

    # Если форма не найдена, то возвращаем типы полей формы из запроса
    result_form = {}
    for key, value in request_form.items():
        for validator in validators.values():
            if validator(value):
                result_form[key] = validator(value)
                break
            result_form[key] = 'text'
    return result_form
