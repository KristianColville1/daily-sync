from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from profiles.forms import EditProfileForm
from cloudinary.forms import cl_init_js_callbacks  
from profiles.models import Profile


class AccountSettingsView(View):
  """
  Account settings view
  """
  def get(self,request, *args, **kwargs):
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = EditProfileForm(instance=profile)
    context = {
      'form': profile_form,
      }
    return render(request, 'account_settings/index.html', context)


  def post(self, request, *args, **kwargs):
    profile = get_object_or_404(Profile, user=request.user)
    form = EditProfileForm(data=request.POST, instance=profile, files=request.FILES)
    context = {
      'form': EditProfileForm(instance=profile),
      }
    if form.is_valid():
      form.save()
      return redirect(request.META.get('/feed/', '/'))

    return render(request, 'account_settings/index.html', context)
  
def privacy_policy(request):
  """
  Privacy policy
  """
  return render(request, 'account_settings/privacy.html')
  
  
def terms_and_conditions(request):
  """
  Terms and conditions
  """
  return render(request, 'account_settings/terms.html')