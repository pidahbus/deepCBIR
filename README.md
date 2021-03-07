# CBIR using features derived by Deep Learning
This repository contains code of Content Based Image Retrieval using features derived by Deep Learning. The academic paper can be found here: https://arxiv.org/abs/2002.07877. In this paper, we propose to use features derived from pre-trained network models from a deep-learning convolution network trained for a large image classification problem. This approach appears to produce vastly superior results for a variety of databases, and it outperforms many contemporary CBIR systems.

## How to set up
This is an UI based implementation. To set up the project, follow the below steps.
- Clone the repository
- Put your database images in the [database folder](https://github.com/pidahbus/deepCBIR/tree/main/app/database). Some sample images are put here.
- Install [requirements.txt](https://github.com/pidahbus/deepCBIR/blob/main/requirements.txt) file by runnig ```pip install -r requirements.txt```
- Navigate to the repository folder and run in the terminal ```python run.py```

## How to Use
The app may take upto several minutes to load for the first time. This is because it will create vectors from database images using deep learning model. Once done, go to the web browser and open ```http://0.0.0.0:5000```. This will open the below page.
![](https://github.com/pidahbus/deepCBIR/blob/main/app/tmp/page-1.jpg)

In this page browse the query image and put the scope value. Then press ```Retrieve``` option. Then it will redirect to a new page and show the retrieved images for the given query image as shown below.
![](https://github.com/pidahbus/deepCBIR/blob/main/app/tmp/page-2.jpg)

## Citation
This paper is submitted for journal publication. If you are using this repository then please use the below BibTeX to cite for now.

```
@ARTICLE{2020arXiv200207877M,
       author = {{Maji}, Subhadip and {Bose}, Smarajit},
        title = "{CBIR using features derived by Deep Learning}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Information Retrieval, Computer Science - Computer Vision and Pattern Recognition, Computer Science - Machine Learning, Statistics - Machine Learning},
         year = 2020,
        month = feb,
          eid = {arXiv:2002.07877},
        pages = {arXiv:2002.07877},
archivePrefix = {arXiv},
       eprint = {2002.07877},
 primaryClass = {cs.IR},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2020arXiv200207877M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

## More Information
For any clarification feel free to raise an issue. Additionally you can reach us at subhadipmaji.jumech@gmail.com

