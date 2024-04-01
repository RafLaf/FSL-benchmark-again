import yaml
import os

all_roots = {}
all_roots["ILSVRC"] = "PATH-TO-IMAGENET" #0
all_roots["Omniglot"] = "/home/datasets/omniglot/" #1
all_roots["Quick Draw"] = "/home/datasets/quickdraw/converted/" #2
all_roots["Birds"] = "/home/datasets/CUB_200_2011/" #3
all_roots["VGG Flower"] = "/home/datasets/vgg_flower/" #4
all_roots["Aircraft"] = "/home/datasets/fgvc-aircraft-2013b/converted/"  #5
all_roots["Traffic Signs"] = "/home/datasets/GTSRB/Final_Training/Images/" #6
all_roots["MSCOCO"] = "/home/datasets/mscoco/imgs_g/" #7
all_roots["Textures"] = "/home/datasets/dtd/" #8
all_roots["Fungi"] = "/home/datasets/fungi/" #9
all_roots["MNIST"] = "PATH-TO-mnist" #10
all_roots["CIFAR10"] = "PATH-TO-cifar10" #11
all_roots["CIFAR100"] = "PATH-TO-cifar100" #12
all_roots["miniImageNet"] = "PATH-TO-miniImageNet" #13

Data = {}

Data["DATA"] = {}


Data["IS_TRAIN"] = 0

names = list(all_roots.keys())
roots = list(all_roots.values())


Data["DATA"]["VALID"] = {}


Data["DATA"]["VALID"]["DATASET_ROOTS"] = [roots[7]]
Data["DATA"]["VALID"]["DATASET_NAMES"] = [names[7]]


Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"] = {}
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_WAYS"] = 5
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"] = 5
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"] = 15
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["MAX_NUM_QUERY"] = 15
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["USE_DAG_HIERARCHY"] = False
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["MIN_EXAMPLES_IN_CLASS"] = Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"]+Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"]
Data["DATA"]["VALID"]["BATCH_SIZE"] = 8
Data["OUTPUT"] = "../new_metadataset_result"
Data["MODEL"] = {}

Data["MODEL"]["NAME"] = "evaluation"
Data["GPU_ID"] = 0

# 1 if use sequential sampling in the original false Meta-Dataset sampling
# 1 used to re-implement the results in the ICML 2023 paper; 0, however, is recommended
Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["SEQUENTIAL_SAMPLING"] = 1

Data["AUG"] = {}

# ImageNet
# Data["AUG"]["MEAN"] = [0.485, 0.456, 0.406]
# Data["AUG"]["STD"] = [0.229, 0.224, 0.225]

# miniImageNet
Data["AUG"]["MEAN"] = [0.4712, 0.4499, 0.4031]
Data["AUG"]["STD"] = [0.2726, 0.2634, 0.2794]


# ImageNet
# Data["DATA"]["IMG_SIZE"] = 224

# miniImageNet
Data["DATA"]["IMG_SIZE"] = 224

Data["MODEL"]["BACKBONE"] = 'clip'

Data["DATA"]["NUM_WORKERS"] = 8

Data["AUG"]["TEST_CROP"] = True

Data["DATA"]["VALID"]["EPISODE_DESCR_CONFIG"]["NUM_TASKS_PER_EPOCH"] = 50


# some examples of gradient-based methods.
Data["MODEL"]["TYPE"] = "fewshot_finetune"
Data["MODEL"]["CLASSIFIER"] = "finetune"
# Data["MODEL"]["CLASSIFIER"] = "eTT"

# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,100,0.02,0.1,False,False,"fc"]# finetune_batchsize,query_feedingbatchsize,epoch,backbone_lr,classifer_lr,use_alpha,use_beta, mode
Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,None,None,None,False,False,"fc"]# finetune
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,None,None,None,True,True,"NCC"]# tsa
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,None,None,None,False,True,"NCC"]# URL
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,None,None,None,False,False,"cc"]# CC
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,None,None,None,"eTT"]# eTT



Data["SEARCH_HYPERPARAMETERS"] = {}

# change this
Data["SEARCH_HYPERPARAMETERS"]["LR_BACKBONE_RANGE"] = [0.01,0.05,0.25]
Data["SEARCH_HYPERPARAMETERS"]["LR_HEAD_RANGE"] = [0.02,0.1,0.5]
Data["SEARCH_HYPERPARAMETERS"]["EPOCH_RANGE"] = [10,20,30]

if not os.path.exists('./configs/search'):
   os.makedirs('./configs/search')
with open('./configs/search/finetune_clip.yaml', 'w') as f:
   yaml.dump(data=Data, stream=f)