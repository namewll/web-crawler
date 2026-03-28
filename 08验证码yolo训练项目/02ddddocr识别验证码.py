from ddddocr import DdddOcr
docr=DdddOcr()
with open("img.png","rb")as f:
    content=f.read()
res=docr.classification(content)
print(res)
