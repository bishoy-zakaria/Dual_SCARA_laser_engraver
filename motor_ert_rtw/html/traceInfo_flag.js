function TraceInfoFlag() {
    this.traceFlag = new Array();
    this.traceFlag["motor.c:151c31"]=1;
    this.traceFlag["motor.c:160c29"]=1;
    this.traceFlag["motor.c:160c41"]=1;
}
top.TraceInfoFlag.instance = new TraceInfoFlag();
function TraceInfoLineFlag() {
    this.lineTraceFlag = new Array();
    this.lineTraceFlag["motor.c:151"]=1;
    this.lineTraceFlag["motor.c:154"]=1;
    this.lineTraceFlag["motor.c:160"]=1;
    this.lineTraceFlag["motor.c:192"]=1;
    this.lineTraceFlag["motor.c:229"]=1;
}
top.TraceInfoLineFlag.instance = new TraceInfoLineFlag();
