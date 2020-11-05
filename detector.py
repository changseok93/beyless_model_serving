import torch, torchvision

import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

import numpy as np
import os, json, cv2, random, sys

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
sys.path.insert(1, '/home/appuser/beyless_model_serving/dataset')
import register_custom_dataset as customDataset


class DTAPI:
    def __init__(self, model_path, weight_path):
        # model configuration
        customDataset.regist_custom_dataset('/home/appuser/beyless_train_header/dataset/')
        self.cfg = get_cfg()
        self.cfg.merge_from_file(model_path)
        self.cfg.MODEL.WEIGHTS = weight_path
        
        # post hyper parameter configuration
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
        self.cfg.MODEL.ROI_HEADS.NUM_CLASSES = 15

        # create default predictor
        self.predictor = DefaultPredictor(self.cfg)
    
    def inference(self, image_in_byte):
        img = np.frombuffer(image_in_byte, np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)

        self.raw_result = self.predictor(img)['instances']     
        return self.raw_result
