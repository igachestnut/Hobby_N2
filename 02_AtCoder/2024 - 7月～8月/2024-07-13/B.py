def cheaker() :
    return


def main() :
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Cx, Cy = map(int, input().split())
    
    rad_ab = (Ay-By)/(Ax-Bx) #x=1の時のyの値
    rad_bc = (By-Cy)/(Bx-Cx) #x=1の時のyの値
    rad_ca = (Cy-Ay)/(Cx-Ax) #x=1の時のyの値
    if abs(rad_ab) == abs(1/rad_bc) or abs(rad_bc) == abs(1/rad_ca) or abs(rad_ca) == abs(1/rad_ab) :
        print("Yes")
    else :
        print("No")
    return

def main2() :
    """ 3平方の定理を使用する 
    
    a^2 + b^2 = c^2
    これを全ての方向で回す
    a,b,c = 各転換の距離、　ab,bc,caとできる
    
    """
    import math 

    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    Cx, Cy = map(int, input().split())
    
    def caluclate(p1, p2) :
        if p1 == p2 :
            return 0
        else :
            return (p1 - p2)**2
        
    def caluclate2(p) :
        if p == 0 :
            return 0
        else :
            return p**2
    
    ab = math.sqrt(caluclate(Ay, By) + caluclate(Ax, Bx))
    bc = math.sqrt(caluclate(By, Cy) + caluclate(Bx, Cx))
    ca = math.sqrt(caluclate(Cy, Ay) + caluclate(Cx, Ax))
    
    if ab == math.sqrt(caluclate2(bc) + caluclate2(ca)) or bc == math.sqrt(caluclate2(ca) + caluclate2(ab)) or ca == math.sqrt(caluclate2(ab) + caluclate2(bc)) :
        print("Yes")
    else :
        print("No") 
           
    

if __name__ == "__main__" :
    main2()
    #cheaker()
