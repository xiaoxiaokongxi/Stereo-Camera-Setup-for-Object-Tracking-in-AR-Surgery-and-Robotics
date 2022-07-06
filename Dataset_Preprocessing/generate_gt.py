import os
import numpy as np
import yaml
import json

from scipy.spatial.transform import Rotation

# set FAT path
json_path = "G:\\paper\\Falling_Things\\Fat\\test1\\left\\json"
scene = "35"
savepath = os.path.join(json_path,"gt.yml")
delete_list = []
countobj = 0
write = {}
for img in os.listdir(json_path):
    if ".json" in img:
        print(img)
    with open(os.path.join(json_path,img)) as f:
        rawdata = json.load(f)
        rotation = []
        translation = []
    try:  
        # for i in rawdata["objects"]:         if need to extract from multiple object scenes, then replace the 'rawdata["objects"][0]' with 'i' and uncomment these two lines
        #     if i["class"]=="035_power_drill_16k":   don't change unless you need to preprocess the multiple object scene
                quat=np.array(rawdata["objects"][0]["quaternion_xyzw"])
                rotation_obj = Rotation.from_quat(quat).as_matrix()
                translation_obj = rawdata["objects"][0]["location"]
                rotation = np.reshape(rotation_obj,newshape=(1,9))[0].tolist()
                translation = translation_obj
                objnum = countobj
                objdict = {}
                objdict["cam_R_m2c"] = rotation
                objdict["cam_t_m2c"] = [10 * i for i in list(translation)]
                objdict["obj_id"] = 35
                templist=[]
                templist.append(objdict)
                write[countobj] = templist
                with open(savepath,"w") as j:
                    yaml.dump(write,j,encoding='cp936')
                countobj += 1
                break

    except IndexError:
        countobj += 1
        print("{}".format(img)+"failed")
        skip = img.replace(".json",".1")
        f.close()
        delete_list.append(img)
        os.rename(os.path.join(json_path,img), os.path.join(json_path,skip))
        continue

# if need to create camera info then:

# json_path = "G:\\paper\\Falling_Things\\Fat\\025\\left\\json"
# scene = "025"
# savepath = os.path.join(json_path,"info.yaml")
# countobj = 0
# write = {}

# while countobj < 1500:
#     intrinsic= [768.16058349609375, 0.0, 480, 0.0, 768.16058349609375, 270, 0.0, 0.0, 1.0]
#     objnum = countobj
#     objdict = {}
#     objdict["cam_K"] = intrinsic
#     objdict["obj_id"] = scene
#     write[countobj] = objdict
#     with open(savepath,"w") as j:
#         yaml.dump(write,j)
#     print("{} created".format(countobj))
#     countobj += 1



