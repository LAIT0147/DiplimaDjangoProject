from django.db import models
from uuid import uuid4
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from os import path
from django.core.exceptions import ValidationError


class Programs(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    desc = models.TextField(max_length=500)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)


    def __str__(self):
        return f'{self.name} on position: {self.position}; Visible: {self.is_visible}'


    class Meta:
        ordering = ('position',)


class Classes(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/classes', filename)

    name = models.CharField(max_length=40, unique=True, db_index=True)
    desc = models.TextField(max_length=300)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=get_file_name)
    photo_thrumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(730, 310)], format='JPEG',
                                      options={'quality': 60})
    def __str__(self):
        return f'{self.name} on position: {self.position}; Visible:{self.is_visible}'


    class Meta:
        ordering = ('position',)


class Types(models.Model):
    name = models.CharField(max_length=70, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'Training: {self.name} on position {self.position}; Visible:{self.is_visible}'


class Trainer(models.Model):
    def get_file_name_trainer(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/trainers', filename)

    name = models.CharField(max_length=50, unique=True, db_index=True, null=True)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    desc = models.TextField(max_length=200, null=True)
    expert = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name_trainer, default='null')
    photo_thrumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(200, 160)], format='JPEG',
                                          options={'quality': 60})
    is_visible = models.BooleanField(default=True)
    facebook = models.CharField(max_length=200, default='-')
    twitter = models.CharField(max_length=200, default='-')
    linkedin = models.CharField(max_length=200, default='-')

    def __str__(self):
        return f'{self.name} : {self.type}'


class Schedule(models.Model):
    class_name = models.CharField(max_length=20, unique=True, db_index=True, null=True)
    position = models.PositiveSmallIntegerField(unique=True, null=True)
    monday = models.CharField(max_length=15, default='-', null=True)
    tuesday = models.CharField(max_length=15, default='-', null=True)
    wednesday = models.CharField(max_length=15, default='-', null=True)
    thursday = models.CharField(max_length=15, default='-', null=True)
    friday = models.CharField(max_length=15, default='-', null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default='-')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'Training: {self.class_name}; Trainer: {self.trainer}'

    class Meta:
        ordering = ('position', )


class ContactUs(models.Model):
    def validate_email(self):
        if "@" in self:
            return self
        else:
            raise ValidationError('Incorrect email')

    name = models.CharField(max_length=30, db_index=True)
    email = models.CharField(max_length=50, validators=[validate_email])
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=500, blank=True)

    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.name} with subject {self.subject}. Note: {self.message[:20]}...'
