import glob

newLabelName = "card"

labelList = []
txtList = []
changeFolder = ['train/labels/*.txt', 'test/labels/*.txt', 'valid/labels/*.txt']

for path in changeFolder:
    for filename in glob.glob(path):
        with open(filename) as f:
            lines = f.readlines()
            txtList = []
            for line in lines:
                labelList = line.split(' ')
                labelList[0] = '0'
                text = ""
                for i in range(len(labelList)):
                    text += labelList[i]
                    if i != len(labelList)-1:
                        text += " "
                txtList.append(text)

        with open(filename, 'w') as f:
            for i in txtList:
                f.write(i)

with open('data.yaml') as f:
    lines = f.readlines()
    txtList = []
    for line in lines:
        try:
            if line.split(':')[0] == "nc":
                txtList.append("nc: 1\n")
            elif line.split(':')[0] == "names":
                txtList.append("names: ['{}']\n".format(newLabelName))
            else:
                txtList.append(line)
        except:
            pass

with open('data.yaml', 'w') as f:
    for i in txtList:
        f.write(i)
