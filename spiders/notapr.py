import scrapy
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class ProductSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['menorpreco.notaparana.pr.gov.br']
    start_urls = [
        'https://menorpreco.notaparana.pr.gov.br/app/combustivel']

    def __init__(self, city):
        self.city = city
        self.driver = webdriver.Firefox()

    def parse(self, response):

        self.driver.get(response.url)

        time.sleep(3)

        actions = ActionChains(self.driver)

        # while True:
        # next = self.driver.find_element_by_xpath(
        #     '//*[@id="header-info"]/div[2]/button[2]')
        try:
            # next.click()

            # city = self.driver.find_element_by_xpath(
            #     '//*[@id="md-input-3"]')
            # city.send_keys(self.city)

            # submit_city = self.driver.find_element_by_xpath(
            #     '//*[@id="cdk-overlay-0"]/md-dialog-container/web-location/div/form/div[3]/button[1]/span')
            # submit_city.click()

            # time.sleep(3)

            showsidebar = self.driver.find_element_by_xpath(
                '/html/body/web-root/div/div/app-root/app-header/md-card/md-card-content/div/button[2]/span/md-icon')
            showsidebar.click()
            time.sleep(2)
            show_products = self.driver.find_element_by_xpath(
                '/html/body/web-root/div/div/app-root/md-sidenav-container/md-sidenav/app-list/div/div[1]/div/p-datalist/div/div/ul/li[1]')
            show_products.click()

            time.sleep(5)

            scroll = self.driver.find_element_by_xpath(
                '/html/body/web-root/div/div/app-root/md-sidenav-container/md-sidenav/app-list/div/div[2]')

            self.driver.execute_script(
                "arguments[0].style='background: rgb(0, 0, 0); width: 7px; position: absolute; top: 1000px; opacity: 0; transition: opacity 0.3s ease 0s; display: block; border-radius: 7px; z-index: 99; right: 1px; height: 30px;'", scroll)

            # actions.drag_and_drop_by_offset(scroll, 400, 400)
            # actions.perform()

            time.sleep(0.5)
            list_products = self.driver.find_elements_by_xpath(
                '/html/body/web-root/div/div/app-root/md-sidenav-container/md-sidenav/app-list/div/div[1]/div[1]/p-datascroller/div/div[1]/ul/li')

            # # gas = list_products[0].find_element_by_xpath(
            # #     '//div/product-item/div/div[1]/div[2]/span').text
            # # print("> Price:" + gas)
            # # gas2 = list_products[1].find_element_by_css_selector(
            # #     'span.preco').text
            # # print("> Price2:" + gas2)

            # # gas3 = list_products[2].find_element_by_class_name(
            # #     'preco').text
            # # print("> Price3:" + gas3)
            # print("> Size products {}".format(len(list_products)))
            for idx, product in enumerate(list_products):
                print("{} > Product: {} > Price: {}"
                      .format(idx, product.find_element_by_css_selector(
                          'span.product').text,
                          product.find_element_by_css_selector(
                          'span.preco').text))
                print("{} > Product2: {} > Price2: {}"
                      .format(idx, product.find_element_by_class_name(
                          'product').text,
                          product.find_element_by_class_name(
                          'preco').text))

            # print(gas)
            #     scraped_infos = {
            #         'gas': gas
            #     }
            # yield scraped_infos
        except AssertionError as error:
            print(error)
            print('error')
            self.driver.close()

    # self.driver.close()
