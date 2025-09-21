//1

// for (let i = 1; i < 100; i +=2) {
//     console.log(i)
// }

//2

// for (let i = 2; i < 99; i += 2) {
//     console.log(i)
// }

//3

// let length = 10
// let width = 7
// let measure = 'feet'
// let total = parseInt(length * width)
// if (measure === 'feet') {
//     console.log(parseFloat(total * 10.7639).toFixed(2))
// }


// let sqfeet = parseFloat(total * 10.7639).toFixed(2)
// console.log(length * width)
// console.log(sqfeet)


//4

// let bill_amount = 200

// let tipPercentage = 15
// let tipAmount = bill_amount * (tipPercentage / 100).toFixed(2)
// console.log((`the tip is $${tipAmount}`))
// console.log(`the total is $${(bill_amount + tipAmount).toFixed()}`)

//5

// let input = "p"
// let number = 6
// let total = 0
// if (input === "s") {
//     for (let i = 1; i <= number; i += 1) {
//         total += i
//     }
//     console.log(total)
// } else if (input === "p") {
//     total = 1
//     for (let i = 1; i <= number; i += 1) {
//         total *= i
//     }
//     console.log(total)
// }

//6

// function shortLongShort(string1, string2) {
//     let shortString = string1.length < string2.length ? string1 : string2
//     let longString = string1.length > string2.length ? string1 : string2

//     return shortString + longString + shortString
// }

// console.log(shortLongShort('abc', 'defgh'));    // "abcdefghabc"
// shortLongShort('abcde', 'fgh');    // "fghabcdefgh"
// shortLongShort('', 'xyz');         // "xyz"


//7 and 8

// function isLeapYear(num) {

//     if (num >= 1752) {
//     if (num % 4 === 0) { 
//         if ( num % 100 === 0 && num % 400 === 0) {
//             console.log("true")
//             return true
//         } else if (num % 100 === 0) {
//             console.log("false")
//             return false
//         }
//         console.log("true")
//         return true
//     }
//     console.log("false")
//     return false
//     }
    
//     return num % 4 === 0

// }
// isLeapYear(2016);      // true
// isLeapYear(2015);      // false
// isLeapYear(2100);      // false
// isLeapYear(2400);      // true
// isLeapYear(240000);    // true
// isLeapYear(240001);    // false
// isLeapYear(2000);      // true
// isLeapYear(1900);      // false
// isLeapYear(1752);      // true
// isLeapYear(1700);      // false
// isLeapYear(1);         // false
// isLeapYear(100);       // false
// isLeapYear(400);       // true

//9

// function multisum(num) {
//     let total = 0;

//     for (let i = 1; i <=num; i += 1) {
//         if (i % 3 === 0 || i % 5 === 0) {
//             total += i
//         }
//     }
//     return total
// }

// console.log(multisum(10))

//10

function utf16Value(string) {
    let sum = 0;

    for (let idx = 0; idx < string.length; idx += 1) {
        sum += string.charCodeAt(idx)
    }
    return sum
}