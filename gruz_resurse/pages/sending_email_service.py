from django.core.mail import EmailMessage


def send_email(form_data, page_name):
    email = EmailMessage(
        subject=f'Нове повідомлення зі сторінки "{page_name}"',
        body=f"Ім'я відправника: {form_data['name']}\n"
             f"Номер телефону: {form_data['phone_number']}\n"
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
