from django.db import models

# Define possible statuses for the models using TextChoices.
class Status(models.TextChoices):
    DRAFT = "DF", "Draft"
    PUBLISHED = "PB", "Published"

# Custom model manager to retrieve only published items.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Status.PUBLISHED)

# About model
class About(models.Model):
    body = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True,default='portfolio_images/default.jpeg')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Manager to return only published items
    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.body

# Education model
class Education(models.Model):
    title = models.CharField(max_length=30)
    date = models.CharField(max_length=50, blank=True)
    body = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Manager to return only published items
    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.title

# Experience model
class Experience(models.Model):
    title = models.CharField(max_length=30)
    date = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Manager to return only published items
    
    class Meta:
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.title

# Service model (capitalize class name)
class Service(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Manager to return only published items

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Service"
