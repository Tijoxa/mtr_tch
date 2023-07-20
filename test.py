import torch
import mtr_tch

print(torch.__version__)
ex = torch.tensor((1, 2), device="cuda")
mtr_tch.add_one(ex)

print(ex)
