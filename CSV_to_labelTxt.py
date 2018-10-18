import csv
from PIL import Image

csv_flie = csv.reader(open('./data/anno_train.csv'))
imagePath = './data/cars_train/'

for i in csv_flie:
    im = Image.open(imagePath+i[0])
    W = im.size[0]
    H = im.size[1]
    x = ((int(i[1]) + int(i[3])) / 2.0) / W
    y = ((int(i[2]) + int(i[4])) / 2.0) / H
    w = (int(i[3]) - int(i[1])) / W
    h = (int(i[4]) - int(i[2])) / H
    txtName = './labelTxt/' + i[0].split('.')[0] + '.txt'
    f = open(txtName, "w")
    labelText = str(int(i[5])-1) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
    f.write(labelText)
    f.close()
