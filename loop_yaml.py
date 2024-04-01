import yaml
import os
import sys

all_roots = {}
all_roots["imagenet"] = "PATH-TO-IMAGENET" #0
all_roots["omniglot"] = "/home/datasets/omniglot/" #1
all_roots["quickdraw"] = "/home/datasets/quickdraw/converted/" #2
all_roots["cub"] = "/home/datasets/CUB_200_2011/" #3
all_roots["vgg_flower"] = "/home/datasets/vgg_flower/" #4
all_roots["aircraft"] = "/home/datasets/fgvc-aircraft-2013b/converted/"  #5
all_roots["traffic_signs"] = "/home/datasets/GTSRB/Final_Training/Images/" #6
all_roots["mscoco"] = "/home/datasets/mscoco/imgs_g/" #7
all_roots["dtd"] = "/home/datasets/dtd/" #8
all_roots["fungi"] = "/home/datasets/fungi/" #9
all_roots["MNIST"] = "PATH-TO-mnist" #10
all_roots["CIFAR10"] = "PATH-TO-cifar10" #11
all_roots["CIFAR100"] = "PATH-TO-cifar100" #12
all_roots["miniImageNet"] = "PATH-TO-miniImageNet" #13

Data = {}

Data["DATA"] = {}


Data["IS_TRAIN"] = 0

names = list(all_roots.keys())
roots = list(all_roots.values())


Data["DATA"]["TEST"] = {}




# 5 way 1 shot example
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"] = {}
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_WAYS"] = 5
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"] = 10
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"] = 7
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["MAX_NUM_QUERY"] = 1
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["USE_DAG_HIERARCHY"] = False
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["USE_BILEVEL_HIERARCHY"] = False
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["MIN_EXAMPLES_IN_CLASS"] = Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"]+Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"]
Data["DATA"]["TEST"]["BATCH_SIZE"] = 1

# 5 way 5 shot example
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"] = {}
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_WAYS"] = 5
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"] = 5
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"] = 15
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["MAX_NUM_QUERY"] = 15
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["USE_DAG_HIERARCHY"] = False
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["USE_BILEVEL_HIERARCHY"] = False
# Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["MIN_EXAMPLES_IN_CLASS"] = Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"]+Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_QUERY"]
# Data["DATA"]["TEST"]["BATCH_SIZE"] = 8

# varied way varied shot example
# Data["DATA"]["TEST"]["BATCH_SIZE"] = 8



Data["OUTPUT"] = "../new_metadataset_result"
Data["MODEL"] = {}

Data["MODEL"]["NAME"] = "evaluation"
Data["GPU_ID"] = 0

# 1 if use sequential sampling in the oroginal biased Meta-Dataset sampling procedure, 0 unbiased.
# 1 can be used to re-implement the results in the ICML 2023 paper (except traffic signs); 0, however, is recommended for unbiased results
Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["SEQUENTIAL_SAMPLING"] = 0

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
Data["DATA"]["IMG_SIZE"] = 84
Data["DATA"]["IMG_SIZE"] = 224
#Data["MODEL"]["BACKBONE"] = 'resnet12'
# Data["MODEL"]["BACKBONE"] = '
# resnet50'
model=sys.argv[1]
if model == 'clip':
   Data["MODEL"]["BACKBONE"] = 'clip'
elif model == 'dino':
   Data["MODEL"]["BACKBONE"] = 'DINO_ViT'
   Data["MODEL"]["BACKBONE_HYPERPARAMETERS"] = ['base', 16]
   Data["MODEL"]["PRETRAINED"] = '/home/raphael/Documents/models/DINO/dino_vitbase16_pretrain.pth'
elif model=='dinov2':
   Data["MODEL"]["BACKBONE"] = 'DINO_v2'
   Data["MODEL"]["BACKBONE_HYPERPARAMETERS"] = ['dinov2_vitb14_reg']


#Data["MODEL"]["PRETRAINED"] = '/home/raphael/Documents/models/ce_miniImageNet_res12.pth'# for example

#Data["DATA"]["NUM_WORKERS"] = 8


# True for re-implementing the results in the ICML 2023 paper.
Data["AUG"]["TEST_CROP"] = True

Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_TASKS_PER_EPOCH"] = 2000

# some examples of gradient-based methods. Hyperparameters need to be tuned by using search_hyperparameter.py
#Data["MODEL"]["TYPE"] = "fewshot_finetune"
#Data["MODEL"]["TYPE"] = "Episodic_Model"
#Data["MODEL"]["CLASSIFIER"] = "finetune"
#Data["MODEL"]["CLASSIFIER"] = "eTT"
#Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,10,0.02,0.1,False,False,"fc"]# finetune_batchsize,query_feedingbatchsize,epoch,backbone_lr,classifer_lr,use_alpha,use_beta, mode
#Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,10,0.02,0.1,False,False,"fc"]# finetune
#Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,10,0.02,0.1,True,True,"NCC"]# tsa
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,10,0.02,0.1,False,True,"NCC"]# URL
#Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,0,0.0,0.0,False,False,"NCC"]# NCC
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,10,0.02,0.1,False,False,"cc"]# CC
# Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,10,0.02,0.1,"eTT"]# eTT

# other adaptation classifiers
#Data["MODEL"]["TYPE"] = "Episodic_Model"
#Data["MODEL"]["CLASSIFIER"] = "LR"
#Data["MODEL"]["CLASSIFIER"] = "metaopt"
#Data["MODEL"]["CLASSIFIER"] = "proto_head"
#Data["MODEL"]["CLASSIFIER"] = "MatchingNet"
S = Data["DATA"]["TEST"]["EPISODE_DESCR_CONFIG"]["NUM_SUPPORT"]
os.makedirs('./configs/benchmark/{}-shot'.format(S,model),exist_ok=True)
os.makedirs('./configs/benchmark/{}-shot/{}'.format(S,model),exist_ok=True)
list_methods  = ['NCC', 'finetune', 'LR', 'matchingnet', 'protohead']
for method in list_methods:
   if method in ['NCC', 'finetune']:
      Data["MODEL"]["TYPE"] = "fewshot_finetune"
      Data["MODEL"]["CLASSIFIER"] = "finetune"
      if method == 'NCC':
         Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,0,0.0,0.0,False,False,"NCC"]
      elif method == 'finetune':
         if model == 'clip':
            Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,30,0.0001,0.1,False,False,"fc"]
         elif model == 'dino':
            Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,30,0.001,0.1,False,False,"fc"]
         elif model == 'dinov2':
            Data["MODEL"]["CLASSIFIER_PARAMETERS"] = [100,100,30,0.0001,0.1,False,False,"fc"]
   elif method == 'LR':
      Data["MODEL"]["TYPE"] = "Episodic_Model"
      Data["MODEL"]["CLASSIFIER"] = "LR"
      Data["MODEL"]["CLASSIFIER_PARAMETERS"]=[]
   elif method == 'matchingnet':
      Data["MODEL"]["TYPE"] = "Episodic_Model"
      Data["MODEL"]["CLASSIFIER"] = "MatchingNet"
      Data["MODEL"]["CLASSIFIER_PARAMETERS"]=[]

   for i in range(1,10):
      dataset = names[i]
      Data["DATA"]["TEST"]["DATASET_ROOTS"] = [roots[i]]
      Data["DATA"]["TEST"]["DATASET_NAMES"] = [dataset]

      if not os.path.exists('./configs/benchmark/{}-shot/{}/{}'.format(S,model,method)):
         os.makedirs('./configs/benchmark/{}-shot/{}/{}'.format(S,model,method))
      with open('./configs/benchmark/{}-shot/{}/{}/{}.yaml'.format(S,model,method,dataset), 'w') as f:
         yaml.dump(data=Data, stream=f)