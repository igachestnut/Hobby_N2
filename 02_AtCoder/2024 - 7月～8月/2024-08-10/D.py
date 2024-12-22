""" 
発想
- 立方体の領域における累積和

- 修正しないけど、
    k =x
    j =y
    i =z扱いをする
"""

def cheaker() :
    return


def main() :
    N = int(input())
    
    cube = [[[0 for i in range(N+1)]for j in range(N+1)]for k in range(N+1)]
    for k in range(1, N+1) :
        for j in range(1, N+1) :
            a = list(map(int, input().split()))
            for i in range(1, N+1) :
                cube[k][j][i] = a[i-1] + cube[k-1][j][i] + cube[k][j-1][i] + cube[k][j][i-1] - cube[k-1][j-1][i] - cube[k][j-1][i-1] - cube[k-1][j][i-1] + cube[k-1][j-1][i-1]
    #print(cube)
    
    Q = int(input())
    for q in range(Q) :
        Lx1, Rx1, Ly1, Ry1, Lz1, Rz1 = map(int, input().split())
        Lx1, Ly1, Lz1 = Lx1-1, Ly1-1, Lz1-1
        print(cube[Rx1][Ry1][Rz1] - cube[Lx1][Ry1][Rz1] - cube[Rx1][Ly1][Rz1] - cube[Rx1][Ry1][Lz1] + cube[Lx1][Ly1][Rz1] + cube[Rx1][Ly1][Lz1] + cube[Lx1][Ry1][Lz1] - cube[Lx1][Ly1][Lz1])
    return


if __name__ == "__main__" :
    main()
    #cheaker()
