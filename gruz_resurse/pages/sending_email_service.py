from django.core.mail import EmailMessage


def send_email(form_data):
    email = EmailMessage(
        subject=f"Повідомлення від користувача на ім'я {form_data['name']}",
        body=f"Номер телефону: {form_data['phone_number']}\n"
             f"Email: {form_data['email']}\n"
             f"Повідомлення: {form_data['message']}",
        from_email="km2022tm@gmail.com",
        to=[
            "www.vladik49@gmail.com"
        ],
    )

    for photo in form_data['photos']:
        email.attach(photo.name, photo.read(), photo.content_type)
    email.send()


def send_feedback_email(form_data):
    email = EmailMessage(
        subject=f"Повідомлення від користувача на ім'я {form_data['name']}",
        body=f"Зателефонуйте мені в період між {form_data['time_range_1'] // 60 + 8}:00 "
             f"і {form_data['time_range_2'] // 60 + 8}:00\n"
             f"Номер телефону: {form_data['phone_number']}\n"
             f"Email: {form_data['email'] if form_data['email'] else 'Не вказана користувачем'}\n",
        from_email="km2022tm@gmail.com",
        to=[
            "www.vladik49@gmail.com"
        ],
    )
    email.send()
