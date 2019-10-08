import torch

"""
代入や要素の指定
"""

t = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
print(t)
print(t.dtype)

# 特定の要素
print(t[0, 2])

# スライス
print(t[:, 1])

# 再代入
t[0, 0] = 11
print(t)

# 再代入
t[1] = 22  # 複数要素に再代入される点に注意！
print(t)

# スライス利用の再代入
t[:, 1] = 33
print(t)

# ブールインデックス参照
print(t[t < 20])
