from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog
from os.path import join


def regist_voucher_dataset():
    """
    COCO format으로된 custom dataset을 추가하는 함수
    """
    for d in ["train", "val"]:
        root_dir = "/detectron2_repo/datasets/data_voucher_2019"
        group_dir = join(root_dir, "group1")
        json_file = join(root_dir, group_dir, "annotations_json/instances_" + d + ".json")
        image_root = join(root_dir, group_dir, d + "_images")
        name = "voucher_" + d
    
        register_coco_instances(name, {}, json_file, image_root)

    voucher_train_metadata = MetadataCatalog.get("voucher_train")
    voucher_test_metadata = MetadataCatalog.get("voucher_val")
    print(voucher_train_metadata)
    print(voucher_test_metadata)

    
def regist_rice_dataset():
    """
    COCO format으로된 custom dataset을 추가하는 함수
    """
    for d in ["train", "val", "test"]:
        root_dir = "/detectron2_repo/datasets/rice_dataset"
        json_file = join(root_dir, d + ".json")
        image_root = join(root_dir, d)
        name = "rice_" + d

        # BoxMode.XYXY_ABS -> 0
        # BoxMode.XYWH_ABS -> 1
        register_coco_instances(name, {"bbox_mode":1}, json_file, image_root)

    rice_train_metadata = MetadataCatalog.get("rice_train")
    rice_val_metadata = MetadataCatalog.get("rice_val")
    rice_test_metadata = MetadataCatalog.get("rice_test")
    
    print(rice_train_metadata)
    print(rice_val_metadata)
    print(rice_test_metadata)
    
       
def regist_beive_dataset():
    """
    COCO format으로된 custom dataset을 추가하는 함수
    """
    for d in ["train", "val", "test"]:
        root_dir = "/detectron2_repo/datasets/beive/beive_ver_0.1"
        json_file = join(root_dir, "json", d + ".json")
        image_root = join(root_dir, d)
        name = "beive_{}".format(d)
        # BoxMode.XYXY_ABS -> 0
        # BoxMode.XYWH_ABS -> 1
        register_coco_instances(name, {"bbox_mode":1}, json_file, image_root)

    beive_train_metadata = MetadataCatalog.get("beive_train")
    beive_val_metadata = MetadataCatalog.get("beive_val")
    beive_test_metadata = MetadataCatalog.get("beive_test")
    
    print(beive_train_metadata)
    print(beive_val_metadata)
    print(beive_test_metadata)

