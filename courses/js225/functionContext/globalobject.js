// let turk = {
//   firstName: 'Christopher',
//   lastName: 'Turk',
//   occupation: 'Surgeon',
//   getDescription() {
//         return this.firstName + ' ' + this.lastName + ' is a ' + this.occupation + '.';
//   },
// };

// // function logReturnVal(func,obj) {
// //   let returnVal = func.call(obj);
// //   console.log(returnVal);
// // }


// let getTurkDescription = turk.getDescription.bind(turk);

//   console.log(getTurkDescription())
//   //console.log(turk.getDescription())
  //console.log(turk)
//logReturnVal(turk.getDescription());

// let TESgames = {
//   titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
//   seriesTitle: 'The Elder Scrolls',
  
//   listGames() {
   
//     this.titles.forEach(function(title) {
//       console.log(this.seriesTitle + ' ' + title);
//     },this);
//   }
// };

// TESgames.listGames();


// let foo = {
//   a: 0,
//   incrementA() {
//     let increment =function() {
//       this.a += 1;
//     }.bind(this);
    
//     increment();
//     increment()

//   }
// };

// console.log(foo)
// foo.incrementA()
// console.log(foo)