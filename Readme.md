# UPGMA Python Implementation

This is an implementation of upgma (Unweighted Pair Group Method With Arithmetic Mean) hierarchical clustering method in python.  
The script generates a graphical view of the phylogenetic trees as well as print the tree in Newick format.  

# Requirement
To visualize the phylogenetic tree you should install the ete3 toolkit.  
use : pip install ete3  


# Examples
**Example 1**  
Newick format : ((((Homme : 0.04600 , Chimpanze : 0.04600 ) : 0.05425 , Gorille : 0.05425 ) : 0.09325 , Orang-outan : 0.09325 ) : 0.10856 , Gibbon : 0.10856 )   
![Exaple 1](https://github.com/iliass-el/upgma/blob/master/Example1.PNG)

**Example 2**  
Newick Format :((((A : 1.00000 , C : 1.00000 ) : 2.00000 , D : 2.00000 ) : 4.50000 , (B : 1.00000 , E : 1.00000 ) : 4.50000 ) : 5.00000 , F : 5.00000 )  
![Exaple 2](https://github.com/iliass-el/upgma/blob/master/Example2.PNG)

# Tree clustering
You can use njplot software to visualize the phylogenetic tree or the online tree viewer of the ETE3 Toolkit using the generated Newick format string.  
[http://etetoolkit.org/treeview/](http://etetoolkit.org/treeview/)