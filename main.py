
import os, glob


# def getFromPI():

print("pi csv")

print("***3")
# csv2_name = "/home/gautambh/var/tmp/sumana"
csv2_name = "/var/tmp/sumana"
# for file in os.listdir(csv2_name):

for file in glob.glob(os.path.join(csv2_name, '*.txt')):
    print("file object = ", file)
    with open(os.path.join(os.getcwd(), file), 'r') as f:
        print("file name = ", file)
        print("End Reading")
print("Finished processing all files")

