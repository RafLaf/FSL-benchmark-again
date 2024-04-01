import torch.nn as nn
import torch

class DINO_V2(nn.Module):
    def __init__(self, name):
        super().__init__()
        self.model = torch.hub.load('facebookresearch/dinov2', name)
        self.model = self.model.float()
        self.outdim = self.model.embed_dim
    def forward(self, x):
        return self.model.forward(x)


def create_model(name='dinov2_vitb14'):
    return DINO_V2(name)
