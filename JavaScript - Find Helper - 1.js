// Find username Alex

var users = [
  { name: 'Jill' },
  { name: 'Alex' },
  { name: 'Bill' }
];

users.find(function(user) {
  return user.name === 'Alex';
});
