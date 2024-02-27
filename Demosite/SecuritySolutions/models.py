from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model):
    #Fields
    #TO-DO-> product name and description should be separate
    product_name = models.CharField(max_length=20, help_text='Product Description')
    product_image=models.ImageField(null=True)
    help_text="Add or remove a product"
    # …

    # Metadata
    class Meta:
        ordering = ['-product_name',
                    
                    ]
        verbose_name_plural = "Products"

    # Methods
   # def get_absolute_url(self):
    #    """Returns the URL to access a particular instance of MyModelName."""
   #     return reverse('Product-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.product_name