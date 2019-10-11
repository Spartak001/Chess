import  copy
import string

class Taxtak:
    taxtak=[[],[],[],[],[],[],[],[]]
    def __init__(self,):
        for i in range(0, 8):
            for j in range(0, 8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.taxtak[i].append(' ')
                    else:
                        self.taxtak[i].append(' ')
                else:
                    if j % 2 == 0:
                        self.taxtak[i].append(' ')
                    else:
                        self.taxtak[i].append(' ')

    def printe(self):
        print(" ",end=" ")
        for k in range(0,8):
           print(str(k)+" ",end=" ")
        print(' ')
        for i in range(0, 8):
            print(str(i), end="")
            for j in range(0, 8):
                if self.taxtak[i][j]!=' ':
                    print("|" + self.taxtak[i][j].name ,end="")
                else:
                    print("| " + self.taxtak[i][j], end="")
            print('|',end=" ")
            print('\n'+"-"*26)


    def ifempty(self,lis):
        if(self.taxtak[lis[0]][lis[1]]==(' ')):
            return True
        else:
            return False
    def setfigure(self,lis,figure):
       # self.taxtak[lis[0]][lis[1]],self.taxtak[figure.cordinat[0]][figure.cordinat[1]]=self.taxtak[figure.cordinat[0]][figure.cordinat[1]],self.taxtak[lis[0]][lis[1]]
        self.taxtak[lis[0]][lis[1]]=self.taxtak[figure.cordinats[0]][figure.cordinats[1]]
        self.taxtak[figure.cordinats[0]][figure.cordinats[1]]=' '
    def setandeat(self,lis,figure):
        self.taxtak[lis[0]][lis][1]=figure
        taxtak[figure.cordinat[0]][figure.cordinat[1]]=None
    def startset(self,figure):
        self.taxtak[figure.cordinats[0]][figure.cordinats[1]]=figure
    def set(self,lis,lis2):
        self.taxtak[lis2[0]][lis2[1]]=self.taxtak[lis[0]][lis[1]]
        self.taxtak[lis[0]][lis[1]]=' '

    def move(self,lis,lis2):
        if self.taxtak[lis[0]][lis[1]].move(lis2):
            self.setfigure(lis,lis2)

def ifshax(kfigure):
    k=kfigure.cordinats[0]
    for i in range(kfigure.cordinats[1]-1,-1,-1):
        if taxtak.taxtak[k][i]!=' ':
            if taxtak.taxtak[k][i].getcolor()!=kfigure.color:
                if taxtak.taxtak[k][i].gettype()=="queen" or taxtak.taxtak[k][i].gettype()=="nav":
                    return True
                else:
                    break
            else:
                break
    for i in range(kfigure.cordinats[1]+1,8):
        if taxtak.taxtak[k][i]!=' ':
            if taxtak.taxtak[k][i].getcolor()!=kfigure.color:
                if taxtak.taxtak[k][i].gettype() == "queen" or taxtak.taxtak[k][i].gettype() == "nav":
                    return True
                else:
                    break
            else:
                break
    k=kfigure.cordinats[1]
    for i in range(kfigure.cordinats[0]+1,8):
        if taxtak.taxtak[i][k]!=' ':
            if taxtak.taxtak[i][k].getcolor()!=kfigure.color:
                if taxtak.taxtak[i][k].gettype() == "queen" or taxtak.taxtak[i][k].gettype()== "nav":
                    return True
                else:
                    break
            else:
                break

    for i in range(kfigure.cordinats[0]-1,-1,-1):
        if taxtak.taxtak[i][k]!=' ':
            if taxtak.taxtak[i][k].getcolor()!=kfigure.color:
                if taxtak.taxtak[i][k].gettype() == "queen" or taxtak.taxtak[i][k].gettype() == "nav":
                    return True
                else:
                    break
            else:
                break
    k1=kfigure.cordinats[0]
    k2=kfigure.cordinats[1]
    while k1>0 and k2<7:
        k1 -= 1
        k2 += 1
        if taxtak.taxtak[k1][k2]!=' ':
            if taxtak.taxtak[k1][k2].getcolor()!=kfigure.color:
                if taxtak.taxtak[k1][k2].gettype() == "pix" or taxtak.taxtak[k1][k2].gettype() == "queen":
                    return True
                else:
                    break
            else:
                break

    k1 = kfigure.cordinats[0]
    k2 = kfigure.cordinats[1]
    while k1>0 and k2>0:
        k1 -= 1
        k2 -= 1
        if taxtak.taxtak[k1][k2]!=' ':
            if taxtak.taxtak[k1][k2].getcolor()!=kfigure.color:
                if taxtak.taxtak[k1][k2].gettype() == "queen" or taxtak.taxtak[k1][k2].gettype() == "pix":
                    return True
                else:
                    break
            else:
                break
    k1 = kfigure.cordinats[0]
    k2 = kfigure.cordinats[1]
    while k1<7 and k2<7:
        k1 += 1
        k2 += 1
        if taxtak.taxtak[k1][k2]!=' ':
            if taxtak.taxtak[k1][k2].getcolor()!=kfigure.color:
                if taxtak.taxtak[k1][k2].gettype() == "queen" or taxtak.taxtak[k1][k2].gettype() == "pix":
                    return True
                else:
                    break
            else:
                break
    k1 =kfigure.cordinats[0]
    k2 = kfigure.cordinats[1]
    while k1<7 and k2>0:
        k1 += 1
        k2 -= 1
        if taxtak.taxtak[k1][k2]!=' ':
            if taxtak.taxtak[k1][k2].getcolor()!=kfigure.color:
                if taxtak.taxtak[k1][k2].gettype() == "queen" or taxtak.taxtak[k1][k2].gettype() == "pix":
                    return True
                else:
                    break
            else:
                break
    k1=kfigure.cordinats[0]-2
    k2=kfigure.cordinats[1]+1
    if  k1>=0 and k2<=7:
        if taxtak.taxtak[k1][k2]!=' ':
            if taxtak.taxtak[k1][k2].gettype()=="dzi" and taxtak.taxtak[k1][k2].color!=kfigure.color:
                return True

    k1 = kfigure.cordinats[0] - 2
    k2 = kfigure.cordinats[1] -1
    if k1>=0 and k2>=0:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True

    k1 = kfigure.cordinats[0]-1
    k2 = kfigure.cordinats[1] +2
    if k1>=0 and k2<=7:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True

    k1 = kfigure.cordinats[0] + 1
    k2 = kfigure.cordinats[1] + 2
    if k1<=7 and k2<=7:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True

    k1 = kfigure.cordinats[0] -2
    k2 = kfigure.cordinats[1] + 1
    if k1>=0 and k2<=7:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True

    k1 = kfigure.cordinats[0] - 2
    k2 = kfigure.cordinats[1] - 1
    if k1>=0 and k2>=0:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True

    k1 = kfigure.cordinats[0] +1
    k2 = kfigure.cordinats[1] - 2
    if k1<=7 and k2>=0:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True
    k1 = kfigure.cordinats[0] -1
    k2 = kfigure.cordinats[1] - 2
    if k1>=0 and k2>=0:
        if taxtak.taxtak[k1][k2] != ' ':
            if taxtak.taxtak[k1][k2].gettype() == "dzi" and taxtak.taxtak[k1][k2].color != kfigure.color:
                return True
    return False

def zinvoriutel(figure):
    lis1 = [None, None]
    lis1[0] = figure.cordinats[0]
    lis1[1] = figure.cordinats[1]
    liss1 = [lis1[0] + 1, lis1[1] + 1]
    liss2 = [lis1[0] + 1, lis1[1] - 1]
    liss3 = [lis1[0] - 1, lis1[1] - 1]
    liss4 = [lis1[0] - 1, lis1[1] + 1]
    if not(taxtak.ifempty(liss1)):
        if lis1[0]<7 and lis1[1]<7:
            if taxtak.taxtak[lis1[0] + 1][lis1[1] + 1].getcolor()!=figure.getcolor():
                return True
    if not(taxtak.ifempty(liss2)):
        if lis1[0]<7 and lis1[1]>0:
            if taxtak.taxtak[lis1[0] + 1][lis1[1] - 1].getcolor()!=figure.getcolor():
                return True
    if not(taxtak.ifempty(liss3)):
        if lis1[1]>0 and lis1[0]>0:
            if taxtak.taxtak[lis1[0] - 1][lis1[1] - 1].getcolor()!=figure.getcolor():
                return True
    if not(taxtak.ifempty(liss4)):
        if lis1[0]>0 and lis1[1]<7:
            if taxtak.taxtak[lis1[0] - 1][lis1[1] + 1].getcolor()!=figure.getcolor():
                return True
    return False

class king:
    color = ' '
    color1 = "white"
    color2 = "black"
    name = None
    cordinats = [None, None]
    typemy = "king"
    delname=None
    def __init__(self,color,list,name,x1,y1,delname):
        self.cordinats = copy.deepcopy(list)
        self.color = color
        self.name = name
        self.cordinats[0]=x1
        self.cordinats[1]=y1
        self.delname=delname
    def ifcanmoveto(self,coord):
        xs=self.cordinats[0]
        ys=self.cordinats[1]
        x=coord[0]
        y=coord[1]
        if x==xs+1 and (y==ys+1 or y==ys-1):
            return True
        elif x==xs-1 and (y==ys-1 or y==ys+1):
            return True
        elif x==xs and (y==ys+1 or y==ys-1):
            return True
        elif y==ys and (x==xs+1 or x==xs-1):
            return True
        return False
    def move(self,lis):
        if self.ifcanmoveto(lis):
            if taxtak.taxtak[lis[0]][lis[1]] == (' '):
                taxtak.setfigure(lis,self)
                self.cordinats = copy.deepcopy(lis)
                return True
            else:#utel
                if taxtak.taxtak[lis[0]][lis[1]].color!=self.color:
                    x1 = lis[0]
                    x2 = lis[1]
                    if self.color=="black":
                        wfigures.pop(taxtak.taxtak[x1][x2].delname)
                    else:
                        bfigures.pop(taxtak.taxtak[x1][x2].delname)
                    taxtak.setfigure(lis, self)
                    self.cordinats = copy.deepcopy(lis)
                    return True
        else:
            return False

    def gettype(self):
        return self.typemy

    def getcolor(self):
        return self.color

class queen:
    color = ' '
    color1 = "white"
    color2 = "black"
    name = None
    cordinats = [None, None]
    typemy = "queen"
    delname=None
    def __init__(self,color,list,name,x1,y1,delname):
        self.cordinats = copy.deepcopy(list)
        self.color = color
        self.name = name
        self.cordinats[0] = x1
        self.cordinats[1] = y1
        self.delname=delname

    def getcolor(self):
        return self.color


    def ifcanmoveto(self,coord):
        xs=self.cordinats[0]
        ys=self.cordinats[1]
        x=coord[0]
        y=coord[1]
        if x>7 or x<0 or y>7 or y<0:
            return False
        if x==xs:
            if y<ys:
                if y-ys==-1:
                    lis=[x,y]
                    if taxtak.ifempty(lis):
                        return True
                    elif taxtak.taxtak[x][y].getcolor!=self.getcolor():
                            return True
                for yc in range(ys-1,0,-1):
                    if taxtak.taxtak[x][yc]==' ':
                        if yc==y+1:
                            return True
                    else:
                        break
                #elif:
                # check other figure
            if y>ys:
                if y-ys==1:
                    lis = [x, y]
                    if taxtak.ifempty(lis):
                        return True
                    elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                        return True
                for yc in range(ys+1,7):
                    if taxtak.taxtak[x][yc]==' ':
                        if yc==y-1:
                            return True
                    else:
                        break
            else:
                return False
                 #elif
                 #check other figure
        elif y==ys:
            if x<xs:
                if x - xs ==-1:
                    lis = [x, y]
                    if taxtak.ifempty(lis):
                        return True
                    elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                        return True
                for xc in range(xs-1,0,-1):
                    if taxtak.taxtak[xc][y]==' ':
                        if xc==x+1:
                            return True
                    else:
                        break
                #elif
                #check other ifgure
            elif x>xs:
                if x-xs==1:
                    if x - xs == 1:
                        lis = [x, y]
                        if taxtak.ifempty(lis):
                            return True
                        elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                            return True
                for xc in range(xs+1,7):
                    if taxtak.taxtak[xc][y]==' ':
                        if xc==x-1:
                            return True
                    else:
                        break
                #elif
                #check other figure
            else:
                return False
        elif x>xs and y>ys:
            if x-xs==1 and y-ys==1:
                lis = [x, y]
                if taxtak.ifempty(lis):
                    return True
                elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                    return True
            if x-xs==y-ys:
                xc=xs
                yc=ys
                while xc<7 and yc<7:
                    xc+=1
                    yc+=1
                    if taxtak.taxtak[xc][yc]==' ':
                        if xc==x-1 and yc==y-1:
                            return True
                    else:
                        break
        elif x<xs and y<ys:
            if x-xs==-1 and y-ys==-1:
                lis = [x, y]
                if taxtak.ifempty(lis):
                    return True
                elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                    return True
            if x-xs==y-ys:
                xc=xs
                yc=ys
                while xc>1 and yc>1:
                    xc-=1
                    yc-=1
                    if taxtak.taxtak[xc][yc]==' ':
                        if xc==x+1 and yc==y+1:
                            return True
                    else:
                        break
        elif x>xs and y<ys:
            if x-xs==1 and y-ys==-1:
                lis = [x, y]
                if taxtak.ifempty(lis):
                    return True
                elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                    return True
            if x-xs==-(y-ys):
                xc=xs
                yc=ys
                while xc<7 and yc>1:
                    xc+=1
                    yc-=1
                    if taxtak.taxtak[xc][yc]==' ':
                        if xc==x-1 and yc==y+1:
                            return True
                    else:
                        break
        elif x<xs and y>ys:
            if x-xs==-1 and y-ys==1:
                lis = [x, y]
                if taxtak.ifempty(lis):
                    return True
                elif taxtak.taxtak[x][y].getcolor != self.getcolor():
                    return True
            if x-xs==-(y-ys):
                xc=xs
                yc=ys
                while xc>1 and yc<7:
                    xc-=1
                    yc+=1
                    if taxtak.taxtak[xc][yc]==' ':
                        if xc==x+1 and yc==y-1:
                            return True
                    else:
                        break
        return False
    def move(self,lis):
        if self.ifcanmoveto(lis):
            if taxtak.taxtak[lis[0]][lis[1]]==(' '):
                taxtak.setfigure(lis,self)
                self.cordinats=copy.deepcopy(lis)
                return True
            else:#eat
                if taxtak.taxtak[lis[0]][lis[1]].color != self.color:
                    x1 = lis[0]
                    x2 = lis[1]
                    if self.color == "black":
                        wfigures.pop(taxtak.taxtak[x1][x2].delname)
                    else:
                        bfigures.pop(taxtak.taxtak[x1][x2].delname)
                    taxtak.setfigure(lis, self)
                    self.cordinats = copy.deepcopy(lis)
                    return True
        else:
            return False

    def gettype(self):
        return self.typemy

class Zinvor:
    start=0
    wname='Զ'
    color=' '
    color1="white"
    color2="black"
    name=None
    cordinats=[None,None]
    typemy="zinvor"
    delname=None

    def __init__(self,guyn,lisi,name,x1,y1,delname):
       # self.cordinat.clear()
        self.cordinats=copy.deepcopy(lisi)
        self.color=guyn
        self.name=name
        self.cordinats[0] = x1
        self.cordinats[1] = y1
        self.delname=delname


    def gettype(self):
        return self.typemy

    def getcolor(self):
        return self.color

    def ifcanmoveto(self,lis2):
        lis1=[None,None]
        lis1[0]=self.cordinats[0]
        lis1[1]=self.cordinats[1]
        liss1 = [lis1[0] + 1, lis1[1] + 1]
        liss2 = [lis1[0] + 1, lis[1] - 1]
        liss3=[lis1[0]-1,lis1[1]-1]
        liss4=[lis1[0]-1,lis1[1]+1]
        if self.start!=0:
           if self.color==self.color1:#spitak
                if lis2[0] < lis1[0] and lis2[1]==lis1[1] and lis1[0]-lis2[0]==1:
                    return True
                elif zinvoriutel(self) and (lis2[0]==self.cordinats[0]+1 and lis2[1]==self.cordinats[1]+1 or self.cordinats[1]-1):
                    return True
                else:
                    return False
           else:
               if lis2[0]>lis1[0] and lis2[1]==lis1[1] and lis2[0]-lis1[0]==1:
                   return True
               elif zinvoriutel(self) and (lis2[0]==self.cordinats[0]+1 and lis2[1]==self.cordinats[1]+1 or self.cordinats[1]-1):
                   return True
               else:
                   return False

        else:
            if ((lis1[0] - lis2[0]==1 and lis2[0]!=0) or lis2[0] - lis1[0] == 1) and  lis1[1]==lis2[1]:
                if self.color ==self.color1:  # spitak
                    plist=[lis1[0]-1,lis1[1]]
                    if taxtak.ifempty(plist):
                        return True
                    elif zinvoriutel(self) and (lis2[0]==self.cordinats[0]-1 and lis2[1]==self.cordinats[1]+1 or self.cordinats[1]-1):
                        return True
                    else:
                        return False
                else:
                    plist=[lis1[0]+1,lis1[1]]
                    if taxtak.ifempty(plist):
                        return True
                    elif zinvoriutel(self) and (lis2[0]==self.cordinats[0]-1 and lis2[1]==self.cordinats[1]+1 or self.cordinats[1]-1):
                        return True
                    else:
                        return False
            else:
                if self.color == self.color1: # spitak
                    if lis2[0] < lis1[0] and lis2[1] == lis1[1] and (lis1[0] - lis2[0] == 1 or lis1[0] - lis2[0] == 2):
                        les=[self.cordinats[0]-2,self.cordinats[1]]
                        if taxtak.ifempty(les):
                            return True
                    elif zinvoriutel(self) and (lis2[0]==self.cordinats[0]-1 and lis2[1]==self.cordinats[1]+1 or self.cordinats[1]-1):
                        return True
                    else:
                        return False
                else:
                    if lis2[0] > lis1[0] and lis2[1] == lis1[1] and (lis2[0] - lis1[0] == 1 or lis2[0] - lis1[0] == 2):
                        les = [self.cordinats[0] + 2, self.cordinats[1]]
                        if taxtak.ifempty(les):
                            return True
                    elif zinvoriutel(self):
                        return True
                    else:
                        return False


    def move(self,lis):
        if self.ifcanmoveto(lis):
            if taxtak.taxtak[lis[0]][lis[1]]==(' '):
                taxtak.setfigure(lis,self)
                self.cordinats=copy.deepcopy(lis)
                self.start+=1
                return True
            else:
                if taxtak.taxtak[lis[0]][lis[1]].color != self.color:
                    x1 = lis[0]
                    x2 = lis[1]
                    if self.color == "black":
                        bfigures.pop(taxtak.taxtak[x1][x2].delname)
                    else:
                        wfigures.pop(taxtak.taxtak[x1][x2].delname)
                    taxtak.setfigure(lis, self)
                    self.cordinats = copy.deepcopy(lis)
                    self.start+=1
                    return True
        else:
            return False

class Dzi:
    color = ' '
    color1 = "white"
    color2 = "black"
    name = None
    cordinats = [None, None]
    typemy = "dzi"
    delname=None

    def __init__(self,color,lisi,name,x1,y1,delname):
        self.cordinats = copy.deepcopy(lisi)
        self.color = color
        self.name = name
        self.cordinats[0] = x1
        self.cordinats[1] = y1
        self.delname=delname

    def getcolor(self):
        return self.color

    def ifcanmoveto(self,lis2):
        lis1=[None,None]
        lis1[0]=self.cordinats[0]
        lis1[1]=self.cordinats[1]
        try:
            if (lis2[0]==(lis1[0]+2) and (lis2[1]==lis1[1]+1 or lis2[1]==lis1[1]-1)):
                return True
            elif (lis2[0]==(lis1[0]-2) and (lis2[1]==lis1[1]+1 or lis2[1]==lis1[1]-1)):
                return True
            elif ((lis2[1]==lis1[1]-2) and (lis2[0]==lis1[0]-1 or lis2[0]==lis1[0]+1)):
                return True
            elif (lis2[1]==lis1[1]+2) and (lis2[0]==lis1[0]-1 or lis2[0]==lis1[0]+1):
               return True
            else:
                return False
        except IndexError:
            return False



    def move(self,lis):
        if self.ifcanmoveto(lis):
            if taxtak.taxtak[lis[0]][lis[1]] == (' '):
                taxtak.setfigure(lis,self)
                self.cordinats = copy.deepcopy(lis)
                return True
            else:
                if taxtak.taxtak[lis[0]][lis[1]].color!=self.color:
                    x1 = lis[0]
                    x2 = lis[1]
                    if self.color == "black":
                        bfigures.pop(taxtak.taxtak[x1][x2].delname)
                    else:
                        wfigures.pop(taxtak.taxtak[x1][x2].delname)
                    taxtak.setfigure(lis, self)
                    self.cordinats = copy.deepcopy(lis)
                    return True
        else:
            return False
    def gettype(self):
        return self.typemy

class nav:
    color = ' '
    color1 = "white"
    color2 = "black"
    name = None
    cordinats = [None, None]
    typemy = "nav"
    delname=None

    def __init__(self,color,lisi,name,x1,y1,delname):
        self.cordinats = copy.deepcopy(lisi)
        self.color = color
        self.name = name
        self.cordinats[0] = x1
        self.cordinats[1] = y1
        self.delname=delname

    def getcolor(self):
        return self.color

    def ifcanmoveto(self, newcoordinate,):
        if newcoordinate[0] != self.cordinats[0] and newcoordinate[1] != self.cordinats[1]:
            # print("wrong coordinate")
            return False

        if newcoordinate[0] == self.cordinats[0]:
            if newcoordinate[1] > self.cordinats[1]:
                k = self.cordinats[1]+1
                while (k < newcoordinate[1]-1):
                    lis = [self.cordinats[0], k]
                    t = taxtak.ifempty(lis)  # ????????
                    if t == False:
                        # print("wrong coordinate")
                        return False
                    k += 1
                return True
            else:
                k = self.cordinats[1] - 1
                while (k > newcoordinate[1]+1):
                    lis = [self.cordinats[0], k]
                    t = taxtak.ifempty(lis)  # ????????
                    if t == False:
                        # print("wrong coordinate")
                        return False
                    k -= 1
                return True

        if newcoordinate[1] == self.cordinats[1]:
            if newcoordinate[0] < self.cordinats[0]:
                k = self.cordinats[0] - 1
                while (k > newcoordinate[0]+1):
                    lis = [self.cordinats[0], k]
                    t = taxtak.ifempty(lis)  # ????????
                    if t == False:
                        # print("wrong coordinate")
                        return False
                    k -= 1
                return True

            else:
                k = self.cordinats[0] + 1
                while (k < newcoordinate[0]-1):
                    lis = [self.cordinats[0], k]
                    t = taxtak.ifempty(lis)  # ????????
                    if t == False:
                        # print("wrong coordinate")
                        return False
                    k += 1
                return True

    def move(self, lis):
        if self.ifcanmoveto(lis):
            if taxtak.taxtak[lis[0]][lis[1]] == (' '):
                taxtak.setfigure(lis, self)
                self.cordinats = copy.deepcopy(lis)
                return True
            else:
                if taxtak.taxtak[lis[0]][lis[1]].color != self.color:
                    x1 = lis[0]
                    x2 = lis[1]
                    if self.color == "black":
                        bfigures.pop(taxtak.taxtak[x1][x2].delname)
                    else:
                        wfigures.pop(taxtak.taxtak[x1][x2].delname)
                    taxtak.setfigure(lis, self)
                    self.cordinats = copy.deepcopy(lis)
                    return True
        else:
            return False

    def gettype(self):
        return self.typemy

class pixx:
    color = ' '
    color1 = "white"
    color2 = "black"
    name = None
    cordinats = [None, None]
    typemy = "pix"
    delname=None

    def __init__(self, color, lisi, name,x1,y1,delname):
        self.cordinats = copy.deepcopy(lisi)
        self.color = color
        self.name = name
        self.cordinats[0]=x1
        self.cordinats[1]=y1
        self.delname=delname
    def getcolor(self):
        return self.color

    def ifcanmoveto(self, newcoordinate,):
        if abs(newcoordinate[0] - self.cordinats[0]) != abs(newcoordinate[1] - self.cordinats[1]):
            return False

        x1 = self.cordinats[0]
        y1 = self.cordinats[1]
        x2 = newcoordinate[0]
        y2 = newcoordinate[1]

        if x1 < x2 and y1 < y2:
            i = x1 + 1
            j = y1 + 1
            while i != x2 and j != y2:
                lis = [i, j]
                t = taxtak.ifempty(lis)
                if t == False:
                    return False
                i += 1
                j += 1
            return True

        if x1 < x2 and y1 > y2:
            i = x1 + 1
            j = y1 - 1
            while i != x2 and j != y2:
                lis = [i, j]
                t = taxtak.ifempty(lis)
                if t == False:
                    return False
                i += 1
                j -= 1
            return True

        if x1 > x2 and y1 < y2:
            i = x1 - 1
            j = y1 + 1
            while i != x2 and j != y2:
                lis = [i,j]
                t = taxtak.ifempty(lis)
                if t == False:
                    return False
                i -= 1
                j += 1
            return True

        if x1 > x2 and y1 > y2:
            i = x1 - 1
            j = y1 - 1
            while i != x2 and j != y2:
                lis = [i,j]
                t = taxtak.ifempty(lis)
                if t == False:
                    return False
                i -= 1
                j -= 1
            return True

    def move(self, lis):
        if self.ifcanmoveto(lis):
            if taxtak.taxtak[lis[0]][lis[1]] == (' '):
                taxtak.setfigure(lis, self)
                self.cordinats = copy.deepcopy(lis)
                return True
            else:
                if taxtak.taxtak[lis[0]][lis[1]].color != self.color:
                    x1 = lis[0]
                    x2 = lis[1]
                    if self.color == "black":
                        bfigures.pop(taxtak.taxtak[x1][x2].delname)
                    else:
                        wfigures.pop(taxtak.taxtak[x1][x2].delname)
                    taxtak.setfigure(lis, self)
                    self.cordinats = copy.deepcopy(lis)
                    return True
        else:
            return False
    def gettype(self):
        return self.typemy

def ifmat(kfigure,shaxf):
    x1=kfigure.cordinats[0]
    y1=kfigure.cordinats[1]
    if x1>0:
        lis = [kfigure.cordinats[0]-1, kfigure.cordinats[1]]
        if taxtak.ifempty(lis):
            val=taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1]=val
                x2=lis[0]
                y2=lis[1]
                taxtak.taxtak[x2][y2]=' '
                kfigure.cordinats[0]+=1
            else:
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                return False
        elif taxtak.taxtak[x1-1][y1].getcolor()!=kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                return False
    elif x1>0 and y1<7:
        lis = [kfigure.cordinats[0] - 1, kfigure.cordinats[1]+1]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1]-=1
            else:
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] -= 1
                return False
        elif taxtak.taxtak[x1 - 1][y1+1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] -= 1
            else:
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] -= 1
                return False
    elif x1>0 and y1>0:
        lis = [kfigure.cordinats[0] - 1, kfigure.cordinats[1]-1]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] += 1
                return False
        elif taxtak.taxtak[x1 - 1][y1-1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] += 1
                kfigure.cordinats[1] += 1
                return False
    elif y1>0:
        lis = [kfigure.cordinats[0], kfigure.cordinats[1]-1]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] += 1
                return False
        elif taxtak.taxtak[x1][y1-1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] += 1
                return False
    elif y1<7:
        lis = [kfigure.cordinats[0], kfigure.cordinats[1]+1]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] -= 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] -= 1
                return False
        elif taxtak.taxtak[x1][y1+1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] -= 1

            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[1] -= 1
                return False
    elif x1<7:
        lis = [kfigure.cordinats[0] + 1, kfigure.cordinats[1]]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0]-=1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1

                return False
        elif taxtak.taxtak[x1 + 1][y1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1

            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1

                return False
    elif x1<7 and y1<7:
        lis = [kfigure.cordinats[0] + 1, kfigure.cordinats[1]+1]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] -= 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] -= 1
                return False
        elif taxtak.taxtak[x1 + 1][y1+1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] -= 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] -= 1
                return False
    elif x1<7 and y1>0:
        lis = [kfigure.cordinats[0] + 1, kfigure.cordinats[1]-1]
        if taxtak.ifempty(lis):
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] += 1
                return False
        elif taxtak.taxtak[x1 + 1][y1-1].getcolor() != kfigure.getcolor():
            val = taxtak.taxtak[x1][y1]
            kfigure.move(lis)
            if ifshax(kfigure):
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] += 1
            else:
                taxtak.taxtak[x1][y1] = val
                taxtak.taxtak[x1][y1] = val
                x2 = lis[0]
                y2 = lis[1]
                taxtak.taxtak[x2][y2] = ' '
                kfigure.cordinats[0] -= 1
                kfigure.cordinats[1] += 1
                return False
    x1 = shaxf[0]
    x2 = shaxf[1]
    les = [x1, x2]
    if kfigure.color=="black":
        for key in bfigures:
            if bfigures[key].ifcanmoveto(les):
                return False
    else:
        for key in wfigures:
            if wfigures[key].ifcanmoveto(les):
                return False

    if kfigure.color=="black":
        x1=kfigure.cordinats[0]
        y1=kfigure.cordinats[1]
        if x1==shaxf[0]:
            if y1<shaxf[1]:
                for key in bfigures:
                    y2 = y1 + 1
                    while y2<=shaxf[1]-1:
                        lis = [x1, y2]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        y2+=1
            elif y1>shaxf[1]:
                for key in bfigures:
                    y2 = y1 - 1
                    while y2 >= shaxf[1] + 1:
                        lis = [x1, y2]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        y2 -= 1
        elif y1==shaxf[1]:
            if x1<shaxf[0]:
                for key in bfigures:
                    x2 = x1 + 1
                    while x2<=shaxf[1]-1:
                        lis = [x2, y1]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        x2+=1
            elif x2>shaxf[0]:
                for key in bfigures:
                    x2 = x1 - 1
                    while x2 >= shaxf[1] + 1:
                        lis = [x2, y1]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        x2 -= 1

        if abs(shaxf[0] - kfigure.cordinats[0]) != abs(shaxf[1] - kfigure.cordinats[1]):
            if x1<shaxf[0] and y1<shaxf[1]:
                for key in bfigures:
                    x2 = x1 + 1
                    y2 = y1 + 1
                    while x2<shaxf[0] and y2<shaxf[1]:
                        lis=[x2,y2]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        x2+=1
                        y2+=1
            elif x1<shaxf[0] and y1<shaxf[1]:
                for key in bfigures:
                    x2 = x1 + 1
                    y2 = y1 - 1
                    while x2<shaxf[0] and y2>shaxf[1]:
                        lis=[x2,y2]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        x2+=1
                        y2-=1
            elif x1>shaxf[0] and y2<shaxf[1]:
                for key in bfigures:
                    x2 = x1 - 1
                    y2 = y1 + 1
                    while x2>shaxf[0] and y2<shaxf[1]:
                        lis=[x2,y2]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        x2-=1
                        y2+=1
            elif x1>shaxf[0] and y2>shaxf[1]:
                for key in bfigures:
                    x2 = x1 - 1
                    y2 = y1 - 1
                    while x2>shaxf[0] and y2>shaxf[1]:
                        lis=[x2,y2]
                        if bfigures[key].ifcanmoveto(lis):
                            return False
                        x2-=1
                        y2-=1
    else:
        x1 = kfigure.cordinats[0]
        y1 = kfigure.cordinats[1]
        if x1 == shaxf[0]:
            if y1 < shaxf[1]:
                for key in wfigures:
                    y2 = y1 + 1
                    while y2 <= shaxf[1] - 1:
                        lis = [x1, y2]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        y2 += 1
            elif y1 > shaxf[1]:
                for key in wfigures:
                    y2 = y1 - 1
                    while y2 >= shaxf[1] + 1:
                        lis = [x1, y2]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        y2 -= 1
        elif y1 == shaxf[1]:
            if x1 < shaxf[0]:
                for key in wfigures:
                    x2 = x1 + 1
                    while x2 <= shaxf[1] - 1:
                        lis = [x2, y1]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        x2 += 1
            elif x1 > shaxf[0]:
                for key in wfigures:
                    x2 = x1 - 1
                    while x2 >= shaxf[1] + 1:
                        lis = [x2, y1]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        x2 -= 1
        if abs(shaxf[0] - kfigure.cordinats[0]) != abs(shaxf[1] - kfigure.cordinats[1]):
            if x1 < shaxf[0] and y1 < shaxf[1]:
                for key in wfigures:
                    x2 = x1 + 1
                    y2 = y1 + 1
                    while x2 < shaxf[0] and y2 < shaxf[1]:
                        lis = [x2, y2]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        x2 += 1
                        y2 += 1
            elif x1 < shaxf[0] and y1 < shaxf[1]:
                for key in wfigures:
                    x2 = x1 + 1
                    y2 = y1 - 1
                    while x2 < shaxf[0] and y2 > shaxf[1]:
                        lis = [x2, y2]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        x2 += 1
                        y2 -= 1
            elif x1 > shaxf[0] and y2 < shaxf[1]:
                for key in wfigures:
                    x2 = x1 - 1
                    y2 = y1 + 1
                    while x2 > shaxf[0] and y2 < shaxf[1]:
                        lis = [x2, y2]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        x2 -= 1
                        y2 += 1
            elif x1 > shaxf[0] and y2 > shaxf[1]:
                for key in wfigures:
                    x2 = x1 - 1
                    y2 = y1 - 1
                    while x2 > shaxf[0] and y2 > shaxf[1]:
                        lis = [x2, y2]
                        if wfigures[key].ifcanmoveto(lis):
                            return False
                        x2 -= 1
                        y2 -= 1
    return True

taxtak=Taxtak()
lis=[1,1]
wzinvor1=Zinvor("white",lis,'WZ',6,0,0)
wzinvor2=Zinvor("white",lis,'WZ',6,1,1)
wzinvor3=Zinvor("white",lis,'WZ',6,2,2)
wzinvor4=Zinvor("white",lis,'WZ',6,3,3)
wzinvor5=Zinvor("white",lis,'WZ',6,4,4)
wzinvor6=Zinvor("white",lis,'WZ',6,5,5)
wzinvor7=Zinvor("white",lis,'WZ',6,6,6)
wzinvor8=Zinvor("white",lis,'WZ',6,7,7)
bzinvor1=Zinvor("black",lis,'BZ',1,0,0)
bzinvor2=Zinvor("black",lis,'BZ',1,1,1)
bzinvor3=Zinvor("black",lis,'BZ',1,2,2)
bzinvor4=Zinvor("black",lis,'BZ',1,3,3)
bzinvor5=Zinvor("black",lis,'BZ',1,4,4)
bzinvor6=Zinvor("black",lis,'BZ',1,5,5)
bzinvor7=Zinvor("black",lis,'BZ',1,6,6)
bzinvor8=Zinvor("black",lis,'BZ',1,7,7)
wqueen=queen("white",lis,"WQ",7,3,8)
bqueen=queen("black",lis,"BQ",0,3,8)
wpix1=pixx("white",lis,'WP',7,2,9)
wpix2=pixx("white",lis,'WP',7,5,9)
bpix1=pixx("black",lis,'BP',0,2,10)
bpix2=pixx("black",lis,'BP',0,5,10)
wnav1=nav("white",lis,"WN",7,0,11)
wnav2=nav("white",lis,"WN",7,7,11)
bnav1=nav("black",lis,"BN",0,0,12)
bnav2=nav("black",lis,"BN",0,7,12)
wdzi1=Dzi("white",lis,"WD",7,1,13)
wdzi2=Dzi("white",lis,"WD",7,6,13)
bdzi1=Dzi("black",lis,"BD",0,1,14)
bdzi2=Dzi("black",lis,"BD",0,6,14)
wking=king("white",lis,"WK",7,4,15)
bking=king("black",lis,"BK",0,4,15)
taxtak.startset(wzinvor1)
taxtak.startset(wzinvor2)
taxtak.startset(wzinvor3)
taxtak.startset(wzinvor4)
taxtak.startset(wzinvor5)
taxtak.startset(wzinvor6)
taxtak.startset(wzinvor7)
taxtak.startset(wzinvor8)
taxtak.startset(bzinvor1)
taxtak.startset(bzinvor2)
taxtak.startset(bzinvor3)
taxtak.startset(bzinvor4)
taxtak.startset(bzinvor5)
taxtak.startset(bzinvor6)
taxtak.startset(bzinvor7)
taxtak.startset(bzinvor8)
taxtak.startset(bqueen)
taxtak.startset(wqueen)
taxtak.startset(bking)
taxtak.startset(wking)
taxtak.startset(wnav1)
taxtak.startset(wnav2)
taxtak.startset(bnav1)
taxtak.startset(bnav2)
taxtak.startset(wdzi1)
taxtak.startset(wdzi2)
taxtak.startset(bdzi1)
taxtak.startset(bdzi2)
taxtak.startset(wpix1)
taxtak.startset(wpix2)
taxtak.startset(bpix1)
taxtak.startset(bpix2)
wfigures=dict()
wfigures.update({0:wzinvor1})
wfigures.update({1:wzinvor1})
wfigures.update({2:wzinvor1})
wfigures.update({3:wzinvor1})
wfigures.update({4:wzinvor1})
wfigures.update({5:wzinvor1})
wfigures.update({6:wzinvor1})
wfigures.update({7:wzinvor1})
wfigures.update({8:wqueen})
wfigures.update({9:wpix1})
wfigures.update({10:wpix2})
wfigures.update({11:wnav1})
wfigures.update({12:wnav2})
wfigures.update({13:wdzi1})
wfigures.update({14:wdzi2})
bfigures=dict()
bfigures.update({0:bzinvor1})
bfigures.update({1:bzinvor1})
bfigures.update({2:bzinvor1})
bfigures.update({3:bzinvor1})
bfigures.update({4:bzinvor1})
bfigures.update({5:bzinvor1})
bfigures.update({6:bzinvor1})
bfigures.update({7:bzinvor1})
bfigures.update({8:bqueen})
bfigures.update({9:bpix1})
bfigures.update({10:bpix2})
bfigures.update({11:bnav1})
bfigures.update({12:bnav2})
bfigures.update({13:bdzi1})
bfigures.update({14:bdzi2})
taxtak.printe()

while True:

    while True:
        print("ԽԱՂԱՑԵՂ 1(սպիտակ)")
        val1=2
        '''try:
            if ifshax(wking):
                val1=0
                print("հիշեք որ շախի տակ եք")
            inp = input("խնդրում ենք գրել որ քարն էք ուզում շարժել")
            inp = inp.translate({ord(c): None for c in string.whitespace})
            x1 = int(inp[0])
            y1 = int(inp[1])
            val=taxtak.taxtak[x1][y1]
            if taxtak.taxtak[x1][y1].getcolor() != "black":
                inp = input("Խնդրում ենք գրել որտեղ եք ուզում տեղափոխել քարը")
                inp = inp.translate({ord(c): None for c in string.whitespace})
                x2 = int(inp[0])
                y2 = int(inp[1])
                lis = [x2, y2]
                if taxtak.taxtak[x1][y1].move(lis):
                    if ifshax(wking):
                        if val1==0:
                            print("շախի տակ եք փակեք շախը")
                        else:
                            print("շախ եք բացում")
                            taxtak.taxtak[x1][y1] = val
                            taxtak.taxtak[x2][y2]=' '
                    else:
                        if ifshax(bking):
                            taxtak.printe()
                            print('\n',"շախ")
                            bshax=[x2,y2]
                            if ifmat(bking,bshax):
                                print("Շախ և Մատ")
                                break
                            else:
                                break
                        else:
                            taxtak.printe()
                            break
                else:
                    print("սխալ կորդինատներ կրկին փորցեք")
            else:
                print("սխալ գույն")
        except:
            print("սխալ կորդինատներ")
            '''
        if ifshax(wking):
            val1 = 0
            print("հիշեք որ շախի տակ եք")
        inp = input("խնդրում ենք գրել որ քարն էք ուզում շարժել")
        inp = inp.translate({ord(c): None for c in string.whitespace})
        x1 = int(inp[0])
        y1 = int(inp[1])
        val = taxtak.taxtak[x1][y1]
        if taxtak.taxtak[x1][y1].getcolor() != "black":
            inp = input("Խնդրում ենք գրել որտեղ եք ուզում տեղափոխել քարը")
            inp = inp.translate({ord(c): None for c in string.whitespace})
            x2 = int(inp[0])
            y2 = int(inp[1])
            lis = [x2, y2]
            if taxtak.taxtak[x1][y1].move(lis):
                if ifshax(wking):
                    if val1 == 0:
                        print("շախի տակ եք փակեք շախը")
                    else:
                        print("շախ եք բացում")
                        taxtak.taxtak[x1][y1] = val
                        taxtak.taxtak[x2][y2] = ' '
                else:
                    if ifshax(bking):
                        taxtak.printe()
                        print('\n', "շախ")
                        bshax = [x2, y2]
                        if ifmat(bking, bshax):
                            print("Շախ և Մատ")
                            break
                        else:
                            break
                    else:
                        taxtak.printe()
                        break
            else:
                print("սխալ կորդինատներ կրկին փորցեք")
        else:
            print("սխալ գույն")

    while True:
        print("ԽԱՂԱՑԵՂ 2(սևվ)")
        val1=2
        '''try:
            if ifshax(bking):
                val1=0
                print("հիշեք որ շախի տակ եք")
            x1=int(input("Խնդրում ենք գրել որ քարն եք ուզում շարժել"))
            y1=int(input())
            val=taxtak.taxtak[x1][y1]
            if taxtak.taxtak[x1][y1].getcolor()!="white":
                x2=int(input("Խնդրում ենք գրել որտեղ եք ուզում տեղափոխել քարը"))
                y2=int(input())
                lis=[x2,y2]
                if taxtak.taxtak[x1][y1].move(lis):
                    if ifshax(bking):
                        if val1==0:
                            print("շախի տակ եք փակեք շախը")
                            taxtak.taxtak[x1][y1] = val
                            taxtak.taxtak[x2][y2] = ' '
                        else:
                            print("շախ եք բացում")
                            taxtak.taxtak[x1][y1]=val
                            taxtak.taxtak[x2][y2] = ' '
                    else:
                        if ifshax(wking):
                            taxtak.printe()
                            print('\n',"շախ")
                            wshax=[x2,y2]
                            if ifmat(wking,wshax):
                                print("mattt")
                                break
                            break
                        else:
                            taxtak.printe()
                            break
                else:
                    print("սխալ կորդինատներ կրկին փորցեք")
            else:
                print("սխալ գույն")
        except:
            print("սխալ")
            '''
        if ifshax(bking):
            val1 = 0
            print("հիշեք որ շախի տակ եք")
        inp = input("խնդրում ենք գրել որ քարն էք ուզում շարժել")
        inp = inp.translate({ord(c): None for c in string.whitespace})
        x1 = int(inp[0])
        y1 = int(inp[1])
        val = taxtak.taxtak[x1][y1]
        if taxtak.taxtak[x1][y1].getcolor() != "white":
            inp = input("Խնդրում ենք գրել որտեղ եք ուզում տեղափոխել քարը")
            inp = inp.translate({ord(c): None for c in string.whitespace})
            x2 = int(inp[0])
            y2 = int(inp[1])
            lis = [x2, y2]
            if taxtak.taxtak[x1][y1].move(lis):
                if ifshax(bking):
                    if val1 == 0:
                        print("շախի տակ եք փակեք շախը")
                        taxtak.taxtak[x1][y1] = val
                        taxtak.taxtak[x2][y2] = ' '
                    else:
                        print("շախ եք բացում")
                        taxtak.taxtak[x1][y1] = val
                        taxtak.taxtak[x2][y2] = ' '
                else:
                    if ifshax(wking):
                        taxtak.printe()
                        print('\n', "շախ")
                        wshax = [x2, y2]
                        if ifmat(wking, wshax):
                            print("mattt")
                            break
                        break
                    else:
                        taxtak.printe()
                        break
            else:
                print("սխալ կորդինատներ կրկին փորցեք")
        else:
            print("սխալ գույն")

