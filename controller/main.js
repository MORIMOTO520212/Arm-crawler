// main.js
webiopi()

// controll.py から呼び出している
function advance() {
    // 前進
    webiopi().callMacro("advance", 0, callbackGetValue);
    document.getElementById('output2').value="Advance";
}
function reverse() {
    // 後進
    webiopi().callMacro("reverse", 0, callbackGetValue);
    document.getElementById('output2').value="Reverse";
}
function left() {
    // 左回り
    webiopi().callMacro("left",  0, callbackGetValue);
    document.getElementById('output2').value="Left";
}
function right() {
    // 右回り
    webiopi().callMacro("right",  0, callbackGetValue);
    document.getElementById('output2').value="Right";
}
function stop() {
    // 停止
    webiopi().callMacro("stop",  0, callbackGetValue);
    document.getElementById('output2').value="Stop";
}

function slid(value){
    document.getElementById('output').value=value;
    webiopi().callMacro("slid", value, callbackGetValue);
}

function kill() {
    // プロセスキル
    webiopi().callMacro("kill",  0, callbackGetValue);
    document.getElementById('output2').value="Process Killed";
}

function callbackGetValue(macro, args, data) {
    console.log(macro);
    console.log(args);
    console.log(data);
}