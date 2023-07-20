# mtr_tch
 
## Build

- Linux

```Bash
export LIBTORCH_USE_PYTORCH=1
maturin develop
```

- Windows

```Bash
set LIBTORCH_USE_PYTORCH=1
maturin develop
```

## Usage

```Python
import torch
import mtr_tch

print(torch.__version__)
ex = torch.tensor((1, 2), device="cuda")
mtr_tch.add_one(ex)

print(ex)
```
