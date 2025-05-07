from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# CharField: For short strings (max 200 characters).
# TextField: For the full blog content.
# DateTimeField(auto_now_add=True): Automatically sets the date/time when a post is created.
# __str__: Controls how the object appears in admin and shell (returns the title).


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.post.title} at {self.created_at}"


# post: A foreign key linking each comment to a specific post.
# content: The content of the comment (the text itself).
# created_at: Automatically set when the comment is created.
