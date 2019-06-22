var post = { id: 4, title: 'New Post' };
var comments = [
  { postId: 4, content: 'awesome post' },
  { postId: 3, content: 'it was ok' },
  { postId: 4, content: 'neat' },
]

function commentsForPosts(post, comments) {
	return comments.filter(function(comment) {
    return comment.postId === post.id;
  });
}

commentsForPosts(post, comments);
