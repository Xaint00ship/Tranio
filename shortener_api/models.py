from django.db import models
from datetime import datetime
from hashlib import sha256
import base64



class Urls(models.Model):

    url = models.URLField(unique=True)
    hash_url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)


    def set_url(self, url):
        try:
            self.url = url
            return self.save()
        except:
            return self.hash_url


    def clicked(self):
        Clicks().set_click(self.hash_url)
        self.clicks += 1
        self.save()
        return


    def save(self):
        if not self.id:
            self.hash_url = (base64.b64encode(
                sha256(self.url.encode()).hexdigest()[:10]
                .encode())[:6]).decode('ascii') # Хеш-функция для ссылки(URL->SHA256[:10]->Base64[:6])
        super().save()
        return self.hash_url

class Clicks(models.Model):

    hash_url = models.URLField()
    date = models.DateField(null=True)


    def set_click(self, hash_url):
        if not self.id:
            self.hash_url = hash_url
            self.date = datetime.today().strftime('%Y-%m-%d')
        super().save()
        return self.hash_url
