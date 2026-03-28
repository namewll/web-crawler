from ultralytics import YOLO
model=YOLO("best.pt")
result=model("img2.png",conf=0.5)
print("---------------------")
print(result)
print("----------------------")
print(result[0])
print("----------------------")
x1,y1,x2,y2=result[0].boxes.xyxy.cpu().numpy()[0]
print(x1,y1,x2,y2)
print("-----------------------")
# m=(x1+x2)/2
# n=(y1+y2)/2
# width=x2-x1
# print(m-width/2)
print(x1)

