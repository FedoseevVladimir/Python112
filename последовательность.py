https://www.youtube.com/playlist?list=PL-Hq_KrfJ31U3vlc1XXUlLI6n2GC7IhPP
117 пара создание проекта с нуля

1. Создаю папку где будет мой проект

2. захожу в папку проекта
cd "название папки проекта"

3. Создаю проект
django-admin startproject "name_project"

4. запускаю сервер, чтобы создались файлы базы данных
python manage.py runserver

4.1. Создаю приложение
python manage.py startapp "school"

5. в файле settings.py регистрируем приложение
'cms.apps.CmsConfig'

6. меняем язык на "ru-Ru"

7. настраиваем статические данные и медиа файлы
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

8. в файле models.py создаем свои модели (базы данных)
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='slider_img/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')
    cms_css = models.CharField(max_length=200, null=True, default='-', verbose_name='css class')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

9. регистрируем модель в админке admin.py
from .models import CmsSlider

admin.site.register(CmsSlider)

10. делаем миграции поочереди
python manage.py makemigrations
python manage.py migrate

11. создаем супер пользователя (админа)
python manage.py createsuperuser
/admin зайти в админку

12. в urls.py
from cms import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.first_page), - для отображения страницы
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
13. в views.py для рендеринга страницы
def first_page(request):
    return render(request, 'cms/index.html')

14. создаем папку cms/templates/cms для файлов html и стилей

15. создаем html файлы в папке /templates/cms