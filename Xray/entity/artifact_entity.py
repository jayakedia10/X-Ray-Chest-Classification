import os
from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader

@dataclass
class DataIngestionArtifaact:
    train_file_path: str
    test_file_path: str
