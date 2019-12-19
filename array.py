import unittest

weed = ["white widow", "orange bud", "bubble kush"]
weed[0] = "start"
number =int(input("what do you want"))
print(weed[number])
input("hi")

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FO')