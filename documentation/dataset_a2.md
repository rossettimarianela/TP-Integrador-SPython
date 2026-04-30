# Dataset XENO-CANTO
## Información general

| Campo | Valor |
|---|---|
| **Nombre** | Xeno-canto - Bird sounds from around the world |
| **Institución proveedora** | Xeno-canto Foundation for Nature Sounds |
| **Cantidad de registros** | 36 |
| **Cobertura geográfica** | Global |
| **Cobertura temporal** | 1900 hasta la actualidad |
| **Coordenadas** | oeste -180, este 180, norte 90, sur -90 |
| **Separador de campos** | Coma |
| **Codificación de caracteres** | UTF-8 |
| **Tipo de licencia** | Creative Commons Attribution Non Commercial (CC-BY-NC) 4.0 License |
| **Frecuencia de actualización** | 2026-02-17 |

## Archivos del dataset

| Archivo | Propósito |
|---|---|
| **occurence.txt** | Este conjunto de datos abarca los sonidos de la colección de sonidos de aves de Xeno-canto (XC).
XC es una base de datos en línea que proporciona acceso a grabaciones de sonidos de la vida silvestre de todo el mundo. |


## Atributos principales del archivo

| Atributo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| **occurrenceID** | Texto | Identificador único global del registro de ocurrencia biológica. Se recomienda que sea persistente y globalmente único. | urn:catalog:UWBM:Bird:89776 |
| **catalogNumber** | Texto | Identificador del registro (preferentemente único) dentro de la colección o dataset. | 2008.1334 |
| **basisOfRecord** | Texto | Tipo o naturaleza del registro de datos, indicando cómo fue generado. | HumanObservation |
| **collectionCode** | Texto | Nombre, acrónimo o código que identifica la colección o conjunto de datos del cual proviene el registro. | EBIRD |
| **dynamicProperties** | Texto | Conjunto de propiedades adicionales del registro expresadas como pares clave:valor (preferentemente en formato JSON). Se recomienda su uso para almacenar información estructurada no cubierta por otros campos del estándar. | {"aspectHeading":277, "slopeInDegrees":6} |
| **otherCatalogNumbers** | Texto | Lista de números de catálogo anteriores o alternativos que identifican el mismo registro en una o varias colecciones o conjuntos de datos. Se separan usando " \| ". | NPS YELLO6778 \| MBG 334244 |
| **genus** | Texto | Nombre científico completo del género al que pertenece el taxón. | Puma |
| **nomenclaturalCode** | Texto | El código nomenclatural (o códigos en el caso de un nombre ambiguo) bajo el cual se construye el dwc:scientificName. | ICN <br> ICZN |
| **identificationRemarks** | Texto | Comentarios o notas sobre dwc:Identification. | "Se distinguen Anthus correndera y Anthus hellmayri en función de la longitud comparativa de las uñas." |
| **vernacularName** | Texto | Un nombre común o vernáculo. | Condor Andino <br> American Eagle |
| **decimalLongitude** | Decimal | Longitud geográfica (en grados decimales, utilizando el sistema de referencia espacial especificado en dwc:geodeticDatum) del centro geográfico de una ubicación (dcterms:Location). Los valores positivos se encuentran al este del meridiano de Greenwich, y los negativos, al oeste. Los valores válidos están comprendidos entre -180 y 180, ambos inclusive. | -121.1761111 |
| **decimalLatitude** | Decimal | La latitud geográfica (en grados decimales, utilizando el sistema de referencia espacial especificado en dwc:geodeticDatum) del centro geográfico de una ubicación (dcterms:Location). Los valores positivos se encuentran al norte del ecuador, y los negativos, al sur. Los valores válidos están comprendidos entre -90 y 90 grados, ambos inclusive. | -41.0983423 |
| **vgeodeticDatum** | Texto |El elipsoide, datum geodésico o sistema de referencia espacial (SRS) sobre el cual se basan las coordenadas geográficas dadas en dwc:decimalLatitude y dwc:decimalLongitude. | Campo Inchauspe <br> European 1950 |
| **country** | Texto | El nombre del país o unidad administrativa principal en la que ocurre el término dcterms:Location. | Denmark <br> Colombia |
| **occurrenceID** | Texto | Identificador único global del registro de ocurrencia biológica. Se recomienda que sea persistente y globalmente único. | urn:catalog:UWBM:Bird:89776 |
| **catalogNumber** | Texto | Identificador del registro (preferentemente único) dentro de la colección o dataset. | 2008.1334 |
| **basisOfRecord** | Texto | Tipo o naturaleza del registro de datos, indicando cómo fue generado. | HumanObservation |
| **collectionCode** | Texto | Nombre, acrónimo o código que identifica la colección o conjunto de datos del cual proviene el registro. | EBIRD |
| **dynamicProperties** | Texto | Conjunto de propiedades adicionales del registro expresadas como pares clave:valor (preferentemente en formato JSON). Se recomienda su uso para almacenar información estructurada no cubierta por otros campos del estándar. | {"aspectHeading":277, "slopeInDegrees":6} |
| **otherCatalogNumbers** | Texto | Lista de números de catálogo anteriores o alternativos que identifican el mismo registro en una o varias colecciones o conjuntos de datos. Se separan usando " \| ". | NPS YELLO6778 \| MBG 334244 |
| **genus** | Texto | Nombre científico completo del género al que pertenece el taxón. | Puma |
| **nomenclaturalCode** | Texto | El código nomenclatural (o códigos en el caso de un nombre ambiguo) bajo el cual se construye el dwc:scientificName. | ICN <br> ICZN |
| **identificationRemarks** | Texto | Comentarios o notas sobre dwc:Identification. | "Se distinguen Anthus correndera y Anthus hellmayri en función de la longitud comparativa de las uñas." |
| **vernacularName** | Texto | Un nombre común o vernáculo. | Condor Andino <br> American Eagle |
| **decimalLongitude** | Decimal | Longitud geográfica (en grados decimales, utilizando el sistema de referencia espacial especificado en dwc:geodeticDatum) del centro geográfico de una ubicación (dcterms:Location). Los valores positivos se encuentran al este del meridiano de Greenwich, y los negativos, al oeste. Los valores válidos están comprendidos entre -180 y 180, ambos inclusive. | -121.1761111 |
| **decimalLatitude** | Decimal | La latitud geográfica (en grados decimales, utilizando el sistema de referencia espacial especificado en dwc:geodeticDatum) del centro geográfico de una ubicación (dcterms:Location). Los valores positivos se encuentran al norte del ecuador, y los negativos, al sur. Los valores válidos están comprendidos entre -90 y 90 grados, ambos inclusive. | -41.0983423 |
| **vgeodeticDatum** | Texto |El elipsoide, datum geodésico o sistema de referencia espacial (SRS) sobre el cual se basan las coordenadas geográficas dadas en dwc:decimalLatitude y dwc:decimalLongitude. | Campo Inchauspe <br> European 1950 |
| **country** | Texto | El nombre del país o unidad administrativa principal en la que ocurre el término dcterms:Location. | Denmark <br> Colombia |
| **specificEpithet** | Texto | El nombre del primer epíteto o epíteto de especie del dwc:scientificName.  | "concolor" "gottschei" |
| **infraspecificEpithet** | Texto | El nombre del epíteto infraespecífico más bajo o terminal del dwc:scientificName, excluyendo cualquier designación de rango  | "concolor" "oxyadenia" "laxa" |
| **scientificName** | Texto | El nombre científico completo, con información sobre la autoría y la fecha, si se conoce, debe ser el nombre del nivel taxonómico más bajo que se pueda determinar | "Coleoptera" "Vespertilionidae" "Manis" |
| **taxonRank** | Texto | El rango taxonómico del nombre más específico en dwc:scientificName  | "subspecies" "varietas" "nothogenus" |
| **kingdom** | Texto | El nombre científico del reino en el que se clasifica el dwc:Taxon | "Plantae" "Bacteria" "Fungi" |
| **family** | Texto | El nombre científico completo de la familia en la que se clasifica el dwc:Taxon.  | "Felidae" "Monocleaceae" |
| **higherClassification** | Texto | Una lista (concatenada y separada) de nombres de taxones que terminan en el rango inmediatamente superior al dwc:Taxon referenciado | "Plantae | Tracheophyta | Magnoliopsida | Ranunculales | Ranunculaceae | Ranunculus" |
| **locality** | Texto | Localidad específica donde se realizó la grabación | `Victoria, Entre Ríos` |
| **verbatimElevation** | Texto | Elevación tal cual fue provista originalmente | `10 m` |
| **recordedBy** | Texto | Persona que realizó la grabación | `Franco Vushurovich` |
| **eventDate** | Texto | Fecha de la grabación | `2025-05-03` |
| **eventTime** | Texto | Hora de la grabación | `11:22` |
| **verbatimEventDate** | Texto | Fecha tal cual fue provista originalmente | `2025-05-03` |
| **fieldNotes** | Texto | Notas de campo sobre el contexto de la grabación | `Vocalizando a baja altura en el denso albardón de Salix humbltiana y Tessaria integrifolia (Bosque de galería a 100mt del Río Paraná)..  .  Migratory bird calling in the gallery forest nearby Parana river..  .  *Elaenia albiceps chilensis.  .; animal seen:no; playback used:no` |