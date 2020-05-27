from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	url = models.TextField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	votes_total = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE) # id of the user, if user is deleted -> product deleted

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')


class Tag(models.Model):
	name = models.CharField(max_length=255)
	products = models.ManyToManyField(Product)

	def __str__(self):
		return(self.name)

# class Vote(models.Model):
# 	productID = models.ForeignKey(Product,on_delete=models.CASCADE)
#     userID = models.ForeignKey(User,on_delete=models.CASCADE)