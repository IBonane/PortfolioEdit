from django.db import models


# Create your models here.

class UserInfo(models.Model):
    names = models.CharField(max_length=255, verbose_name="Nom et prenom *", primary_key=True)
    competenceDomain = models.CharField(max_length=400, verbose_name="Domaine de compétence *")
    mail = models.EmailField(verbose_name="Adresse mail *")
    phone = models.CharField(max_length=20, verbose_name="numéro de téléphone *")
    imageProfile = models.ImageField(verbose_name="image de profile",  blank=True)
    firstParagraph = models.TextField(verbose_name="Mettez une petite phrase d'accroche",  blank=True)
    wordsOfFirstParagraph = models.TextField(verbose_name="Citez quelques outils ou logiciels que vous maitriser", blank=True)
    imageParagraph = models.ImageField(verbose_name="image de la phrase d'accroche", blank=True)

    def __str__(self):
        return self.names


class Competence(models.Model):
    author = models.ForeignKey(UserInfo, verbose_name="Auteur", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Titre de la compétence")
    year = models.DateField(verbose_name="Année")
    explain = models.TextField(verbose_name="Détails")

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre de la compétence")
    year = models.DateField(verbose_name="Année")
    explain = models.TextField(verbose_name="Détails")

    def __str__(self):
        return self.title


class Formation(models.Model):
    formationFields = models.CharField(max_length=255, verbose_name="Nom de la formation et diplome préparé ou obtenu")
    formationYear = models.DateField(verbose_name="Année")
    schoolName = models.CharField(max_length=255)
    countryAndCity = models.CharField(max_length=255)
    explain = models.TextField(verbose_name="Détails", blank=True)

    def __str__(self):
        return self.formationFields
