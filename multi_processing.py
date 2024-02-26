"""
Multi-processing- It is a python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage
of multiple cores or processors on your system and can significantly improves the performance of your code.
_  -> under throw variable
"""
import multiprocessing
import requests

def downloadFile(url,name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"file/file{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
process = []
for i in range(5):
    p = multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    process.append(p)

for p in process:
    p.join()
