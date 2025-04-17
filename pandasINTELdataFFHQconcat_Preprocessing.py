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
## **Data CONCAT & Preprocessing with Pandas** SUMMARY
import pandas

def pandasINTELdataFFHQconcat_Preprocessing():


  #FFHQ / INTEL Load&Pandas

  FFHQtrainPics_set, len_FFHQtrainPics_set, FFHQtestPics, len_FFHQtestPics, FFHQusedTest_Pics_set, len_FFHQusedTest_Pics_set, FFHQresTestPics, len_FFHQresTestPics =pSplit__FFHQpartition()

  # ...TRAIN & TEST...#

  #FFHQ (HumFaces)

  print('len_FFHQtrainPics_set is ... ', len_FFHQtrainPics_set)
  print('len_FFHQusedTest_Pics_set is ...', len_FFHQusedTest_Pics_set)

  FFHQtrain_Xdf=pd.DataFrame(FFHQtrainPics_set)
  FFHQtrain_Xdf
  FFHQtrain_Xdf.head

  FFHQusedTest_Xdf=pd.DataFrame(FFHQusedTest_Pics_set)
  FFHQusedTest_Xdf
  FFHQusedTest_Xdf.head

  FFHQtr_classeID=['FFHQtr_{}'.format(i) for i in FFHQtrain_Xdf.index]
  #CIFtr_classeID , FFHQtr_classeID
  FFHQusedTest_classeID=['FFHQusedTest_{}'.format(i) for i in FFHQusedTest_Xdf.index]


#FFHQtrain_Xdf.index
  FFHQtrain_Xdf['jayIndex']=FFHQtrain_Xdf.index
  FFHQusedTest_Xdf['test_jayIndex']=FFHQusedTest_Xdf.index


  FFHQtrain_Xdf['ID']=FFHQtrain_Xdf['jayIndex'].apply(lambda x:FFHQtr_classeID[x])
  FFHQtrain_Xdf.head
  FFHQtrain_Xdf['SubCateg']='HumanFace'
  FFHQtrain_Xdf

  FFHQusedTest_Xdf['test_ID']=FFHQusedTest_Xdf['test_jayIndex'].apply(lambda x:FFHQusedTest_classeID[x])
  FFHQusedTest_Xdf.head
  FFHQusedTest_Xdf['test_SubCateg']='HumanFace'
  FFHQusedTest_Xdf


  abstract_FFHQtrain_Xdf=FFHQtrain_Xdf[["ID","jayIndex","SubCateg"]]
  abstract_FFHQtrain_Xdf

  abstract_FFHQusedTest_Xdf=FFHQusedTest_Xdf[["test_ID","test_jayIndex","test_SubCateg"]]
  abstract_FFHQusedTest_Xdf


  #np.array(train_dataJay).shape, len(train_dataJay)
  INTELobj_train.keys()
  #np.array(labels_list)
  INTELobj_test.keys()

#INTEL  (Non Faces) sceneries
  INTELtrain_Xdf=pandas.DataFrame()
  INTELtrain_Xdf['ID']=np_labels_list
  INTELtrain_Xdf['jayIndex']=INTELtrain_Xdf.index
  INTELtrain_Xdf['SubCateg']= INTELtrain_Xdf['ID'].apply(lambda x: x.split('_')[0])
  INTELtrain_Xdf

  INTELtest_Xdf=pandas.DataFrame()
  INTELtest_Xdf['test_ID']=np_test_labels_list
  INTELtest_Xdf['test_jayIndex']=INTELtest_Xdf.index
  INTELtest_Xdf['test_SubCateg']= INTELtest_Xdf['test_ID'].apply(lambda x: x.split('_')[0])
  INTELtest_Xdf


  len(INTELtrain_Xdf),len(abstract_FFHQtrain_Xdf), len(INTELtrain_Xdf) + len(abstract_FFHQtrain_Xdf)
  len(INTELtest_Xdf),len(abstract_FFHQusedTest_Xdf), len(INTELtest_Xdf) + len(abstract_FFHQusedTest_Xdf)


      # pd.concat([abstract_CIFARtrain_Xdf,abstract_FFHQtrain_Xdf],axis=1) # all indexes included
  mergedTRAIN_INTEL_FFHQ_df=pd.concat([INTELtrain_Xdf,abstract_FFHQtrain_Xdf],axis=0) # all indexes included
  mergedTRAIN_INTEL_FFHQ_df

  mergedTEST_INTEL_FFHQ_df=pd.concat([INTELtest_Xdf,abstract_FFHQusedTest_Xdf],axis=0) # all indexes included
  mergedTEST_INTEL_FFHQ_df


  print('\n FFHQtrain_Xdf: \n {}'.format(FFHQtrain_Xdf))
  print('\n FFHQusedTest_Xdf: \n {}'.format(FFHQusedTest_Xdf))


  #Readjustment & Mergence (INTEL & FFHQ)

  INTELtrain_Xdf=INTELtrain_Xdf[["ID","jayIndex","SubCateg"]]
  print('\n abstract_INTELtrain_Xdf is : \n {}'.format(INTELtrain_Xdf))

  INTELtest_Xdf=INTELtest_Xdf[["test_ID","test_jayIndex","test_SubCateg"]]
  print('\n abstract_INTELtest_Xdf is : \n {}'.format(INTELtest_Xdf))


  abstract_FFHQtrain_Xdf=FFHQtrain_Xdf[["ID","jayIndex","SubCateg"]]
  print('\n abstract_FFHQtrain_Xdf is: \n {}'.format(abstract_FFHQtrain_Xdf))

  abstract_FFHQusedTest_Xdf=FFHQusedTest_Xdf[["test_ID","test_jayIndex","test_SubCateg"]]
  print('\n abstract_FFHQusedTest_Xdf is: \n {}'.format(abstract_FFHQusedTest_Xdf))


  len(INTELtrain_Xdf) + len(abstract_FFHQtrain_Xdf)

  len(INTELtest_Xdf) + len(abstract_FFHQusedTest_Xdf)


  mergedTRAIN_INTEL_FFHQ_df=pd.concat([INTELtrain_Xdf,abstract_FFHQtrain_Xdf],axis=0) # all indexes included
  print('\n mergedTRAIN_INTEL_FFHQ_df is : \n {}'.format(mergedTRAIN_INTEL_FFHQ_df))

  mergedTEST_INTEL_FFHQ_df=pd.concat([INTELtest_Xdf,abstract_FFHQusedTest_Xdf],axis=0) # all indexes included
  print('\n mergedTEST_INTEL_FFHQ_df is : \n {}'.format(mergedTEST_INTEL_FFHQ_df))


  #Check Balances

  #TRAIN
  len(INTELtrain_Xdf) + len(abstract_FFHQtrain_Xdf) == len(mergedTRAIN_INTEL_FFHQ_df)
  print('\n Mergence CheckBalance is : {} as ...\n len(INTELtrain_Xdf) is: {} \n len(abstract_FFHQtrain_Xdf) is {} \
\n len(mergedTRAIN_INTEL_FFHQ_df) is {} '.format((len(INTELtrain_Xdf) + len(abstract_FFHQtrain_Xdf) == len(mergedTRAIN_INTEL_FFHQ_df)),len(INTELtrain_Xdf), len(abstract_FFHQtrain_Xdf),len(mergedTRAIN_INTEL_FFHQ_df)  ))

  #TEST
  len(INTELtest_Xdf) + len(abstract_FFHQusedTest_Xdf) == len(mergedTEST_INTEL_FFHQ_df)
  print('\n Mergence CheckBalance is : {} as ...\n len(INTELtest_Xdf) is: {} \n len(abstract_FFHQusedTest_Xdf) is {} \
\n len(mergedTRAIN_INTEL_FFHQ_df) is {} '.format((len(INTELtest_Xdf) + len(abstract_FFHQusedTest_Xdf) == len(mergedTEST_INTEL_FFHQ_df)),len(INTELtest_Xdf), len(abstract_FFHQusedTest_Xdf),len(mergedTEST_INTEL_FFHQ_df)  ))


  return [INTELtrain_Xdf, len(INTELtrain_Xdf) ,FFHQtrain_Xdf, abstract_FFHQtrain_Xdf, len(abstract_FFHQtrain_Xdf), mergedTRAIN_INTEL_FFHQ_df, len(mergedTRAIN_INTEL_FFHQ_df)] , [INTELtest_Xdf, len(INTELtest_Xdf) ,FFHQusedTest_Xdf, abstract_FFHQusedTest_Xdf, len(abstract_FFHQusedTest_Xdf), mergedTEST_INTEL_FFHQ_df, len(mergedTEST_INTEL_FFHQ_df)]