# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError


class Address(models.Model):
    STATE_CHOICES = (
        (None, '(Seleccione)'),
        (1, 'Buenos Aires'),
        (2, 'Buenos Aires-GBA'),
        (3, 'Capital Federal'),
        (4, 'Catamarca'),
        (5, 'Chaco'),
        (6, 'Chubut'),
        (7, 'Córdoba'),
        (8, 'Corrientes'),
        (9, 'Entre Ríos'),
        (10, 'Formosa'),
        (11, 'Jujuy'),
        (12, 'La Pampa'),
        (13, 'La Rioja'),
        (14, 'Mendoza'),
        (15, 'Misiones'),
        (16, 'Neuquén'),
        (17, 'Río Negro'),
        (18, 'Salta'),
        (19, 'San Juan'),
        (20, 'San Luis'),
        (21, 'Santa Cruz'),
        (22, 'Santa Fe'),
        (23, 'Santiago del Estero'),
        (24, 'Tierra del Fuego'),
        (25, 'Tucumán')
    )
    address = models.CharField(
        "Direccion", max_length=50, blank=False, null=False)
    city = models.CharField("Ciudad", max_length=50, blank=False, null=False)
    state = models.IntegerField(
        "Provincia", choices=STATE_CHOICES, blank=False, null=False)
    country = models.CharField("Pais", max_length=50, blank=False, null=False)
    zip_code = models.IntegerField("Cod Postal", blank=False, null=False)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "{}".format(self.address)

    def get_address(self):
        return self.address


class User(models.Model):

    GENDER_CHOICES = (
        ("M", 'Hombre'),
        ("F", 'Mujer'),  # code --> (DB, label)
    )

    first_name = models.CharField(
        "Nombre", max_length=50, blank=False, null=False)
    last_name = models.CharField(
        "Apellido", max_length=50, blank=False, null=False)
    gender = models.CharField(
        "Genero",
        max_length=2,
        choices=GENDER_CHOICES,
        default="M",
        blank=False,
        null=False,
        help_text='Solamente existen 2 géneros',
    )
    email = models.EmailField(blank=False, null=False,
                              help_text="Ejemplo: usuario@mail.com")
    phone = models.IntegerField(blank=True, null=True)
    active = models.BooleanField("Activo", default=False)
    fecha_alta = models.DateTimeField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True, null=False, blank=False)
    fecha_modificacion = models.DateTimeField(
        auto_now=True, editable=False, null=False, blank=False)
    # auto_now_add=False --> exclusivo con auto_now
    address = models.ForeignKey(Address)  # un User tiene una sola direccion

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

    def clean_first_name(self):
        name = self.first_name

        if len(name) < 2:
            raise ValidationError("Ingrese un nombre con mas de 2 caracteres")
        else:
            self.first_name = name.title()

    def clean_last_name(self):
        name = self.last_name

        if len(name) < 2:
            raise ValidationError(
                "Ingrese un apellido con mas de 2 caracteres")
        else:
            self.last_name = name.title()

    def clean_email(self):
        email = self.email

        if email == '':
            raise ValidationError("Ingrese un email")
        else:
            base, prov = email.split("@")
        # dom, ext = prov.split(".")

        if not prov.lower() == "gmail.com":
            raise ValidationError("Por favor utilice una cuenta de Gmail")
        else:
            self.email = email.lower()

    def clean(self):
        self.clean_last_name()
        self.clean_first_name()
        self.clean_email()

    def total_social_medias(self):
        total = self.media_set.all().count()
        # total = Media.objects.filter(user_id=self.id).count()
        return total

    total_social_medias.short_description = '# Redes'

    #  Nombre de la columna en el Admin

    def sex(self):
        if self.gender == "M":
            return "H"
        return "F"


class Media(models.Model):
    name = models.CharField(max_length=50, blank=False,
                            null=False, help_text='Ej: Facebook Cuenta Oficial')
    url = models.URLField(blank=False, null=False,
                          help_text='Ej: https://es-la.facebook.com/leomessi/')
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.name
