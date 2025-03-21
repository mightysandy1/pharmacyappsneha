from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    license_no = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('comp_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return self.name

class Medicine(models.Model):
    company = models.ForeignKey('yolo_site.Company', related_name='company', on_delete=models.CASCADE)
    class Type(models.TextChoices):
        mg = "mg"
        mcg = "mcg"
    name = models.CharField(max_length=128)
    salt_name = models.CharField(max_length=256)
    salt_quantity = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=128, choices=Type.choices, blank=True, null=True)
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    shelf_number = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    pack_quantity = models.PositiveIntegerField()
    # in the form of 10 X 3 for a pack of 3 strips containing 10 tabs each
    updated_on = models.DateTimeField(auto_now=True)

    def update_stock(self, quantity):
        print("Updating stock")
        self.stock -= quantity
        self.save()

    def get_absolute_url(self):
        return reverse('med_detail', kwargs={'pk':self.pk})
    
    def price_per_tablet(self):
        return self.selling_price / self.pack_quantity

    def __str__(self):
        if not self.salt_quantity:
            return self.name
        elif self.salt_quantity and self.unit:
            return str(self.name) + " " + str(self.salt_quantity) + " " + str(self.unit)
        else:
            return str(self.name) + " " + str(self.salt_quantity)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    name = models.CharField(max_length=128, blank=True)
    job_title = models.CharField(max_length=128, blank=True)
    contact_no = models.CharField(max_length=128, blank=True)
    bank_account = models.CharField(max_length=256, blank=True)
    salary = models.FloatField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('emp_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return self.user.username

class BillDetails(models.Model):
    generated_by = models.ForeignKey('auth.User', editable=False, related_name='detail_billing_employee', on_delete=models.CASCADE)
    customer = models.CharField(max_length=128)
    items = models.ManyToManyField(Medicine, through='BillItems')
    created_on = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        
        bitems = BillItems.objects.filter(bill=self).prefetch_related('med_id')

        total = 0

        for item in bitems:
            total += item.med_id.selling_price * item.quantity / item.med_id.pack_quantity

        return total

    def get_absolute_url(self):
        return reverse('bill_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return 'To '+ str(self.customer) + ' From ' + str(self.generated_by.username)

class BillItems(models.Model):
    bill = models.ForeignKey(BillDetails, on_delete=models.CASCADE)
    med_id = models.ForeignKey(Medicine, related_name='med_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def update_stock(self):
        self.med_id.update_stock(self.quantity)

    def amt(self):
        return self.med_id.selling_price * self.quantity / self.med_id.pack_quantity

class Bill(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
