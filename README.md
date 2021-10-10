
# Welcome to CytoData Hackathon 2021! 

Welcome to Cytodata Hackathon 2021. Grab a cup of your favourite drink and join us in a journey that will bring you to learn new skills, make new friends and put your quantitative skills to the test while dealing with an interesting challenge in stem cells.

<br/>

Pluripotency is the capacity of certain stem cells to give rise to virtually any cell of the body. Pluripotent cells can be taken from the early stages of development or induced through transduction of specific transcription factors (reprogramming).

Human iPSC (induced pluripotent stem cells) continuously face a choice between making exact copies of themselves (‘self-renew’), or turn into any human cell type (‘differentiation’), providing great potential for research and therapeutic uses.

Cell death or loss of pluripotency are common in iPSC culturing. Thus, assessing cell state (e.g. good/pluripotent or bad/differentiated) is a critical step in stem cell research, both in academia (to study them) or in biotech (for quality control).

<br/>

* ‘Good’: Colonies with pluripotent cells
* ‘Bad’: Colonies with differentiated cells
* ‘Empty’: Empty wells, no or very few cells

We imaged human iPSC cells on 96-well plates over 2 weeks using Sartorius Incucyte device. For your convenience we provide a training set divided as above in good, bad, empty and test sets with real-life examples.

Images will have single cells from early timepoints dividing to make colonies over time; feel free to take full advantage of cell morphology, colony morphology and/or context features such as how distant cells are to each other over time, etc..

This year, we challenge you to build pipelines that can analyse and assess the pluripotency of iPSC based just on phase microscopy images. The result of this hackathon could lead to more efficient processes in iPSC culturing and analysis.




<br/><br/>

## Table of Contents

[Challenges](#challenges)

[Prizes](#prizes)

[Dataset](#dataset)

[Who](#who)

[When](#when-all-times-in-bst-uk-time)

[Where](#where)

[What](#what)

[Questions?](#questions)


<br/><br/>

## Challenges
The CytoData Hackathon 2021: 3 challenges for your quantitative/qualitative minds. Please use our standardised format sheet for reporting your clustering predictions. Evaluations will have two quantitative scores and one qualitative jury prize. 


### Challenge 1: 
Using the dataset in the ‘Training’ folder, cluster the images in the ‘Test 1’ folders correctly into ‘Good’ and ‘Bad’ categories. Teams which clustered the most images correctly will get the highest score.


### Challenge 2a:
How generalisable is your algorithm? Can it assess images independent of the time point on a single image? Please use your algorithm to cluster the images in the ‘Test 2a’ folder. Teams with the most images correctly clustered will get the highest score.


### Challenge 2b:
Can you obtain spatial information from the images? Would you be able to tell which part of the colony is good and which part is bad for the images in our folders? You can start from training test1 and move onto the others too. 


### Challenge 3:
Come up with your own standards to assess the pluripotency of iPSC. Any other bright idea welcome, let your imagination run, the sky's the limit. The aim is to have a feedback loop clustering in good/bad the culture status to be used for quality control.

<br/><br/>

## Prizes

Consist in a combination of cytodata glory, legendary bit.bio mugs, other surprises

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

Test2a 6550 files -> 13GB (scrambled from time information)



<br/>

All data can be downlodaed using the following links: 

[Training.zip](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/Training.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PYQ7KGDWK%2F20211004%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211004T145706Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d91993d2e38ba2da13a2bd6d68a7ab8ad1990104d5c0dd005750128bb6381d8e) (4.7 GB)

[Test.zip](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/Test.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PS6T2VXYB%2F20211008%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211008T153204Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=bfeb82b5d4a1590a4a251205be99151c28eb4bd52bc2d5e895f03d4b78505091)

If you find the Test.zip too large to download, you can download separately subsets of the Test dataset using links below:

[Test 1.zip](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/Test1.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PYQ7KGDWK%2F20211004%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211004T224009Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=ec97be5262980d1022665fd7d34f37555ebead1517734846dc38b926fc9d5963)

[Test 2a.zip](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/Test2a.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PYQ7KGDWK%2F20211004%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211004T223814Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e4ef0dba1ebe24def6d9d059481b3a3202442b0e6556c2983cc85944ef60e9da)



<br/>


We have done some preliminary colony segmentation using Cell Profiler. We have not segmented further objects inside each colony. The measurements for colony segmentation can be downloaded here as csv files: [docs.csv](https://bitbio-ext-pheno-hackathon.s3.amazonaws.com/docs_csv.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQIB6BT2PS6T2VXYB%2F20211006%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211006T134814Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f4fa777639caf928e59ac689f0cc4ca68a38a34ec3e37fd1f94be4faf213b461). Feel free to use any of the parameters as a starting point to analyse colony pluripotency state: colony area, diameter, circularity, cell distances, cell morphology, any of the above, combined cell profiler features, multidimensional hyperspaces, etc.

Thanks to Cytodata and all scientists in our Cellular Phenotyping team for support. The experiments for this dataset were set up and acquired by Sarah Hussain, Stefan Milde, Fiona Connolly at bit.bio using Sartorius Incucyte device. The dataset was organised with the help from Sanaullah Nazir at bit.bio. 


<br/><br/>

## Who?

Over 70 hackathon participants will be grouped in 9 teams. Please select a team by clicking here: [CytoData 2021 - Teams Registration](https://docs.google.com/spreadsheets/d/19BG9SuqtaowQ7qc3F0YIFzv47Y7-RwAlZlvkppntxk4/edit#gid=0), enter your name and timezone. We encourage you to select team members on similar timezones.

Feel free to use the [Slack channel](https://cytodata.slack.com/ssb/redirect#/shared-invite/email) to add a few words about yourself or a link to your website or workplace. Great chance to meet up sharing your passion for image analysis and computation.



<br/><br/>

## When (all times in BST, UK time)

Wednesday 6th October:
 - Dataset and instructions released
 - Please make sure you can download the data and read me


Friday 8th October:
 - 13:00-14:00: Introduction to dataset
 - 14:00-16:00: Open desk for participants to ask questions


Monday 11th October:
 - 13:00-14:00: Refresher for dataset background
 - 14:00-16:00: Open desk for participants to ask questions


Wednesday 13th October:
 - 13:00-16:30: Cytodata conference
 - 16:30-18:00: Supervised hacking


Thursday 14th October:
 - 13:00-16:30: Cytodata conference
 - 16:30-18:00: Supervised hacking


Friday 15th October:
 - 13:00-14:00: Supervised hacking wrap up
 - 14:00-17:00: All hackers to showcase their work
 - 17:00-17:30: The Jury gathers
 - 17:30-18:00: Closure ceremony and winners communicated



<br/><br/>

## Where?

**Conference Zoom channel**


**Main Zoom channel for Hackathon**

[https://us02web.zoom.us/j/89647782734?pwd=Nmx5d1VSazdZZlRZRXNyQmhML2N5dz09](https://us02web.zoom.us/j/89647782734?pwd=Nmx5d1VSazdZZlRZRXNyQmhML2N5dz09)

Once you have finalised your teams, please join the corresponding Zoom breakout room in the link above. We will do our best to have one of us 1-6pm UK time. That will give you a chance to ask questions so we all make sure the tasks are clear.


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

Git link: [https://github.com/Esme233/Cytodata-hackathon-2021](https://github.com/Esme233/Cytodata-hackathon-2021)






