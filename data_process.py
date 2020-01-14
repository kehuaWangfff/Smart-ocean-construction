#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:42:25 2020

@author: kh
"""
import pandas as pd
import pathlib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data_path="/home/kh/github/dataset/hy_round1_train_20200102/"

def apend_allcsv(datapath):
    data_root=pathlib.PosixPath(data_path)
    all_data_path=list(data_root.glob('*'))
    all_data_paths=[str(path) for path in all_data_path]
    ocean_data=pd.read_csv(all_data_paths[0])
    for i in range(1,len(all_data_paths)):
        ocean_data=ocean_data.append(pd.read_csv(all_data_paths[i]))
    ocean_data=ocean_data.rename(columns={"渔船ID":"shipId","速度":"speed","方向":"direction"})
    return ocean_data
        
ocean_data=pd.read_csv("/home/kh/github/dataset/hy_round1_train_20200102/all_info.csv")
ocean_data=ocean_data.rename(columns={"渔船ID":"shipId","速度":"speed","方向":"direction"})
ocean_data["x_sd"]=(ocean_data["x"]-np.min(ocean_data["x"]))/(np.max(ocean_data["x"])-np.min(ocean_data["x"]))
ocean_data["y_sd"]=(ocean_data["y"]-np.min(ocean_data["y"]))/(np.max(ocean_data["y"])-np.min(ocean_data["y"]))
ocean_data.type=pd.Categorical(ocean_data.type)
ocean_data["type_index"]= ocean_data.type.cat.codes


shipFishing=ocean_data[["shipId","type"]].drop_duplicates()
shipFishing.groupby("type").count()


ocean_data[["type"]].drop_duplicates()

test=apend_allcsv(data_path)
test["x_sd"]=(test["x"]-np.min(test["x"]))/(np.max(test["x"])-np.min(test["x"]))
test["y_sd"]=(test["y"]-np.min(test["y"]))/(np.max(test["y"])-np.min(test["y"]))

