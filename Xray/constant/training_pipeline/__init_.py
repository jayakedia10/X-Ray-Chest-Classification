#Contains all the variable related to the training pipeline
from datatime import datatime
from  typing import List
import torch
TIMESTAMP: datetime=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

#creating artifact directory
ARTIFACT_DIR: str="artifacts"
BUCKET_NAME: str="xraylungimgs"
S3_DATA_FOLDER: str="data"
CLASS_LABEL_1: str="NORMAL"
CLASS_LABEL_1: str="PNEUMONIA"



 