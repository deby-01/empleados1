from django.db import models

class Perfil(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    COMUNAS_CHOICES = [
        ('1', 'Santiago'),
        ('2', 'Providencia'),
        ('3', 'Las Condes'),
        ('4', 'Maipu'),
        ('5', 'Cerrillos'),
        ('6', 'Pudahuel'),
        ('7', 'San Bernardo'),
        ('8', 'La Cisterna'),
        ('9', 'La Florida'),
        ('10', 'Cerro navia'),
        ('11', 'Quilicura'),
        ('12', 'Ñuñoa'),
        ('13', 'La Florida'),
        ('14', 'Recoleta'),
        ('15', 'Conchali'),
        ('16', 'Independencia'),
        ('17', 'Macul'),
        ('18', 'La Reina'),
        ('19', 'Vitacura'),
        ('20', 'Lo Barnechea'),
        ('21', 'Peñalolen'),
        ('22', 'Puente Alto'),
        ('23', 'Pirque'),
        ('24', 'La Pintana'),
        ('25', 'Huechuraba'),
        ('26', 'Renca'),
        ('27', 'Quinta Normal'),
        ('28', 'Estacion Central'),
        ('29', 'San Miguel'),
        ('30', 'El Bosque'),
        ('31', 'Padre Hurtado'),
        ('32', 'Pedro Aguirre Cerda'),
        ('33', 'Lo Espejo'),
        ('34', 'Peñaflor'),
        ('35', 'Talagante'),
        ('36', 'Melipilla'),
        ('37', 'Lo Prado'),
        ('38', 'El Monte'),
        ('39', 'Buin'),
        ('40', 'San Joaquin'),
        ('41', 'San Ramon'),
        ('42', 'No Registrada'),  
    ]

    AREA_CHOICES = [
        ('TI', 'Tecnología de la Información'),
        ('MA', 'Marketing'),
        ('FI', 'Finanzas'),
        ('RH', 'Recursos Humanos'),
        ('VT', 'Ventas'),
        ('PR', 'Produccion Operacionales'),
        ('LO', 'Logistica'),
        ('AD', 'Recursos Administrativos'),
        ('FI', 'Finanzas'),
        ('PN', 'Personal Externo'),
        ('OT', 'Agregar Otro'),
    ]

    id=models.AutoField(primary_key=True)
    foto = models.ImageField(null=True, upload_to='foto')
    nombre_user=models.CharField(max_length=15)
    nombres= models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    rut= models.CharField(unique=True, max_length=20)
    edad= models.PositiveIntegerField()
    fecha_nac=models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    correo = models.EmailField()
    comuna= models.CharField(max_length=20, choices=COMUNAS_CHOICES)
    direccion= models.CharField(max_length=100)
    telefono= models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(null=True)
    area= models.CharField(max_length=20, choices=AREA_CHOICES)
    cargo= models.CharField(max_length=50)
    sueldo_base= models.PositiveIntegerField(null=True, blank=True)
                            
