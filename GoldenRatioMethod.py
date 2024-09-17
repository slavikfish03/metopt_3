from target_function import function
import numpy as np

PHI = (1 + np.sqrt(5)) / 2


class GoldenRatioMethod:
    def __init__(self, a, b, precision):
        self.a = a
        self.b = b
        self.precision = precision

        self.opt_x = None
        self.opt_val = None
        self.n = 2

        self.solve()

    def solve(self):
        x_1 = self.b - (self.b - self.a) / PHI
        x_2 = self.a + (self.b - self.a) / PHI

        y_1 = function(x_1)
        y_2 = function(x_2)
        while np.abs(self.b - self.a) > self.precision:
            # x_1 = self.b - (self.b - self.a) / PHI
            # x_2 = self.a + (self.b - self.a) / PHI
            #
            # y_1 = function(x_1)
            # y_2 = function(x_2)

            if y_1 >= y_2:
                self.a = x_1
                x_1 = x_2
                x_2 = self.a + (self.b - self.a) / PHI

                y_1 = y_2

                if np.abs(self.b - self.a) < self.precision:
                    break

                y_2 = function(x_2)

                self.n = self.n + 1
            else:
                self.b = x_2
                x_2 = x_1
                x_1 = self.b - (self.b - self.a) / PHI
                y_2 = y_1

                if np.abs(self.b - self.a) < self.precision:
                    break

                y_1 = function(x_1)
                self.n = self.n + 1

        self.opt_x = [self.a, self.b]
        self.opt_val = [function(self.a), function(self.b)]


    def get_count(self, number):
        s = str(number)
        if '.' in s:
            return abs(s.find('.') - len(s)) - 1
        else:
            return 0
