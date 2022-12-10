  


import os

output_path = 'C:/Users/shnhc/source/data/dataset/output/blender_1/Annotations/'

folder_path = 'C:/Users/shnhc/source/data/dataset/blender_annotations/'




inputlst = [os.listdir(folder_path)]
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        files = open(os.path.join(folder_path,filename), 'r')
        output=open(os.path.join(output_path, filename),'wt')
        for line in files:
            nums = line.split(' ')
            if len(nums) > 5:
                output.write(str(nums[0]) 
                    + " " + str(nums[1]) 
                    + " " + str(nums[2])
                    + " " + str(nums[3])
                    + " " + str(nums[4])
                    + " " + str(nums[5])
                    + '\n')

