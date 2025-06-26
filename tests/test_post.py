from lib.post import Post

def test_post_initialises_with_correct_attributes(db_connection):
    post = Post("Post Title 1", "Content for post 1", 150, 1)
    assert isinstance(post, Post)
    assert post.title == "Post Title 1"
    assert post.content == "Content for post 1"
    assert post.views == 150
    assert post.account_id == 1 


def test_post_repr_method_formats_nicely():
    post = Post("Post Title 1", "Content for post 1", 150, 1)
    assert str(post) == "Post(Post Title 1, Content for post 1, 150, 1)"


def test_posts_are_equal():
    post_1 = Post("Post Title 1", "Content for post 1", 150, 1)
    post_2 = Post("Post Title 1", "Content for post 1", 150, 1)
    assert post_1 == post_2