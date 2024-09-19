from django.db import models



class Villa(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey("owner.Owner", on_delete=models.CASCADE, related_name = 'owner')
    is_currently_rented = models.BooleanField(default=False)
    city = models.CharField(max_length=255)
    address = models.TextField()
    features = models.TextField()
    price  = models.PositiveBigIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='villa_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    villa = models.ForeignKey("Villa", on_delete=models.CASCADE, related_name='villa')
    user = models.ForeignKey("user.Customer", on_delete=models.CASCADE, related_name='costumer')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment

class Rate(models.Model):
    villa = models.ForeignKey("Villa", on_delete=models.CASCADE, related_name='Rated_villad')
    user = models.ForeignKey("user.Customer", on_delete=models.CASCADE, related_name='rater')
    rate = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rate}'


class Rent(models.Model):
    villa = models.ForeignKey("Villa", on_delete=models.CASCADE, related_name='rented_villa')
    user = models.ForeignKey("user.Customer", on_delete=models.CASCADE, related_name='renter')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.villa}, {self.user}"

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title




