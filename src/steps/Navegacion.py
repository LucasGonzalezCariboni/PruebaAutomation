import unittest
import allure

from Andreani_QA_Selenium.Selenium import Selenium


def navegacion_URL(self):
    with allure.step("Navegacion"):
        Selenium.get_element(self, self.data_resource["URL"])




