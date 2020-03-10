'''Adriana A. Rojas
4/2/19
This script reads a .csv output from the results to a shape descriptor analysis from FIJI
Convert the x and y positions into an array of positions
Determine the best number of 
'''
import pandas as pd
import pprint
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib import rcParams
rcParams['font.family']='sans-serif'
rcParams['font.sans-serif']=['Arial']
size=10
##
def opencsv(filename,headerlines):
    '''input: filename is a string indicating the name of the file in the working directory
                    headerlines is of type string to indicate the row with the header columns
    output:  the X and Y positions of the particles as pd.Series'''
##    conv=4.58   # conversion factor from 1 um to "conv" pixels
    file=pd.read_csv(filename,header=headerlines)
    X=pd.to_numeric(file['BX'],downcast='float',errors='coerce') # units in pixels
    Y=pd.to_numeric(file['BY'],downcast='float',errors='coerce') # units in pixels
    return X,Y
##
def graph(x,y,sym='o'):
    '''input: x and y are pd.Series
                    sym is of type string, it is the symbol of the markers
    output: plot the graph'''
    plt.plot(x,y,sym,color='dodgerblue',markersize=6,linewidth=1,mew=0.5, mec='k')
    return
def formatGraph():
    ''' formatting conditions for the graph'''
    plt.xlabel('x',fontsize=size)
    plt.ylabel('y', fontsize=size)
    plt.tick_params(labelsize=size)
    plt.tick_params(which='major',right='on',direction='in',top='on',length=6)
    plt.tick_params(which='minor',right='on',direction='in',top='on',length=3)
    plt.tight_layout()   
    return
##
file='Results.csv'
date='200310'
colors=['royalblue','mediumseagreen','m','lightslategrey','goldenrod']

x,y=opencsv(file,0)
#
#graph the positions of the particles
fig=plt.figure(figsize=(4.5,3),dpi=300)
graph(x,y)
formatGraph()
plt.axis([0,1022,654,0])
plt.savefig(date+'_BxBy_position')
plt.close()
#
xy=[]
#Convert the x and y pd.Series into a single array of positions
for i in range(len(x)):
    xy.append([x.iloc[i],y.iloc[i]])
xy=np.array(xy)
#
variation=[]
##random_state=0, for a deterministic output
# run the KMeans algorithm on a different number of clusters, cluster_num
for cluster_num in range(1,10):
    kmeans = KMeans(n_clusters=cluster_num, random_state=None).fit(xy)
    #
    fig=plt.figure(figsize=(4.5,3),dpi=300)
    plt.scatter(xy[:, 0], xy[:, 1], c=kmeans.labels_)
    plt.axis([0,1022,654,0])
    formatGraph()
    plt.savefig(date+'_BxBy_clustered'+str(cluster_num))
    plt.close()
    #
    variation.append(kmeans.inertia_)
#
# graph the Inertia versus the number of clusters proposed
fig=plt.figure(figsize=(3,3),dpi=300)
graph(range(1,10),variation,sym='o-')
formatGraph()
plt.xlabel('Cluster Number')
plt.ylabel('Inertia')
plt.savefig('Inertia_v_Num_Clusters')
#
# calculate the change in Inertia, and graph it against the number of clusters
delta_var=[]
for i in range(len(variation)-1):
    delta_var.append(variation[i+1]-variation[i])
fig=plt.figure(figsize=(3,3),dpi=300)
graph(range(2,10),delta_var,sym='o-')
formatGraph()
plt.xlabel('Cluster Number')
plt.ylabel('$\Delta$Inertia')
plt.savefig('delInertia_v_Num_Clusters')
    
