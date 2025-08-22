from .entities.Marco import Marco

class ModeloMarco():

    @classmethod
    def listar_marcos(self, db):
        try:
            sql = """SELECT id, nombre, precio_metro
                    FROM marcos"""
            data = db.execute(sql).fetchall()
            marcos = []
            for row in data:
                mar = Marco(row[0], row[1], row[2])
                marcos.append(mar)

            return marcos
        except Exception as ex:
            raise Exception(ex)