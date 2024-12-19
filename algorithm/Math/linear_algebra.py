class Matrix:
    def __init__(self, data):
        # 初始化矩陣
        # 檢查輸入資料是否為有效矩陣（所有列長度必須相同且資料不可為空）
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("所有列必須具有相同的長度且資料不可為空。")
        self.data = data
        self.rows = len(data)  # 矩陣的行數
        self.cols = len(data[0])  # 矩陣的列數

    def __repr__(self):
        # 定義矩陣的字串表示，方便打印輸出
        return "\n".join([str(row) for row in self.data])

    def add(self, other):
        # 矩陣加法
        # 檢查矩陣維度是否一致
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("矩陣的維度必須相同才能進行加法運算。")
        # 計算結果矩陣
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def subtract(self, other):
        # 矩陣減法
        # 檢查矩陣維度是否一致
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("矩陣的維度必須相同才能進行減法運算。")
        # 計算結果矩陣
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def multiply(self, other):
        # 矩陣乘法
        # 檢查是否可以進行矩陣乘法（第一個矩陣的列數等於第二個矩陣的行數）
        if self.cols != other.rows:
            raise ValueError("矩陣的列數必須等於另一矩陣的行數才能進行乘法運算。")
        # 計算結果矩陣
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def transpose(self):
        # 矩陣轉置
        # 將矩陣的行和列互換
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)

    def is_square(self):
        # 檢查矩陣是否為方陣
        return self.rows == self.cols

    def determinant(self):
        # 計算方陣的行列式
        if not self.is_square():
            raise ValueError("只有方陣才能計算行列式。")

        def _det_recursive(matrix):
            # 遞迴計算行列式
            if len(matrix) == 1:
                return matrix[0][0]
            if len(matrix) == 2:
                # 2x2矩陣的行列式公式
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            
            det = 0
            # 展開計算行列式（拉普拉斯展開）
            for col in range(len(matrix)):
                # 計算子矩陣（去掉當前行和列）
                minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
                det += ((-1) ** col) * matrix[0][col] * _det_recursive(minor)
            return det

        return _det_recursive(self.data)

    def inverse(self):
        # 計算方陣的逆矩陣
        if not self.is_square():
            raise ValueError("只有方陣才能計算逆矩陣。")
        if self.determinant() == 0:
            raise ValueError("此矩陣是奇異矩陣，無法求逆。")

        n = self.rows
        # 創建單位矩陣
        identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        # 將原矩陣與單位矩陣組成增廣矩陣
        augmented = [self.data[i] + identity[i] for i in range(n)]

        for i in range(n):
            # 將主對角線元素歸一化
            pivot = augmented[i][i]
            for j in range(2 * n):
                augmented[i][j] /= pivot

            # 消去其他行的元素
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]

        # 提取逆矩陣部分
        inverse_data = [row[n:] for row in augmented]
        return Matrix(inverse_data)
    
class decomposition :
    """
        矩陣分解方法
    
    """
    def __init__(self):
        pass

class vector_space :
    """
        向量空間相關
    
    """
    def __init__(self):
        pass

class utils :
    """
        工具函數
    
    """
    def __init__(self):
        pass