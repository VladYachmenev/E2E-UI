from page_store.page import StorePage


class TestStore:
    def test_store(self):
        store_page = StorePage()
        store_page.open_browser()
        store_page.authorization()
        store_page.add_product()
        store_page.go_to_shopping_cart()
        added_product = store_page.check_product()
        store_page.click_checkout()
        assert added_product == "Sauce Labs Backpack"
        store_page.fill_information()
        store_page.scroll()
        store_page.click_continue_button()
        store_page.scroll()
        store_page.click_finish_button()
        finally_inscriptions = store_page.check_finally_inscription()
        assert finally_inscriptions == "Thank you for your order!"

    def test_store_2(self):
        store_page = StorePage()
        store_page.open_browser()


