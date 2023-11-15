function balancingParentheses(string) {
  let closes = 0;
  let opens = 0;
  for ( let index = 0; index < string.length; index++) {
    const value = string[index]
    if (value === "(") {
      opens++;
    }
    if (value === ")") {
      closes++;
    }
  }
  return Math.abs(opens - closes);
  // type your code here
}

if (require.main === module) {
  // add your own tests in here
  console.log("Expecting: 0");
  console.log(balancingParentheses('(()())'));

  console.log("");

  console.log("Expecting: 2");
  console.log(balancingParentheses('()))'));

  console.log("");

  console.log("Expecting: 1");
  console.log(balancingParentheses(')'));
}

module.exports = balancingParentheses;

// Please add your pseudocode to this file
/**
 * given a string
 * iterate over the string,
 * tally the total of open and close parentheses,
 * return the absolute value of the difference
 */
// And a written explanation of your solution
/**
 * for this problem, the only thing that matters is the number of parentheses needed to get
 * a working balance, which means we don't care about the type of parenthesis needed,
 * so we can just iterate over the string and return the difference of the two values
 */
