
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                # открываем страницу
    page.should_be_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_in_basket()
    page.name_equal()
