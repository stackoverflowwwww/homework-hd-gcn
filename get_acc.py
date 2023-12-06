import os
import pickle
import numpy as np
def get_acc(dataset,main_dir):
    if 'UCLA' in dataset:
        label = []
        with open('./data/' + 'NW-UCLA/' + '/val_label.pkl', 'rb') as f:
            data_info = pickle.load(f)
            for index in range(len(data_info)):
                info = data_info[index]
                label.append(int(info['label']) - 1)
    elif 'ntu120' in dataset:
        if 'xsub' in dataset:
            npz_data = np.load('./data/' + 'ntu120/' + 'NTU120_CSub.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'xset' in dataset:
            npz_data = np.load('./data/' + 'ntu120/' + 'NTU120_CSet.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
    elif 'ntu' in dataset:
        if 'xsub' in dataset:
            npz_data = np.load('./data/' + 'ntu/' + 'NTU60_CS.npz')
            label = np.where(npz_data['y_test'] > 0)[1]
        elif 'xview' in dataset:
            npz_data = np.load('./data/' + 'ntu/' + 'NTU60_CV.npz')
            label = np.where(npz_data['y_test'] > 0)[1]

    with open(os.path.join(main_dir, 'epoch1_test_score.pkl'), 'rb') as r1:
        r1 = list(pickle.load(r1).items())
    logits=np.zeros((len(r1),len(r1[0][1])))
    for i in range(len(r1)):
        logits[i]=r1[i][1]

    predict_l=np.argmax(logits,axis=1)
    print(np.sum(label==predict_l)/len(predict_l))
    print()


# dataset='ntu/xsub'
# temp='joint_CoM_1'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/joint_CoM_1_backup/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)


dataset='ntu/xsub'
temp='no-aha'
main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/ablation/joint_CoM_1_{temp}'
print(temp)
get_acc(dataset,main_dir)

dataset='ntu/xsub'
temp='rsap_no-h-edge'
main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/ablation/joint_CoM_1_{temp}'
print(temp)
get_acc(dataset,main_dir)

dataset='ntu/xsub'
temp='sap_h-edge'
main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/ablation/joint_CoM_1_{temp}'
print(temp)
get_acc(dataset,main_dir)

dataset='ntu/xsub'
temp='sap_no-h-edge'
main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/ablation/joint_CoM_1_{temp}'
print(temp)
get_acc(dataset,main_dir)

# dataset='ntu120/xsub'
# temp='joint_CoM_1'
# main_dir=f'./work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)


# dataset='ntu120/xsub'
# temp='joint_CoM_1'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)

# dataset='ntu120/xsub'
# temp='bone_CoM_1'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)

# dataset='ntu120/xsub'
# temp='joint_CoM_2'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)

# dataset='ntu120/xsub'
# temp='bone_CoM_2'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)

# dataset='ntu120/xsub'
# temp='joint_CoM_21'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)

# dataset='ntu120/xsub'
# temp='bone_CoM_21'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu120_hdgcn/cross-subject/{temp}/'
# print("ntu120",temp)
# get_acc(dataset,main_dir)


# dataset='ntu/xsub'
# temp='joint_CoM_1'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/{temp}/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)

# dataset='ntu/xsub'
# temp='bone_CoM_1'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/{temp}/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)

# dataset='ntu/xsub'
# temp='joint_CoM_2'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/{temp}/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)

# dataset='ntu/xsub'
# temp='bone_CoM_2'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/{temp}/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)

# dataset='ntu/xsub'
# temp='joint_CoM_21'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/{temp}/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)

# dataset='ntu/xsub'
# temp='bone_CoM_21'
# main_dir=f'/media/wmb/Data/wmb/hd-gcn/work_dir/ntu_hdgcn/cross-subject/{temp}/'
# print("ntu60",temp)
# get_acc(dataset,main_dir)