#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:42:25 2020

@author: kh
"""
import pandas as pd
import pathlib
import numpy as np
#data_path="/home/kh/github/dataset/hy_round1_train_20200102/"
#data_root=pathlib.PosixPath(data_path)
#all_data_path=list(data_root.glob('*'))
#all_data_paths=[str(path) for path in all_data_path]
#ocean_data=pd.read_csv(all_data_paths[0])
#for i in range(1,len(all_data_paths)-1):
#    ocean_data=ocean_data.append(pd.read_csv(all_data_paths[i]))
#    
#ocean_data.to_csv("/home/kh/github/dataset/hy_round1_train_20200102/all_info.csv",index=False)

ocean_data=pd.read_csv("/home/kh/github/dataset/hy_round1_train_20200102/all_info.csv")
ocean_data=ocean_data.rename(columns={"渔船ID":"shipId","速度":"speed","方向":"direction"})
shipFishing=ocean_data[["shipId","type"]].drop_duplicates()
shipFishing.groupby("type").count()

