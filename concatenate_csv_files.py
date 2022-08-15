###descriptive statistics##create a file with 

##concatenating all the phenotype progeny for each cluster1
import os
import glob
import pandas as pd
os.chdir("/class/datamine/corporate/bayer/Diana_Escamilla/cluster_1")
extension= 'progenyPhenotype.csv'
all_files= [i for i in glob.glob('*.{}'.format(extension))]
file_list=[]
for file in all_files:
  df= pd.read_csv(file)
  df['filename']=file
  file_list.append(df)


combined_progenyPhenotype = pd.concat(file_list,ignore_index=True)
combined_progenyPhenotype.to_csv("/class/datamine/corporate/bayer/Diana_Escamilla/merge_files/combined_progenyPhenotypeCL1.csv", index=False)


### Do the same for cluster 2
import os
import glob
import pandas as pd
os.chdir("/class/datamine/corporate/bayer/Diana_Escamilla/cluster_2")
extension= 'progenyPhenotype.csv'
all_files= [i for i in glob.glob('*.{}'.format(extension))]

file_list=[]
for file in all_files:
  df= pd.read_csv(file)
  df['filename']=file
  file_list.append(df)


combined_progenyPhenotype = pd.concat(file_list,ignore_index=True)
combined_progenyPhenotype.to_csv("/class/datamine/corporate/bayer/Diana_Escamilla/merge_files/combined_progenyPhenotypeCL2.csv", index=False)


##concatenating genotyping files
##concatenating all the genotype progeny for each cluster1
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
os.chdir("/class/datamine/corporate/bayer/Diana_Escamilla/cluster_1")
extension= 'combinedgeno.csv'
all_files= [i for i in glob.glob('*.{}'.format(extension))]


file_list=[]
for file in all_files:
  df= pd.read_csv(file)
  df['filename']=file
  file_list.append(df)
  
comb_prog_genotype = pd.concat(file_list, ignore_index=True)
comb_prog_genotype.to_csv("/class/datamine/corporate/bayer/Diana_Escamilla/merge_files/combined_progenygenotypeCL1.csv")


### Do the same for cluster 2
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
os.chdir("/class/datamine/corporate/bayer/Diana_Escamilla/cluster_2")
extension= 'combinedgeno.csv'
all_files= [i for i in glob.glob('*.{}'.format(extension))]


file_list=[]
for file in all_files:
  df= pd.read_csv(file)
  df['filename']=file
  file_list.append(df)
  
comb_prog_genotype = pd.concat(file_list, ignore_index=True)
comb_prog_genotype.to_csv("/class/datamine/corporate/bayer/Diana_Escamilla/merge_files/combined_progenygenotypeCL2.csv")

