function CodeMetrics() {
	 this.metricsArray = {};
	 this.metricsArray.var = new Array();
	 this.metricsArray.fcn = new Array();
	 this.metricsArray.var["rtDW"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	size: 8};
	 this.metricsArray.var["rtM_"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	size: 493};
	 this.metricsArray.var["rtU"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	size: 8};
	 this.metricsArray.var["rtX"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	size: 8};
	 this.metricsArray.var["rtY"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	size: 8};
	 this.metricsArray.fcn["memcpy"] = {file: "C:\\Program Files\\Polyspace\\R2019a\\sys\\lcc\\include\\string.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["motor.c:rt_ertODEUpdateContinuousStates"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	stack: 104,
	stackTotal: -1};
	 this.metricsArray.fcn["motor_derivatives"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	stack: 8,
	stackTotal: 8};
	 this.metricsArray.fcn["motor_initialize"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["motor_step"] = {file: "C:\\Users\\COMPUMARTS\\Desktop\\Graduation_project\\motor_ert_rtw\\motor.c",
	stack: 8,
	stackTotal: -1};
	 this.getMetrics = function(token) { 
		 var data;
		 data = this.metricsArray.var[token];
		 if (!data) {
			 data = this.metricsArray.fcn[token];
			 if (data) data.type = "fcn";
		 } else { 
			 data.type = "var";
		 }
	 return data; }; 
	 this.codeMetricsSummary = '<a href="motor_metrics.html">Global Memory: 525(bytes) Maximum Stack: 104(bytes)</a>';
	}
CodeMetrics.instance = new CodeMetrics();
