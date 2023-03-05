import random
import sys



def write_input(three: list, stay: list):
    with open("input.txt", "w") as f:
        f.write(f"{len(three)} {len(stay)}\n")

        for el in three:
            f.write(f"{el[0]} {el[1]}\n")
        

        for variant in stay: 
            f.write(f"{len(variant)}\n")
            f.write(f"{' '.join(str(v) for v in variant)}\n")



def write_output(res: list):
     with open("output.txt", "w") as f:
        for var in res:
            for el in var:
                f.write(f"{el[0]} {el[1]}\n")


def generate_data(n: int, q: int):
    # Выстраиваем сотрудников в линию (1, 2, 3 .... n) n-босс
    three = [[i, i+1] for i in range(1, n+1)]
    three[-1][1] = 0
    
    all_stay = []
    all_res = []
    for _ in range(q):
        stay = random.sample(range(1, n), q - 2 if q < 20 else min(n//2, random.randint(1, 20)))
        stay.append(three[-1][0])
        all_stay.append(stay)

        sorted_stay = sorted(stay)

        res = [[sorted_stay[i], sorted_stay[i+1]] for i in range(len(sorted_stay) - 1)]
        res.append(three[-1])
        all_res.append(res)
    return three, all_stay, all_res


def generate_data_heap(n: int, q: int):
    # Выстраиваем сотрудников в кучу (1, 2, 3 .... n) 1-босс
    #              1
    #       2            3
    #   4      5     6       7
    #

    three = [[i, i//2] for i in range(1, n+1)]
    three[0][1] = 0
    
    all_stay = []
    #all_res = []
    for _ in range(q):
        stay = random.sample(range(2, n+1), q - 2 if q < 20 else min(n//2, random.randint(1, 19)))
        stay.append(three[0][0])
        all_stay.append(stay)

        # TODO не знаю как тут сгенерить правильный ответ))))
        #sorted_stay = sorted(stay)

        #res = [[sorted_stay[i], sorted_stay[i+1]] for i in range(len(sorted_stay) - 1)]
        #res.append(three[-1])
        #all_res.append(res)
    return three, all_stay, [[]]




if __name__ == "__main__":
    print("start main")
    if sys.argv[1] == "heap":
        three, stay, res = generate_data_heap(10000, 1000)
    elif  sys.argv[1] == "line":
        three, stay, res = generate_data(10000, 1000)
        
    write_input(three, stay)
    write_output(res)
