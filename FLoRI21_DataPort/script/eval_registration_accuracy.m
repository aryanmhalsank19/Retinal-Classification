% This is a demo script that calculates the registration success rate as a
% function of the mean registration error (MRE) threshold and the
% corresponding AUC number.
% 
% It accompanies the paper:
% L. Ding, T. Kang, A. Kuriyan, R. Ramchandran, C. Wykoff, and G. Sharma,
% "Combining feature correspondence with parametric chamfer alignment: Hybrid two-stage registration for ultra-widefield retinal images,”
% IEEE Trans. Biomed. Eng., to appear. [Online]. Available: https://doi.org/10.1109/TBME.2026.31965
%
% If you use this code, please cite the above paper.
%
% Contact:
% Gaurav Sharma: gaurav.sharma@rochester.edu
%
% Last update: Aug 2022

clc;clear;close all;
load('sample_transformed_points.mat');

dataset_root = '../data';
n_pair = 15;

count = 1;
all_MRE = zeros(n_pair,1);

for subject_idx = 1:5
    subject_name = ['Subject_', num2str(subject_idx)];
    control_point_files = dir(fullfile(dataset_root,subject_name,'ControlPoints','*txt'));
    n_file = length(control_point_files);
    
    for fa_idx = 1:n_file
        file = control_point_files(fa_idx);
        control_points = readmatrix(fullfile(file.folder, file.name));
        fa_points = control_points(:,3:4);
        
        key = ['FA_',num2str(fa_idx),'_Subject_',num2str(subject_idx)];
        transformed_points = sample_transformed_points(key);
        
        diff = fa_points - transformed_points;
        dist = mean(vecnorm(diff,2,2));
        
        all_MRE(count) = dist;
        count = count+1;
    end    
end

%%
all_th = 0:1:90; n_th = length(all_th);
all_ratio = zeros(n_th,1);
for index = 1:n_th
    th = all_th(index);
    success = sum(all_MRE<th)/n_pair;
    all_ratio(index) = success;
end
cur_auc = trapz(all_th,all_ratio)/max(all_th);
fprintf('Area under the curve: %f\n', cur_auc);

figure;plot(all_th,all_ratio);%title('FIRE');
xlabel('Error Threshold $\tau_e$','interpreter','latex'); ylabel('Success Rate','interpreter','latex');
ax = gca;
ax.FontSize = 16;