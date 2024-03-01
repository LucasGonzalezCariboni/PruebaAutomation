import unittest
import allure

from Andreani_QA_Selenium.Selenium import Selenium
from src.steps import Navegacion as NavegacionSteps

# Esto es un comentario

"""Esto tambien es un comentario"""
class Navegacion(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step("Prueba navegación"):
            Selenium.set_env("Test")
            Selenium.set_proyect(self)
            Selenium.set_retry(self, 5)

    def test_000_prueba_navegacion(self):
        NavegacionSteps.navegacion_URL(self)

    def tear_down(self):
        self.tear_down()


if __name__ == '__main__':
    unittest.main()


