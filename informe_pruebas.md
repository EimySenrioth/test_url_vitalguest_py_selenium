
# Informe de Pruebas de URLs - Selenium

Fecha: 12/11/2025
Sitio probado: https://vitalgest.vercel.app
Usuario de pruebas: adminseed@vitalgest.mx

## Pruebas realizadas

| # | URL manipulada | Qué prueba | Resultado esperado |
|---|-------------------------------|-----------------------------|-------------------|
| 1 | /dashboard/delegations/       | Añadir / al final           | Debe cargar igual |
| 2 | /dashboard/delegations/123    | Añadir ID falso             | "No encontrado" o redirigir |
| 3 | /dashboard/delegations/../users | Path traversal delegations | NO debe permitir salir del dashboard |
| 4 | /dashboard/delegations?debug=true | Query param raro         | Debe ignorarlo o no romper |
| 5 | /dashboard/delegations#admin  | Hash raro                   | Debe ignorarlo    |
| 6 | /dashboard/DELEGATIONS        | Mayúsculas en ruta          | 404 si sensible   |
| 7 | /dashboard/delegations;       | Punto y coma en ruta        | Debe sanitizar o redirigir |

## Resultados

Revisa la consola y el archivo resultado.png para ver los resultados de cada prueba. Puedes copiar aquí los resultados obtenidos tras ejecutar el script.

---

¿Quieres que el script guarde automáticamente los resultados aquí? Si es así, puedo modificar el script para que lo haga.
