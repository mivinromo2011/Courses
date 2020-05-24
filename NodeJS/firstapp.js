var logger = require('./logger');

console.log(logger);

logger.tell('message');
function sayHello(name){
    console.log('hello '+ name);
}

sayHello('Mithun');