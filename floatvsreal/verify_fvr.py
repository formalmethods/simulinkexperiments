import intrepyd as ip

# Import translated circuits
import float_vs_real_real
import float_vs_real_float

def doMain(instance):
    ctx = ip.Context()
    inst = instance.SimulinkCircuit(ctx, 'float_vs_real')
    inst.mk_circuit()
    prop = inst.targets['$bdroot/Proof Objective']
    target = ctx.mk_not(prop)
    br = ctx.mk_backward_reach()
    br.add_target(target)
    result = br.reach_targets()
    print result
    if result == ip.engine.EngineResult.REACHABLE:
        trace = br.get_last_trace()
        dataframe = trace.get_as_dataframe(ctx.net2name)
        print dataframe

if __name__ == "__main__":
    print 'Verifying with infinite precision reals'
    doMain(float_vs_real_real)
    print 'Verifying with floating points'
    doMain(float_vs_real_float)
