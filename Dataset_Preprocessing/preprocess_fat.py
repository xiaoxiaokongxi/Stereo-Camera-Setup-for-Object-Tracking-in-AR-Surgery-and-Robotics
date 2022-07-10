import os
import shutil



# set FAT path
FAT_path = "G:\paper\Falling_Things\Fat"
single_path = os.path.join(FAT_path,"single")
mix_path = os.path.join(FAT_path,"mix")
model_path = os.path.join(FAT_path,"model")
test_path = os.path.join(FAT_path,"test")

scene = "002_master_chef_can_16k" # name of subfolder like: 002_master_chef_can_16k, 035_power_drill_16k ...
scenepath = os.path.join(single_path,scene)
imgfolder = os.listdir(scenepath)

#make target folder if not exist
if os.path.exists(os.path.join(FAT_path, scene[0:3])) == False:
    os.makedirs(os.path.join(FAT_path, scene[0:3]))
new_scene_path = os.path.join(FAT_path, scene[0:3]) #/fat/002/

# prepare and check whether we divide according to scene or not
count_left = 0
count_right = 0
count_left_mask = 0
count_right_mask = 0
count_left_json = 0
count_right_json = 0
count_left_depth = 0
count_right_depth = 0

divide_rgb_and_mask_and_json = True # flag used for testing code, don't need to change

#put all right or left files in same /right /left folders
if divide_rgb_and_mask_and_json == True:
    for folder in imgfolder: #../kitchen_0
        path = os.path.join(scenepath,folder) #..\Fat\single\019_pitcher_base_16k\kitchen_0
        for img in os.listdir(path):
            print("processing {}".format(img))
            #for left in name copy to left .png, check end with jpg and rename to .png
            if 'left.jpg' in img:
                left_source = os.path.join(path,img)
                left_folder = os.path.join(new_scene_path, "data") # /fat/002/data/
                if os.path.exists(left_folder) == False:
                    os.makedirs(left_folder)
                left_rgb = os.path.join(left_folder, "rgb") # /fat/002/left/rgb
                if os.path.exists(left_rgb) == False:
                    os.makedirs(left_rgb)
                left_filename = img.replace(img,"%04d.png" %count_left)
                left_file = os.path.join(left_rgb,left_filename)
                count_left += 1
                shutil.copy(left_source, left_file)

            #for right in name copy to right .png
            elif 'right.jpg' in img:
                right_source = os.path.join(path,img)
                right_folder = os.path.join(new_scene_path, "right")# /fat/002/right/
                if os.path.exists(right_folder) == False:
                    os.makedirs(right_folder)
                right_rgb = os.path.join(right_folder, "rgb")# /fat/002/right/rgb
                if os.path.exists(right_rgb) == False:
                    os.makedirs(right_rgb)            
                right_filename = img.replace(img,"%04d.png" %count_right)
                right_file = os.path.join(right_rgb,right_filename)
                count_right +=1
                shutil.copy(right_source, right_file)

            elif "left.seg.png" in img:
                left_source = os.path.join(path,img)
                left_folder = os.path.join(new_scene_path, "data") # /fat/002/data/
                if os.path.exists(left_folder) == False:
                    os.makedirs(left_folder)
                left_seg = os.path.join(left_folder, "mask") # /fat/002/left/mask
                if os.path.exists(left_seg) == False:
                    os.makedirs(left_seg)
                left_filename = img.replace(img,"%04d.png" %count_left_mask)
                left_file = os.path.join(left_seg,left_filename)
                count_left_mask += 1
                shutil.copy(left_source, left_file)

            elif "right.seg.png" in img:
                right_source = os.path.join(path,img)
                right_folder = os.path.join(new_scene_path, "right")# /fat/002/right/
                if os.path.exists(right_folder) == False:
                    os.makedirs(right_folder)
                right_seg = os.path.join(right_folder, "mask")# /fat/002/right/mask
                if os.path.exists(right_seg) == False:
                    os.makedirs(right_seg)            
                right_filename = img.replace(img,"%04d.png" %count_right_mask)
                right_file = os.path.join(right_seg,right_filename)
                count_right_mask +=1
                shutil.copy(right_source, right_file)   

            #first put json in one path
            elif "left.json" in img:
                left_source = os.path.join(path,img)
                left_folder = os.path.join(new_scene_path, "data") # /fat/002/data/
                if os.path.exists(left_folder) == False:
                    os.makedirs(left_folder)
                left_json = os.path.join(left_folder, "json") # /fat/002/left/json
                if os.path.exists(left_json) == False:
                    os.makedirs(left_json)
                left_filename = img.replace(img,"%04d.json" %count_left_json)
                left_file = os.path.join(left_json,left_filename)
                count_left_json += 1
                shutil.copy(left_source, left_file)

            elif "right.json" in img:
                right_source = os.path.join(path,img)
                right_folder = os.path.join(new_scene_path, "right")# /fat/002/right/
                if os.path.exists(right_folder) == False:
                    os.makedirs(right_folder)
                right_json = os.path.join(right_folder, "json")# /fat/002/right/json
                if os.path.exists(right_json) == False:
                    os.makedirs(right_json)            
                right_filename = img.replace(img,"%04d.json" %count_right_json)
                right_file = os.path.join(right_json,right_filename)
                count_right_json +=1
                shutil.copy(right_source, right_file)   

            #first put depth in one path
            elif "left.depth" in img:
                left_source = os.path.join(path,img)
                left_folder = os.path.join(new_scene_path, "data") # /fat/002/data/
                if os.path.exists(left_folder) == False:
                    os.makedirs(left_folder)
                left_depth = os.path.join(left_folder, "depth") # /fat/002/left/depth
                if os.path.exists(left_depth) == False:
                    os.makedirs(left_depth)
                left_filename = img.replace(img,"%04d.png" %count_left_depth)
                left_file = os.path.join(left_depth,left_filename)
                count_left_depth += 1
                shutil.copy(left_source, left_file)

            elif "right.depth" in img:
                right_source = os.path.join(path,img)
                right_folder = os.path.join(new_scene_path, "right")# /fat/002/right/
                if os.path.exists(right_folder) == False:
                    os.makedirs(right_folder)
                right_depth = os.path.join(right_folder, "depth")# /fat/002/right/depth
                if os.path.exists(right_depth) == False:
                    os.makedirs(right_depth)            
                right_filename = img.replace(img,"%04d.png" %count_right_depth)
                right_file = os.path.join(right_depth,right_filename)
                count_right_depth +=1
                shutil.copy(right_source, right_file)   
