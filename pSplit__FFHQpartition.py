#necessary libraries import
import sys
import tensorflow as tf
from tensorflow import keras

# Pandas and numpy for data manipulation
import pandas as pd
import numpy as np
np.random.seed(42)

# Matplotlib and seaborn for plotting
import plotly.express as px
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns

# Scipy helper functions
from scipy.stats import percentileofscore
from scipy import stats

# FFHQ SPLIT Partition (Train|Test)
def pSplit__FFHQpartition():

  pSplit=float(input('Please PROVIDE a percentage of TRAINING for a total of {} Training-Test records:  '.format(len(filePath_list))))
  train_picIndex_choice=np.random.choice(picIndex_list, size=int((len(filePath_list)*pSplit)//100))
  len(train_picIndex_choice)

  # picsList=[obj[str(num)] for num in picIndex_list]
  # picsList
  # len(picsList)

  train_picIndex_set=set(train_picIndex_choice)

  #CRUCIAL...image path definition as Thumbnails OR Image ...CRUCIAL !!!
  trainPics_set=['./thumbnails128x128/{}'.format(obj[str(enum)]['thumbnail']["file_path"].split('/')[-1]) for enum in train_picIndex_set]
  #len(trainPics_set), trainPics_set[-1], trainPics_set[22089]  #DJSc_testing

  trainPics_set
  print('FFHQTraining Pics Count as {}% Representative...{}'.format(pSplit,len(train_picIndex_choice)))
  print('FFHQTraining Pics Count as Set...{} ... as {}% true representation'.format(len(trainPics_set),len(trainPics_set)*100//len(picIndex_list) ))
  print(len(train_picIndex_choice)-len(trainPics_set), 'representes the amount of duplicated pictures\
  in our random choice...Hence offsetting the value of our Split percentage Repesentative {} ... :-) Never Mind!!'.format(pSplit) )

  #testPics=[obj[str(num)]['image']["file_path"] for num in picIndex_list if num not in train_picIndex_set] #testPics NO Need to be cast as Set!!!
  #print('FFHQTest Pics Count...{}'.format(len(testPics)))
  testPicIndex_list=[num for num in picIndex_list if num not in train_picIndex_set]
  testPics=['./thumbnails128x128/{}'.format(obj[str(enum)]['thumbnail']["file_path"].split('/')[-1]) for enum in testPicIndex_list]
  print('FFHQTest Pics Count...{}'.format(len(testPics)))


  #Test data PARTITIONing@partiSpliTest into used & reserved(res) portions of TestData.
  partiSpliTest=0.01 #TEST Split
  usedTest_picIndex_choice=np.random.choice(testPicIndex_list, size=int(len(testPics)*partiSpliTest))
  len(usedTest_picIndex_choice)

  usedTest_picIndex_set=set(usedTest_picIndex_choice)

  #CRUCIAL...image path definition as Thumbnails OR Image ...CRUCIAL !!!
  usedTest_Pics_set=['./thumbnails128x128/{}'.format(obj[str(enum)]['thumbnail']["file_path"].split('/')[-1]) for enum in usedTest_picIndex_set]
  #trainPics_set=[obj[str(num)]['image']["file_path"] for num in train_picIndex_set]
  usedTest_Pics_set

  print('FFHQusedTest Pics Count as {}% Representative...{}'.format(partiSpliTest*100,len(usedTest_picIndex_choice)))
  print('FFHQusedTest Pics Count as Set...{} ... as {:.2f}% true Representation'.format(len(usedTest_Pics_set),len(usedTest_Pics_set)*100/len(testPicIndex_list) ))
  print(len(usedTest_picIndex_choice)-len(usedTest_Pics_set), 'represents the amount of duplicated pictures\
  in our random choice...Hence offsetting the value of our Partition percentage Repesentative {}% ... :-) Never Mind!!'.format(partiSpliTest*100) )

  resTest_Pics=['./thumbnails128x128/{}'.format(obj[str(enum)]['thumbnail']["file_path"].split('/')[-1]) for enum in testPicIndex_list if enum not in usedTest_picIndex_set]
  #testPics NO Need to be cast as Set!!!


  len(testPics)==len(usedTest_Pics_set) +len(resTest_Pics)
  Total=len(trainPics_set) + len(testPics)

  print('FFHQtrainPics_set Count is ...', len(trainPics_set))
  print('FFHQusedTest_Pics_set Count is ...', len(usedTest_Pics_set))
  print('FFHQresTest_Pics Count is ...', len(resTest_Pics))

  print('{} + {} + {} = {} TotalFFHQ'.format(len(trainPics_set),len(usedTest_Pics_set), len(resTest_Pics), len(trainPics_set) + len(usedTest_Pics_set) + len(resTest_Pics) ))
  print(Total== (len(trainPics_set) + len(usedTest_Pics_set) + len(resTest_Pics)))

  return trainPics_set, len(trainPics_set), testPics, len(testPics),usedTest_Pics_set, len(usedTest_Pics_set), resTest_Pics, len(resTest_Pics) #4x2 (8) returned variables