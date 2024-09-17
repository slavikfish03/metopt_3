from target_function import function
import numpy as np

PHI = (1 + np.sqrt(5)) / 2


def Fib(n):
    return (np.float_power(PHI, n) - np.float_power(-PHI, -n)) / (2 * PHI - 1)


class FibonacciMethod:
    def __init__(self, a, b, precision):
        self.a = a
        self.b = b
        self.precision = precision
        self.n = 0
        self.count_iter = self.calculate_count_iter()

        self.opt_x = None
        self.opt_val = None

        #self.solve()

    def calculate_count_iter(self):
        N = (self.b - self.a) / self.precision
        i = 0
        fib = Fib(i)
        while N >= fib:
            fib = Fib(i + 1)
            i = i + 1

        print(i)
        return i

    def solve(self):
        x_1 = self.a + (self.b - self.a) * (Fib(self.count_iter - 2) / Fib(self.count_iter))
        x_2 = self.a + (self.b - self.a) * (Fib(self.count_iter - 1) / Fib(self.count_iter))

        y_1 = function(x_1)
        y_2 = function(x_2)
        while self.count_iter >= 1:
            if self.count_iter == 1:
                self.n = self.n + 1
                self.opt_x = [x_2, x_1]
                # self.opt_val = [function(x_2), function(x_1)]
                return
            else:
                self.count_iter = self.count_iter - 1
                if y_1 > y_2:
                    self.a = x_1
                    x_1 = x_2
                    x_2 = self.b - (x_1 - self.a)

                    y_1 = y_2

                    if self.count_iter == 1:
                        break
                    y_2 = function(x_2)
                    self.n = self.n + 1
                else:
                    self.b = x_2
                    x_2 = x_1
                    x_1 = self.a + (self.b - x_2)
                    y_2 = y_1

                    if self.count_iter == 1:
                        break
                    y_1 = function(x_1)
                    self.n = self.n + 1

        self.opt_x = [self.a, self.b]
        self.opt_val = [function(self.a), function(self.b)]
