function RTW_rtwnameSIDMap() {
	this.rtwnameHashMap = new Array();
	this.sidHashMap = new Array();
	this.rtwnameHashMap["<Root>"] = {sid: "motor"};
	this.sidHashMap["motor"] = {rtwname: "<Root>"};
	this.rtwnameHashMap["<S1>"] = {sid: "system_simulation:2"};
	this.sidHashMap["system_simulation:2"] = {rtwname: "<S1>"};
	this.rtwnameHashMap["<S2>"] = {sid: "system_simulation:6"};
	this.sidHashMap["system_simulation:6"] = {rtwname: "<S2>"};
	this.rtwnameHashMap["<S1>/In1"] = {sid: "system_simulation:3"};
	this.sidHashMap["system_simulation:3"] = {rtwname: "<S1>/In1"};
	this.rtwnameHashMap["<S1>/P-Gain"] = {sid: "system_simulation:4"};
	this.sidHashMap["system_simulation:4"] = {rtwname: "<S1>/P-Gain"};
	this.rtwnameHashMap["<S1>/Sum"] = {sid: "system_simulation:5"};
	this.sidHashMap["system_simulation:5"] = {rtwname: "<S1>/Sum"};
	this.rtwnameHashMap["<S1>/steper motor"] = {sid: "system_simulation:6"};
	this.sidHashMap["system_simulation:6"] = {rtwname: "<S1>/steper motor"};
	this.rtwnameHashMap["<S1>/Out1"] = {sid: "system_simulation:11"};
	this.sidHashMap["system_simulation:11"] = {rtwname: "<S1>/Out1"};
	this.rtwnameHashMap["<S2>/In1"] = {sid: "system_simulation:7"};
	this.sidHashMap["system_simulation:7"] = {rtwname: "<S2>/In1"};
	this.rtwnameHashMap["<S2>/Gain"] = {sid: "system_simulation:8"};
	this.sidHashMap["system_simulation:8"] = {rtwname: "<S2>/Gain"};
	this.rtwnameHashMap["<S2>/Integrator"] = {sid: "system_simulation:9"};
	this.sidHashMap["system_simulation:9"] = {rtwname: "<S2>/Integrator"};
	this.rtwnameHashMap["<S2>/Out1"] = {sid: "system_simulation:10"};
	this.sidHashMap["system_simulation:10"] = {rtwname: "<S2>/Out1"};
	this.getSID = function(rtwname) { return this.rtwnameHashMap[rtwname];}
	this.getRtwname = function(sid) { return this.sidHashMap[sid];}
}
RTW_rtwnameSIDMap.instance = new RTW_rtwnameSIDMap();
