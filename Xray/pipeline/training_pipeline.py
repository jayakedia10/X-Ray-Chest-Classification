import sys
from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifaact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging 

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

        def start_data_ingestion (self) -> DataIngestionArtifaact
        