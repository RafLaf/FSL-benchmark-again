import yaml
import os

Data = {}
Data["DATA"] = {}


Data["DATA"]["TRAIN"] = {}

Data["DATA"]["TRAIN"]["DATASET_ROOTS"] = ["PATH-TO-miniIMAGENET"]
Data["DATA"]["TRAIN"]["DATASET_NAMES"] = ["miniImageNet"]

Data["DATA"]["TRAIN"]["IS_EPISODIC"] = False




Data["DATA"]["VALID"] = {}




Data["DATA"]["VALID"]["DATASET_ROOTS"] = ["PATH-TO-miniIMAGENET"]
Data["DATA"]["VALID"]["DATASET_NAMES"] = ["miniImageNet"]



Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"] = {}
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_WAYS"] = 5
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"] = 5
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"] = 15
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["MAX_NUM_QUERY"] = 15
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["USE_DAG_HIERARCHY"] = False
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["MIN_EXAMPLES_IN_CLASS"] = Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"]+Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"]

Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_TASKS_PER_EPOCH"] = 600
Data["DATA"]["VALID"]["BATCH_SIZE"] = 8


Data["AUG"] = {}
Data["AUG"]["MEAN"] = [0.4712, 0.4499, 0.4031]
Data["AUG"]["STD"] = [0.2726, 0.2634, 0.2794]

Data["OUTPUT"] = "../new_metadataset_result"

Data["MODEL"] = {}
Data["MODEL"]["TYPE"] = "CE"
Data["MODEL"]["CLASSIFIER"] = "proto_head"
Data["MODEL"]["NAME"] = "miniImageNet_Res12_CE"


Data["MODEL"]["BACKBONE"] = 'resnet12'

Data["DATA"]["IMG_SIZE"] = 84
Data["DATA"]["NUM_WORKERS"] = 8
Data["GPU_ID"] = 2
Data["TRAIN"] = {}
Data["TRAIN"]["EPOCHS"] = 60

Data["DATA"]["TRAIN"]["BATCH_SIZE"] = 256

Data["TRAIN"]["BASE_LR"] = 0.1*Data["DATA"]["TRAIN"]["BATCH_SIZE"]/128





if not os.path.exists('./configs/CE'):
   os.makedirs('./configs/CE')

with open('./configs/CE/miniImageNet_res12.yaml', 'w') as f:
   yaml.dump(data=Data, stream=f)