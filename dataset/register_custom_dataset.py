from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog
from os.path import join

def regist_custom_dataset(dataset_dir='/home/appuser/beyless_train_header/dataset'):
    for d in ["train", "val", "test"]:
        json_file = join(dataset_dir, "json", d + ".json")
        image_root = join(dataset_dir, d)
        name = "custom_{}".format(d)
        # BoxMode.XYXY_ABS -> 0
        # BoxMode.XYWH_ABS -> 1
        register_coco_instances(name, {"bbox_mode":1}, json_file, image_root)

    MetadataCatalog.get("custom_train").thing_classes = ["콜라", 
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

    custom_train_metadata = MetadataCatalog.get("custom_train")
    custom_val_metadata = MetadataCatalog.get("custom_val")
    custom_test_metadata = MetadataCatalog.get("custom_test")
    

