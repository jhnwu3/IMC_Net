check = exist('data','var');
if check ~= 1
    data = load("tiff_images.mat", "Tiff_all");
    data = data.Tiff_all;
end
check = exist('fnames','var');
if check ~= 1
    fnames = load("tiff_images.mat", "gates");
    fnames = fnames.gates;
end

% 19, 20, 24-30
ind = [1:18, 21:23, 31:42];
[num_patients, num_expressions] = size(data);
for i=1:num_patients
    im = data(i, :);
    im = im(:, ind);
    fname = string(fnames(i, 1));
    num_expressions = length(im);
    file_name = "/Users/soham/SpatialCell/Data/tiff_files/" + fname + "_full.tiff";
    im_data = double(cell2mat(im(1, 1)));
    imwrite(im_data, file_name);
    for j=2:num_expressions
        im_data = double(cell2mat(im(1, j)));
        imwrite(im_data, file_name, 'WriteMode','append');
    end
end






