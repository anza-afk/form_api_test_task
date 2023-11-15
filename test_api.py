import httpx

URL = 'http://127.0.0.1:8000/get_form'


def test_api(data: dict) -> dict:
    return httpx.post(URL, json=data).text


test_data = [
    {
        "username": "anza",
        "password": "pass777",
        "register_date": "28-09-1988",
        "user_email": "zapokami@gmail.com"
    },
    {
        "username": "anza",
        "password": "help",
        "register_date": "28-09-1988",
        "user_email": "email.ru"
    },
    {
        "username": "anza",
        "password": "help",
        "register_date": "a8-09-1988",
        "user_email": "zapokami@gmail.com"
    },
    {
        "mobile_phone": "+7916 000 55 44",
        "home_phone": "+7999 111 55 44",
        "personal_email": "zapokami@gmail.com"
    },
    {
        "mobile_phone": "7916 000 55 44",
        "home_phone": "+7999 111 55 44",
    },
    {
        "author": "Jerome Salinger",
        "title": "The Catcher in the Rye",
        "added": "20.11.2000"
    },
    {
        "vendor_code": "1783092-1-11",
        "client_email": "zapokami@gmail@com",
        "order_date": "20.11.2000"
    },
    {
        "vendor_code": "1783092-1-11",
        "client_email": "zapokami@gmail.com",
        "order_date": "20.11.2000"
    },
    {
        "title": "Dr. No",
        "release_date": "06.10.1962",
    },
    {
        "home_phone": "79104022100",
        "personal_email": "zapokami@gmail.com",
        "work_email": "zapokami@gmail.com"
    },
    {
        "first_name": "Anatoly",
        "last_name": "Zapravadov",
        "user_email": "zapokami@gmail.com",
        "mobile_phone": "+79104022100"
    },
    {
        "first_name": "Anatoly",
        "last_name": "Zapravadov",
        "favorite_food": "pizza",
        "mobile_phone": "+79104022100"
    },
    {
        "title": "Dr. No",
        "release_date": "06.10.1962",
        "main_actor": 'Sean Connery'
    },
    {
        "vendor_code": "1783092-1-11",
        "client_email": "zapokami@gmail@com",
        "order_date": "20.11.2000",
        "reserved": "True"
    },
]


if __name__ == "__main__":
    for data in test_data:
        print(test_api(data))
