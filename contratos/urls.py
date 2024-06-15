from django.urls import path
from .views import cadastrar_orcamento, detalhar_orcamento, orcamentos, propriedades_por_cliente,cadastrar_tipo_pagamento,tipos_pagamento

urlpatterns = [
    path('orcamentos/', orcamentos, name='orcamentos'),
    path('cadastrar_orcamento/', cadastrar_orcamento, name='cadastrar_orcamento'),
    path('cadastrar_orcamento/<int:cliente_id>', cadastrar_orcamento, name='cadastrar_orcamento_com_cliente'),
    path('detalhar_orcamento/<int:orcamento_id>', detalhar_orcamento, name='detalhar_orcamento'),
    path('ajax/propriedades_por_cliente/<int:cliente_id>/', propriedades_por_cliente, name='propriedades_por_cliente'),
     path('cadastrar_tipo_pagamento/', cadastrar_tipo_pagamento, name='cadastrar_tipo_pagamento'),
    path('tipos_pagamento/', tipos_pagamento, name='tipos_pagamento'),

    # Outras URLs conforme necessário
]
