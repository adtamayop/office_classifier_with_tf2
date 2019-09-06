from keras.preprocessing.image import load_img,img_to_array# ,save_img
import numpy as np
import pathlib
import shutil
import time
import h5py
import os

class Preprocesar_imagenes:
    
    def __init__(self,directorio):                
        self.path_imagenes = pathlib.Path(directorio)         
        
    def leer_imagenes(self):
        """
        Se listan las rutas de cada imágen dentro del path del proyecto
        """        
        self.rutas_imagenes = list(self.path_imagenes.glob('*/*'))
        self.rutas_imagenes = [str(path) for path in self.rutas_imagenes]
        print("Se leyeron: ",len(self.rutas_imagenes), " imágenes")
        
    def etiquetar_imagenes(self):  
        """
        Asigno un número entero a cada clase de mi dataset
        """
        # se listan los nombres de las carpetas de las imágenes
        self.lista_etiquetas = os.listdir(self.path_imagenes)
        # asignación de indices a etiquetas
        self.diccionario_etiquetas = dict((nombre, indice) for indice,nombre in enumerate(self.lista_etiquetas))
        self.etiquetas_imagenes = [self.diccionario_etiquetas[pathlib.Path(path).parent.name] for path in self.rutas_imagenes]
        print("Las clases de mi base de datos son: \n",self.diccionario_etiquetas)
        
    
    def sacar_extension(self,path):
          """
          Obtiene la extensión de los archivos e imágenes leídos
          """
          ext = "" 
          for x in reversed(path):
            if x == ".":
              ext += x
              break
            else:
              ext += x
           
          return ext[::-1]
             

    def resize_images(self,resolucion):
      """
      Construye el dataset con las imágenes en la resolución deseada
      """  
      counter = 0
      imagenes_no_leidas = 0
      
      X_images = []
      y_images = []
      name_images = []
      extensiones_raras = {".ini"}
      
      for path_imagen in self.rutas_imagenes:
        
        extension = self.sacar_extension(path_imagen)
        
        if extension.lower() in [".jpeg",".gif",".jpg",".png"]:
          
          try:            
              imagen_cargada = img_to_array(load_img(path_imagen,target_size=resolucion))    
          except:
              imagenes_no_leidas += 1
              
          # si quisiera guardar las imagenes transformadas en disco
          # save_img('/content/sample_data/imagen_resize.jpeg',imagen_cargada)      
          
          clase_imagen = self.diccionario_etiquetas[pathlib.Path(path_imagen).parent.name]
    
          nombre_imagen = "clase_"+str(clase_imagen)+"_"+str(counter)+extension
    
          X_images.append(imagen_cargada)
          y_images.append(clase_imagen)
          name_images.append(nombre_imagen)
        
          counter += 1   
      
        else:
            
            extensiones_raras.add(extension)
        
      print(f"No se pudieron leer {imagenes_no_leidas} imágenes de un total de {len(self.rutas_imagenes)} imágenes" )
#      print(extensiones_raras)
            
      self.dataset = np.array([name_images,X_images,y_images])   


    def save_dataset(self,path):  
      """
      Guarda el data set en disco en formato h5
      """      
      # Inicialmente creamos la carpeta donde vamos 
      # a guardar las imagenes redimensionadas  
      if os.path.exists(path):    
        shutil.rmtree(path, ignore_errors=True)
        print("La carpeta ya existía y se ha eliminado")
      else:
        os.mkdir(path)
      
      # necesario porque no alcanza a actualizar la información de google drive
      time.sleep(5) 
                     
      with h5py.File(path+"hdf5_data.h5","w") as hdf:
      
        hdf.create_dataset('X', data = list(self.dataset[1]))
        hdf.create_dataset('y',data = list(self.dataset[2]))
        hdf.create_dataset('nombres',data = np.array((self.dataset[0]), dtype='S'))           
        
        
    def load_dataset(self,path):
      """
      Carga el archivo h5 
      """      
      with h5py.File(path+"/hdf5_data.h5","r") as hdf:
        
        # ls = list(hdf.keys())        
        X = np.array(hdf.get('X'))    
        y = np.array(hdf.get('y'))        
        nombres = np.array(hdf.get('nombres'))
        
        return X,y,nombres
        


#preprocesar = Preprocesar_imagenes("dataset")
#preprocesar.leer_imagenes()
#preprocesar.etiquetar_imagenes()
#preprocesar.resize_images((224,224))
#preprocesar.save_dataset("base_redimensionada/")
#dataset_cargado = preprocesar.load_dataset("base_redimensionada")

