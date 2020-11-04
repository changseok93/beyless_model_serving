from __future__ import print_function

import grpc
import NormalDetect_pb2
import NormalDetect_pb2_grpc
import os

def run():
    input_image = open('/home/appuser/beyless_train_header/dataset/train/9999.jpg', 'rb').read()

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = NormalDetect_pb2_grpc.NormalDetectorStub(channel)
        # 품목 선정
        product_list = ["콜라",
                        "몬스터",
                        "박카스",
                        "칠성사이다",
                        "파워에이드",
                        "토레타",
                        "광동옥수수수염차",
                        "펩시",
                        "cu블루레몬에이드",
                        "포도봉봉",
                        "갈아만든배",
                        "top더블랙",
                        "top마스터라떼",
                        "top스위트아메리카노",
                        "비타500"]

        response = stub.detect(NormalDetect_pb2.ImageRequest(requestId=123, 
                                                             data=input_image, 
                                                             height=1, 
                                                             width=2, 
                                                             deviceId=3, 
                                                             stage='2', 
                                                             appType='beyless', 
                                                             shelfId=2,
                                                             operationLogId=5,
                                                             productCodes=product_list))
        print(response)

if __name__ == '__main__':
    run()
