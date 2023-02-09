
import uuid
from django.shortcuts import render,redirect,HttpResponse
from .models import login_sys
from .models import admin_login_sys
from .models import Product_details
import hashlib
from django.contrib import messages  # import messages

# Create your views here.

def home(request):
    # messages.success(request, 'Email already being taken')
    brand_new=Product_details.objects.filter(pcategory='Brand New')
    refurbished=Product_details.objects.filter(pcategory='Refurbished')

    return render(request,'home.html',{'brand_new':brand_new,'refurbished':refurbished})

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')


def signup(request):
  if request.method=='POST':
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    pnum=request.POST['pnum']
    state=request.POST['state']
    city=request.POST['city']
    gender=request.POST['gender']
    user_image=request.FILES['user_image']
    l_pass=request.POST['l_pass']
    cpass=request.POST['cpass']
    m = hashlib.md5()
    m.update(l_pass.encode('utf-8'))
    l_pass = m.hexdigest()
    user=login_sys(
      f_name=fname,
      l_name=lname,
      email=email,
      p_num=pnum,
      city=city,
      state=state,
      gender=gender,
      image=user_image,
      pass1=l_pass,
      pass2=cpass
    )
    user.save()
    messages.success(request, 'You have been signed up')

    return redirect('/')
  return render(request,'home.html')

def login_user(request):
  if request.method=='POST':
   log_email=request.POST['log_email']   
   log_pass=request.POST['log_pass']   
   m = hashlib.md5()
   m.update(log_pass.encode('utf-8'))
   log_pass = m.hexdigest()
  
   try:
      user = login_sys.objects.get(email=log_email)
      if user.pass1==log_pass :
       request.session['f_name'] = user.f_name
       User_image=user.image
       messages.success(request, 'You have been signed up')
       return redirect('/')
      else:
         messages.warning(request, 'Wrong credential')
         return redirect('/')
      return render(request,'home.html')
   except login_sys.DoesNotExist:
      messages.warning(request, 'Wrong credential')
      return redirect('/')
  else:
   return render(request,'home.html')
  

def log_out(request):
    del request.session['f_name']
    messages.success(request, 'You have been logged out')
    return redirect('/')





def admin_login(request):
   if request.method=='POST':
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    pnum=request.POST['pnum']
    state=request.POST['state']
    city=request.POST['city']
    gender=request.POST['gender']
    user_image=request.FILES['user_image']
    l_pass=request.POST['l_pass']
    cpass=request.POST['cpass']
    m = hashlib.md5()
    m.update(l_pass.encode('utf-8'))
    l_pass = m.hexdigest()
    user=admin_login_sys(
      admin_f_name=fname,
      admin_l_name=lname,
      admin_email=email,
      admin_p_num=pnum,
      admin_city=city,
      admin_state=state,
      admin_gender=gender,
      admin_image=user_image,
      admin_pass1=l_pass,
      admin_pass2=cpass
    )
    user.save()
    messages.success(request, 'You have been signed up')

    return redirect('/')
  
   return render(request,'admin_login.html')



def admin_log(request):
  if request.method=='POST':
   admin_email=request.POST['admin_email']   
   admin_pass=request.POST['admin_pass']   
   m = hashlib.md5()
   m.update(admin_pass.encode('utf-8'))
   admin_pass = m.hexdigest()

   try:
      user = admin_login_sys.objects.get(admin_email=admin_email)
      if user.admin_pass1==admin_pass:
       request.session['admin_f_name'] = user.admin_f_name
       messages.success(request, 'You have been signed up')
       return redirect('/')
      return render(request,'home.html')
   except login_sys.DoesNotExist:
      messages.warning(request, 'Wrong credential')
      return redirect('/')
  else:
   return render(request,'admin_log.html')
  




def admin_logout(request):
    del request.session['admin_f_name']
    messages.success(request, 'You have been logged out')
    return redirect('/')



def upload_data(request):
  if request.method=='POST':
    P_name=request.POST['pname']
    P_mrp=request.POST['mrp']
    P_dprice=request.POST['dprice']
    P_bname=request.POST['bname']
    P_vender=request.POST['vender']
    P_category=request.POST['pcategory']
    P_image=request.FILES['product_image']
    P_desc=request.POST['pdescription']
    try:
       All_product=Product_details(
       pname=P_name,
       pcategory=P_category,
       mrp=P_mrp,
       dprice=P_dprice,
       bname=P_bname,
       vender_name=P_vender,
       description=P_desc,
       p_image=P_image
       )
       All_product.save()
       messages.success(request, 'Data has been successfully uploaded')  
    except:
      messages.warning(request,'Some error occured during uploading data')
  return render(request,'upload_data.html')



def view_data(request):
  Show_products=Product_details.objects.all()
  return render(request,'view_data.html',{'Show_products':Show_products})


def multidata_data_upload(request):
  if request.method=='POST':
    P_name=request.POST.getlist('pname')
    P_mrp=request.POST.getlist('mrp')
    P_dprice=request.POST.getlist('dprice')
    P_bname=request.POST.getlist('bname')
    P_vender=request.POST.getlist('vender')
    P_category=request.POST.getlist('pcategory')
    P_image=request.FILES.getlist('product_image')
    P_desc=request.POST.getlist('pdescription')
    print(P_name,P_mrp)
    for x in range(0,len(P_name)):
        All_product=Product_details(
          pname=P_name[x],
          pcategory=P_category[x],
          mrp=P_mrp[x],
          dprice=P_dprice[x],
          bname=P_bname[x],
          vender_name=P_vender[x],
          description=P_desc[x],
          p_image=P_image[x]
        )
        All_product.save()
        messages.success(request, 'Bulk Data ha been successfully uploaded')  
    return redirect('/')    
  return render(request,'multi_data_upload.html')



def del_data(request,id):
  if request.method=='POST':
   del_row=Product_details.objects.filter(id=id)
   del_row.delete()
   return redirect('view_data')
  return render(request,'view_data.html')


def edit_data(request,id):
  if request.method=='POST':
    P_name=request.POST['pname']
    P_mrp=request.POST['mrp']
    P_dprice=request.POST['dprice']
    P_bname=request.POST['bname']
    P_vender=request.POST['vender']
    P_category=request.POST['pcategory']
    P_image=request.FILES['product_image']
    P_desc=request.POST['pdescription']
    All_product=Product_details(
    id=id,
    pname=P_name,
    pcategory=P_category,
    mrp=P_mrp,
    dprice=P_dprice,
    bname=P_bname,
    vender_name=P_vender,
    description=P_desc,
    p_image=P_image
    )
    All_product.save()
    messages.success(request, 'Data ha been successfully edited')  
    return redirect('view_data')


  return render(request,'view_data.html')


def Add_cart(request,id):
    if request.method=='GET':
      Add_cart=Product_details.objects.filter(id=id)
      return render(request,'Add_cart.html',{'Add_cart':Add_cart})
    return render(request,'Add_cart.html')




from .helper import send_forget_password_mail

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['remail']
        print(email)
        if login_sys.objects.filter(email=email):
            token = str(uuid.uuid4())
            profile_email = login_sys.objects.get(email=email)
            profile_email.forget_password_token = token
            profile_email.save()
            send_forget_password_mail(email, token)
            messages.success(request, 'An email has been sent ')
            return redirect('/')

        else:
            messages.success(request, 'Sorry your email is not registered')
            return redirect('/')

    return render(request,'reset-password.html')

def change_pass(request,token):
  
    profile_email = login_sys.objects.filter(forget_password_token=token).first()

    print(profile_email)
    context = {'user_id' : profile_email.id}
   
    if request.method =='POST':
        l_pass=request.POST['new_pass']
        cpass=request.POST['confirm_pass']
        user_id = request.POST.get('user_id')
        print(l_pass,cpass)

        m = hashlib.md5()
        m.update(l_pass.encode('utf-8'))
        l_pass = m.hexdigest()

        m1 = hashlib.md5()
        m1.update(cpass.encode('utf-8'))
        cpass = m1.hexdigest()
        if  l_pass != cpass:
                messages.error(request, 'both should  be equal.')
                return redirect(f'/change_pass/{token}/')

        else:
            change_pass=login_sys.objects.get(id=user_id)
            change_pass.pass1=l_pass
            change_pass.pass2=cpass
            change_pass.save(update_fields=['pass1','pass2'])
            messages.error(request, 'pass changed.')

            return redirect('/')

    return render(request,'change_pass.html',context)




