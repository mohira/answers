import torch

"""
Tensorの作成
"""
t1 = torch.tensor([[1, 2],
                   [3, 4]])

print(t1)
print(t1.dtype)

# 要素をfloatにすれば勝手に torch.float32
t2 = torch.tensor([[1., 2.], [3., 4.]])
print(t2)
print(t2.dtype)

# ゼロ埋め
t3 = torch.zeros(size=(3, 2))
print(t3)
print(t3.dtype)

# 1埋め
t4 = torch.ones(size=(3, 2))
print(t4)
print(t4.dtype)

# 正規分布に従う乱数
t5 = torch.randn(size=(4, 3))
print(t5)
print(t5.dtype)
