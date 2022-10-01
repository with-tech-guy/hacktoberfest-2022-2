def commonFootsteps(a, b, c, d):
    result = []
    for i in b:
        if c <= i and d >= i:
            result.append(i)
            
    return result if len(result) >= 1 else [-1]        

def main():
    a = 6
    b = [29, 38, 12, 48, 39, 55]
    c = 15
    d = 20
    result = commonFootsteps(a , b, c, d)
    print(" ".join([str(res) for res in result]))    
    
if __name__ == "__main__":
    main()
