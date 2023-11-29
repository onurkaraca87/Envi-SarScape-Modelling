# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:50:25 2023

@author: sukruonur.karaca
"""
import cv2
import glob

# two_2D="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\visualization_2D\\*.png"
# two_2D_output="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\video\\2D.avi"
# line_graph="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\Line_graph\\*.png"
# line_graph_output="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\video\\line_graph.avi"
# three_3D="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\visualizataion_3D\\*.png"
# three_3D_output="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\video\\3D.avi"
ROI="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\Roi\\*.png"
ROI_output="E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\video\\ROI.avi"


img_array = []
for filename in glob.glob(ROI):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
out = cv2.VideoWriter(ROI_output,cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
for i in range(167): #Band number
    out.write(img_array[i])
out.release()


