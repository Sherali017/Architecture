from django.db import models

class SpecializationModel(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'specialization'
        verbose_name_plural = 'specializations'




class projectsModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

class TeamModel(models.Model):
    name = models.CharField(max_length=75)
    job = models.CharField(max_length=50)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'

class ClientsModel(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'




class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    post_by = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'

class PartnerModel(models.Model):
    logo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = 'partner'
        verbose_name_plural = 'partners'



