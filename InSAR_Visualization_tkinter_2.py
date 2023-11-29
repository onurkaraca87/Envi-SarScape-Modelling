# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:25:34 2023

@author: sukruonur.karaca
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:33:21 2022

@author: sukruonur.karaca
"""


import tkinter as tk
import InSAR_Visualization_main_2

window=tk.Tk()
window.title("For ENVI-SARSCAPE - 2D-3D Visualizations - Time Series")
window.geometry("1000x500")

def enter():
    global input_data
    input_data=giris_verisi.get()
    
def output():
    global output_data
    output_data=output_path.get()
    
def raster():   
    global raster_folder
    raster_folder=main_folder.get()
    
def pixel_raws():   
    global pixel_raw_number
    pixel_raw_number=int(select_raw_pixel.get())
    
def pixel_coloumn():   
    global pixel_coloumn_number
    pixel_coloumn_number=int(coloumn_pixel.get())
    
def how_many_band():
    global the_number_of_band
    the_number_of_band=int(band_num.get())

def data_gap():   
    global band_increase_number 
    band_increase_number=int(Band_Number.get())
    
def Close():
    window.destroy()

e1=tk.Label(text="Input Raw Geotiff file",font="Verdana 18")
e1.pack()
giris_verisi=tk.Entry(width=150,)
giris_verisi.insert(0, "E:\\Python_Project\\InSAR_Visualization\\Asc_all\\3D_167_fix_before_eq.tif")
giris_verisi.pack()

e2=tk.Label(text="Output File",font="Verdana 18")
e2.pack()
output_path=tk.Entry(width=150)
output_path.insert(0, "E:\\Python_Project\\InSAR_Visualization\\Asc_all\\Output\\")
output_path.pack()

e3=tk.Label(text="Main Folder (Raster) to get date names",font="Verdana 18")
e3.pack()
main_folder=tk.Entry(width=150)
main_folder.insert(0, "E:\\Python_Project\\InSAR_Visualization\\Asc_all\\raster")
main_folder.pack()

e4=tk.Label(text="The number of gap for each dates (must be '1')",font="Verdana 18")
e4.pack()
Band_Number=tk.Entry(width=150)
Band_Number.insert(0, "1")
Band_Number.pack()

e6=tk.Label(text="Pixel Colomn Number",font="Verdana 18")
e6.pack()
coloumn_pixel=tk.Entry(width=150)
coloumn_pixel.insert(0, "100")
coloumn_pixel.pack()

e7=tk.Label(text="The number of band",font="Verdana 18")
e7.pack()
band_num=tk.Entry(width=150)
band_num.insert(0, "167")
band_num.pack()

e5=tk.Label(text="Pixel Raw Number - Start Point",font="Verdana 18")
e5.pack()
select_raw_pixel=tk.Entry(width=150)
select_raw_pixel.pack()
b5=tk.Button(text="Apply", command=lambda: [enter(),output(),raster(),data_gap(), pixel_raws(), pixel_coloumn(), how_many_band(), Close()])
b5.pack()
window.mainloop()    

dates=InSAR_Visualization_main_2.dates_list(raster_folder, band_increase_number, the_number_of_band)

rois=InSAR_Visualization_main_2.roi(input_data,
          output_data,
          pixel_raw_number,
          the_number_of_band,
          pixel_coloumn_number,
          dates)

# list_of_3d=InSAR_Visualization_main_2.visualization_for_3D(input_data,
#                                 output_data,
#                                 band_increase_number,
#                                 the_number_of_band,
#                                 dates)    

# list_of_each_line=InSAR_Visualization_main_2.each_line_graph (input_data,
#                                 raster_folder,
#                                 output_data,
#                                 pixel_raw_number,
#                                 the_number_of_band,
#                                 dates)

# visualization_2D=InSAR_Visualization_main_2.two_D(input_data,
#           output_data,
#           pixel_raw_number,
#           the_number_of_band,
#           pixel_coloumn_number, dates)