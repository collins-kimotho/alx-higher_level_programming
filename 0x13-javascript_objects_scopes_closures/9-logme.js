#!/usr/bin/node

let numArgs = 0; // initialize the count

exports.logMe = function (item) {
  console.log(`${numArgs} : ${item}`);
  numArgs++; // increment the count
};
