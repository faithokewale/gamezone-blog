from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title.")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(help_text="Write your main blog article here.")
    
    # BOTH OPTIONS: You can now use either or both!
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text="Upload an image from your computer.")
    featured_image_url = models.URLField(blank=True, null=True, help_text="OR paste an image URL link from the web.")
    
    video_url = models.URLField(blank=True, null=True, help_text="Paste a YouTube embed link here if the post has a video.")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Smart helper function to figure out which image to use
    @property
    def get_image(self):
        if self.featured_image:
            return self.featured_image.url
        elif self.featured_image_url:
            return self.featured_image_url
        return None

    def __str__(self):
        return self.title