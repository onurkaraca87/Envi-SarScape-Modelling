# Envi-SarScape-Modelling
The following code snippet demonstrates the utilization of Envi-SarScape for Small Baseline Subset (SBAS) or Permanent Scatterer (PS) methods in SAR processing. When implementing these methods within Envi-SarScape, users can generate comprehensive 2D and 3D models as well as conduct time series analyses.


"""Begin by executing the script named 'InSAR_Visualization_main_2.py' followed by running the second script named 'InSAR_Visualization_tkinter_2.py'. This action will prompt the interface to appear. Ensure that you have established an 'Output' folder and provided all required inputs. The subsequent steps in the code will autonomously execute.

Upon completion, the generated products will be available. To create videos from these products, utilize the script labeled 'InSAR_Visualization_for_videos_2.py'."""

For reference please :"KARACA, Ş. O., ERTEN, G., ERGİNTAV, S., KHAN, S. D. (n.d.). Anthropogenic problems threatening major cities: Largest surface deformations observed in Hatay, Turkey based on SBAS-InSAR. Bulletin of the Mineral Research and Exploration1-1."
https://doi.org/10.19111/bulletinofmre.1298494

![Hatay_Sbas](https://github.com/onurkaraca87/Envi-SarScape-Modelling/assets/127317839/eb5c31c0-9ff1-461c-adbe-6be23a0358ac)

This is code for Envi-SarScape SBAS-PS Modelling
input_for_raw_data , output, raster_input, band_increase_number, Pixel raw number, the number of the band
input_for_raw_data     : The "input_for_raw_data" should be geotiff format that inclued all bands.
output                 : The "output" file must be created by user.
raster_input           : The "raster_input" files have to have files for the dates. For the Envi-SarScape output for SBAS or PS process
                          results create "raster" file. 
band_increase_number   : The "band_increase_number" must be 1.
Pixel raw number       : The "Pixel raw number" shows start point for the pixel number on the raws.
The number of the band : The number of the band shows how many bands are inside of the "input_for_raw_data".
![Hatay_Sbas_Interface](https://github.com/onurkaraca87/Envi-SarScape-Modelling/assets/127317839/b5e86688-6a6c-493f-87fa-9199ff2719ff)


If you have any additional inquiries or require further assistance, please don't hesitate to reach out to us via email at "onurkaraca87@hotmail.com" or "gultekinerten@gmail.com". We're here to help and provide support.

