from django.db import models

class Usuario(models.Model):

    # -------- CHOICES --------
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    DEPARTAMENTO_CHOICES = [
        ('CALDAS', 'Caldas'),
        ('ANTIOQUIA', 'Antioquia'),
    ]

    CARGO_CHOICES = [
        ('ASESOR', 'Asesor'),
    ]

    # -------- CAMPOS --------
    clasificacion = models.CharField(max_length=100)
    login = models.CharField(max_length=100)

    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='ACTIVO'
    )

    identificacion_usuario = models.BigIntegerField()
    fecha_ingreso = models.DateField()
    fecha_retiro = models.DateField()

    vicepresidente = models.CharField(max_length=100)
    gerencia = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    canal = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100)
    nro_contrato = models.CharField(max_length=100)

    subcanal = models.CharField(max_length=100)
    punto = models.CharField(max_length=100)
    cc_supervisor = models.CharField(max_length=100)

    lider_etb = models.CharField(max_length=100)

    departamento = models.CharField(
        max_length=20,
        choices=DEPARTAMENTO_CHOICES
    )

    ciudad = models.CharField(max_length=100)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()

    celular = models.CharField(max_length=20)
    eps = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    sexo = models.CharField(max_length=20)

    cargo = models.CharField(
        max_length=20,
        choices=CARGO_CHOICES,
        default='ASESOR'
    )

    perfil_portal_suma = models.CharField(max_length=100)

    restriccion = models.CharField(max_length=100)
    causa_restriccion = models.CharField(max_length=200)
    id_fibra = models.CharField(max_length=100)

    fija = models.IntegerField()
    movil = models.IntegerField()
    id_cobre = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.identificacion_usuario}"
