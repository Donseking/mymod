import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
y = sp.Symbol('y')

class Differentiation:
    """
    微分相關功能
    """
    def __init__(self, func_expr, var):
        # 自動將字符串轉換為 sympy 表達式
        if isinstance(func_expr, str):
            func_expr = sp.sympify(func_expr)
        if isinstance(var, str):
            var = sp.Symbol(var)
        self.func_expr = func_expr
        self.var = var

    def symbolic_derivative(self):
        """
        計算符號微分
        """
        return sp.diff(self.func_expr, self.var)

    def numeric_derivative(self, value):
        """
        計算指定點的數值微分
        """
        derivative = sp.diff(self.func_expr, self.var)
        return float(derivative.subs(self.var, value))

    def visualize_derivative(self, x_vals):
        """
        可視化函數與其導數
        """
        f_lambdified = sp.lambdify(self.var, self.func_expr, "numpy")
        derivative = sp.diff(self.func_expr, self.var)
        df_lambdified = sp.lambdify(self.var, derivative, "numpy")

        y_vals = f_lambdified(x_vals)
        dy_vals = df_lambdified(x_vals)

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        plt.plot(x_vals, dy_vals, label="f'(x)", color="orange")
        plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
        plt.title("函數與其導數")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()

class Integration:
    """
    積分相關功能
    """
    def __init__(self, func_expr, var):
        self.func_expr = func_expr  # 傳入 sympy 表達式
        self.var = var              # 傳入變數（sympy.Symbol）

    def indefinite_integral(self):
        """
        計算不定積分
        """
        return sp.integrate(self.func_expr, self.var)

    def definite_integral(self, a, b):
        """
        計算定積分
        """
        return sp.integrate(self.func_expr, (self.var, a, b))

    def visualize_definite_integral(self, a, b):
        """
        可視化定積分區域
        """
        f_lambdified = sp.lambdify(self.var, self.func_expr, "numpy")
        x_vals = np.linspace(a - 1, b + 1, 500)
        y_vals = f_lambdified(x_vals)

        x_fill = np.linspace(a, b, 500)
        y_fill = f_lambdified(x_fill)

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f"$f(x) = {sp.pretty(self.func_expr)}$", color="blue")
        plt.fill_between(x_fill, y_fill, color="skyblue", alpha=0.4, label=f"定積分區域: $\\int_{{{a}}}^{{{b}}} f(x) dx$")
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
        plt.title("定積分的幾何意義")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid()
        plt.show()

class Utilities:
    """
    其他數學功能（如極限）
    """
    def __init__(self, func_expr, var):
        self.func_expr = func_expr  # 傳入 sympy 表達式
        self.var = var              # 傳入變數（sympy.Symbol）

    def calculate_limit(self, point, direction="both"):
        """
        計算極限
        :param point: 極限點
        :param direction: 趨近方向 ('both', 'left', 'right')
        """
        if direction == "both":
            return sp.limit(self.func_expr, self.var, point)
        elif direction == "left":
            return sp.limit(self.func_expr, self.var, point, dir='-')
        elif direction == "right":
            return sp.limit(self.func_expr, self.var, point, dir='+')
        else:
            raise ValueError("方向應為 'both', 'left', 或 'right'")

    def visualize_limit(self, x_vals, point=None, y_limit=None):
        """
        可視化極限的行為
        """
        f_lambdified = sp.lambdify(self.var, self.func_expr, "numpy")
        y_vals = f_lambdified(x_vals)

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        if point is not None:
            plt.axvline(x=point, color="red", linestyle="--", label=f"x -> {point}")
        if y_limit is not None:
            plt.axhline(y=y_limit, color="green", linestyle="--", label=f"lim f(x) = {y_limit}")
        plt.title("函數極限行為")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.legend()
        plt.show()
