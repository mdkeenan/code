// Find username Alex (only finds the first record)

var users = [
  { name: 'Jill' },
  { name: 'Alex' },
  { name: 'Bill' },
  { name: 'Alex' }
];

users.find(function(user) {
  return user.name === 'Alex';
});
