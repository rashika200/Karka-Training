# days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# total_days=30
# day_list=[]
# for i in range(len(days)):
#     a=[]
#     for j in range(i+1,total_days+1,len(days)):
#         a.append(j)
#     week={"day":days[i],"day_list":a}
#     day_list.append(week)
# print(day_list)
        


n=0
candidate=[]
while n<10:
    name=input("enter the name :")
    if (name=="A" or name=="B" or name=="C"):
        candidate.append(f"candidate{name}")
        n=n+1
        print(candidate)
    else:
        print("error")
x=(candidate.count("candidateA"))     
y=(candidate.count("candidateB"))        
z=(candidate.count("candidateC"))   
print("candidateA",x,"\ncandidateB",y,"\ncandidateC",z)  





    
    