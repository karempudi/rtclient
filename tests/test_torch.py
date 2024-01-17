import torch

def test_GPU():
    assert torch.cuda.is_available() is True
