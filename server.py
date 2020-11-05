from concurrent import futures
import logging
import time
import grpc
import argparse
import numpy as np

import NormalDetect_pb2
import NormalDetect_pb2_grpc
from detector import DTAPI
from detectron2.data import MetadataCatalog
from detectron2.external_functions.category_disabler import category_disabler

parser = argparse.ArgumentParser('detectron2 gRPC server')
parser.add_argument("--model_path", help="path to model", default='/home/appuser/beyless_train_header/results/faster_rcnn_R_101_C4_3x.yaml_1604398136.6431131/config.yaml')
parser.add_argument("--weight_path", help="path to weight parameter", default='/home/appuser/beyless_train_header/results/faster_rcnn_R_101_C4_3x.yaml_1604398136.6431131/model_0004999.pth')



class beyless_detector(NormalDetect_pb2_grpc.NormalDetectorServicer):
    def __init__(self, model_path, weight_path):
        self.call_counter = 1
        self.detector = DTAPI(model_path, weight_path)
        self.label_in_str = MetadataCatalog.get("custom_train").thing_classes
        category_disabler.cat_all_regist(self.label_in_str)

    def detect(self, ImageRequest, context):
        category_disabler.cat_in_regist(ImageRequest.productCodes)
        t0 = time.time()
        detection = self.detector.inference(ImageRequest.data)
        t1 = time.time()
        
        # create return form
        result = NormalDetect_pb2.DetectResponse()
        result.requestId = ImageRequest.requestId
        result.usedTime = t1 - t0
        result.status = 1
        result.msg = 'hello'
        
        boxes = []
        for i in range(len(detection)):
            _box = detection[i].pred_boxes.tensor.cpu().numpy().astype(np.int32).tolist()[0]
            _label = self.label_in_str[detection[i].pred_classes.cpu().numpy().astype(np.int32).tolist()[0]]
            _score = detection[i].scores.cpu().numpy().tolist()[0]
            data = NormalDetect_pb2.NormalBox(xmin = _box[0],
                                              ymin = _box[1], 
                                              xmax = _box[2], 
                                              ymax = _box[3], 
                                              label = _label, 
                                              score = _score )
            
            result.normalBoxes.append(data)
            
        return result

    
def serve(model_path, weight_path):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    NormalDetect_pb2_grpc.add_NormalDetectorServicer_to_server(beyless_detector(model_path, weight_path), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    args = parser.parse_args()
    serve(args.model_path, args.weight_path)
