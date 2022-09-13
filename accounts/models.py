from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# CustomUserModel manager
class CustomUserModelManager(BaseUserManager):

    def create_user(self, email, username, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.

class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=100)

class SubGroup(models.Model):
    subgroup_id = models.IntegerField(primary_key=True)
    subgroup_name = models.CharField(max_length=100)
    group_id = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone_number = PhoneNumberField(blank=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False, default=" ")
    last_name = models.CharField(max_length=50, null=False, blank=False, default=" ")
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    sub_group = models.ForeignKey(SubGroup, on_delete=models.CASCADE, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = CustomUserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


