import unittest
import question1 as q1


class Question1Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        # 終了処理
        pass

    def easyCase1(self):
        self.assertEqual("10", q1.createFormula([1, 2, 3, 4]))

    def easyCase2(self):
        self.assertEqual("10", q1.createFormula([1, 3, 5, 7]))

    def easyCase3(self):
        self.assertEqual("10", q1.createFormula([1, 1, 2, 5]))

    def easyCase4(self):
        self.assertEqual("10", q1.createFormula([1, 1, 2, 4]))

    def Case1(self):
        self.assertEqual("10", q1.createFormula([1, 1, 1, 6]))

    def Case2(self):
        self.assertEqual("10", q1.createFormula([1, 2, 7, 7]))

    def Case3(self):
        self.assertEqual("10", q1.createFormula([5, 5, 5, 7]))

    def Case4(self):
        self.assertEqual("10", q1.createFormula([9, 9, 9, 9]))

    def difficultCase1(self):
        self.assertEqual("10", q1.createFormula([1, 3, 3, 7]))

    def difficultCase2(self):
        self.assertEqual("10", q1.createFormula([1, 1, 9, 9]))

    def difficultCase3(self):
        self.assertEqual("10", q1.createFormula([1, 1, 5, 8]))

    def difficultCase4(self):
        self.assertEqual("10", q1.createFormula([3, 4, 7, 8]))


if __name__ == "__main__":
    unittest.main()
