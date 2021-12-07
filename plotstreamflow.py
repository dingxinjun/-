# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:53:46 2021

@author: dingxj
"""

# import os
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import matplotlib.dates as mdate
# mopex_path=r'\\192.168.0.110\d\dingxinjun\mopex\mopex_data\trans_data'
# pic_path=r'\\192.168.0.110\d\dingxinjun\mopex\mopex_data\pic_test'
# file_list=os.listdir(mopex_path)
# for filename in file_list:
#     print(filename)
#     file=os.path.join(mopex_path,filename)
#     df=pd.read_csv(file,index_col=0)
    
#     Q=df['daily streamflow discharge (mm)']
#     Q[Q<0]=np.nan
#     figure, ax = plt.subplots(figsize=(12,8))
#     pic_name=filename[:-8]+'.png'
    
#     ax.plot(df.index,Q)
    
#     ax.set_xlim([df.index[0], df.index[-1]])
#     ax.set_xticks(df.index[::3650],)
#     ax.xaxis.set_major_formatter(mdate.DateFormatter('%d/%m/%Y'))
#     ax.set_ylim(ymin=0)
#     plt.savefig(os.path.join(pic_path,pic_name))
#     plt.close()
#%%
#plot the mopex_camel data set
#这次plot按照camel数据文件夹一样存放数据的图片，所以加了一项，如果没有这样一个文件夹就创建一个文件夹并且存放图片
# import os
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import matplotlib.dates as mdate
# camel_path=r'C:\F\code_notebook\Priestly_taylor\hydrological_input_data\camel_mopex'
# data_save_path=r'\\192.168.0.110\d\dingxinjun\mopex\Q-pic\mopex_camel'
# Folders=['01','02','03','04','05','06','07','08','09','10','11','12','13',
#        '14','15','16','17','18']
# # for num in Folders[:2]:
# for num in Folders:
#     folder_path=os.path.join(camel_path,num)
#     list_of_file=os.listdir(folder_path)
#     for file in list_of_file:
#         file_path= os.path.join(camel_path,num,file)
#         df=pd.read_csv(file_path,index_col=0)
#         df.index=pd.to_datetime(df.index)
#         Q=df['daily streamflow discharge (mm)']
#         Q[Q<0]=np.nan
#         figure, ax = plt.subplots(figsize=(12,8))
#         pic_name=file[:-4]+'.png'
        
#         ax.plot(df.index,Q)
        
#         ax.set_xlim([df.index[0], df.index[-1]])
#         ax.set_xticks(df.index[::3650])
#         ax.xaxis.set_major_formatter(mdate.DateFormatter('%d/%m/%Y'))
#         ax.set_ylim(ymin=0)
#         #如果不存在num path就创建文件夹
#         # data_save_path=r'\\192.168.0.110\d\dingxinjun\mopex\Q-pic\camel'
#         save_folder_path=os.path.join(data_save_path,num)
#         if not os.path.exists(save_folder_path):
#             os.makedirs(save_folder_path)
#         plt.savefig(os.path.join(save_folder_path,pic_name))
#         plt.close()
#%%
#plot the camel data set
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdate
camel_path=r'C:\F\code_notebook\Priestly_taylor\hydrological_input_data\day_met'
data_save_path=r'\\192.168.0.110\d\dingxinjun\mopex\Q-pic\camel'
Folders=['01','02','03','04','05','06','07','08','09','10','11','12','13',
       '14','15','16','17','18']
# for num in Folders[:2]:
for num in Folders:
    folder_path=os.path.join(camel_path,num)
    list_of_file=os.listdir(folder_path)
    for file in list_of_file:
        file_path= os.path.join(camel_path,num,file)
        df=pd.read_csv(file_path,index_col=0)
        df.index=pd.to_datetime(df.index)
        Q=df['OBS_RUN']
        Q[Q<0]=np.nan
        figure, ax = plt.subplots(figsize=(12,8))
        pic_name=file[:-4]+'.png'
        
        ax.plot(df.index,Q)
        
        ax.set_xlim([df.index[0], df.index[-1]])
        ax.set_xticks(df.index[::3650])
        ax.xaxis.set_major_formatter(mdate.DateFormatter('%d/%m/%Y'))
        ax.set_ylim(ymin=0)
        #如果不存在num path就创建文件夹
        # data_save_path=r'\\192.168.0.110\d\dingxinjun\mopex\Q-pic\camel'
        save_folder_path=os.path.join(data_save_path,num)
        if not os.path.exists(save_folder_path):
            os.makedirs(save_folder_path)
        plt.savefig(os.path.join(save_folder_path,pic_name))
        plt.close()
        
