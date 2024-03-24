import numpy as np 

FinalBoard=[[""]*8]*8


FinalBoard[6]=["Wp"]*8
#
# Set up of the black pieces
#
FinalBoard[1]=["Bp"]*8
FinalBoard[0][0]="Br"
FinalBoard[0][7]="Br"
FinalBoard[0][1]="Bn"
FinalBoard[0][6]="Bn"
FinalBoard[0][2]="Bb"
FinalBoard[0][5]="Bb"
FinalBoard[0][3]="Bq"
FinalBoard[0][4]="Bk"

#
# Set up of the white pieces
#

FinalBoard[7][0]="Wr"
FinalBoard[7][7]="Wr"
FinalBoard[7][1]="Wn"
FinalBoard[7][6]="Wn"
FinalBoard[7][2]="Wb"
FinalBoard[7][5]="Wb"
FinalBoard[7][3]="Wq"
FinalBoard[7][4]="Wk"


print(FinalBoard[0],'\n',FinalBoard[1],'\n', FinalBoard[6],'\n', FinalBoard[7])