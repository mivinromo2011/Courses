const EventEmitter = require('events');

const emitter = new EventEmitter();

emitter.on('Message logged', function(){
    console.log('Got message');
});

emitter.emit('Message logged');