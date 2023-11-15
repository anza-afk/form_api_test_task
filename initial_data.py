from db import db

db.insert_multiple(
    [
        {
            "name": "User profile",
            "first_name": "text",
            "last_name": "text",
            "user_email": "email",
            "mobile_phone": "phone"
        },
        {
            "name": "Register form",
            "username": "text",
            "password": "text",
            "register_date": "date",
            "user_email": "email"
        },
        {
            "name": "Movie form",
            "title": "text",
            "release_date": "date",
        },
        {
            "name": "Contacts form",
            "mobile_phone": "phone",
            "home_phone": "phone",
            "personal_email": "email",
            "work_email": "email"
        },
        {
            "name": "Store book form",
            "author": "text",
            "title": "text",
            "added": "date"
        },
        {
            "name": "Store order form",
            "vendor_code": "text",
            "client_email": "email",
            "order_date": "date"
        }
    ]
)
