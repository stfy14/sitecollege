from flask_sqlalchemy import SQLAlchemy
from models import db, Contacts
import requests

def import_data_from_url(url):
    db.drop_all()
    db.create_all()
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()

    for item in json_data['value']:
        number_phones = []
        for list in item['КонтактнаяИнформация']:
            NumberPhoneTemp = list.get('НомерТелефона', None)
            if NumberPhoneTemp:
                number_phones.append(NumberPhoneTemp)
        NumberPhone = ', '.join(number_phones)
        new_contacts = Contacts(
            Description=item.get('ФИО'),
            Sex=item.get('Пол'),
            NumberPhone=NumberPhone,
            DateLife=item.get('ДатаРождения')
        )
        db.session.add(new_contacts)
    db.session.commit()

