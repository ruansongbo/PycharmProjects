import arcgisscripting, os, sys, math, string
gp = arcgisscripting.create()
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


p = range(200)
o = range(200)
PI = 3.1415926535897931
x1=range(200)
x2=range(200)
yy1=range(100)
y2=range(200)
b1=range(200)
l1=range(200)
b2=range(200)
l2=range(200)
k=range(10)
rg=range(200)
aa3 = 0
bb2 = 0.0
aa1 = 1
#输入坐标文本文件
inputFile = sys.argv[1]
#输出坐标文本文件
outputFile = sys.argv[2]
#inputt the number of the points 
n = int(sys.argv[4])
#inputt the coordiate 54 or 80
d = int(sys.argv[3])
#ensure the zhengsuan,fansuan or huandan
k0 = int(sys.argv[5])
#when fansuan ensure the l0(起始中央子午线经度)
try:
    if len(sys.argv) > 9:
        l0 = int(sys.argv[8])
    else:
        l0=0
except Exception, ErrorDesc:
    gp.AddError(str(ErrorDesc))
    

# 输入结束中央子午线经度
ll1 = int(sys.argv[6])
# 选择3度带或者6度带
d1 = int(sys.argv[7])
    
def zs1():
    print
def fs1():
    print
def hd():
    print


def k54():
    k[0]=6399698.90178271
    k[1]=6367558.49687
    k[2]=32005.7801
    k[3]=133.9213
    k[4]=0.7032
    k[5]=0.005051773902
    k[6]=0.000029838676
    k[7]=6.738525414683492e-3
    k[8]=0.000000241496

def k80():
    k[0]=6399596.65198801
    k[1]=6367452.13279
    k[2]=32009.8575
    k[3]=133.9602
    k[4]=0.6976
    k[5]=0.005052505593
    k[6]=0.000029847335
    k[7]=6.739501819472925e-3
    k[8]=0.0000002416

def jdzh1(jd):
    i=float(jd)
    i = int(i)
    
    j=float(jd)*100-int(i)*100
    j = int(j)
    ##gp.AddError(i)
    ##gp.AddError(j)
    k1=float(jd)*10000-float(i)*10000-float(j)*100
    ##gp.AddError(k1)
    
    if k1>=60:
        j=j+1
        k1=0
    jdd=float(i)*PI/180+float(j)*PI/180/60+float(k1)*PI/180/3600
    ##gp.AddError(jdd)
    return jdd

def jdzh2(jd):
    
    
    i=float(jd)*180/PI
    i = int(i)
    
    j=(float(jd)*180/PI-int(i))*60
    j=int(j)
    
    k=((float(jd)*180/PI-int(i))*60-int(j))*60
    k = float(k)
    
    jdd=float(i)+float(j)/100+float(k)/10000
   
    return jdd
i = 0
if k0==1:
   f=open(inputFile)
   for a in f.readlines():
       fu = a.split(',')
       b1[i]=fu[0]
       
       l1[i]=fu[1]
       
       i +=1
else:
     f=open(inputFile)
     for a in f.readlines():
         fu = a.split(',')
         yy1[i]=float(fu[0])
   
         x1[i]=float(fu[1])
         i += 1
def zs():
    o=range(20)
    ##gp.AddError(b2[i])
    
    o[1]=math.tan(b2[i])
    ##gp.AddError(o[1])
    
    o[2]=math.cos(b2[i])
    ##gp.AddError(o[2])
    
    o[3]=k[7]*o[2]*o[2]
    ##gp.AddError(o[3])
    
    o[4]=o[1]*o[1]
    ##gp.AddError(o[4])
    
    o[5]=1+o[3]
    ##gp.AddError(o[5])
    
    o[6]=k[0]/math.sqrt(o[5])
    ##gp.AddError(o[6])
    
    o[7]=(l2[i]-ll2)*o[2]
    o[8]=o[7]*o[7]
    o[9]=o[1]*o[2]
    o[10]=o[9]*o[9]
    o[11]=(k[2]+o[10]*(k[3]+o[10]*k[4]))
    ###gp.AddError(o[11])
    x2[i]=k[1]*b2[i]-o[9]*o[2]*o[11]+((((o[4]-58)*o[4]+61)*o[8]/30+(4*o[3]+5)*o[5]-o[4])*o[8]/12+1)*o[6]*o[1]*o[8]/2
    
    y2[i]=((((o[4]-18)*o[4]-(58*o[4]-14)*o[3]+5)*o[8]/20+o[5]-o[4])*o[8]/6+1)*o[6]*o[7]
    ####gp.AddError(y2[i])
    o[12]=(o[1]*o[7]*(1+o[8]*((o[5]+o[3])*o[5]/3+o[8]*(2-o[4])/15)))
    rg[i]=jdzh2(o[12])

def fs():
    yy1[i]
    
    yy1[i]=yy1[i]-500000
    
    p[1]=x1[i]/k[1]
    p[2]=math.sin(p[1])
    p[3]=p[2]*p[2]
    p[4]=p[1]+p[2]*math.cos(p[1])*(k[5]-p[3]*(k[6]-p[3]*k[8]))
    o[1]=math.tan(p[4])
    o[2]=math.cos(p[4])
    o[3]=k[7]*o[2]*o[2]
    o[4]=o[1]*o[1]
    o[5]=1+o[3]
    o[6]=k[0]/math.sqrt(o[5])
    p[5]=yy1[i]/o[6]
    p[6]=p[5]*p[5]
    
    b1[i]=p[4]-((((45*o[4]+90)*o[4]+61)*p[6]/30-(3-9*o[3])*o[4]-5-o[3])*p[6]/12+1)*p[6]*o[1]*o[5]/2
    
    l1[i]=((((24*o[4]+28)*o[4]+(8*o[4]+6)*o[3]+5)*p[6]/20-2*o[4]-o[5])*p[6]/6+1)*p[5]/o[2]
    
if d==54:
    k54()
if d==80:
    k80()




if k0==1:
    zs1()
    for i in range(0,n):
        bb1=b1[i]
        b2[i]=jdzh1(bb1)
        
        bb1=l1[i]
        l2[i]=jdzh1(bb1)
        
        bb1=ll1
        ll2=jdzh1(bb1)
        
        zs()
        if(d1==6): y2[i]=y2[i]+(bb1+3)/6*1000000+500000
	elif(d1==3): y2[i]=y2[i]+bb1/3*1000000+500000
	else: y2[i]=y2[i]+500000
        ##aa3=aa3+1
        ##if aa3%49==0:
        ##    zs1()
        ##aa3=aa3+1
        ##if aa3%49==0:
        ##    zs1()
	##gp.AddError(d1)
	##gp.AddError(y2[i])
        f=open(outputFile,'a')
        lis1 = str(y2[i])
        lis2 = str(x2[i])
        f.writelines(lis1 + "," + lis2 + "\n")
        f.flush()   
        f.close
##################### 测试

if k0==2:
    fs1()
    for i in range(0,n):
        bb2=ll1
        ll3=jdzh1(bb2)
        
        aa1=(yy1[i]/1e6)
        aa1 = int(aa1)
        ###dd1 = float(aa1)*1e6
        
        yy1[i]=yy1[i]-float(aa1)*1e6#############问题所在
        
        fs()
        bb1=b1[i]
        
        b2[i]=jdzh2(bb1)
        
        bb2=l1[i]+ll3
        l2[i]=jdzh2(bb2)
        #aa3=aa3+1
        #if aa3%49==0:
        #    fs1()
        #aa3=aa3+1
        #if aa3%49==0:
        #    fs1()
        #aa3=aa3+1                           
        f=open(outputFile,'a')
        lis1 = str(l2[i])
        lis2 = str(b2[i])
        f.writelines(lis1 + "," + lis2 + "\n")
        f.flush()   
        f.close


if k0==3:
    for i in range(0,n):
        bb1=l0
        ll3=jdzh1(bb1)
        bb2=ll1
        ll2=jdzh1(bb2)
        aa1=yy1[i]/1e6
        yy1[i]=yy1[i]-float(aa1)*1e6
        fs()
        l1[i]=l1[i]+ll3
        b2[i]=b1[i]
        l2[i]=l1[i]
        zs()
        bb1=b1[i]
        b1[i]=jdzh2(bb1)
        bb2=l1[i]
        l1[i]=jdzh2(bb2)
        aa3=aa3+1
        if aa3%49==0:
            hd()
        aa3=aa3+1
        if aa3%49==0:
            hd()
        aa3=aa3+1
        if aa3%49==0:
            hd()
        if d1==6:
            y2[i]=y2[i]+(ll1+3)/6*1000000+500000
        if d1==3:
            y2[i]=y2[i]+(ll1+3)/2*1000000+500000    
        if d1 ==1:
            y2[i]=y2[i]+500000
        aa3=aa3+1
        if aa3%49==0:
            hd()
        aa3=aa3+1
        if aa3%49==0:
            hd()
        f=open(outputFile,'a')
        lis1 = str(l2[i])
        lis2 = str(b2[i])
        f.writelines(lis1 + "," + lis2 + "\n")
        f.flush()   
        f.close




