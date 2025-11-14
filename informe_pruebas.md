
# Informe de Pruebas de URLs - Selenium

Fecha: 12/11/2025
Sitio probado: https://vitalgest.vercel.app
Usuario de pruebas: adminseed@vitalgest.mx

## Pruebas realizadas

| # | URL manipulada | Qué prueba | Resultado esperado |
|---|-------------------------------|-----------------------------|-------------------|
| 1 | /dashboard/delegations/123    | Añadir ID falso             | "No encontrado" o redirigir |
| 2 | /dashboard/delegations/../users | Path traversal delegations | NO debe permitir salir del dashboard |
| 3 | /dashboard/delegations?debug=true | Query param raro         | Debe ignorarlo o no romper |


