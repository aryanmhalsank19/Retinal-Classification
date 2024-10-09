% This README file accompanies the FloRI21 dataset described in the paper:
% L. Ding, T. Kang, A. Kuriyan, R. Ramchandran, C. Wykoff, and G. Sharma,
% Combining feature correspondence with parametric chamfer alignment: Hybrid two-stage registration for ultra-widefield retinal images,
% IEEE Trans. Biomed. Eng., to appear. [Online]. Available: https://doi.org/10.1109/TBME.2026.31965
%
% If you use this code, please cite the above paper.
%
% The software code is provided "as is" with ABSOLUTELY NO WARRANTY expressed or
% implied. Use at your own risk.
%
% Contact:
% Gaurav Sharma: gaurav.sharma@rochester.edu
%
% Last update: Aug 2022

- Dataset

The FLoRI21 dataset provides ultra-widefield fluorescein angiography (UWF FA) images for the development and evaluation of retinal image registration algorithms. Images are included across five subjects. For each subject, there is one montage FA image that serves as the common reference image for registration and a set of two or more individual ("raw") FA images (taken over multiple clinic visits) that are target images for registration. Overall, these constitute 15 reference-target image pairs for image registration. Relevant details for the images can be found in the associated paper cited below. For each image pair, a set of manually selected corresponding points (control points) are included for quantitative evaluation of registration accuracy. A set of scripts is also included that illustrates the computation of accuracy metrics and visualizes the correspondences between control points in a reference and target image pair.

The naming convention of files are as follow:
	Montage FA images: Montage_Subject_X.tif, where "X" is the subject ID.
	Raw FA images: Raw_FA_N_Subject_X, where "N" is the raw FA image ID for this subject.
	Ground truth control points: ControlPoints_Montage_FA_N_Subject_X.txt

The ground truth file for each pair of images has the following format:
	Montage_point_1_x, Montage_point_1_y, FA_point_1_x, FA_point_1_y
	Montage_point_2_x, Montage_point_2_y, FA_point_2_x, FA_point_2_y
	...
	Montage_point_M_x, Montage_point_M_y, FA_point_M_x, FA_point_M_y

- Scripts
Two demonstration scripts are included in this dataset. 

The first one, "eval_registration_accuracy.m", calculates the registration success rate as a function of the mean registration error (MRE) threshold and the corresponding AUC number.

The second one, "vis_control_points_FLoRI21.m",	visualizes the correspondences between the control points in one raw FA image and the corresponding montage