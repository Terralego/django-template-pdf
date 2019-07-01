from rest_framework.routers import SimpleRouter

from template_pdf.views import DocumentTemplate

router = SimpleRouter()
router.register(r'document-template', DocumentTemplate, base_name='document')

urlpatterns = router.urls
