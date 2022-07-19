from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from core_app.views import QuestionViewSet, AnswerViewSet, OptionViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'option', OptionViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Listagem API",
        default_version='v1',
        description="Test description",
        license=openapi.License(name="BSD License"),
),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/report', AnswerViewSet.as_view({"get" : "report"}))
]

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
