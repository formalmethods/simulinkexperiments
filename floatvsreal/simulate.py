import intrepyd
import intrepyd.tools as ts

def doMain():
    ctx = intrepyd.Context()
    circ = ts.translate_simulink(ctx, 'counter.slx', 'real')
    circ.mk_circuit()
    outputs = [item[1] for item in circ.outputs.items()]
    ts.simulate(ctx, 'counter', 10, outputs)

if __name__ == "__main__":
    doMain()

