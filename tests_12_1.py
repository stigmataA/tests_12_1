import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self): # метод, в котором создаётся объект класса Runner с произвольным именем
        a = runner.Runner(name = 'Ivan') # создаём объект
        for i in range(10): # вызов метода walk у этого объекта 10 раз
            a.walk()
        self.assertEqual(a.distance, 50) # сравните distance этого объекта со значением 50 (assertEqual функция из модуля unittest, которая используется в модульном тестировании для проверки равенства двух значений)

    def test_run(self): # метод, в котором создаётся объект класса Runner с произвольным именем
        a = runner.Runner(name = 'Ivan') # создаём объект
        for i in range(10): # вызов метода run у этого объекта 10 раз
            a.run()
        self.assertEqual(a.distance, 100) # сравние distance этого объекта со значением 100

    def test_challenge(self): # метод в котором создаются 2 объекта класса Runner с произвольными именами
        a = runner.Runner(name = 'Ivan') # создаём объект a
        b = runner.Runner(name = 'Petr') # создаём объект b
        for i in range(10): # вызов метода walk и run у этих объектов 10 раз
            a.walk()
            b.run()
        self.assertNotEqual(a.distance, b.distance) # сравнение distance объектов a и b (assertNotEqual метод из модуля unittest, который проверяет, что два заданных значения не равны)

if __name__ == '__main__':
    unittest.main()