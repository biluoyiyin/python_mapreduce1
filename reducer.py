import os
import threading
from collections import OrderedDict

di = OrderedDict()
def reducer(targetFile):
	with open(targetFile, "rt") as rFile:
		for rline in rFile:
			key, value = rline.split(",")
			if key in di.keys():
				di[key] += int(value)
			else:
				di[key] = int(value)

def start():
	fileName = [ name for name in os.listdir("./out") if name.startswith("re")]
	for file in fileName:
		targetFile = os.path.join("./out", file)
		mapthd = threading.Thread(target = reducer, args = (targetFile,))
		mapthd.start()
	mapthd.join()
	count, total = 0, 0
	with open("./res", "wt") as wFile:
		for key, value in di.items():
			wFile.write("{}, {}{}".format(key, value, "\n"))
			total += value
			count += 1
		wFile.write("{} {} {} {} {}".format("Taken together, it has", count, "different IP, has", total, "connections.\n"))
	print("reducer done")
	print("Taken together, it has", count, "different IP, has", total, "connections.")
	
if __name__ == '__main__':
	start()
