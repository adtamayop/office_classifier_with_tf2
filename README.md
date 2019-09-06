# Clasificador de objetos de oficina 

Clasificador de imágenes de objetos de oficina utilizando diferentes arquitecturas y transfer learning 

Los modelos fueron implementados en tensorflow 2.0-Beta

Base de datos: 
https://drive.google.com/file/d/1mZvzT6jJjdc9V-P5dl-nUHRV-tqSMWIP/view?usp=sharing

Dicha base de datos contiene 17 Clases, las cuales son:

* Grapadora
* Clip
* Escritorio
* Lapicero
* Cinta adhesiva 
* Silla
* Armario
* Tijera
* Marcador
* Fax
* Mouse
* Maletin 
* Fotocopiadora
* Memoria usb
* Monitor
* Cuaderno
* Agenda

Métricas obtenidas en el conjunto de prueba:

* Arquitectura propia: accuracy de 80.4%

![alt text](/images/accuracy_basic_model.png)


* ResNet50: accuracy de 86.78 %

![alt text](/images/acurracy_resnet50.png)

* MobileNetV2: accuracy de 92.2 %

![alt text](/images/accuracy_mobileNetV2.png)


