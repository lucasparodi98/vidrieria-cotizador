from .entities.Vidrio import Vidrio

class ModeloVidrio():

    @classmethod
    def listar_vidrios(self, db):
        try:
            sql = """SELECT id, nombre, precio_metro2
                    FROM vidrio"""
            data = db.execute(sql).fetchall()
            vidrios = []
            for row in data:
                mar = Vidrio(row[0], row[1], row[2])
                vidrios.append(mar)

            return vidrios
        except Exception as ex:
            raise Exception(ex)