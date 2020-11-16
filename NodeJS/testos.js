const os = require('os');

var fm = os.freemem();
var tm = os.totalmem();

console.log('Total Memory: '+ tm);
console.log('Free Memory: '+ fm);