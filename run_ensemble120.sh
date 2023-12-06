echo "\nNTU-RGB+D 120 Cross-Subject: all\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \

echo "\nNTU-RGB+D 120 Cross-Subject: CoM-1\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \
	--CoM-1 True \
	--CoM-2 False \
	--CoM-21 False \

echo "\nNTU-RGB+D 120 Cross-Subject: CoM-2\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \
	--CoM-1 False \
	--CoM-2 True \
	--CoM-21 False \

echo "\nNTU-RGB+D 120 Cross-Subject: CoM-21\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \
	--CoM-1 False \
	--CoM-2 False \
	--CoM-21 True \

echo "\nNTU-RGB+D 120 Cross-Subject: CoM-1 and CoM-2\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \
	--CoM-1 True \
	--CoM-2 True \
	--CoM-21 False \

echo "\nNTU-RGB+D 120 Cross-Subject: CoM-1 and CoM-21\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \
	--CoM-1 True \
	--CoM-2 False \
	--CoM-21 True \

echo "\nNTU-RGB+D 120 Cross-Subject: CoM-2 and CoM-21\n"
python ensemble.py \
	--dataset ntu120/xsub \
	--main-dir /media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject \
	--CoM-1 False \
	--CoM-2 True \
	--CoM-21 True \