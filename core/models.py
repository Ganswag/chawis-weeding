from ckeditor.fields import RichTextField
from django.db import models


class SiteData(models.Model):
    site_name = models.CharField(
        verbose_name="Nombre del sitio", max_length=50, null=False)
    favicon = models.ImageField(
        upload_to='site/favicon/', verbose_name="Favicon",
        null=True, blank=True)
    logo = models.ImageField(
        upload_to='site/logos/', verbose_name="Logo del sitio",
        null=True, blank=True)
    main_image = models.ImageField(
        upload_to='site/images/', verbose_name="Portada del sitio",
        null=True, blank=True)
    site_description = models.CharField(
        verbose_name="Descripción del sitio",
        max_length=500, null=False)
    google_tag = models.CharField(
        verbose_name="Site Tag Google", max_length=50, null=True, blank=True)
    facebook_pixel = models.CharField(
        verbose_name="Pixel de Facebook", max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Información del Sitio'
        verbose_name_plural = 'Información del Sitio'
        ordering = ['updated_at']


class Status(models.TextChoices):
    NO_CONFIRMED = "sin-confirmar", "Sin Confirmar"
    CONFIRMED = "confirmado", "Confirmado"
    CANCELED = "cancelado", "Cancelado"

class Guest(models.Model):
    guest_name = models.CharField(
        verbose_name="Nombre de invitado", max_length=50, null=False)
    companion_name = models.CharField(
        verbose_name="Nombre del acompañante", max_length=50)
    total_guests = models.IntegerField(
        verbose_name="Total de invitados", max_length=1)
    slug = models.SlugField(
        verbose_name="URI identificador", max_length=75, null=False)
    table = models.CharField(
        verbose_name="Mesa", max_length=50, default=None)
    status = models.CharField(
        verbose_name="Stats", max_length=25, null=False,
        choices=Status.choices,
        default=Status.NO_CONFIRMED
    )

    class Meta:
        verbose_name = 'Invitado'
        verbose_name_plural = 'Invitados'
        ordering = ['guest_name']