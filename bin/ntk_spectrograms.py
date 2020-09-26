#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:20:56 2020

@author: timb
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%

datatype = 'betaSquare'
datatype = 'thetaH'
net_sta_loc = 'NM.SLM.--'
chans = 'BHZ_BHE_BHN'
filename = net_sta_loc + '.' + chans + '.2008-12-31T00_00_00.2009-01-10T00_00_00.frequency.txt'

current_path = Path.cwd()
data_path = current_path / '..' / Path('data/POLAR') / Path(net_sta_loc) / Path(chans) / Path(datatype)

colnames = ['date', 'time', 'freq', datatype]
data = pd.read_csv(data_path / filename, sep='\t', names=colnames, parse_dates=[[0,1]])
print(data)

#%%

date_time_all = pd.to_datetime(data['date_time'], format='%Y-%m-%d %H_%M_%S').to_numpy()
freq_all = data['freq'].to_numpy()
freq_all_log = np.log10(freq_all)
data_val_column = data[datatype].to_numpy()

date_times =np.unique(date_time_all)
freqs_log =np.unique(freq_all_log)

delta_freqs_log = np.mean(np.diff(freqs_log))
delta_date_times = np.mean(np.diff(date_times))

# inspired/lifted from http://chris35wills.github.io/gridding_data/
i = ((freq_all_log - freqs_log[0]) / delta_freqs_log).astype(int) # y locations as grid indices
j = ((date_time_all - date_times[0]) / delta_date_times).astype(int) # x locations as grid indices
data_val_mesh = np.nan * np.empty(( len(freqs_log), len(date_times) ))
data_val_mesh[i,j] = data_val_column

# # inspired/lifted from http://chris35wills.github.io/gridding_data/
# # Bin the data onto a 10x10 grid
# # Have to reverse x & y due to row-first indexing
# data_val_mesh, yi, xi = np.histogram2d(freq_all_log, date_time_all, bins=(len(freqs_log), len(date_times)), 
#                             weights=data_val_column, normed=False)

fig, ax = plt.subplots()
img = ax.pcolormesh(date_times, 10**freqs_log, data_val_mesh)
ax.set_yscale('log')
fig.colorbar(img)
fig.autofmt_xdate()
ax.set_title(datatype + '   ' + net_sta_loc)