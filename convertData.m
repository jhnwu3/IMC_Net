FileData = load('CyTOFData.mat');
csvwrite('CyTOFData.csv', FileData.M)
save('FileData','-v6')