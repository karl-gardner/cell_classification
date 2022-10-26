# imports
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import itertools
import numpy as np

def filter(dataset):
  datasets = ["catsvsdogs", "PC3vsDU145", "PC3vsLnCAP", "SKOV3nvsd"]
  class_names = [["dogs", "cats"], ["DU145", "PC3"], ["LnCAP", "PC3"], ["drSKOV3", "nSKOV3"]]
  if datasets[dataset] == "catsvsdogs":
    code_byte = "JFIF"
    extension = ".jpg"
  else:
    code_byte = "PNG"
    extension = ".png"
  class_1 = 0
  class_2 = 0
  for class_name in class_names[dataset]:
    for split in ["training", "testing", "validation"]:
      folder_path = f"{datasets[dataset]}/split_ds/{split}/{class_name}"
      for fname in os.listdir(folder_path):
        fpath = f"{folder_path}/{fname}"
        try:
          fobj = open(fpath, "rb")
          check_1 = tf.compat.as_bytes(code_byte) in fobj.peek(10)
          check_2 = fpath[-4:] == extension
        finally:
          fobj.close()
        if (not check_1) or (not check_2):
          # Delete corrupted image
          os.remove(fpath)
          if class_name == class_names[dataset][0]:
            class_1  += 1
          if class_name == class_names[dataset][1]:
            class_2 += 1
  return (class_1, class_2)



def save_confusion_matrix(cm, target_names, fname="/confusion_matrix.tif", normalize=True):

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy
    
    cmap = plt.get_cmap('summer')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=15)

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45,fontsize=20)
        plt.yticks(tick_marks, target_names,fontsize=20)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color= "black",fontsize=20)
    plt.tight_layout()
    plt.ylabel("True label", fontsize=20)
    plt.xlabel("Predicted label".format(accuracy, misclass), fontsize=20)
    plt.savefig(fname, dpi=500, bbox_inches="tight", transparent="True")
    plt.show()
