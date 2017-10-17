import intrepyd
import intrepyd.tools as ts

def doMain():
    ctx = intrepyd.Context()
    circ = ts.translate_simulink(ctx, 'counter_verify.slx', 'real')
    circ.mk_circuit()
    for target in circ.targets:
        print 'Processing proof objective:', target
        br = ctx.mk_backward_reach()
        target_net = circ.targets[target]
        br.add_target(target_net)
        br.add_watch(target_net)
        result = br.reach_targets()
        print result
        if result == intrepyd.engine.EngineResult.REACHABLE:
            trace = br.get_last_trace()
            dataframe = trace.get_as_dataframe(ctx.net2name)
            print dataframe

if __name__ == "__main__":
    doMain()
