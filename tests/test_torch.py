import torch

def test_GPU():
    assert torch.__version__.startswith('2.1.2')
