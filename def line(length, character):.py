def line(length, character):
    if character == "":
        character = "*"
    else:
        character = character[0]
    print(character * length)

def triangle(height):
    width = 1
    while width <= height:
        line(width, "#")
        width += 1 
  
if __name__ == "__main__":
    triangle(3)
    print()
    triangle(5)