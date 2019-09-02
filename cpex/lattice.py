# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:48:44 2019

@author: cs17809
"""
import os
import numpy as np
import matplotlib.pyplot as plt

class Load():
    
    def __init__(self, fpath):
        data = np.load(fpath)
        self.e = data['e']
        self.s = data['s']
        self.lat = data['lat']
        self.dims = data['dims']
        self.rot = data['rot']
        self.v = data['v']
        self.N = data['N']
        self.num_frames = data['num_frames']
        self.num_grains = data['num_grains']
        
        self.rot[:, :,0] = self.rot[:, :,1]
        
        
    
    def plot(self, y='stress', x='frame', idx=1):
        
        #Need tp average over volume.
        
        dy = {'strain':self.e,
             'stress':self.s,
             'lattice':self.lat,
             'rot':self.rot - self.rot[:,:, 0][:, :, None]}
        
        dx = {'time':np.arange(self.num_frames),
             'stress':np.nanmean(self.s[idx], axis=0),
             'strain':np.nanmean(self.e[idx], axis=0),
             'frame':np.arange(self.num_frames),
             'lattice':np.nanmean(self.lat[idx], axis=0)}
        
        
        plt.plot(dx[x], dy[y][idx].T, color='k', alpha=0.2)
        plt.plot(dx[x],np.nanmean(dy[y][idx], axis=0), color='r')
        plt.ylabel(y)
        plt.xlabel(x)


    def extract_lattice(self):
        pass
    
    def calc_lattice_tensor(self):
        pass
    
    
    
if __name__ == '__main__':
    folder = os.path.join(os.path.dirname(__file__), r'data') # should be sub [0]
    fpath = os.path.join(folder, r'test_cpex.npz')
    data = Load(fpath)
    data.plot(x='strain', y='stress')
    # data.plot(x='lattice', y='stress')
