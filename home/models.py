from django.db import models

# Create your models here.
class login_sys(models.Model):
    f_name=models.CharField( max_length=50)
    l_name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    p_num=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    state=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)
    image=models.ImageField( upload_to='profile_pics',default=None,null=True,blank=True)
    pass1=models.CharField( max_length=150)
    pass2=models.CharField( max_length=150)
    forget_password_token=models.CharField (max_length=150 ,null=True)
    SuperUser= models.CharField( max_length=50,default=0)




class admin_login_sys(models.Model):
    admin_f_name=models.CharField( max_length=50)
    admin_l_name=models.CharField( max_length=50)
    admin_email=models.EmailField( max_length=254)
    admin_p_num=models.CharField( max_length=50)
    admin_city=models.CharField( max_length=50)
    admin_state=models.CharField( max_length=50)
    admin_gender=models.CharField( max_length=50)
    admin_image=models.ImageField( upload_to='profile_pics',default=None,blank=True,null=True)
    admin_pass1=models.CharField( max_length=150)
    admin_pass2=models.CharField( max_length=150)


class Product_details(models.Model):
    user=models.ForeignKey(login_sys, on_delete=models.CASCADE,null=True)
    pname=models.CharField( max_length=50)
    pcategory=models.CharField( max_length=50)
    mrp=models.CharField( max_length=50)
    dprice=models.CharField( max_length=50)
    bname=models.CharField( max_length=50)
    vender_name=models.CharField( max_length=50)
    description=models.TextField()
    p_image=models.ImageField( upload_to='P_images',null=True,blank=True)



