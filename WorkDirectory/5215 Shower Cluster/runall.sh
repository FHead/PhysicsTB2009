cd ~/CMSSW_2_2_13/src
eval `scramv1 runtime -sh`
cd - > /dev/null 2> /dev/null
export CMSSW_SEARCH_PATH=$CMSSW_SEARCH_PATH:~/CMSSW_2_2_13/work/EssentialFiles

for i in $*
do
   cat Clustering_template.py | sed "s/__RUNNUMBER__/$i/g" > Clustering_$i.py
   cmsRun Clustering_$i.py
done

