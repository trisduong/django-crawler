from django.db import models


class awesome_job(models.Model):
    title = models.CharField(max_length=400)
    detail = models.TextField(max_length=None)

    def get_absolute_url(self):
        return "/awesomejob/{}".format(self.id)


class fami_post(models.Model):
    title = models.CharField(max_length=400)
    link = models.CharField(max_length=400)


class python_fami_post(models.Model):
    title = models.CharField(max_length=400)
    link = models.CharField(max_length=400)


class sys_fami_post(models.Model):
    title = models.CharField(max_length=400)
    link = models.CharField(max_length=400)


class com_fami_post(models.Model):
    title = models.CharField(max_length=400)
    link = models.CharField(max_length=400)
