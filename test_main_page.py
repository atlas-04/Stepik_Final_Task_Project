from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                # открываем страницу
    page.should_be_login_link()    # выполняем метод страницы — проверяем есть ли на стронице кнопка "Войти или зарегистрироваться"


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                # открываем страницу
    page.go_to_login_page()    # выполняем метод страницы — переходим на страницу логина
    
    
def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                # открываем страницу
    page.should_be_login_page()    # выполняем методы страницы — 1. проверяем в url стр, есть ли login в url, есть ли форма для логина и форма для регистрации

