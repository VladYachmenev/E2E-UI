from faker import Faker


class UserData:
    faker_ru = Faker('ru_RU')
    username = "standard_user"
    password = "secret_sauce"
    first_name = faker_ru.first_name()
    last_name = faker_ru.last_name()
    postal_code = '123456'
