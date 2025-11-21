// for (let i = 0; i < 11; i += 1) {
//     setTimeout(() => {
//         console.log(`${i} seconds later`)
//     },i)
// }

function makeLogger(number) {
    return function() {
        console.log(number)
    }
}

function delayLog() {
    for (let index = 1; index <= 10; index += 1) {
        let logger = makeLogger(index);
        setTimeout(logger, index * 1000);
    }
}