# beyless_model_serving
DL model deploy


## how to use

### 1.clone repository
$ cd $HOME <br>
$ git clone https://github.com/changseok93/beyless_model_serving <br>

### 2. get into docker environment
$ cd beyless_model_serving/docker <br>
$ bash ./bootstrap.sh <br>
 <br>
### 3. install compile grpc protobuf files
$ cd $HOME/beyless_model_serving <br>
$ cd ./compile_proto.sh <br>
 <br>
### 4. install detectron patches
$ cd $HOME/beyless_model_serving/detectron_sources <br>
$ ./install.sh <br>
 <br>
### 5. download beyless sample dataset
$ cd $HOME/beyless_model_serving/dataset <br>
$ ./download_beyless_dataset.sh <br>
 <br>
### 6. download beyless sample DL model
$ cd $HOME/beyless_model_serving/model <br>
$ ./download_samples.sh <br>
 <br>
### 7. run gRPC server
$ cd $/HOME/beyless_model_serving <br>
$ python3 server.py --model_path /home/appuser/beyless_model_serving/model/faster_rcnn_R_101_C4_3x.yaml_1604398136.6431131/config.yaml --weight_path /home/appuser/beyless_model_serving/model/faster_rcnn_R_101_C4_3x.yaml_1604398136.6431131/model_0004999.pth <br>
 <br>
