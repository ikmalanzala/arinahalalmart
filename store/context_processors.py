from .models import SettingWebsite

def setting_website(request):
    setting = SettingWebsite.objects.first()
    return {'setting': setting}