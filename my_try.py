import os


def make_graph(h, s):
    children = {}
    parent = {}
    node = -1
    for i in range(len(s)):
        children.setdefault(h[i], []).append(s[i])
        parent[s[i]] = h[i]
        if h[i] == 0:
            node = s[i]
    return children, parent, node
    

def dfs(graph, node, time, weights):  #function for dfs
    ##print(f"node {node}")
    weights[node] = [time]
    time += 1
    if node in graph:
        for neighbour in graph[node]:
            time = dfs(graph, neighbour, time, weights)
    
    weights[node].append(time)
    return time
        


def create_graph():
    path = os.path.realpath(os.path.dirname(__file__))
    with open(path + '/input.txt') as file:
        with open(path + '/output_my.txt', 'w') as out_file:
        
            # кол-во сотрудников и запросов
            n, q = list(map(int, file.readline().split()))
            s, h = [], []
            for i in range(n):
                cur_s, cur_h = list(map(int, file.readline().split()))
                s.append(cur_s)  # номера работников
                h.append(cur_h)  # начальники работников

            children_graph, parent_graph, node = make_graph(h, s)
            #print(children_graph)
            #print(parent_graph)
            #print(node)
            
            weights = {}
            dfs(children_graph, node, 0, weights)
            #print(f"{weights=}")
            #Vreturn children_graph, parent_graph, weights

            for i in range(q):

                k = int(file.readline())  # кол-во оставшихся сотрудников
                remain = list(map(int, file.readline().split()))

                intervals = {}

                for key in remain:
                    intervals[tuple(weights[key])] = key
                #print(f"{intervals=}")


                full_res = []
                for k in intervals:
                    #print(f"{intervals[k]=}, {k=}")
                    if intervals[k] == node:
                        full_res.append((node, 0))
                        #out_file.write(f"{node} 0\n")
                        continue
                    parent_interval = find_parent(k, intervals)
                    res = intervals[parent_interval]
                    full_res.append((intervals[k], res))
                    #print(f"{res=}, {parent_interval=}")
                    
                

                full_res.sort(key=lambda x: x[0])
                for qwe in full_res:
                    out_file.write(f"{qwe[0]} {qwe[1]}\n")
                    ##print(f"{res=}, {parent_interval=}")
                    #out_file.write(f"{k} {parent[k]}\n")


def find_parent(cur_interval, intervals):
    mb_interval = (float('-inf'), float('inf'))
    for interval in intervals:
        if if_in(cur_interval, interval):
            if if_in(interval, mb_interval):
                mb_interval = interval
    return mb_interval



def if_in(interval1, interval2):
    #print(interval1, interval2)
    if interval1[0] > interval2[0] and interval1[1] <= interval2[1]:
        #print(True)
        return True
    #print(False)
    return False


if __name__ == '__main__':
    create_graph()

