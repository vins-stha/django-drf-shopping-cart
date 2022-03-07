from django.db import models

def upload_to(instance,filename):
    print('filname==>', filename, 'instance ==', instance)
    return 'cats/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(blank=False, null=False,max_length=200, default="new_cat")
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]



"""
Model class for Product
"""
class Product(models.Model):

    colors = (
        ('red','Red'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('white', 'White'),
        ('grey', 'Silver')
    )

    inStock = (("yes","Yes"), ("no", "No"),("limited","Limited (< 10 )"))
    title = models.CharField(blank=False,max_length=200)
    description = models.TextField(blank=True,max_length=1000)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    cat_id = models.ForeignKey(Category,on_delete=models.PROTECT, default=1)
    colors = models.CharField(max_length=20, choices=colors, default="black")
    available = models.IntegerField(default=0)
    inStock = models.CharField(default="No",choices=inStock, max_length=20)
    added_on = models.DateField(auto_now=True)
    barcode = models.IntegerField(blank=False, default=1234567890)
    product_image = models.ImageField("Product_image", upload_to=upload_to, default="empty_cart.png")

    def __str__(self):
        if not self.title:
            return "No title"
        return str(self.title)

    class Meta:
        ordering = ("-title","price","-added_on")


"""
Customers Model 
"""
class Customer(models.Model):
    fname = models.CharField(max_length=100,blank=False,null=False, default="fname_")
    lname = models.CharField(max_length=100,blank=False,null=False, default="Lname_")

    # avatar = models.ImageField("Avatar", upload_to="avatars/", default="empty_cart.png")


    def __str__(self):
        return self.fname


"""
Cart Model 
"""
class Cart(models.Model):
    pass
