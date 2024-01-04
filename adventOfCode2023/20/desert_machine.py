import re
import networkx as nx
import matplotlib.pyplot as plt
import math


class Gate:
    def __init__(self, id, outputs: list) -> None:
        self.id = id
        self.outputs = outputs

    def pulse(self, graph, state, fro=''):

        wave = []
        for output in self.outputs:
            #print(self.id + (' -high-> ' if state else ' -low-> ') + output)
            if output in graph:
                wave.append((self.id, state, output))
        return wave

class Broadcaster(Gate):
    pass

class FLipFlop(Gate):
    def __init__(self, id, outputs) -> None:
        super().__init__(id, outputs)
        self.state = False

    def pulse(self, graph, state, fro):
        if not state:
            self.state = not self.state
            return super().pulse(graph, self.state, fro)
        return []

class Conjunction(Gate):
    def set_inputs(self, inputs):
        self.inputs = {input: False for input in inputs}

    def pulse(self, graph, state, fro):
        self.inputs[fro] = state

        if [True] * len(self.inputs) == list(self.inputs.values()):
            return super().pulse(graph, False, fro)
        else:
            return super().pulse(graph, True, fro)

# import the machine
gates = {}
conjunctions = []
with open('./adventOfCode2023/20/input.txt', 'r') as desert_machine:
    for part in desert_machine:
        m = re.search('(?P<identifier>broadcaster|\%\w+|\&\w+) \-\> (?P<outputs>.+)', part)
        outputs = m.group('outputs').split(', ')

        if m.group('identifier') == 'broadcaster':
            gates['broadcaster'] = Broadcaster('broadcaster', outputs)
            continue

        type = m.group('identifier')[0]
        id   = m.group('identifier')[1:]
        gates[id] = FLipFlop(id, outputs) if type == '%' else Conjunction(id, outputs)

        if type == '&':
            conjunctions.append(id)

# now that we have all the parts of the machine, configure the Conjunctions with their inputs
for conjunction in conjunctions:
    inputs = []
    for id, gate in gates.items():
        if conjunction in gate.outputs:
            inputs.append(id)
    gates[conjunction].set_inputs(inputs)


# Draw the machine with as a network(x)
graph = nx.DiGraph()
graph.add_nodes_from(gates)

for node, object in gates.items():
    edges = [(node, connection) for connection in object.outputs]
    graph.add_edges_from(edges)

nx.draw_networkx(graph, arrows=True, with_labels=True, **{'arrowstyle': '-|>'})
plt.show()

'''
From plotting the machine we can see that it consists of Four parts
 * each part connected to the broadcaster as it's input, and
 * each part's output connected to a conjunction module that has 'rx' as sole output

 Figure out how many button presses it takes for each part of the machine to issue a True
'''

gates['rx'] = Broadcaster('rx',[])

# split the machine into it's constituent parts
part_presses = []
for source in gates['broadcaster'].outputs:
    part = set(['broadcaster']) # initialize each part of the machine with the button/broadcaster
    for path in nx.all_simple_paths(graph, source, 'rx'):
        part.update(path)

    # Each part has it's own output conjunction which connects to rx, the goal is for this output to receive a High pulse
    goal = (path[-3], True, path[-2])

    # perform button presses, until rx receives a low-pulse
    button_presses = 0
    while(True):
        button_presses += 1
        #print('\nbutton -low-> broadcaster')
        pulses = gates['broadcaster'].pulse(part, False, 'button')

        while len(pulses) != 0 and goal not in pulses:
            wave = []
            for source, signal, sink in pulses:
                wave = wave + gates[sink].pulse(part, signal, source)
            pulses = wave

        if len(pulses) != 0:
            break

    print(button_presses)
    part_presses.append(button_presses)

# Now we do the least-common-multiple 'trick' to get the number of button presses necessary for rx to receive a low pulse
print(math.lcm(*part_presses))
