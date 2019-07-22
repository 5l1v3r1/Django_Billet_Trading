from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, rank, squadron, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not rank:
            raise ValueError("Users must have an Rank, Example: E-1")
        if not squadron:
            raise ValueError("Users must have an squadron")

        user = self.model(
                email=self.normalize_email(email),
                username=username,
                rank=rank,
                squadron=squadron,                
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, rank, squadron, password):
        user  = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
                rank=rank,                
                squadron=squadron,                
                )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    rank_options = [
        ('E-1','E-1'),
        ('E-2','E-2'),
        ('E-3','E-3'),
        ('E-4','E-4'),
        ('E-5','E-5'),
        ('E-6','E-6'),
        ('E-7','E-7'),
        ('E-8','E-8'),
        ('E-9','E-9'),
    ]
    email       = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username    = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_superuse = models.BooleanField(default=False)
    rank        = models.CharField(max_length=3, choices = rank_options,)
    squadron    = models.CharField(max_length=15)	
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','rank', 'squadron',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True








