import json
import os
import django

# Configura el entorno de Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CubaVoto.settings')
django.setup()

from apps.votation.models import Provincia, Municipio, Persona, Diputados

def load_provincia_data():
    with open('../json/provincias.json', 'r', encoding='utf-8') as file:
        #print(file.readlines())
        datap = json.load(file)
        #print(data)
    with open('../json/municipios.json', 'r', encoding='utf-8') as file:
        #print(file.readlines())
        datam = json.load(file)
        #print(data)
        
    for item in datap["nombre"]:
        provincia = Provincia(
            nombre=item
        )
        provincia.save()
        for m in datam[item]:
            municipio=Municipio(
                nombre=m,
                provincia=provincia
            )
            municipio.save()
    
    print(f"Se han insertado {len(datap)} provincias en la base de datos.")


def load_municipio_data():
    with open('../json/municipios.json', 'r', encoding='utf-8') as file:
        #print(file.readlines())
        data = json.load(file)
        #print(data)
        
    for item in data:
        for munic in item:

            municip = Municipio(
                nombre=munic,
                provincia=int(item)
            )
            municip.save()
    
    print(f"Se han insertado municipios en {len(data)} provincias en la base de datos.")


def load_diputado_data():
    provincias=["Pinar del Río","Artemisa","Mayabeque","La Habana","Matanzas","Cienfuegos","Villa Clara","Sancti Spíritus","Ciego de Ávila","Camagüey","Las Tunas","Holguín","Santiago de Cuba","Guantánamo","Isla de la Juventud","Granma"]
    for i,p in enumerate(provincias):
        with open(f'../json/{p}.json', 'r', encoding='utf-8') as file:
            #print(file.readlines())
            data = json.load(file)
            print(data)
        prov=Provincia.objects.get(nombre=p)
            
        for item in data:
            diputado = Diputados(
                nombre=item["nombre"],
                age=item["age"],
                cargo=item["cargo"],
                biografia=item["biografia"],
                provincia=prov,
                municipio=Municipio.objects.get(prov, nombre=item["municipio"]).id
            )
            diputado.save()
        
        print(f"Se han insertado {len(data)} diputados de {p} en la base de datos.")



def load_persona_data():
    with open('../json/provincias.json', 'r', encoding='utf-8') as file:
        #print(file.readlines())
        data = json.load(file)
        print(data)
        
    for item in data["nombre"]:
        publication = Provincia(
            nombre=item
        )
        publication.save()
    
    print(f"Se han insertado {len(data)} publicaciones en la base de datos.")

    
if __name__ == '__main__':
    load_provincia_data()
    #load_municipio_data()
    #load_diputado_data()

