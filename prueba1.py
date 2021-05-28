from pymongo import MongoClient
client = MongoClient("localhost")



def probando_data_base():
    db = client["prueba"]
    col = db["personas"]   ### crea la coleccion a nuestra base de datos 

    '''
    col.insert_one({
        "edad" : 22,
        "nombre" : "Bastian ",
        "intereses" : ["informatica","apple","tecnologia"]
    })
    '''

    print(col.count_documents({}))  ### muestra la cantidad de documentos nuuesta coleccion 
    print(db.list_collection_names()) ### muestra los nombre de las colecciones


    '''#col.insert_many([                  ###agrega a nuestra coleccion mas de un documento 
        {
            "edad" : 40, 
            "nombre" : "hola_mejorao", 
            "intereses" : ["mejorao", "hola"]
        },
        {
            "edad" : 40, 
            "nombre" : "Diego Maradona",
             "intereses" : ["jalar", "AAAAAaa"]       
        }

    ])
    '''
    '''
    for i in  col.find({}): ## nos muestra todo los datos que tenemos en la coleccion 
        print(i)
    '''
    '''
    for i in  col.find_({
        "edad" : {
            "$gt" : 40
        }
    }):
        print(i)
    '''
    doc = col.find_one({
        "edad" :22
    })

    print(doc)
    '''
    col.delete_one({    ### elimina el  primer documento que cumpla con la condicion 
        "edad" : 22 
    })
    '''

    col.delete_many({        ### nos elimina todos los documetos que cumplan la condiccion 
        "edad" : 22         
    })

    for i in col.find({}):
        print(i)
    col.update_one({     ### modifica un dato 
        "edad" : 40
    }, {
        "$set" : {
            "edad" : 90
        }
        
    })

    '''
    db.drop_collection("personas")  ### va eliminar la coleccion 
    client.drop_database("prueba")  ### elimina la case de datos 
    '''
    
if __name__ == "__main__":

    probando_data_base()






