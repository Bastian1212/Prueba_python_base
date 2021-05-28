from pymongo import MongoClient
client = MongoClient("localhost")

#--------------------#
db = client["prueba2"]
#--------------------#

def arregar_persona(col, nom, apell,edad, cel, rut ):
    col.insert_one({
        "RUT" :rut,
        "edad" : edad,
        "nombre" : nom,
        "apellido" : apell,
        "Telefono" : cel
 
    })

def mostrar_documentos(col):
    for i in  col.find({}): 
        print(i)


def buscar_un_ql(col,rut):


    doc = col.find({"RUT" : rut})
    print(doc)






if __name__ == "__main__":
   
    col = col = db["personas"] 
    arregar_persona(col,"bastian","villanueva",22,"932631681","20.135.031-k")
    ##mostrar_documentos(col)
    buscar_un_ql(col,"20.135.031-k")
    db.drop_collection("personas")
   




   


