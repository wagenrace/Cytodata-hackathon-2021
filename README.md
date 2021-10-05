
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





## Data
The following table describes information of the two datasets we are providing. More details can be found in the metadata.csv files. 

Dataset  | Colony types | Cell line | Imaging time interval
------------- | -------------  | -------------  | ------------
VIPS  | 'Good' & 'Ugly' | BobC, KOLF | Every 24 hrs, then every 2-3 days
Incucyte  | 'Good', 'Bad' & 'ugly' | BobC, KOLF | Every 4 hrs

All data is available in Google Drive: [CytoData 2021](https://drive.google.com/drive/folders/15nshkzrdj8ZdL8cgWMH6ghFyapqoac9E) (about xxGB) 


