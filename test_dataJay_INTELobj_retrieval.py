
import numpy as np

DIR_train= './IntelClassImg_GoodOne/NonFace_seg_train/seg_train' #labelsDirectories
#DIR_train= './seg_train/seg_train'

DIR_test= './IntelClassImg_GoodOne/NonFace_seg_test/seg_test' #labelsDirectories
#DIR_test= './seg_test/seg_test'

INTELcategCard=call_INTELcategCard_JayForm()


def call_INTELcategCard_JayForm(): #@title jayForm
  #@markdown Please INPUT the amount of images for each INTELCategory:
  INTELcategCard=10 #@param{type:'integer'}
  #print(imgNum)
  return INTELcategCard

def test_dataJay_INTELobj_retrieval():
  test_dataJay=[]
  test_labels_list=[]
  INTELobj_test={}
 

  subCount=0
  for Sub in os.listdir(DIR_test):
    itemCount=0
    test_Sub_labels_list=[]
    #print(Sub)
    SubPath=os.path.join(DIR_test,Sub)
    print(f'Test_label <{Sub}> path is:  {SubPath}')
    Sub_DIR_test=os.listdir(SubPath)
    for item in Sub_DIR_test:
      if itemCount> INTELcategCard:         # max<700> per category...reduced amount to avoid CRASH!!!
        break

      #print(item)
      #print(item_SubPath)
      elif item.endswith('.jpg'):
        #print(item)
        item_fullPath_test=os.path.join(SubPath,item)# or os.path.join(DIR_train,Sub,item)
        #print(item_fullPath_train)
        imageMatrix=cv2.imread(item_fullPath_test)

        imageMatrix_rsz=cv2.resize(imageMatrix, (224,224))
        imageMatrix_rsz_arr=img_to_array(imageMatrix_rsz)
        test_dataJay.append(imageMatrix_rsz_arr) #here... 2be Def RETURN (1)

      # extract the class label from the image path and update the labels list
      label=str(Sub+'_'+item)
      test_Sub_labels_list.append(label)

      test_labels_list.append(label)

      itemCount+=1


    INTELobj_test[Sub]=test_Sub_labels_list #here... 2be Def RETURN (2)

    #print(INTELobj_train[Sub])

    #print(INTELobj_train)

    subCount+=1
    #if subcount>1: # reduced count required to avoid ... CRASH!!!!...if needed
    #break

  np_test_labels_list=np.array(test_labels_list) #here... 2be in Def RETURN
  #np.array(train_dataJay) ... cause CRASH!!!
  #print(labels_list)
  #print(INTELobj_train)

  return test_dataJay, np_test_labels_list, INTELobj_test

