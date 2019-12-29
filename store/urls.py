from rest_framework.routers import SimpleRouter
from store.views import *

router = SimpleRouter()
router.register("Product", ProductOp)

urlpatterns = router.urls
