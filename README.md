# Cluster-Determination-from-SEM-Image
How do we understand the distribution of a material in an electrode? 

Battery electrode performance is closely related to the distribution of its materials. 
In this exercise, a slurry was composed such that it contained ion-conducting material, electron-conducting material, 
active material, and a binder.  This slurry was processed subsequently into an electrode. 

To gain an understanding of the distribution of a component of interest, an SEM image with elemental mapping
was acquired. The SEM image of the particles was processed in Fiji (ImageJ) into a binary image (black/white) using autothresholding.  The position of each particle was output in terms of pixel distance, and an analysis for clustering was run on this data set.  

The KMeans clustering algorithm in Scikit learn was used to map the clustering.  
The clustering algorithm was repeated on a different number of clusters, and its  inertia (sum of the squared 
distances of samples to their closest cluster center) was tracked. The number of clusters can be chosen based on the 
biggest reduction in variation observed.  
