import os
import mapper
import reducer
import shutil

output = [[] for _ in range(9) ] 
def wirteFile(targetNum):
	if (not output[targetNum]):
		return 
	targetfile = os.path.join("./in", "{}-{}".format("temp", str(targetNum)))
	with open(targetfile, "at") as wFile:
		for wline in output[targetNum]:
			wFile.write(wline)
		output[targetNum] = []


def toWrite():
	for index in range(9):
		wirteFile(index)

def master():
	if not os.path.exists("./in"):
		os.mkdir("./in")
	else:
		shutil.rmtree("./in")
		os.mkdir("./in")
	count = 0
	with open("./access_log", "rt") as rFile:
		for rline in rFile:
			output[count % 9].append(rline)
			count += 1

	toWrite()


if __name__ == '__main__':
	master()
	mapper.start()
	reducer.start()






		
