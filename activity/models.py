from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class UsersManager(BaseUserManager):
    def _create_user(self, email,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,password,user_id,tz):
        user=self._create_user(
            email,
            password=password
        )
        user.tz=tz
        user.user_id=user_id
        user.save(using=self._db)
        return user
    def create_staffuser(self, email, password,user_id,tz):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self._create_user(
            email,
            password=password,
        )
        user.tz=tz
        user.user_id=user_id
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,user_id,tz):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self._create_user(
            email,
            password=password,
        )
        user.tz=tz
        user.user_id=user_id
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Myuser(AbstractBaseUser):
    email=models.CharField(primary_key=True,max_length=155)
    user_id=models.CharField(unique=True,max_length=9,default='no id')
    name=models.CharField(max_length=50,default='jay')
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    tz=models.CharField(max_length=50)
    time_stamp=models.TimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_id','tz']
    def get_first_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    object=UsersManager()
class Activity_period(models.Model):
    email=models.ForeignKey(Myuser,on_delete='cascade')
    start_time=models.CharField(max_length=50)
    end_time=models.CharField(max_length=50)