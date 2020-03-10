# Cluster-Determination-from-SEM-Image
A slurry was composed such that it contains ion-conducting material, electron-conducting material, 
active material, and a binder.  This slurry was processed subsequently into a useable electrode. 
To gain an understanding of the distribution of component of interest, an SEM image with elemental mapping
was carried out.  
The SEM image of the particles was processed in Fiji (ImageJ) into a binary image (black/white).  
The position of each particle was output in terms of pixel distance, and an analysis for clustering was run 
on this data set.  
The KMeans clustering algorithm in Scikit learn was used to map the clustering.  
Repeat the clustering algorithm on a different number of clusters and track the inertia (sum of the squared 
distances of samples to their closest cluster center.) The number of clusters can be chosen based on the 
biggest reduction in variation observed.  
