import numpy as np

data_path = 'C:/Users/shnhc/source/data/dataset/nerf1_original.txt'
gt_path = 'C:/Users/shnhc/source/data/dataset/nerf_1_gt.txt'
output_path = 'C:/Users/shnhc/source/data/dataset/output/'

g_class2color = {'ceiling':	[0,255,0],
                 'floor':	[0,0,255],
                 'wall':	[0,255,255],
                 'beam':        [255,255,0],
                 'column':      [255,0,255],
                 'window':      [100,100,255],
                 'door':        [200,200,100],
                 'table':       [170,120,200],
                 'chair':       [255,0,0],
                 'sofa':        [200,100,100],
                 'bookcase':    [10,200,100],
                 'board':       [200,200,200],
                 'clutter':     [50,50,50]} 

# -----------------------------------------------------------------------------
# Clean .off file
# -----------------------------------------------------------------------------

original_file=open(data_path, 'rt')
output_original=open(output_path + 'output_original.txt','wt')
original_lines = original_file
for original_line in original_lines:
    original_nums = original_line.split(' ')
    if len(original_nums) > 5:
        output_original.write(str(original_nums[0]) 
            + " " + str(original_nums[1]) 
            + " " + str(original_nums[2])
            + " " + str(original_nums[3])
            + " " + str(original_nums[4])
            + " " + str(original_nums[5])
            + '\n')

gt_file=open(gt_path, 'rt')
output_gt=open(output_path + 'output_gt.txt','wt')
gt_lines = gt_file
for gt_line in gt_lines:
    gt_nums = gt_line.split(' ')
    if len(gt_nums) > 5:
        output_gt.write(str(gt_nums[0]) 
            + " " + str(gt_nums[1]) 
            + " " + str(gt_nums[2])
            + " " + str(gt_nums[3])
            + " " + str(gt_nums[4])
            + " " + str(gt_nums[5])
            )

# -----------------------------------------------------------------------------
# Split .off file to each class file
# -----------------------------------------------------------------------------


for element in g_class2color.keys():

    gt_openfile=open(output_path + 'output_gt.txt', 'rt')
    gt_points = gt_openfile
    output = open(output_path + str(element) +'.txt','wt')
    for gt_point in gt_points:

        gt_nums = gt_point.split(' ')
        color = [int(gt_nums[3]), int(gt_nums[4]), int(gt_nums[5])]

        gt_vertecies = [gt_nums[0], gt_nums[1], gt_nums[2]]

        if g_class2color[element] == color:
            original_openfile=open(output_path + 'output_original.txt', 'rt')
            original_points = original_openfile
            for original_point in original_points:
                original_nums = original_point.split(' ')

                if [original_nums[0], original_nums[1], original_nums[2]] == gt_vertecies:       
                    output.write(str(original_nums[0]) 
                        + " " + str(original_nums[1]) 
                        + " " + str(original_nums[2])
                        + " " + str(original_nums[3])
                        + " " + str(original_nums[4])
                        + " " + str(original_nums[5])
                        )
    print(output)






