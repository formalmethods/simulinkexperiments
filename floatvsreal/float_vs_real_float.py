import intrepyd as ip
import intrepyd.scr
import intrepyd.circuit
import collections

class SimulinkCircuit(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_naked_circuit_impl(self, inputs):
        input_keys = list(inputs)
        # In1 -> n1
        n1 = inputs[input_keys[0]]
        # $bdroot/Add -> n2
        tn4 = self.context.mk_add(n1, n1)
        tn3 = self.context.mk_add(n1, tn4)
        tn2 = self.context.mk_add(n1, tn3)
        tn1 = self.context.mk_add(n1, tn2)
        tn0 = self.context.mk_add(n1, tn1)
        n2 = self.context.mk_add(n1, tn0)
        self.nets['$bdroot/Add'] = n2
        # $bdroot/Constant
        n3 = self.context.mk_number('0.7', self.context.mk_float32_type())
        self.nets['$bdroot/Constant'] = n3
        # $bdroot/Relational\nOperator -> n4
        n4 = self.context.mk_neq(n2, n3)
        self.nets['$bdroot/Relational\nOperator'] = n4
        self.targets['$bdroot/Proof Objective'] = n4
        outputs = collections.OrderedDict()
        return outputs

    def _mk_inputs(self):
        # $bdroot/In1 -> n1
        n1 = self.context.mk_input('In1', self.context.mk_float32_type())
        self.inputs['In1'] = n1

