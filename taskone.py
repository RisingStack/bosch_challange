"""
@author "Laszlo Szoke (CC-AD/ENG1-Bp)" <fixed-term.laszlo.szoke@hu.bosch.com>
"""
import copy
import json
import os
import pickle
import sys

global_paths=[]
map_one = None

def select_next_node(possible_nodes, prev_nodes):
    min_key = list(possible_nodes.keys())[0]
    min_time = possible_nodes[min_key]["Time"]
    for node_id, value in possible_nodes.items():
        if value["Time"] < min_time and node_id not in prev_nodes:
            min_time = value["Time"]
            min_key = node_id
        elif node_id in prev_nodes:
            min_time = 1000
    return min_key, min_time

def paths(current_node, prev_nodes=None, target_node="D1"):
    if prev_nodes is None:
        prev_nodes = []
    possible_paths = {current_node:{}}
    prev_nodes.append(current_node)
    for node_id, node_value in map_one[current_node].items():
        if target_node == node_id:
            prev_nodes.append(node_id)
            possible_paths[current_node][node_id] = {"path":prev_nodes, "time": calculate_time(prev_nodes)}
            global_paths.append({"path":prev_nodes, "time": calculate_time(prev_nodes)})
            return possible_paths
        elif node_id not in prev_nodes:
            new_path = paths(node_id, copy.deepcopy(prev_nodes), target_node=target_node)
            if isinstance(new_path,list):
                possible_paths[current_node][node_id] = new_path
            elif isinstance(new_path, dict):
                possible_paths[current_node].update(new_path)
        else:
            continue
    return possible_paths

def calculate_time(full_path):
    sum_time = 0
    for i in range(len(full_path)-2):
        sum_time += map_one[full_path[i]][full_path[i+1]]["Time"]
    return sum_time


def search_best_path(start_pos= 'A1', end_pos= 'D1'):
    final_path = paths(start_pos, target_node=end_pos)
    mini_time = 1000
    best_path = None
    for item in global_paths:
        if mini_time > item["time"]:
            mini_time = item["time"]
            best_path = copy.deepcopy(item['path'])

    return best_path


# all_times = 0
# while (end_node != current_node):
#     next_node, time = select_next_node(prev_nodes=previous_nodes, possible_nodes=map_one[current_node])
#     all_times += time
#     current_node = next_node
#     previous_nodes.append(next_node)
#
# print(previous_nodes)

if __name__ == "__main__":
    solution_file_name = os.path.basename(__file__).split('.')[0] + '_solution.pkl'
    if os.path.exists(solution_file_name):
        with open(solution_file_name, "rb") as file:
            best_path = pickle.load(file)

    else:
        map_file = "../boschtest/taskOne.json"
        with open(map_file, "r") as f:
            map_one = json.load(f)

        best_path = search_best_path()
        with open(solution_file_name, "wb") as file:
            pickle.dump(best_path,file)

    currentPos = sys.argv[1]
    current_Best = best_path.index(currentPos)+1
    print(best_path[current_Best])