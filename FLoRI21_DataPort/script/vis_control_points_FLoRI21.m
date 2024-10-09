% This is a demo script that visualizes the correspondences between
% control points in a raw FA image and the corresponding montage
%
% It accompanies the paper:
% L. Ding, T. Kang, A. Kuriyan, R. Ramchandran, C. Wykoff, and G. Sharma,
% “Combining feature correspondence with parametric chamfer alignment: Hybrid two-stage registration for ultra-widefield retinal images,”
% IEEE Trans. Biomed. Eng., to appear. [Online]. Available: https://doi.org/10.1109/TBME.2026.31965
%
% If you use this code, please cite the above paper.
%
% Contact:
% Gaurav Sharma: gaurav.sharma@rochester.edu
%
% Last update: Aug 2022


clc;clear;close all;


montage_image_file = '../data/Subject_5/Montage/Montage_Subject_5.tif';
fa_image_file = '../data/Subject_5/FA/Raw_FA_3_Subject_5.tif';
control_points_file = '../data/Subject_5/ControlPoints/ControlPoints_Montage_FA_3_Subject_5.txt';

montage_image = imread(montage_image_file);
fa_image = imread(fa_image_file);
control_points = readmatrix(control_points_file);

control_points_montage = control_points(:,1:2);
control_points_fa = control_points(:,3:4);

figure;
showMatchedFeatures(montage_image, fa_image, control_points_montage,control_points_fa, 'montage')