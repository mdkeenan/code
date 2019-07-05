// Find the account with a balance of 12 and assign it to the variable 'account'.

var balance;

var accounts = [
  { balance: -10 },
  { balance: 12 },
  { balance: 0 }
];

var account = accounts.find(x => x.balance === 12);
