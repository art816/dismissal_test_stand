import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    i = 0
    with open(sys.argv[1]) as f, open(sys.argv[2]) as f_actual:
        while True:  
            expected =  f.readline()
            actual  = f_actual.readline()
            if expected == '' and actual == '':
                print(i)
                break
            assert expected == actual, f"{expected} | {actual}"
            i += 1
