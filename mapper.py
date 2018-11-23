import os
import threading
import shutil

# Map function


import os

def combine(maplist):
	# use dictonary is better here, but sort before, we can count
	res = []
	cur, count = maplist[0], 1
	for index, value in enumerate(maplist, 1):
		if value == cur:
			count += 1
			continue
		else:
			res.append("{}, {}".format(value, count))
			cur, count = value, 1
	return res

def partition(mylist):
	# 0 ~ 255, can be divided into different reducers. However, it is not a good algorithm.
	baseDir = "./out"
	temp = [[] for _ in range(17)]
	for i in mylist:
		temp[int(i.split(",")[0].split(".")[0]) // 16].append(i)
	for index, value in enumerate(temp):
		if (value):
			target = os.path.join(baseDir, "{}-{}".format("re", index))
			with open (target, "at") as wFile:
				for j in value:
					wFile.write("{}{}".format(j, "\n"))

def mapper(targetFile):
	res = []
	with open(targetFile, "rt") as rFile:
		for rLine in rFile:
			url = rLine.split(" ")[0]
			res.append(url)
	res.sort()
	di = combine(res)
	res = []
	partition(di)


def start():
	if not os.path.exists("./out"):
		os.mkdir("./out")
	else:
		shutil.rmtree("./out")
		os.mkdir("./out")
	fileName = [ name for name in os.listdir("./in") if name.startswith("temp")]
	for file in fileName:
		targetFile = os.path.join("./in", file)
		mapthd = threading.Thread(target = mapper, args = (targetFile,))
		mapthd.start()
	mapthd.join()
	print("mapper done")
	
if __name__ == '__main__':
	start()


