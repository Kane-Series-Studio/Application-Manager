var _speedconstant = 8.9997e-9;
var d = new Date();
var amount = 150000000;

var estprocessor = 1.7;
console.log("running loop " + amount + " times.\nEstimated time (for " + estprocessor + "ghz processor) is "
 + (Math.round(((_speedconstant * amount) / estprocessor) * 100) / 100) + "s");
for (var i = amount; i > 0; i--) { }
var newd = new Date();
var accnewd = Number(String(newd.getSeconds()) + "." + String(newd.getMilliseconds()));
var accd = Number(String(d.getSeconds()) + "." + String(d.getMilliseconds()));
var di = accnewd - accd;
if (d.getMinutes() != newd.getMinutes()) {
    di = (60 * (newd.getMinutes() - d.getMinutes())) + di
}
spd = ((_speedconstant * amount) / di);
console.log("Time: " + Math.round(di * 1000) / 1000 + "s, \nestimated speed: " + Math.round(spd * 1000) / 1000 + "GHZ");


// DISPLAY VARIABLES
var loops = amount;
var proccessor = `${estprocessor} ghz processor`;
var speed = Math.round(spd * 1000) / 1000 + "GHZ";