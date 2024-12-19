"""
# MathAlgo - 數學算法工具包

## 簡介
這個包提供了各種數學計算和分析的工具。

## 主要功能

### 1. 微積分模組 (Calculus)
* 符號微分和數值微分
* 定積分和不定積分
* 極限計算
* 泰勒展開
* 函數繪圖

### 2. 矩陣模組 (Matrix)
* 矩陣基本運算（加、減、乘）
* 矩陣轉置
* 行列式計算
* 逆矩陣計算

## 快速開始
    >>> from mathalgo import Calculus
    >>> f = Calculus("x**2")
    >>> derivative = f.derivative()
    >>> print(derivative)  # 輸出: 2*x

版本信息:
    - 版本: 0.1.0
    - 作者: Your Name
    - 許可證: MIT License
    - 文檔: https://github.com/yourusername/mathalgo

注意事項:
    1. 確保已安裝所需依賴：sympy, numpy, matplotlib
    2. 使用前請查看完整文檔
    3. 歡迎提交問題和建議到 GitHub
"""

# 版本信息
__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# 導入主要類別
from mathalgo.Math.Calculus import Calculus
from mathalgo.Math.Matrix import Matrix

# 設定要導出的類別
__all__ = [
    "Calculus",
    "Matrix"
]

# 檢查必要的依賴
def _check_dependencies():
    required_packages = {
        "sympy": "用於符號計算",
        "numpy": "用於數值計算",
        "matplotlib": "用於繪圖功能"
    }
    
    missing_packages = []
    
    for package, purpose in required_packages.items():
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(f"{package} ({purpose})")
    
    if missing_packages:
        raise ImportError(
            "缺少必要的依賴套件。請安裝以下套件：\n" +
            "\n".join(f"- {pkg}" for pkg in missing_packages) +
            "\n\n可以使用以下命令安裝：\npip install " + " ".join(pkg.split()[0] for pkg in missing_packages)
        )

# 在導入時檢查依賴
_check_dependencies()