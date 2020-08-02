def backlimit():
    sql = """SELECT
        genaircooler.timestamp AS timestamp,
        genaircooler.MW AS MW,
        genaircooler.MVAR AS MVAR,
        genaircooler.SlotA1 AS SlotA1,
        genaircooler.SlotA2 AS SlotA2,
        genaircooler.SlotA3 AS SlotA3,
        genaircooler.SlotB1 AS SlotB1,
        genaircooler.SlotB2 AS SlotB2,
        genaircooler.SlotB3 AS SlotB3,
        genaircooler.SlotC1 AS SlotC1,
        genaircooler.SlotC2 AS SlotC2,
        genaircooler.SlotC3 AS SlotC3,
        genaircooler.26AIS1 AS 26AIS1,
        genaircooler.26AIS2 AS 26AIS2,
        genaircooler.26AIS3 AS 26AIS3,
        genaircooler.26AIS4 AS 26AIS4,
        genaircooler.26AOS1 AS 26AOS1,
        genaircooler.26AOS2 AS 26AOS2,
        genaircooler.26AOS3 AS 26AOS3,
        genaircooler.26AOS4 AS 26AOS4,
        genaircooler.26AIS AS 26AIS,
        genaircooler.26AOS AS 26AOS,
        genaircooler.dTemp AS dTemp,
        genaircooler.F AS F,
        genaircooler.Cp AS Cp,
        genaircooler.p AS p,
        genaircooler.Q AS Q
        FROM
        genaircooler
        ORDER BY
        timestamp DESC
    """
    return sql

def backlast():
    sql = """SELECT
        genaircooler.timestamp AS timestamp,
        genaircooler.MW AS MW,
        genaircooler.MVAR AS MVAR,
        genaircooler.SlotA1 AS SlotA1,
        genaircooler.SlotA2 AS SlotA2,
        genaircooler.SlotA3 AS SlotA3,
        genaircooler.SlotB1 AS SlotB1,
        genaircooler.SlotB2 AS SlotB2,
        genaircooler.SlotB3 AS SlotB3,
        genaircooler.SlotC1 AS SlotC1,
        genaircooler.SlotC2 AS SlotC2,
        genaircooler.SlotC3 AS SlotC3,
        genaircooler.26AIS1 AS 26AIS1,
        genaircooler.26AIS2 AS 26AIS2,
        genaircooler.26AIS3 AS 26AIS3,
        genaircooler.26AIS4 AS 26AIS4,
        genaircooler.26AOS1 AS 26AOS1,
        genaircooler.26AOS2 AS 26AOS2,
        genaircooler.26AOS3 AS 26AOS3,
        genaircooler.26AOS4 AS 26AOS4,
        genaircooler.26AIS AS 26AIS,
        genaircooler.26AOS AS 26AOS,
        genaircooler.dTemp AS dTemp,
        genaircooler.F AS F,
        genaircooler.Cp AS Cp,
        genaircooler.p AS p,
        genaircooler.Q AS Q
        FROM
        genaircooler
        ORDER BY
        timestamp DESC
        limit 4
    """
    return sql
