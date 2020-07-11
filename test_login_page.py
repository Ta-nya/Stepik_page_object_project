from .pages.login_page import LoginPage

login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/" # заменить ссылку или модернизировать ее так чтобы можно было задавать значение языка

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, login_link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_form()          # выполняем метод страницы - проверяем наличие формы авторизации

def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, login_link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_register_form() # выполняем метод страницы - проверяем наличие формы регистрации

def test_should_be_login_url(browser):
    page = LoginPage(browser, login_link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_url() # выполняем метод страницы - проверяем что это страница логин