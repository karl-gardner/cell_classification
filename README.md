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
  
  <a href="https://www.cancer.gov/">
  <img src="https://user-images.githubusercontent.com/91646805/211325390-f26d7325-acc9-499f-9e42-594ca1ce6444.svg" height="32"/></a><br>

  <a href="https://aip.scitation.org/journal/aml">
  <img src="https://user-images.githubusercontent.com/91646805/211326974-a4d8b218-784c-4236-b309-cb90520f77a9.svg" height="35"/></a>

  <a href="https://colab.research.google.com/github/karl-gardner/ctc_classification/blob/main/ENetV2_classifier.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/211091206-4bee10e4-0e41-4639-899f-e52dec841878.svg" height="32"/></a>

  <a href="https://colab.research.google.com/github/karl-gardner/ctc_classification/blob/main/ResNet_classifier.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/211091614-8e8b4c0a-9f0f-4276-bb36-0ce92040dbe8.svg" height="32"/></a>

 <a href="https://colab.research.google.com/github/karl-gardner/ctc_classification/blob/main/split_dataset.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/173894210-b7c51cae-0ce9-4de7-aab6-faa19fc626bd.svg" height="32"/></a>


# Cell Classification
Cancer diagnostics is an important field of cancer recovery and survival with many expensive procedures needed to administer the correct treatment. Machine Learning (ML) approaches can help with the diagnostic prediction from circulating tumor cells (CTCs) in liquid biopsy, or from a primary tumor in solid biopsy. After predicting the metastatic potential from a deep learning model, doctors in a clinical setting can administer a safe and correct treatment for a specific patient. This paper investigates the use of deep convolutional neural networks for predicting a specific cancer cell line as a tool for label free identification. Specifically, deep learning strategies for weight initialization and performance metrics are described, with transfer learning and the accuracy metric utilized in this work. The equipment used for prediction involve brightfield microscopy without the use of chemical labels, advanced instruments, or time-consuming biological techniques, giving an advantage over current diagnostic methods. In the procedure, three different binary datasets of well-known cancer cell lines were collected, each having a difference in metastatic potential. Two different classification models were adopted (EfficientNetV2 and ResNet-50) with the analysis given for each stage in the ML architecture. The training results for each model and dataset are provided and systematically compared. We found that the test set accuracy showed favorable performance for both ML models with EfficientNetV2 accuracy reaching up to 99%. These test results allowed EfficientNetV2 to outperform ResNet-50 at an average percent increase of 3.5% for each dataset. The high accuracy obtained from the predictions demonstrate that the system can be retrained on a large-scale clinical dataset.
</div>

<img src="https://user-images.githubusercontent.com/91646805/211077815-91b7d636-9bd1-435a-bd97-9aa37845d1cf.jpg"/></a>

<details>
<summary>Instructions (click to expand)</summary>
<br>


1) First create a folder in your google drive account called "cell_classification" (This step is important in order to keep the directories in check)
2) Use this link <a href="https://drive.google.com/drive/folders/1gDWWXDQp-M0cqsKTranTf05x-TqDn4a0?usp=sharing">
  <img src="https://user-images.githubusercontent.com/91646805/156700933-5cc77dba-5df1-40c0-94c8-7459abb6402b.svg" height="18"/></a> to access the shared google drive folder
3) At the top there will be a dropdown arrow after the folder location (Shared with me > data_files): click on this dropdown arrow
4) Click on the "Add shortcut to Drive" button then navigate to inside your ctc_classification folder and click the blue "Add Shortcut" button.  This will add a shortcut to the shared google drive folder in your ctc_classification folder.
5) Open the ENetV2_classifier.ipynb colab notebook from the colab badge provided above then click "Save a copy in Drive" under File > Save a copy in Drive.
6) This will save the notebook in the "Colab Notebooks" folder in your google drive.  Move this notebook to the ctc_classification folder and rename it ENetV2_classifier.ipynb in order for the directories to be correct.
7) Do the same with the ResNet_classifier.ipynb colab notebook. The final cell_classification folder should look like this:![image](https://user-images.githubusercontent.com/91646805/211118374-f74252d6-f332-4112-a95e-eddb16755a3a.png)
7) You can now use the notebooks to perform more testing or contribute to the project.  You can find the code written for many of the figures in the final paper: DOI Website
</details>

<details>
<summary>Testing (click to expand)</summary><br>
Nearly all figures and tables from the paper are outlined in ENetV2 and ResNet50 colab notebooks. First choose the dataset that you would like to investigate, e.g. the SKOV3nvsd dataset. Therefore choose the "dataset" variable as 3 because this is the fourth element in the datasets list:
<img src="https://user-images.githubusercontent.com/91646805/211102029-c66b01c7-064f-48e8-a272-50e47353faad.png"/></a>

Table 1 displays the annotation summary for each dataset after augmentations. This can be shown in section 2.2 of each colab notebook:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/220817076-c79f3e54-9704-4815-a07b-d9014c64a552.png"/></a>

<br><br>
After running this cell you will get the following output:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/220817473-27ce2684-f142-4d4a-a747-6e9ac044020f.png"/></a>

<br><br>
This matches the numbers for the SKOV3drvsn data in Table 2 in the publication:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/221083899-a7e3e9f2-d9ad-4e1d-8356-a60e235afa75.png"/></a>

</details>

<details open>
<summary>Contributions</summary><br>

 **Publication Authors:**<br>Karl Gardner, Rutwik Joshi, Nayeem Kashem, Thanh Pham, Qiugang Lu, and Wei Li<br><br>
 
 **Publication Acknowledgements:**<br>WL acknowledge support from National Science Foundation (CBET, Grant No. 1935792) and National Institute of Health (IMAT, Grant No. 1R21CA240185-01).
</details>
