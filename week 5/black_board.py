def process():
    
    while(board_isEmpty()==False):
        
        num1 = board_min()
        board_erase(num1)
        if(board_isEmpty()==False):
            num2 = board_min()
            board_erase(num2)
            board_write(abs(num1-num2))
            
        else:
            return num1