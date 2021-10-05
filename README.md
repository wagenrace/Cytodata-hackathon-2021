
# Welcome to CytoData Hackathon 2021! 

Welcome to Cytodata Hackathon 2021. Grab a cup of your favourite drink and join us in a journey that will bring you to learn new skills, make new friends and put your quantitative skills to the test dealing with an interesting challenge in stem cells.

<br/>

Pluripotency is the capacity of certain stem cells to give rise to virtually any cell of the body. Pluripotent cells can be taken from the early stages of development or induced through transduction of specific transcription factors (reprogramming).

Human iPSC (induced pluripotent stem cells) continuously face a choice between making exact copies of themselves (‘self-renew’), or turn into any human cell type (‘differentiation’), providing great potential for research and therapeutic uses.

Cell death or loss of pluripotency are common in iPSC culturing. Thus, assessing cell state (e.g. good/pluripotent or bad/differentiated) is a critical step in stem cell research, both in academia (to study them) or in biotech (for quality control).

<br/>

This year, we challenge you to build pipelines that can analyse and assess the pluripotency of iPSC based just on phase microscopy images. The result of this hackathon could lead to more efficient processes in iPSC culturing and analysis.

Please note that single cells make colonies over time when dividing, so feel free to take full advantage of cell morphology and colony morphology and to include context features such as how distant cells are to each other over time, etc..

We have imaged human iPSC cells on 96-well plates over 2 weeks using the Incucyte time-lapse imaging system. For your convenience we provide a training set as divided below: 
* ‘Good’: Colonies with pluripotent cells
* ‘Bad’: Colonies with differentiated cells
* ‘Empty’: Empty wells with no cells or very few

<br/><br/>


## Challenges
The CytoData Hackathon 2021 presents 3 challenges for your quantitative minds.
Please use our standardised format sheet for reporting your clustering prediction.

### Challenge 1: 
Using the dataset in the ‘Training’ folder, cluster the images in the ‘Test 1’ folders correctly into ‘Good’ and ‘Bad’ categories. Teams which clustered the most images correctly will get the highest score.

### Challenge 2a:
How generalisable is your algorithm? Can it assess images independent of the time point on a single image? Please use your algorithm to cluster the images in the ‘Test 2a’ folder. Teams with the most images correctly clustered will get the highest score.

### Challenge 2b:
Does your algorithm work on assessing images in the ‘Test 2b’ folder, which are acquired using another imaging device called VIPS (Verified In-situ Plate Seeding)?

### Challenge 2c:
Can you obtain spatial information from the images? Would you be able to tell which part of the colony is good and which part is bad for the images in ‘Test 1’, ‘Test 2a’ and ‘Test 2b’ folders? 

### Challenge 2d:
Come up with your own standards to assess the pluripotency of iPSC. Any other bright idea welcome, let your imagination run, the sky's the limit. The aim is to have a feedback loop on the culture status that could be used as a quality control.


<br/><br/>

## Prizes

**1. Best score on cluster Test 1**

**2. Best score on cluster Test 2a**

**3. Best jury prize (visualisation-showcasing)**





## Dataset
75 human iPS colonies

2 different human iPS cell lines

90 images per well over 2 weeks
 
Training set (Good - Bad - Empty)

Test1 6550 files -> 13GB (containing time information)
Test2 6550 files -> 13GB (scrambled from time information)
Test3 252 files -> 6GB (images from another device)

All data can be downlodaed using the following links: 

[Training.zip](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/Training.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PYQ7KGDWK%2F20211004%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211004T145706Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d91993d2e38ba2da13a2bd6d68a7ab8ad1990104d5c0dd005750128bb6381d8e) (4.7 GB)

[Test.zip](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/Test.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PYQ7KGDWK%2F20211004%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211004T180937Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=3f82c637be9310c3e46cbe2a7fa40b35844c77637121ceec9439ea6e50c8ff83) (27 GB)

We have done some preliminary colony segmentation using Cell Profiler. We have not segmented further objects inside each colonies. The measurements for colony segmentation will be found soon in the same folder, in the metadata.csv file. Feel free to use any of the parameters as a starting point to analyse colony pluripotency state: colony area, diameter, circularity, cell distances, cell morphology, any of the above, all the cell profiler features together, etc.

We are grateful to all the scientists in the Cellular Phenotyping team for support. The experiments for the Hackathon image dataset were generated by Sarah Hussain, Stefan Milde, Fiona Connolly at bit.bio using Sartorius Incucyte and VIPS devices.





