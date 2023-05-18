from django.db import models

# Create your models here.
# logo, img, text, social midia link, address, phone number 

class WebSiteData(models.Model):
    logo = models.ImageField(upload_to='logo_img')
    Hading_img = models.ImageField(upload_to='site_img')
    Hading_text = models.CharField(max_length=200)
    Hading_desc_text = models.CharField(max_length=200)
    About_us_text = models.CharField(max_length=1000)
    facebook = models.URLField()
    linkedin = models.URLField()
    address = models.CharField(max_length=1000)
    Email = models.EmailField()

    def __str__(self) -> str:
        return ('Site Data')


class CardData(models.Model):
    card_img = models.ImageField(upload_to='card_img')
    Product_title = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=200)
    product_hading_img = models.ImageField(upload_to='card_hading')
    product_help_img = models.ImageField(upload_to='card_help')
    product_help_desc = models.CharField(max_length=200)
    product_Features1  = models.CharField(max_length=100, null=True, blank=True)
    product_Features2  = models.CharField(max_length=100, null=True, blank=True)
    product_Features3  = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return (self.Product_title)
   
class ContectForm(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    select_product = models.CharField(max_length=200, choices=[(card.Product_title, card.Product_title) for card in CardData.objects.all()])
    message = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.first_name

