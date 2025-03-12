-- Fichero que se guardara, con la extensi�n .sql
-- Posicionarse en la BBDD ha trabajar
USE NEPTUNO
-- Como agrupar por pa�s destinatario
--SELECT (DP.PrecioUnidad*DP.PrecioUnidad) AS Importe 
--FROM Pedidos p, [Detalles de pedidos] DP 
--WHERE P.IdPedido = DP.IdPedido;

--AGRUPACI�N EN SQL
--SELECT p.Pa�sDestinatario, SUM(dP.Cantidad) AS Cantidades FROM Pedidos p, [Detalles de pedidos] dp, Productos pr
--WHERE P.IdPedido = dp.IdPedido AND dp.IdProducto = pr.IdProducto
--GROUP BY p.Pa�sDestinatario
--ORDER BY p.Pa�sDestinatario ASC
-- PARA AGRUPAR NECESITO UNA FUNCI�N DE RESUMEN: SUM, AVERAGE, MAX, MIN, COUNT, 
--DISTINCTCOUNT,... EL RESUMEN VA EN EL SUJETO SIEMPRE, Y TIENE QUE IR
--LA DIMENSI�N POR LA QUE QUEREMOS AGRUPAR. EL GROUP BY SIEMPRE DEBE CONTENER
--LA DIMENSI�N. LA FUNCI�N DE RESUMEN, NO.


SELECT p.Pa�sDestinatario, SUM(dP.Cantidad* dp.PrecioUnidad) AS Importe FROM Pedidos p, [Detalles de pedidos] dp, Productos pr
WHERE P.IdPedido = dp.IdPedido AND dp.IdProducto = pr.IdProducto
GROUP BY p.Pa�sDestinatario
ORDER BY p.Pa�sDestinatario ASC