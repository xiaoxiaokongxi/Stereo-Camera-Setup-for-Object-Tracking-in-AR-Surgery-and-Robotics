# Stereo-Camera-Setup-for-Object-Tracking-in-AR-Surgery-and-Robotics
Semester project in pd|z, aiming at solving 3D tracking problem for surgery application.

## Introduction
The code here contains: The Parallel Attention Mapping EfficientPose, the Preprocessing code for Falling Things, and the API for our stereo camera.

We based our work on the official implementation of [EfficientPose](https://arxiv.org/abs/2011.04307). 

## Dataset and pretrained weights

You can download the preprocessed Falling Things datasets [here](https://drive.google.com/drive/folders/1fI4XbMSCpWm_UspnZXBglgQQKTHg6_Xv?usp=sharing), and the pretrained weights from [link](https://drive.google.com/drive/folders/1IidOwTSMuyXEQdbhy-s0DVhcKC6BC1Ij?usp=sharing).

Just download file and you can train or evaluate using these datasets as described below.

The dataset is originally downloaded from [Nvidia/FAT](https://research.nvidia.com/publication/2018-06_falling-things-synthetic-dataset-3d-object-detection-and-pose-estimation) and were preprocessed using the ```/Dataset_Preprocessing/preprocess_fat.py``` to split the file into the linemod format and then use the ```/Dataset_Preprocessing/generate_gt.py``` to generate the corresponding ground truth file.

The dataset format is shown as below:
```
Dataset
    data(left camera images)
        35(object_number)
            depth
            mask
            rgb
            gt.yml
            info.yml
            test.txt
            train.txt
            val.txt
    models
        obj_35.ply
        models_info.yml
    right
        35(object_number)
            depth
            mask
            rgb
            gt.yml
            info.yml
```

## Installation of PAM EfficientPose

1) Clone this repository
2) Create a new environment with ```conda create -n EfficientPose python==3.7```
3) Activate that environment with ```conda activate EfficientPose```
4) Install Tensorflow 1.15.0 with ```conda install tensorflow-gpu==1.15.0```
5) Go to the PAM_EfficientPose dir and install the other dependencys using ```pip install -r requirements.txt```(if you are using colab, you need ```!pip install gast==0.2.2``` to avoid warnings)
6) Compile cython modules with ```python setup.py build_ext --inplace```

## Training Example Falling Things Dataset
To train a phi = 0 PAM EfficientPose model on object 35 of Falling Things (driller) using our pretrained weights(with batch size 5 and validate every 900 steps):
```
python train.py --phi 0 --batch-size 5 --steps 900 --weights /path_to_weights/PAM.h5 linemod /dataPAM --object-id 35
```

## Evaluating Example Falling Things Dataset
To evaluate a trained phi = 0 EfficientPose model on object 35 of Falling Things (driller) using our pretrained weights and (optionally) save the predicted images:
```
python evaluate.py --phi 0 --weights /path_to_weights/PAM.h5 --validation-image-save-path /where_to_save_predicted_images/ linemod /dataPAM --object-id 35
```

## Runtime Evaluation

To measure the runtime of PAM EfficientPose on your machine you can use ```python benchmark_runtime.py```.
The needed parameters, e.g. the path to the model can be modified in the ```benchmark_runtime.py``` script.

## Debugging Dataset and Generator

The original EfficientPose provide debugging code, if you want to modify the generators or build a new custom dataset, it can be very helpful to display the dataset annotations loaded from your generator to make sure everything works as expected.
With 
```
python debug.py --phi 0 --annotations linemod /dataPAM --object-id 35
```
 you can display the loaded and augmented image as well as annotations prepared for a phi = 0 model from object 35 of the Linemod dataset.
Please see ```debug.py``` for more arguments.

## Original EfficientPose
You can get the original [EfficientPose](https://arxiv.org/abs/2011.04307), and try our Mono.h5 pretained weights for our dataset and compare the result.

## Stereo EfficientPose
If you want to try the direct concatenated EfficientPose network, see ```train.py``` and uncomment the "build_Direct_Concate_EfficientPose" function, and use the corresponding pretrained weight we provide.
