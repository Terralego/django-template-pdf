from rest_framework.routers import SimpleRouter

from template_pdf.views import DocumentTemplateViewSet

router = SimpleRouter()
router.register(r'document-template', DocumentTemplateViewSet, base_name='document')

urlpatterns = router.urls
