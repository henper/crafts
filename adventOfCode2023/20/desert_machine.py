import re

highs = 0
lows = 0

class Gate:
    def __init__(self, id, outputs: list) -> None:
        self.id = id
        self.outputs = outputs

    def pulse(self, state, fro=''):
        global gates, highs, lows

        wave = []
        for output in self.outputs:
            print(self.id + (' -high-> ' if state else ' -low-> ') + output)
            if output in gates.keys():
                wave.append((self.id, state, output))

        if state:
            highs += len(self.outputs)
        else:
            lows  += len(self.outputs)

        return wave

class Broadcaster(Gate):
    pass

class FLipFlop(Gate):
    def __init__(self, id, outputs) -> None:
        super().__init__(id, outputs)
        self.state = False

    def pulse(self, state, fro):
        if not state:
            self.state = not self.state
            return super().pulse(self.state, fro)
        return []

class Conjunction(Gate):
    def set_inputs(self, inputs):
        self.inputs = {input: False for input in inputs}

    def pulse(self, state, fro):
        self.inputs[fro] = state

        if [True] * len(self.inputs) == list(self.inputs.values()):
            return super().pulse(False, fro)
        else:
            return super().pulse(True, fro)




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


# perform button presses
for press in range(1000):
    print('\nbutton -low-> broadcaster')
    lows += 1
    pulses = gates['broadcaster'].pulse(False, 'button')

    while len(pulses) != 0:
        wave = []
        for source, signal, sink in pulses:
            wave = wave + gates[sink].pulse(signal, source)
        pulses = wave


print(f'{highs} * {lows} = {highs * lows}')

