def rotate(mat):
    for row in range(N):
            for col in range(N-1,-1,-1):
                print(mat[col][row],end=' ')
            print()
N = 4
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Angle = int(input())
if Angle%90!=0:
    print("INVALID")
    quit()
if Angle % 360 == 0:
    for row in mat:
        print(*row)
else:
    if Angle%360==90:
        rotate(mat)
    elif Angle%360 == 180:
        mat.reverse()
        tran = list(zip(*mat))
        rotate(tran)
    elif Angle%360 == 270:
        tran = list(zip(*mat))
        for row in tran[::-1]:
            print(*row)
