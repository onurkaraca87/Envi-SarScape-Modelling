# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:46:13 2023

@author: sukruonur.karaca
"""
# ----------------------------------------------------------------------------------------------------------
# This is code for Envi-SarScape SBAS-PS Modelling
# input_for_raw_data , output, raster_input, band_increase_number, Pixel raw number, the number of the band
# ----------------------------------------------------------------------------------------------------------
# input_for_raw_data     : The "input_for_raw_data" should be geotiff format that inclued all bands.
# output                 : The "output" file must be created by user.
# raster_input           : The "raster_input" files have to have files for the dates. For the Envi-SarScape output for SBAS or PS process
#                          results create "raster" file. 
# band_increase_number   : The "band_increase_number" must be 1.
# Pixel raw number       : The "Pixel raw number" shows start point for the pixel number on the raws.
# The number of the band : The number of the band shows how many bands are inside of the "input_for_raw_data".

import os
def dates_list(raster_input, band_increase_number, the_number_of_band):
    """ This function create date of list from the "raster" file. (The "raster" file is Envi-SarScape SBAS or PS result.)
    The output           : The "output" file must be created by user.
    band_increase_number : The "band_increase_number" must be 1.
    the_number_of_band   : The number of the band shows how many bands are using."
    """
    liste_for_dates=[]
    time=[file for file in os.listdir(raster_input) if file [-6:]=='SD.sml' and file[0:7]=="G_SI_20"] #---------Dosyayı listeledik

    for f in range(the_number_of_band):  
        date=time[f].split("_")    
        dates_all=date[2]
        year = dates_all[0]+dates_all[1]+dates_all[2]+dates_all[3]
        month = dates_all[4]+dates_all[5]
        day = dates_all[6]+dates_all[7]
        seperated_dates=year + "_" + month +"_" + day
        liste_for_dates.append(seperated_dates)
    return (liste_for_dates)   


def roi(input_for_raw_data, output, pixel_raw_number, the_number_of_band, pixel_column_number, List_of_dates):
    """  This function create time series from coressponding pixel number!
    input_for_raw_data : The "input_for_raw_data" should be geotiff format that inclued all bands.
    The output             : The "output" file must be created by user.
    pixel_raw_number       : The "Pixel raw number" shows start point for the pixel number on the raws.
    the_number_of_band     : The number of the band shows how many bands are using.
    pixel_column_number    : The "pixel_column_number" shows start point for the pixel number on the columns.
    List_of_dates          : This is necessary function that create previous step which call "def dates_list".
    """     
    ds = gdal.Open(input_for_raw_data)
    liste_roi=[]
    os.mkdir(output+ "Roi")
    for a in range(the_number_of_band):
        bands_for_roi =ds.GetRasterBand(a+1).ReadAsArray() 
        pixel_num_for_roi=bands_for_roi[int(pixel_raw_number),int(pixel_column_number)] 
        liste_roi.append(pixel_num_for_roi)

    liste_roi.append(np.NaN)
    liste_roi.append(0)
    List_of_dates.append("")
    List_of_dates.append("")
    arr=np.full((the_number_of_band+2),np.nan)
    list_1 = arr.tolist()
    list_1[the_number_of_band+1]=1  
    
    for ok in range(the_number_of_band+2):
        list_1[ok]=liste_roi[ok]
        plt.ylim(40, -1000)
        plt.plot(List_of_dates, list_1)
        plt.gca().invert_yaxis()
        plt.xlabel("Dates", fontweight='bold')
        plt.ylabel("Displacement (mm)", fontweight='bold')
        plt.xticks(List_of_dates[::22], rotation = 45)
        plt.title("ROI Displacement" + " " + "raws" +"_" + str(pixel_raw_number) + "x" + str(pixel_column_number) + "_" + "columns")    
        plt.savefig(output + "\\Roi" +"/"+ str("ROI") + "_" + List_of_dates[ok] + "_" + str(pixel_raw_number) + "x" + str(pixel_column_number)+ "_pixels" + ".png",dpi=250, bbox_inches='tight')
        plt.show()

import rasterio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def visualization_for_3D (input_for_raw_data, output, band_increase_number, the_number_of_band, List_of_dates): 
    """ This function create 3D view of each bands.
    input_for_raw_data     : The "input_for_raw_data" should be geotiff format that inclued all bands.
    The output             : The "output" file must be created by user.
    band_increase_number   : The "band_increase_number" must be 1.
    the_number_of_band     : The number of the band shows how many bands are using.
    List_of_dates          : This is necessary function that create previous step.
    """
    ds_image=rasterio.open(input_for_raw_data)
    image=ds_image.read()
    #im = Image.open('E:\\PROFILLER\\Video_\\hatay\\Hatay_Interferogram_border.tif') # Add picture
    #im = im.resize((560, 400))# Add picture
    os.mkdir(output+ "visualizataion_3D")
    n=1
    for band in range(the_number_of_band): #while ile aynı çalışıyor
          image1=image[band,:,:]  
          image2= image1[:-1, :-1]
          xx, yy = np.mgrid[0:image2.shape[0], 0:image2.shape[1]]
          pos = np.empty(xx.shape+(2,))
          pos[:,:,0]=xx
          pos[:,:,1]=yy
          fig = plt.figure()
          ax = fig.add_subplot(111, projection='3d')
          surf = ax.plot_surface(xx, yy, image2, cmap="jet", vmin=-800, vmax=800,
                                linewidth=0, antialiased=False)
          ax.view_init(elev=30, azim=-30)
          ax.set_zlim(0,-1250)
          plt.gca().invert_zaxis()
          ax.set_xlabel('$X-Axis$', fontsize=10, rotation=150)
          ax.set_ylabel('$Y-Axis$', fontsize=10, rotation=150)
          ax.set_zlabel('$Deformation (mm)$', fontsize=10, rotation=0)
          cbar=fig.colorbar(surf, location = 'left')
          cbar.set_label('Deformation Values (mm)')
          #fig.figimage(im, xo=1690, yo=640) # Ayrı resim ekleme
          fig.savefig(output + "visualizataion_3D\\"  +  List_of_dates[band] + ".png",dpi=300)
          plt.show()   
          img = Image.open(output +"visualizataion_3D\\" + List_of_dates[band] + ".png")
          I1 = ImageDraw.Draw(img)
          myFont = ImageFont.truetype('arial.ttf', size=50) 
          I1.text((428, 36), "Hatay Descending\nTime Series\n" + List_of_dates[band], font=myFont, fill=(0, 0, 255))
          band=band+n


from osgeo import gdal
def each_line_graph (input_for_raw_data, raster_input, output, pixel_raw_number, the_number_of_band, List_of_dates):
    """ This function making graph lines from corresponding raw number. This graph line location illustrated on 2d graph as well.
    input_for_raw_data     : The "input_for_raw_data" should be geotiff format that inclued all bands.
    raster_input           : The "raster_input" files have to have files for the dates. 
                             For the Envi-SarScape output for SBAS or PS process results create "raster" file. 
    The output             : The "output" file must be created by user.
    pixel_raw_number       : The "Pixel raw number" shows start point for the pixel number on the raws.
    the_number_of_band     : The number of the band shows how many bands are using.
    List_of_dates          : This is necessary function that create previous step which call "def dates_list".
    """     
    ds = gdal.Open(input_for_raw_data)
    os.mkdir(output+ "Line_graph")
    for a in range(the_number_of_band):
        bands =ds.GetRasterBand(a+1).ReadAsArray() 
        Pixel_start=0 
        liste=[]  
        for pixel in range(bands.shape[1]-1):
            pixel_num=bands[int(pixel_raw_number),Pixel_start]
            liste.append(pixel_num)
            Pixel_start=Pixel_start+1            
            #--------------------------------------------------------------UZUNLUK HESABI -----------------------------------------------
        metre_uzunlugu=[]
        pixel_uzunlugu = [pixel for pixel in range(bands.shape[1]-1)]
        for pixel in range (bands.shape[1]-1):
            metre_uzunlugu.append(pixel_uzunlugu[pixel]*12.5)
            #--------------------------------------------------------------UZUNLUK HESABI -----------------------------------------------  
        plt.plot(metre_uzunlugu, liste)
        plt.xlabel("Distance(metre)")
        plt.ylabel("LOS Deformation Value - Millimeters")
        plt.ylim(-1000, 50)
        plt.title("Time Series" + str(List_of_dates[a]))
        plt.savefig(output +"line_graph\\" + str(pixel_raw_number) + "_" + str(List_of_dates[a]) + "_pixel_start_number.png", dpi=300)
        a=a+1
            
def two_D(input_for_raw_data, output, pixel_raw_number, the_number_of_band, pixel_columns, List_of_dates):   
    """ This function making 2D view of each bands.
    input_for_raw_data     : The "input_for_raw_data" should be geotiff format that inclued all bands.
    The output             : The "output" file must be created by user.
    pixel_raw_number       : The "Pixel raw number" shows start point for the pixel number on the raws.
    the_number_of_band     : The number of the band shows how many bands are using.
    pixel_column_number    : The "pixel_column_number" shows start point for the pixel number on the columns.
    List_of_dates          : This is necessary function that create previous step which call "def dates_list".
    """    
    os.mkdir(output+ "visualization_2D")
    for cam in range(the_number_of_band):   #♠ depremden sonrası ıstersen 184 yap
        ds_two_D = gdal.Open(input_for_raw_data)
        band_for_2d=ds_two_D.GetRasterBand(cam+1).ReadAsArray()
        band_for_2d[pixel_raw_number]=1000
        #band_for_2d[:, pixel_columns] = 1000
        band_for_2d[pixel_raw_number-1, pixel_raw_number-1] = 1000
        band_for_2d[pixel_raw_number-2, pixel_raw_number-2] = 1000
        band_for_2d[pixel_raw_number+1, pixel_raw_number+1] = 1000
        band_for_2d[pixel_raw_number+2, pixel_raw_number+2] = 1000
        band_for_2d[pixel_raw_number-1, pixel_raw_number+1] = 1000
        band_for_2d[pixel_raw_number-2, pixel_raw_number+2] = 1000
        band_for_2d[pixel_raw_number+1, pixel_raw_number-1] = 1000
        band_for_2d[pixel_raw_number+2, pixel_raw_number-2] = 1000
        plt.subplot()
        plt.figure(figsize=(10,10))
        plt.imshow(band_for_2d, vmin=-800, vmax=800, cmap="jet")
        plt.title(List_of_dates[cam], fontsize=20, fontweight="bold")
        cbb=plt.colorbar( orientation="horizontal")
        cbb.ax.tick_params(labelsize=25)
        cbb.set_label(label="Displacement (mm)", weight="bold", size=20)
        plt.savefig(output + "\\visualization_2D\\"+ str("2D") + "_" + str(List_of_dates[cam]) + ".png", dpi=300)









