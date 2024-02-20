from django.db import models


# Create your models here.

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    CARRERA_CHOICES = [
        ('', ''),
        ('Tecnologia en Agua y Saneamiento Ambiental', 'Tecnologia en Agua y Saneamiento Ambiental'),
        ('Tecnologia en Desarrollo de Software', 'Tecnologia en Desarrollo de Software'),
        ('Tecnologia en Electromecanica', 'Tecnologia en Electromecanica'),
        ('Tecnologia en Redes y Telecomunicaciones', 'Tecnologia en Redes y Telecomunicaciones'),
    ]

    carrera = models.CharField(
        max_length=100,
        choices=CARRERA_CHOICES,
        default='',
        verbose_name='Carrera'
    )

    MODALIDAD_CHOICES = [
        ('', ''),
        ('PRESENCIAL', 'PRESENCIAL'),
        ('DUAL', 'DUAL'),
    ]

    modalidad = models.CharField(
        max_length=100,
        choices=MODALIDAD_CHOICES,
        default='',
        verbose_name='Modalidad'
    )

    razon_social = models.CharField(max_length=100, verbose_name='Razon Social')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    email = models.EmailField(max_length=100, verbose_name="Correo electronico")
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    telefono = models.IntegerField(verbose_name='Telefono')
    celular = models.IntegerField(verbose_name='Celular')
    INSTITUCION_CHOICES = [
        ('', ''),
        ('PUBLICA', 'PUBLICA'),
        ('PRIVADA', 'PRIVADA'),
        ('ORGANISMO INTERNACIONAL', 'ORGANISMO INTERNACIONAL'),
        ('TERCER SECTOR', 'TERCER SECTOR'),
        ('OTRAS', 'OTRAS'),
    ]
    institucion_recep = models.CharField(max_length=100, choices=INSTITUCION_CHOICES, default='',
                                         verbose_name='Institucion receptora')
    responsable = models.CharField(max_length=100, verbose_name='Responsable')
    nomb_apell = models.CharField(max_length=100, verbose_name='Nombres y Apellidos')
    cedula = models.IntegerField(verbose_name='Cedula')
    PRACTICAS_CHOICES = [
        ('', ''),
        ('LABORAL', 'LABORAL'),
        ('SERVICIO A LA COMUNIDAD', 'SERVICIO A LA COMUNIDAD'),
    ]

    tipo_practica = models.CharField(
        max_length=100,
        choices=PRACTICAS_CHOICES,
        default='',
        verbose_name='Tipo de Practica'
    )
    CAMPO_AM_CHOICES = [
        ('', ''),
        ('EDUCACION', 'EDUCACION'),
        ('ARTES Y HUMANIDADES', 'ARTES Y HUMANIDADES'),
        (
            'CIENCIAS SOCIALES, PERIODISMO, INFORMACION Y DERECHO',
            'CIENCIAS SOCIALES, PERIODISMO, INFORMACION Y DERECHO'),
        ('ADMINISTRACION', 'ADMINISTRACION'),
        ('CIENCIAS NATURALES, MATEMATICAS Y ESTADISTICA', 'CIENCIAS NATURALES, MATEMATICAS Y ESTADISTICA'),
        ('TECNOLOGIAS DE LA INFORMACION Y COMUNICACION (TICS)', 'TECNOLOGIAS DE LA INFORMACION Y COMUNICACION (TICS)'),
        ('INGENIERIA, INDUSTRIA Y CONSTRUCCION', 'INGENIERIA, INDUSTRIA Y CONSTRUCCION'),
        ('AGRICULTURA, SOLVICULTURA, PESCA Y VETERINARIA', 'AGRICULTURA, SOLVICULTURA, PESCA Y VETERINARIA'),
        ('SALUD Y BIENESTAR', 'SALUD Y BIENESTAR'),
        ('SERVICIOS', 'SERVICIOS'),
    ]

    CAMPO_ES_CHOICES = [
        ('', ''),
        ('EDUCACION', 'Educacion'),
        ('ARTES', 'Artes'),
        ('HUMANIDADES', 'Humanidades'),
        ('IDIOMAS', 'Idiomas'),
        ('CIENCIAS SOCIALES Y DEL COMPORTAMIENTO', 'Ciencias Sociales y del Comportamiento'),
        ('PERIODISMO E INFORMACION', 'Periodismo e Informacion'),
        ('DERECHO', 'Derecho'),
        ('EDUCACION COMERCIAL Y ADMINISTRACION', 'Educacion Comercial y Administracion'),
        ('CIENCIAS BIOLOGICAS Y AFINES', 'Ciencias biologicas y afines'),
        ('MEDIO AMBIENTE', 'Medio Ambiente'),
        ('CIENCIAS FISICAS', 'Ciencias fisicas'),
        ('MATEMATICAS Y ESTADISTICA', 'Matematicas y estadistica'),
        ('TECNOLOGIAS DE LA INFORMACION Y DE LA COMUNICACION (TIC)',
         'Tecnologias de la informacion y de la comunicaion'),
        ('INGENIERIA Y PROFESIONES AFINES', 'Ingenieria y profesiones afines'),
        ('INDUSTRIA Y PRODUCCION', 'Industria y produccion'),
        ('ARQUITECTURA Y CONSTRUCCION', 'Arquitectura y construccion'),
        ('SALUD', 'Salud'),
        ('Bienestar', 'Bienestar'),
        ('SERVICIOS PERSONALES', 'Servicios personales'),
        ('SERVICIOS DE PROTECCION', 'Servicios de proteccion'),
        ('SERVICIOS DE SEGURIDAD', 'Servicios de seguridad'),
        ('SERVICIOS DE TRANSPORTE', 'Servicios de transporte'),
    ]

    campo_am = models.CharField(
        max_length=100,
        choices=CAMPO_AM_CHOICES,
        default=' ',
        verbose_name='Campo Amplio'
    )

    campo_es = models.CharField(
        max_length=100,
        choices=CAMPO_ES_CHOICES,
        default=' ',
        verbose_name='Campo Especifico'
    )

    tutor_acad = models.CharField(max_length=100, verbose_name='Tutor academico')

    RELACION_CON_CHOICES = [
        ('Convenio', 'Convenio'),
        ('Proyecto de Investigación', 'Proyecto de Investigación'),
        ('Proyecto de Vinculación', 'Proyecto de Vinculación'),
    ]
    CONFIRMACION_CHOICES = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]
    relacion_con = models.CharField(max_length=100, choices=RELACION_CON_CHOICES, verbose_name='Relacion con')
    confirmacion = models.CharField(max_length=2, choices=CONFIRMACION_CHOICES, verbose_name='Confirmacion')
    codigo = models.CharField(max_length=100, verbose_name='Codigo')
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    comentarioAsignaturas = models.TextField(blank=True, verbose_name='Asignaturas de la malla curricular y temáticas de mayor '
                                                                      'utilidad para el desarrollo de la práctica:')
    #Toca poner esto que solo sea llenado por el funcionario de la EPN
    info_actividades=models.CharField(max_length=100,verbose_name="Información sobre las actividades",default='PARA FUNCIONARIO DE EMPRESA O INSTITUCIÓN')
    areaAsignada = models.CharField(max_length=100, verbose_name='Area Asignada: ')
    reporteI = models.CharField(max_length=100, verbose_name='Inicio DD/MM/AAAA:')
    reporteT = models.CharField(max_length=100, verbose_name='Terminacion DD/MM/AAAA:')

    
    horario_semanal_practicas = models.CharField(max_length=2,verbose_name="Horario Semanal de Prácticas")
    lunes_inicio = models.TimeField(verbose_name="Lunes Inicio")
    lunes_inicio_almuerzo = models.TimeField(verbose_name="Lunes Inicio Almuerzo")
    lunes_fin_almuerzo = models.TimeField(verbose_name="Lunes Fin Almuerzo")
    lunes_fin = models.TimeField(verbose_name="Lunes Fin")
    martes_inicio = models.TimeField(verbose_name="Martes Inicio")
    martes_inicio_almuerzo = models.TimeField(verbose_name="Martes Inicio Almuerzo")
    martes_fin_almuerzo = models.TimeField(verbose_name="Martes Fin Almuerzo")
    martes_fin = models.TimeField(verbose_name="Martes Fin")
    miercoles_inicio = models.TimeField(verbose_name="Miercoles Inicio")
    miercoles_inicio_almuerzo = models.TimeField(verbose_name="Miercoles Inicio Almuerzo")
    miercoles_fin_almuerzo = models.TimeField(verbose_name="Miercoles Fin Almuerzo")
    miercoles_fin = models.TimeField(verbose_name="Miercoles Fin")
    jueves_inicio = models.TimeField(verbose_name="Jueves Inicio")
    jueves_inicio_almuerzo = models.TimeField(verbose_name="Jueves Inicio Almuerzo")
    jueves_fin_almuerzo = models.TimeField(verbose_name="Jueves Fin Almuerzo")
    jueves_fin = models.TimeField(verbose_name="Jueves Fin")
    viernes_inicio = models.TimeField(verbose_name="Viernes Inicio")
    viernes_inicio_almuerzo = models.TimeField(verbose_name="Viernes Inicio Almuerzo")
    viernes_fin_almuerzo = models.TimeField(verbose_name="Viernes Fin Almuerzo")
    viernes_fin = models.TimeField(verbose_name="Viernes Fin")
    sabado_inicio = models.TimeField(verbose_name="Sábado Inicio")
    sabado_inicio_almuerzo = models.TimeField(verbose_name="Sábado Inicio Almuerzo")
    sabado_fin_almuerzo = models.TimeField(verbose_name="Sábado Fin Almuerzo")
    sabado_fin = models.TimeField(verbose_name="Sábado Fin")
    domingo_inicio = models.TimeField(verbose_name="Domingo Inicio")
    domingo_inicio_almuerzo = models.TimeField(verbose_name="Domingo Inicio Almuerzo")
    domingo_fin_almuerzo = models.TimeField(verbose_name="Domingo Fin Almuerzo")
    domingo_fin = models.TimeField(verbose_name="Domingo Fin")
    @property
    def total_horas_semanales(self):
        total_horas = 0
        dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
        for dia in dias:
            hora_inicio = getattr(self, f"{dia}_inicio")
            hora_inicio_almuerzo = getattr(self, f"{dia}_inicio_almuerzo")
            hora_fin_almuerzo = getattr(self, f"{dia}_fin_almuerzo")
            hora_fin = getattr(self, f"{dia}_fin")
            if hora_inicio and hora_inicio_almuerzo and hora_fin_almuerzo and hora_fin:
                horas_trabjo = (hora_inicio_almuerzo - hora_inicio).total_seconds() / 3600
                horas_almuerzo = (hora_fin_almuerzo - hora_inicio_almuerzo).total_seconds() / 3600
                horas_trabajadas_despues_almuerzo = (hora_fin - hora_fin_almuerzo).total_seconds() / 3600
                total_horas += horas_trabjo + horas_trabajadas_despues_almuerzo - horas_almuerzo
        
        return total_horas
    observaciones_horario = models.CharField(max_length=100, verbose_name="Observaciones",default="Aspectos del horario que considere importante")
    pasantias_pagadas = models.CharField(max_length=2, choices=CONFIRMACION_CHOICES,verbose_name="Pasantías pagadas")
    valor_canc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Valor cancelado")
    principales_actividades = models.CharField(max_length=100, verbose_name="Principales actividades desarrolladas")
    habilidades_adq = models.CharField(max_length=100, verbose_name="Habilidades, destrezas o conocimientos adquiridos")
    seguimiento_tutor = models.CharField(max_length=2, choices=CONFIRMACION_CHOICES, verbose_name="¿El tutor académico de prácticas preprofesionales de la EPN realizó el seguimiento de la práctica preprofesional?")
    observaciones_segui = models.CharField(max_length=100, verbose_name="Observaciones sobre el seguimiento")
    EVALUACION_CHOICES = [
    ('excelente', 'Excelente'),
    ('muy_buena', 'Muy Buena'),
    ('satisfactoria', 'Satisfactoria'),
    ('deficiente', 'Deficiente')
    ]
    asistencia = models.CharField(
        max_length=20,
        choices=EVALUACION_CHOICES,
        verbose_name='Asistencia y Puntualidad'
    )
    desempeno = models.CharField(
        max_length=20,
        choices=EVALUACION_CHOICES,
        verbose_name='Desempeño'
    )
    motivacion = models.CharField(
        max_length=20,
        choices=EVALUACION_CHOICES,
        verbose_name='Motivación'
    )
    conocimientos_d = models.CharField(
        max_length=20,
        choices=EVALUACION_CHOICES,
        verbose_name='Conocimientos, Destrezas y Valores'
    )
    eva_practicas=models.CharField(max_length=100,verbose_name="Evaluación de la práctica preprofesional",default="PARA TUTOR ACADÉMICO DE PRACTICAS PREPROFESIONALES")
    novedades_reportadas = models.CharField(max_length=100,verbose_name="Novedades reportadas o encontradas en el desarrollo de la práctica:")
    
    ev_recomienda = models.CharField(max_length=100,verbose_name="¿Recomienda que otros estudiantes realicen sus prácticas preprofesionales en esta Institución o Empresa?",choices=CONFIRMACION_CHOICES)
    ev_r_obs=models.CharField(max_length=100,verbose_name="Observaciones")
    ev_aportaron = models.BooleanField(max_length=100,verbose_name="En general, ¿las prácticas preprofesionales realizadas por el estudiante aportaron a su formación profesional, es decir aportaron a cumplir con su perfil de egreso?",choices=CONFIRMACION_CHOICES)
    ev_a_obs=models.CharField(max_length=100,verbose_name="Observaciones")
    ev_aprobacion = models.CharField(max_length=100,verbose_name="¿Recomienda la aprobación de las prácticas preprofesionales del estudiante?",choices=CONFIRMACION_CHOICES)
    ev_b_obs=models.CharField(max_length=100,verbose_name="Observaciones")
    
    rec_com=models.CharField(max_length=10,verbose_name="Recomendación de la comisión de prácticas preprofesionales ",default=" PARA CPP")
    ap_cpp=models.CharField(max_length=100,verbose_name="La Comisión de Prácticas Preprofesionales, una vez revisada, analizada y validada la información reportada por el estudiante, ¿avala la aprobación de las horas de prácticas preprofesionales indicadas en este informe?",choices=CONFIRMACION_CHOICES, default='')
    obs_cpp=models.CharField(max_length=100,verbose_name="Observaciones", default='')
    
    
    def __str__(self):
        return str(self.cedula)
