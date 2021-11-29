from django.db import models
#
# class CategoryModel(models.Model):
#     title = models.CharField(max_length=100,default=None )
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'


class AuthorModel(models.Model):
    title = models.CharField(max_length=200, default=True)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class PostTagModel(models.Model):
    title = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(PostTagModel, related_name='posts')
    # category = models.ForeignKey(CategoryModel, default=None, on_delete=models.CASCADE, related_name='posts')

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField( blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'