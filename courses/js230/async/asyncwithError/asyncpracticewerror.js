// function flakyService() {
//     return new Promise( (resolve, reject) => {
//         if (Math.random() > 0.5) {
//             resolve("Operation successful");
//         }
//         else {
//             reject ("Operation failed");
//         }
//     })
// }

// //flakyService().then(console.log).catch(console.log)

// async function callFlaky() {

//     try {
//         let data = await flakyService()
//         console.log(data)
//     } catch (err) {
//         console.log(err)
//     }
// }

// callFlaky()


// function operation() {
//   return new Promise((resolve) => {
//     console.log("Operation started");
//     setTimeout(() => {
//       resolve("Operation complete");
//     }, 1000);
//   });
// }

// async function callOperation() {
//     try {
//         let data = await operation()
//         console.log(data)
//     } catch (err) {
//         console.log(err)
//     } finally {
//         console.log("Cleaning up resources...")
//     }
// }

// // operation()
// //   .then(console.log)
// //   // Logs: Operation complete
// //   .finally(() => {
// //     console.log("Cleaning up resources...");
// //     // Always logs after operation completion
// //   });

// callOperation()


// async function retryOperation(operationFunc) {
//     let attempts = 0;
    
//     async function attempt() {

//         try {
//             let data = await operationFunc
//             console.log(data)
//         } catch (err) {
//             if (attempts < 2) {
//                 attempts += 1
//                 console.log(`Retry attempt ${attempts}`)
//                 return attempt()
//             } else {
//                 throw err
//             }
//         }
       
//     }
//     try {
//         await attempt()
//     } catch {
//         console.error("Operation failed")
//     }
// }


// function retryOperation(operationFunc) {
//   let attempts = 0;

//   function attempt() {
//     return operationFunc().catch((err) => {
//       if (attempts < 2) {
//         attempts++;
//         console.log(`Retry attempt #${attempts}`);
//         return attempt();
//       } else {
//         throw err;
//       }
//     });
//   }

//   return attempt().catch(() => console.error("Operation failed"));
// }

// async function asyncLoadData() {
//     try {
//         const result = await new Promise((resolve, reject) => {
//             setTimeout( () => {
//                         if (Math.random() > 0.5) {
//           resolve("Data loaded");
//         } else {
//           reject("Network error");
//         }
//             },1000)
//         });
//         return result
//     } catch {
//         return "Using cached data"
//     } 
// }

// async function processData() {
//     console.log(await asyncLoadData())
// }
// processData()