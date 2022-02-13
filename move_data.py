import pandas as pd
import os
from shutil import move
"""
this py file is used to create folder and move the out of date range data
"""
#enter the path and create the new folder
os.chdir(r'C:\F\data_for_lumped_model\removed_daily_camel_data')
Folders = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
               '14', '15', '16', '17', '18']
# for dirName in Folders:
#     if not os.path.exists(dirName):
#         os.mkdir(dirName)
#         print("Directory " , dirName ,  " Created ")
#
#     else:
#         print("Directory " , dirName ,  " already exists")
#
def is_date_in_list(start_date, end_date, date_list):
    """
    identify whether the date is in the list
    if date is out of range, print the prompt
    :param start_date: date, YYYY-MM
    :param end_date: date, YYYY-MM
    :param date_list: date series used for detection  # list
    :return: bool
    """
    date_list = pd.date_range(start=date_list[0], end=date_list[-1])
    if (start_date not in date_list) or (end_date not in date_list):
#         if language == 'English':
#             print('Date out of range!')
#         elif language == '中文':
        print('日期超出了范围！')
        return False
    else:
        return True
        print('数据日期正常')
Camel_path=r'C:\F\data_for_lumped_model\daily_camel_data'
distrot=r'C:\F\data_for_lumped_model\removed_daily_camel_data'

count1=0
count2=0
count3=0
for folder in Folders:
    # 进入文件夹
    folder_path = os.path.join(Camel_path, folder)
    print(folder_path)
    list_of_file = os.listdir(folder_path)
    list_of_file_name = [i[:-4] for i in list_of_file]
    for file in list_of_file:

        file_path = os.path.join(folder_path, file)
        # 读取数据并且将其index的时间弄出来
        data = pd.read_csv(file_path, index_col=0)
        data.index = pd.to_datetime(data.index)
        condition = is_date_in_list('1982-10-01', '2014-12-01', data.index)

        if condition:
            print('{}数据正常'.format(file))
            count1 = count1 + 1
        else:
            print('{}数据ERROR'.format(file))
            count2 = count2 + 1
            srcroot = file_path

            distroot = os.path.join(distrot, folder)
            move(srcroot, distroot)
            count3 = count3 + 1

print('正常数据：', count1, '不正常数据', count2, '第二次移除数据', count3)
