-- Fichero que se guardara, con la extensión .sql
-- Posicionarse en la BBDD ha trabajar
USE NEPTUNO
-- Como agrupar por país destinatario
--SELECT (DP.PrecioUnidad*DP.PrecioUnidad) AS Importe 
--FROM Pedidos p, [Detalles de pedidos] DP 
--WHERE P.IdPedido = DP.IdPedido;

--AGRUPACIÓN EN SQL
--SELECT p.PaísDestinatario, SUM(dP.Cantidad) AS Cantidades FROM Pedidos p, [Detalles de pedidos] dp, Productos pr
--WHERE P.IdPedido = dp.IdPedido AND dp.IdProducto = pr.IdProducto
--GROUP BY p.PaísDestinatario
--ORDER BY p.PaísDestinatario ASC
-- PARA AGRUPAR NECESITO UNA FUNCIÓN DE RESUMEN: SUM, AVERAGE, MAX, MIN, COUNT, 
--DISTINCTCOUNT,... EL RESUMEN VA EN EL SUJETO SIEMPRE, Y TIENE QUE IR
--LA DIMENSIÓN POR LA QUE QUEREMOS AGRUPAR. EL GROUP BY SIEMPRE DEBE CONTENER
--LA DIMENSIÓN. LA FUNCIÓN DE RESUMEN, NO.


SELECT p.PaísDestinatario, SUM(dP.Cantidad* dp.PrecioUnidad) AS Importe FROM Pedidos p, [Detalles de pedidos] dp, Productos pr
WHERE P.IdPedido = dp.IdPedido AND dp.IdProducto = pr.IdProducto
GROUP BY p.PaísDestinatario
ORDER BY p.PaísDestinatario ASC