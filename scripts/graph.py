# graph.py
# use account array to create GML files
# by Xiaoyu Tai

def filter(array_all_nodes, minimum):
  d = {}
  f = []
  for x in array_all_nodes:
    d[x] = d.get(x, 0) + 1
  for (key, value) in d.items():
    if value >= minimum:
      f.append(key)
  return f

def node(array_all_nodes):
  d = {}
  i = 0
  for x in array_all_nodes:
    if not d.get(x):
      d[x] = i
      i += 1
  for (key, value) in d.items():
    print "  node ["
    print "    id " + str(value)
    print "    label \"" + key + "\""
    print "  ]"
  return d

def sorting_RT(array, minimum):
  d = {}
  a = []
  s = 0
  for x in array:
    d[x] = d.get(x, 0) + 1

def edge(arrays, ids, names):
  i = 0
  for array in arrays:
    d = {}
    source_id = ids[names[i]]
    i += 1
    for n in array:
      d[n] = d.get(n, 0) + 1
    for (key, value) in d.items():
      if ids.get(key):
        if value > 3:
          print "  edge ["
          print "    source " + str(source_id)
          print "    target " + str(ids[key])
          print "    weight " + str(value)
          print "  ]"

def graph(nodes, all_node, node_id, id_names):
  print "graph ["
  print "  directed 1"
  node_id = node(filter(nodes, 5))
  edge(all_node, node_id, id_names)
  # Testing
  # node_id = node(["a", "b", "c"])
  # edge([["a"], ["b"], ["c"]], node_id, ["b", "c", "a"])
  print "]"

graph()
