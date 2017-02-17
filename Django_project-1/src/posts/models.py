from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s"%(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id,filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Title = models.CharField(max_length = 120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = upload_location,
                              null = True,
                              blank= True,
                              height_field="height_field",
                              width_field="width_field",)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    Content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    Timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = PostManager()

    def __unicode__(self):   # python 2.7
        return self.Title

    def __str__(self):   # python 3
        return self.Title

    def get_absolute_url(self):
        return reverse("posts:post_detail",kwargs={'slug':self.slug})
        # return "/post/%s/"%(self.id)

    class Meta:
        ordering = ["-Updated"]


def create_slug(instance, new_slug = None):
    slug = slugify(instance.Title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(work_slug,qs.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, sender = Post)
