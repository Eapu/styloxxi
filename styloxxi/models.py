from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):

	def get_queryset(self):
		return super(PublishedManager, self).get_queryset()

class Servicio(models.Model):

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	image = models.FileField(null=True, blank=True)
	image2 = models.FileField(null=True, blank=True)
	image3 = models.FileField(null=True, blank=True)
	video = models.FileField(null=True, blank=True)
	body = models.TextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('', args=[self.publish.year, 
			self.publish.strftime('%m'),
			self.publish.strftime('%d'),
			self.slug])


class Producto(models.Model):
	title = models.CharField(max_length=250,null=True, blank=True)
	servicio = models.ManyToManyField(Servicio, blank=True, related_name="productos")
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	image = models.FileField(null=True, blank=True)
	video = models.FileField(null=True, blank=True)
	body = models.TextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	published = PublishedManager()
	objects = models.Manager()
	
	class Meta:
		ordering = ('-publish', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('', args=[self.publish.year, 
			self.publish.strftime('%m'),
			self.publish.strftime('%d'),
			self.slug])

class Video(models.Model):

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish")
	video = models.FileField(null=True, blank=True)
	body = models.TextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('', args=[self.publish.year, 
			self.publish.strftime('%m'),
			self.publish.strftime('%d'),
			self.slug])
	
class Logo(models.Model):

	company_name = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish",null=True, blank=True)
	logo = models.FileField(null=True, blank=True)
	title = models.CharField(max_length=250,null=True, blank=True)
	video = models.FileField(null=True, blank=True)
	body = models.TextField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('', args=[self.publish.year, 
			self.publish.strftime('%m'),
			self.publish.strftime('%d'),
			self.slug])
		

class Photocall(models.Model):

	title = models.CharField(max_length=250,null=True, blank=True)
	slug = models.SlugField(max_length=250, unique_for_date="publish",null=True, blank=True)
	image_1 = models.FileField(null=True, blank=True)
	image_2 = models.FileField(null=True, blank=True)
	image_3 = models.FileField(null=True, blank=True)
	image_4 = models.FileField(null=True, blank=True)
	publish = models.DateTimeField(default=timezone.now)
	published = PublishedManager()
	objects = models.Manager()
	class Meta:
		ordering = ('-publish', )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('', args=[self.publish.year, 
			self.publish.strftime('%m'),
			self.publish.strftime('%d'),
			self.slug])
		


