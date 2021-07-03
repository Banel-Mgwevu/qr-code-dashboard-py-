from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class stockitems(models.Model):
    id=models.AutoField(primary_key=True)
    stock_info=models.CharField(max_length=500, null=False)
    brand=models.CharField(max_length=500, null=False)
    barcode=models.IntegerField(blank=True, null=False)
    product_name=models.CharField(max_length=500, null=False)
    qr_code = models.ImageField(upload_to='qr_codeS', blank=False)
    quantity=models.IntegerField(blank=True, null=False)
    currentDate=models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return str(self.stock_info)

    def save(self, *args, **kwargs):
        qrcode_img =qrcode.make(self.stock_info)
        canvas =Image.new('RGB',(290,290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname =f'qr_code-{self.stock_info}.png'
        buffer =BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close
        super().save(*args, **kwargs)
