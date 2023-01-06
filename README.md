<h4 align="center">Author: Karl Gardner<br>PhD Candidate, Department of Chemical Engineering, Texas Tech University</h4>

<div align="center">
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/154190573-53e361f6-7c60-4062-b56b-7cbd11d39fc4.jpg"/></a><br><br>
  
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/156635015-0cdcb0bb-0482-4693-b096-04f2a78f6b8e.svg" height="32"/></a>
  
  <a href="https://sites.google.com/view/scalab/">
  <img src="https://user-images.githubusercontent.com/91646805/211090371-b36f11db-15e7-48eb-901a-44204998ec38.svg" height="35"/></a>
  
  <a href="https://www.depts.ttu.edu/che/">
  <img src="https://user-images.githubusercontent.com/91646805/156641068-be8f0336-89b5-43e9-aa64-39481ce37c94.svg" height="32"/></a>
  
  <a href="https://roboflow.com/">
  <img src="https://user-images.githubusercontent.com/91646805/156641388-c609a6aa-8fce-47f0-a111-abfde9c5da05.svg" height="32"/></a><br>
  
  <a href="https://www.rsc.org/journals-books-databases/about-journals/lab-on-a-chip/">
  <img src="https://user-images.githubusercontent.com/91646805/169677461-13cb1d50-e7cf-457e-8777-cc6df29ce0bd.svg" height="32"/></a>
  
  <a href="https://colab.research.google.com/github/karl-gardner/ctc_classification/blob/main/classify_ctcs.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/211091206-4bee10e4-0e41-4639-899f-e52dec841878.svg" height="32"/></a>

  <a href="https://colab.research.google.com/github/karl-gardner/ctc_classification/blob/main/split_dataset.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/173894210-b7c51cae-0ce9-4de7-aab6-faa19fc626bd.svg" height="32"/></a>

  <a href="https://github.com/ultralytics">
  <img src="https://user-images.githubusercontent.com/91646805/156641066-fbc3635b-f373-4cb7-b141-9bcaad21beff.svg" height="32"/></a>




# CTC Classification
Cancer diagnostics is an important field of cancer recovery and survival with many expensive procedures needed to administer the correct treatment. Machine Learning (ML) approaches can help with the diagnostic prediction from circulating tumor cells (CTCs) in liquid biopsy, or from a primary tumor in solid biopsy. After predicting the metastatic potential from a deep learning model, doctors in a clinical setting can administer a safe and correct treatment for a specific patient. This paper investigates the use of deep convolutional neural networks for predicting a specific cancer cell line as a tool for label free identification. Specifically, deep learning strategies for weight initialization and performance metrics are described, with transfer learning and the accuracy metric utilized in this work. The equipment used for prediction involve brightfield microscopy without the use of chemical labels, advanced instruments, or time-consuming biological techniques, giving an advantage over current diagnostic methods. In the procedure, three different binary datasets of well-known cancer cell lines were collected, each having a difference in metastatic potential. Two different classification models were adopted (EfficientNetV2 and ResNet-50) with the analysis given for each stage in the ML architecture. The training results for each model and dataset are provided and systematically compared. We found that the test set accuracy showed favorable performance for both ML models with EfficientNetV2 accuracy reaching up to 99%. These test results allowed EfficientNetV2 to outperform ResNet-50 at an average percent increase of 3.5% for each dataset. The high accuracy obtained from the predictions demonstrate that the system can be retrained on a large-scale clinical dataset.
</div>

<img src="https://user-images.githubusercontent.com/91646805/211077815-91b7d636-9bd1-435a-bd97-9aa37845d1cf.jpg"/></a>

<details>
<summary>Instructions (click to expand)</summary>
<br>

1) First create a folder in your google drive account called "ctc_classification" (This step is important in order to keep the directories in check)
2) Use this link <a href="https://drive.google.com/drive/folders/1gDWWXDQp-M0cqsKTranTf05x-TqDn4a0?usp=sharing">
  <img src="https://user-images.githubusercontent.com/91646805/156700933-5cc77dba-5df1-40c0-94c8-7459abb6402b.svg" height="18"/></a> to access the shared google drive folder
3) At the top there will be a dropdown arrow after the folder location (Shared with me > data_files): click on this dropdown arrow
4) Click on the "Add shortcut to Drive" button then navigate to inside your ctc_classification folder and click the blue "Add Shortcut" button.  This will add a shortcut to the shared google drive folder in your ctc_classification folder.
5) Open the classify_ctcs.ipynb colab notebook from this link <a href="https://colab.research.google.com/github/karl-gardner/ctc_classification/blob/main/classify_ctcs.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/174132568-f2367233-46f3-45f2-8cfe-7e89ce4789ed.svg" height="19"/></a> then click "Save a copy in Drive" under File > Save a copy in Drive.

6) This will save the notebook in the "Colab Notebooks" folder in your google drive.  Move this notebook to the ctc_classification folder and rename it classify_ctcs.ipynb in order for the directories to be correct.  The final ctc_classification folder should look like this:![image](https://user-images.githubusercontent.com/91646805/173897636-ec024bb9-5484-444e-8709-497db1ffcab9.png)

7) You can now use the notebooks to perform more testing or contribute to the project.  You can find the code written for many of the figures in the final paper: DOI Website
</details>

<details>
<summary>Testing (click to expand)</summary><br>
Nearly all figures and tables from the paper are outlined in yolov3.ipynb and yolov5.ipynb colab notebooks. For example Table 2 displays the annotation summary for cell and droplet models before augmentations. This can be shown in section 2. of the colab notebook:
![table_2](https://user-images.githubusercontent.com/91646805/170845758-27eae439-ad1f-4327-b970-9c21235a06b7.jpg)
You may run this for example by first uncommenting section 1.1 labeled "Data with No Augmentation (No_Augmentation)" then uncommenting section 2. labeled: "For droplet model". Then the following output will be printed:
![table_2](https://user-images.githubusercontent.com/91646805/169673813-3c9c0321-fec8-4ae4-a092-fdf8be4f3464.jpg)
![table_2](https://user-images.githubusercontent.com/91646805/169673815-b5ea0589-038f-4a4c-8d84-2fdd2b69ba58.png)
![table_2_droplet](https://user-images.githubusercontent.com/91646805/169673816-8f4f5a29-fe0d-43aa-bd8d-3f9e9f994a8f.png)

</details>

<details open>
<summary>Contributions</summary><br>

 **Publication Authors:**<br>Karl Gardner, Md Mezbah Uddin, Linh Tran, Thanh Pham, Siva Vanapalli, and Wei Li<br><br>
 
 **Publication Acknowledgements:**<br>WL acknowledge support from National Science Foundation (CBET, Grant No. 1935792) and National Institute of Health (IMAT, Grant No. 1R21CA240185-01).
</details>
