from django.conf import settings
from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField('标题', max_length=200, unique=True)
    content = models.TextField('内容')
    edit_status = models.IntegerField('编写状态', default=0)
    comment_status = models.IntegerField('评论状态', default=1)
    likes = models.PositiveIntegerField('点赞量', default=0)
    collection = models.PositiveIntegerField('收藏量', default=0)
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(
        'Account',
        verbose_name='作者',
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField('Tag',verbose_name='标签集合', blank=True)

    class Meta:
        db_table = 'blog'
        