// // // // // // // function logOddNumbers(num) {
    
// // // // // // //     for (let i = 1; i <= num; i += 2) {

// // // // // // //         console.log(i)

// // // // // // //      }
// // // // // // // }

// // // // // // // logOddNumbers(19)

// // // // // // // function multiplesOfThreeAndFive(min,numb){

// // // // // // //     for (let i = min; i <= numb; i += 1) {
// // // // // // //         if (i % 3 === 0 && i % 5 === 0) {
// // // // // // //             console.log(`${i}!`)
// // // // // // //         }
// // // // // // //         else if (i % 3 === 0 || i % 5 === 0) {
// // // // // // //             console.log(i)
// // // // // // //         }
// // // // // // //     }
// // // // // // // }


// // // // // // // multiplesOfThreeAndFive(0,5)

// // // // // // function logMultiples(num) {

// // // // // //     for (let i = num; i <= 100; i += num) {
// // // // // //         if (i % 2 === 1) {
// // // // // //             console.log(i)
// // // // // //         }
// // // // // //     }
// // // // // // }

// // // // // // logMultiples(21)

// // // // // function fizzbuzz() {

// // // // //     for (let i = 1; i <= 100; i += 1) {
// // // // //         if (i % 3 === 0 && i % 5 === 0) {
// // // // //             console.log("FizzBuzz")
// // // // //         }
// // // // //         else if (i % 3 === 0 ) {
// // // // //             console.log("Fizz")
// // // // //         }
// // // // //         else if (i % 5 === 0) {
// // // // //             console.log("buzz")
// // // // //         }
// // // // //         else {
// // // // //             console.log(i)
// // // // //         }
// // // // //     }
// // // // // }

// // // // // fizzbuzz()


// // // // // isPrime = function hello(num) {
    
// // // // //     if (num <= 1 || num % 2 === 0 || num === 2) {
// // // // //         return false
// // // // //     }

// // // // //     for (let i=3; i <num; i+= 2) {
// // // // //         if (num % i === 0) {
// // // // //             return false
// // // // //         }
// // // // //     }
// // // // //     return true
// // // // // }

// // // // // console.log(isPrime(39))

// // // // // function isXor(value1, value2) {
// // // // //     if (!!value1 === true && !!value2 === false) {
// // // // //         return true
// // // // //     }
// // // // //     else if (!!value1 === false && !!value2 === true) {
// // // // //         return true
// // // // //     }
    
// // // // //     return false
// // // // // }

// // // // // console.log(isXor(false, true));     // true
// // // // // isXor(true, false);     // true
// // // // // console.log(isXor(false, false));    // false
// // // // // isXor(true, true);      // false


// // // // // isXor(false, 3);        // true
// // // // // isXor('a', undefined);  // true
// // // // // isXor(null, '');        // false
// // // // // isXor('2', 23);         // false

// // // // // const PASSWORD = 'hello'
// // // // // let failedAttempts = 0;

// // // // // while (true) {
// // // // //     let guess = prompt("What is the password")

// // // // //     if (guess === PASSWORD) {
// // // // //         console.log("You have successfully logged in.")
// // // // //         break;
// // // // //     }
// // // // //     failedAttempts += 1;

// // // // // if (failedAttempts === 3) {
// // // // //     console.log("You have been denied access.")
// // // // //     break;
// // // // // }


// // // // // }

// // // // // let score = 90

// // // // // switch (true) {
// // // // //     case (score >= 90):
// // // // //         console.log("A")
// // // // //         break;
// // // // //     case (score >= 70):
// // // // //         console.log("B")
// // // // // }

// // // // // function gcd(num1, num2) {
// // // // //     let lower_number = num1 > num2 ? num2 :  num1
// // // // //     //console.log(lower_number)

// // // // //     for (let i = lower_number; i > 0; i -= 1) {
// // // // //         if (num1 % i === 0 && num2 % i === 0) {
// // // // //             return i
// // // // //         }
// // // // //     }
// // // // //     return NaN
// // // // // }


// // // // // console.log(gcd(12, 4));   // 4
// // // // // console.log(gcd(15, 10));  // 5
// // // // // gcd(9, 2);    // 1


// // // // function checkGoldbach(num) {

// // // //     for (let firstNumber = 2; firstNumber < num; firstNumber += 1) {
// // // //         let diff = num - firstNumber
// // // //         if (checkIsPrime(diff) && checkIsPrime(firstNumber)) {
// // // //             console.log(`${firstNumber} ${diff}`)
// // // //         }
// // // //     }
// // // //  /*
// // // //  in order to solve this we should take the number passed in
// // // //  then for each number below that get the difference between that number
// // // //  and the number subtracted
// // // //  check if each one of those numbers is prime
// // // //  if both are prime create a hashmap with the key being the larger number

// // // //  */
// // // // }

// // // // function checkIsPrime(num) {
// // // //     if (num % 2 === 0 || num <=1 || num === 2) {
// // // //         return false
// // // //     }
// // // //     for (let i = 3; i < num; i += 2) {
// // // //         if (num % i === 0) {
// // // //             return false
// // // //         }

// // // //     }
// // // //     return true
// // // // }

// // // // console.log(checkIsPrime(3))

// // // // checkGoldbach(3);
// // // // // logs: null

// // // // checkGoldbach(4);
// // // // // logs: 2 2

// // // // checkGoldbach(12);
// // // // // logs: 5 7

// // // // checkGoldbach(100);
// // // // // logs:
// // // // // 3 97
// // // // // 11 89
// // // // // 17 83
// // // // // 29 71
// // // // // 41 59
// // // // // 47 53

// // // // function generatePattern(num) {
// // // //     let number = 1
// // // //     let stars = ""
// // // //     totalString = "1"
// // // //     for (let i = 1; i < num; i += 1) {
// // // //         stars += "*"
// // // //     }
// // // //     console.log(String(number) + stars)
// // // //     counter = stars.length -1
// // // //     do { 
        
// // // //         stars = stars.slice(0,counter)
// // // //         if (number < num) {
// // // //             stars += "*"
// // // //         }
// // // //         number += 1
// // // //         totalString = totalString + String(number)
// // // //         console.log(totalString + stars)
       
// // // //         counter -= 1
        
// // // //     } while (number < num)

// // // // }

// // // // generatePattern(15)


// // // // function trim(string){
// // // //     let result = ""
// // // //     copyMode = false
// // // //     for (let i = 0; i < string.length; i += 1) {
// // // //         if (string[i] !== " ") {
// // // //             copyMode = true
// // // //         }
// // // //         if (copyMode) {
// // // //             result += string[i]
// // // //         }
// // // //         }
    
    
// // // //     let placeholder = 0
// // // //     for (let i = result.length; i >= 0; i -= 1) {
// // // //         if (result[i] !== " ") {
// // // //             placeholder = i
// // // //             break;
// // // //         }

// // // //     }

// // // //     final_result = ""
// // // //     for (let i = 0; i < placeholder; i += 1) {
// // // //         final_result += result[i]
// // // //     }

// // // //     return final_result
// // // //     }

// // // // console.log(trim("  abc   "))


// // // function splitString(string, delimiter) {

// // //     if (delimiter === undefined) {
// // //         console.log("ERROR: no delimeter")
// // //     }
// // //     result = ""

// // //     for (let i = 0; i < string.length; i+= 1) {
// // //         if (string[i] === delimiter) {
// // //             console.log(result)
// // //             result = ""
// // //         } else if (delimiter === "") {
// // //             console.log(string[i])
// // //         }
// // //         else {
// // //             result += string[i]
// // //         }
// // //     }
    
// // //     console.log(result)

// // //   // …
// // // }

// // // splitString('abc,123,hello world', ',');
// // // // logs:
// // // // abc
// // // // 123
// // // // hello world

// // // splitString('hello');
// // // // logs:
// // // // ERROR: No delimiter

// // // splitString('hello', '');
// // // // logs:
// // // // h
// // // // e
// // // // l
// // // // l
// // // // o

// // // splitString('hello', ';');
// // // // logs:
// // // // hello

// // // splitString(';hello;', ';');
// // // // logs:
// // // //  (this is a blank line)
// // // // hello


// // function repeat(string, times) {
// //     if (times === 0) {
// //         return ""
// //     }
// //     if (times < 0 || !(Number.isInteger(times))) {

// //         return undefined
// //     }
// //     let result = ""
// //     let counter = 0
// //     do {
// //         result += string
// //         counter += 1
// //     }
// //     while (counter < times)
// //     return result
// //   // …
// // }

// // repeat('abc', 1);       // "abc"
// // console.log(repeat('abc', 2));       // "abcabc"
// // repeat('abc', -1);      // undefined
// // repeat('abc', 0);       // ""
// // console.log(repeat('abc', 'a'));     // undefined
// // repeat('abc', false);   // undefined
// // console.log(repeat('abc', null));    // undefined
// // console.log(repeat('abc', '  '));    // undefined

// function startsWith(string, searchString) {
//   // …
//   if (searchString === "" || searchString === '') {
//     return true
//   }

//   if (searchString.length > string.length) {
//     return false
//   }
//   console.log(searchString)
//   for (let i = 0; i < searchString.length; i += 1) {
//     if (string[i] !== searchString[i]) {
//         return false
//     }
//   }
//   console.log(true)
//   return true
// }

// let str = 'We put comprehension and mastery above all else';
// //startsWith(str, 'We');              // true
// //startsWith(str, 'We put');          // true
// startsWith(str, '');                // true
// // startsWith(str, 'put');             // false

// // let longerString = 'We put comprehension and mastery above all else!';
// // startsWith(str, longerString);      // false