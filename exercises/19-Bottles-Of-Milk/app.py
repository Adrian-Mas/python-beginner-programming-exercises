# ✅↓ Write your code here ↓✅
def number_of_bottles():
    
    for song in range(99, 0, -1):
        if song > 1:
            print(f"{song} bottles of milk on the wall, {song} bottles of milk.Take one down and pass it around,{song-1} bottles of milk on the wall.")
        elif song == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
        else:
            print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()
number = []