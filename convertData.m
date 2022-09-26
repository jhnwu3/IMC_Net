%FileData = load('CyTOFData.mat');
% csvwrite('CyTOFData.csv', FileData)
%save('FileData','-v6')

names = whos('-file','CyTOFData.mat');
tiff = load('CyTOFData.mat',names(5).name);
root_folder_name = 'png';
for i = 1:height(tiff.Tiff_all)
    mkdir([root_folder_name, sprintf('%d',i)])
    for j = 1:width(tiff.Tiff_all)
        tiff_mat = cell2mat(tiff.Tiff_all(i,j));
        imwrite(tiff_mat, fullfile(strcat(root_folder_name,sprintf('%d',i)),strcat(sprintf('%d',j),'.png')))
    end

end