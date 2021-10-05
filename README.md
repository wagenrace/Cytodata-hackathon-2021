
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



<br/><br/>

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

<br/>

We have done some preliminary colony segmentation using Cell Profiler. We have not segmented further objects inside each colonies. The measurements for colony segmentation will be found soon in the same folder, in the metadata.csv file. Feel free to use any of the parameters as a starting point to analyse colony pluripotency state: colony area, diameter, circularity, cell distances, cell morphology, any of the above, all the cell profiler features together, etc.

We are grateful to all the scientists in the Cellular Phenotyping team for support. The experiments for the Hackathon image dataset were generated by Sarah Hussain, Stefan Milde, Fiona Connolly at bit.bio using Sartorius Incucyte and VIPS devices.

<br/><br/>




## When (all times in BST, UK time)

Wednesday 6th October:
 - 13:00-14:00: Dataset released and brief introduction.

Friday 8th October:
 - 13:00-14:00: Refresher for dataset background.
 - 14:00-16:00: Open desk for participants to ask questions.

Monday 11th October:
 - 13:00-14:00: Refresher for dataset background.
 - 14:00-16:00: Open desk for participants to ask questions.

Wednesday 13th October:
 - 16:30-18:00: Supervised hacking.

Thursday 14th October:
 - 16:30-18:00: Supervised hacking.

Friday 15th October:
 - 13:00-14:00: Supervised hacking.
 - 14:00-17:00: All hackers to showcase their work.
 - 17:00-17:30: The Jury gathers
 - 17:30-18:00: Closure ceremony and winners communicated


<br/><br/>

## Where?

**Main Zoom channel for Hackathon**

[https://us02web.zoom.us/j/89753772712?pwd=K2xncHVicEx6anhPR3ZjOGY0QUxpQT09](https://us02web.zoom.us/j/89753772712?pwd=K2xncHVicEx6anhPR3ZjOGY0QUxpQT09)

**Team Zoom channels**

Team 1:

[https://us02web.zoom.us/j/83167550073?pwd=N2IrTlZHZC9mZm1ITThJOUdNRElNQT09](https://us02web.zoom.us/j/83167550073?pwd=N2IrTlZHZC9mZm1ITThJOUdNRElNQT09)

Team 2:

[https://us02web.zoom.us/j/83553958700?pwd=MnE5NGJQQ1FWVWlUZWMyd1haUURIQT09](https://us02web.zoom.us/j/83553958700?pwd=MnE5NGJQQ1FWVWlUZWMyd1haUURIQT09)

Team 3:

[https://us02web.zoom.us/j/83713948743?pwd=T0xTLzdwMkJRWENxM3JhMVI1MS9mZz09](https://us02web.zoom.us/j/83713948743?pwd=T0xTLzdwMkJRWENxM3JhMVI1MS9mZz09)

Team 4:

[https://us02web.zoom.us/j/83935588368?pwd=ditCQitmVzdiQklCcEc1V0JPaGs5dz09](https://us02web.zoom.us/j/83935588368?pwd=ditCQitmVzdiQklCcEc1V0JPaGs5dz09)

Team 5: 

[https://us02web.zoom.us/j/84016626657?pwd=dlJ2aFU4MEJISU1nS3hYSW5LQVFmQT09](https://us02web.zoom.us/j/84016626657?pwd=dlJ2aFU4MEJISU1nS3hYSW5LQVFmQT09)

Team 6:

[https://us02web.zoom.us/j/89253200447?pwd=cWpNd0J0cFlrMkxMaFRrRjlhZjZyZz09](https://us02web.zoom.us/j/89253200447?pwd=cWpNd0J0cFlrMkxMaFRrRjlhZjZyZz09)

Team 7:

[https://us02web.zoom.us/j/83817866495?pwd=WVM5V0hsTFZTcjhhN3dnbTErTm4zdz09](https://us02web.zoom.us/j/83817866495?pwd=WVM5V0hsTFZTcjhhN3dnbTErTm4zdz09)

Team 8:

[https://us02web.zoom.us/j/89673434880?pwd=MmYvWE1qRG5JbS9yQ3JSb2NxcC9NZz09](https://us02web.zoom.us/j/89673434880?pwd=MmYvWE1qRG5JbS9yQ3JSb2NxcC9NZz09)

Team 9:

[https://us02web.zoom.us/j/84547362023?pwd=Qm9BZ3R6Y2ZMODNxS3J3R3dndEEyQT09](https://us02web.zoom.us/j/84547362023?pwd=Qm9BZ3R6Y2ZMODNxS3J3R3dndEEyQT09)

<br/><br/>



## What?

Please note this is a chance to bring together a community of creators, scientists and analysts with the spirit of learning together. We are confident everyone will respond to this spirit and we will not tolerate disruptive, offensive or inappropriate behaviour.

The Hackathon and conference is organised by bit.bio and Cytodata together. All code submissions should be available under MIT license (open source). The data from the shared dataset should be made available under CC0 license (open source).

This will allow anyone to use freely, to build on the community expertise as in the past years and to enjoy the occasion to build connections, learn about new opportunities to share experience with other participants.

<br/><br/>

## Questions?

Feel free to reach us out on the dedicated zoom main hackathon channel.
Alternatively please feel free to post on the cytodata slack channel.
See [https://society.cytodata.org](https://society.cytodata.org) and [https://www.bit.bio/events/cytodata2021](https://www.bit.bio/events/cytodata2021)






