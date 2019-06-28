from rest_framework.routers import SimpleRouter

from template_pdf.views import EnrichDocumentTemplateViewSet

router = SimpleRouter()
router.register(r'document-template', EnrichDocumentTemplateViewSet, base_name='document')

urlpatterns = router.urls
