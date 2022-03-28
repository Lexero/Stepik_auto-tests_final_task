from .base_page import BasePage


class MainPage(BasePage):
    """
    Заглушка для класса MainPage, благодаря которой наследуются все методы из MainPage
    Метод __init__ вызывается при создании объекта.
    Конструктор с ключевым словом super только вызывает конструктор класса предка и передает ему все те аргументы,
    которые были переданы в конструктор MainPage.
    """
    def __init__(self, *args, **kwargs):    # Конструкцию можно заменить одним pass
        super(MainPage, self).__init__(*args, **kwargs)
    # pass
