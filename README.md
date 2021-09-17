# CytoData-2021 Challenge 
Welcome to CytoData Hackathon 2021! 

iPSC can be differentiated into any human cell type, providing great potential for research and therapeutic uses. Cell death or loss of pluripotency are common issues in iPSC culturing. Thus, selecting ‘good’ colonies with homogenous population and well-defined edges to carry forward is a critical quality control step in iPSC research.

This year, we challenge you to build an image analysis pipeline that can accurately predict ‘good’ colony formation from an early stage of development (ie. A few hours/days after seeding). The result of this hackathon could lead to a much more efficient quality control process in iPSC culturing. 
We have imaged BobC and KOLF iPSC cell lines on 96-well plates using VIPS (Verified In-situ Plate Seeding) and Incucyte time-lapse imaging systems. We then classified the images as ‘good’ ‘bad’ or ‘ugly’ colonies based on these criteria: 
* ‘Good’: one or more healthy colonies containing homogenous population
* ‘Bad’: colonies with stress (eg. differentiating factors) introduced during development 
* ‘Ugly’: no colony formation because of cell death




## Challenge
You are given both VIPS and Incucyte datasets in the TRAIN folder with images taken over 2 weeks. We have done some preliminary colony segmentation using Cell Profiler. The goal of the challenge is to analyse the pluripotency of these colonies and successfully predict ‘good’, ‘bad’ or ‘ugly’ colonies from the early-stage images in the TEST folder. 

The following parameters can be used as a starting point to analyse colony quality: colony area, diameter, circularity, cell distances etc. 


## Data
The following table describes information of the two datasets we are providing. More details can be found in the metadata.csv files. 

Dataset  | Colony types | Cell line | Imaging time interval
------------- | -------------  | -------------  | ------------
VIPS  | 'Good' & 'Ugly' | BobC, KOLF | Every 24 hrs, then every 2-3 days
Incucyte  | 'Good', 'Bad' & 'ugly' | BobC, KOLF | Every 4 hrs

All data is available in Google Drive: [CytoData 2021](https://drive.google.com/drive/folders/15nshkzrdj8ZdL8cgWMH6ghFyapqoac9E) (about xxGB) 


