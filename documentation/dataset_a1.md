# Dataset IADIZA-COI
## Información general

| Campo | Valor |
|---|---|
| **Nombre** | Colección Ornitológica del IADIZA-CCT CONICET Mendoza: IADIZA-COI |
| **Institución proveedora** | Instituto Argentino de Investigaciones de las Zonas Áridas. |
| **Cantidad de registros** | 2.365 |
| **Cobertura geográfica** | La información proviene principalmente de localidades de Argentina y algunos países limítrofes. |
| **Cobertura temporal** | 2017-10-04 |
| **Coordenadas** | Norte: -46.02, Sur: -22.25, Este: -53.735, Oeste: -71.647 |
| **Separador de campos** | \t (tabulación) |
| **Codificación de caracteres** | UTF-8 |
| **Tipo de licencia** | Creative Commons Attribution Non Commercial (CC-BY-NC) 4.0 License |
| **Frecuencia de actualización** | notPlanned |

## Archivos del dataset

| Archivo | Propósito |
|---|---|
| **occurrence.txt** | El propósito del archivo es documentar las características y datos de localización, comportamiento, etc, de aves en la provincia de Mendoza, Argentina. |


## Atributos principales del archivo

| Atributo | Tipo de dato | Descripción | Ejemplo |
|---|---|---|---|
| **geodeticDatum** | Texto | Sistema de referencia geográfica utilizado para las coordenadas del registro. Es un valor constante aplicado a todos los registros del dataset. | WGS84 |
| **gbifID** | Numérico | Identificador único y estable asignado por GBIF a cada registro de ocurrencia. | 1660908055 |
| **accessRights** | Texto | Indica las condiciones de acceso al recurso (si existen restricciones de uso o privacidad). | Restricted access / Open access |
| **bibliographicCitation** | Texto | Referencia bibliográfica del recurso utilizada para su citación. No tiene formato obligatorio, solo debe permitir identificar el dataset de forma clara. | GBIF Occurrence Download 0025550-260208012135463 (GBIF, 2026) |
| **language** | Texto | Idioma en el que está descrita la información del recurso. Se recomienda usar códigos estándar como ISO 639. | en (English) |
| **license** | Texto | Documento o condición legal que establece los permisos de uso del recurso, indicando cómo puede utilizarse o compartirse. | CC_BY_NC_4_0 |
| **modified** | Fecha | Fecha en la que el recurso fue modificado por última vez o actualizado. | 2015-05-19T00:00:00Z |
| **publisher** | Texto | Entidad responsable de publicar y poner a disposición el recurso. | GBIF Secretariat |
| **references** | Texto | Enlace a un recurso externo relacionado con el registro. |  https://www.gbif.org/occurrence/... |
| **rightsHolder** | Texto | Persona u organización que posee los derechos legales sobre el recurso o dataset. Se recomienda usar un identificador URI si está disponible, pero puede usarse un nombre en texto. | No especificado |
| **type** | Texto | Naturaleza o tipo del recurso según vocabulario controlado (DCMI Type). | Dataset |
| **institutionID** | Texto | Identificador de la institución que tiene la custodia del material o información del registro. | http://grscicoll.org/institution/museum-southwestern-biology |
| **collectionID** | Texto | Identificador de la colección o conjunto del cual proviene el registro. | https://scientific-collections.gbif.org/collection/fbd3ed74-5a21-4e01-b86a-33d36f032d9c |
| **datasetID** | Texto | Identificador del conjunto de datos, que puede ser global o específico de una institución. | 	b15d4952-7d20-46f1-8a3e-556a512b04c5 |
| **institutionCode** | Texto | Acrónimo o nombre corto de la institución que tiene la custodia del material o información del registro. | IADIZA |
| **collectionCode** | Texto | Código o abreviatura que identifica la colección de origen del registro. | COI |
| **datasetName** | Texto | Nombre del conjunto de datos del cual proviene el registro. | Grinnell Resurvey Mammals |
| **institutionCode** | Texto | Acrónimo o nombre utilizado por la institución que tiene la custodia del material o información del registro. | NPS |
| **basisOfRecord** | Texto | Indica la naturaleza del registro de datos, es decir, el tipo de evidencia en la que se basa (por ejemplo, observación o espécimen conservado). | PRESERVED_SPECIMEN |
| **informationWithheld** | Texto | Información adicional que existe sobre el registro pero que no fue publicada o fue restringida en el dataset. | location information not given for endangered species |
| **dataGeneralizations** | Texto | Indica si los datos fueron simplificados o generalizados respecto de su forma original para reducir el nivel de detalle publicado. | Coordinates generalized from original GPS coordinates to the nearest half degree grid cell. |
| **dynamicProperties** | Texto | Conjunto de propiedades adicionales del registro expresadas como pares clave:valor (preferentemente en formato JSON). Su objetivo es almacenar información estructurada no contemplada en otros campos del estándar. | {"targusLengthInMeters":0.014, "weightInGrams":120} |
| **occurrenceID** | Texto | Identificador único del registro biológico (ocurrencia), independiente del registro digital del dataset. Se recomienda un identificador único, persistente y global | IADIZA:COI:006861 |
| **catalogNumber** | Texto | Identificador (preferiblemente único) del registro dentro de una colección o dataset. | 006866 |
| **recordNumber** | Texto | Identificador asignado al registro en el momento de su recolección, generalmente utilizado en notas de campo del colector. | OPP 7101 |
| **recordedBy** | Texto | Nombre de la persona, grupo u organización responsable de la recolección o registro original del dato. | R.G. Spurr |
| **recordedByID** | Texto | Identificador global de la persona u organización que realizó el registro original del dato. | https://orcid.org/0000-0002-1825-0097 (for an individual) |
| **individualCount** | Numérico | Número de individuos presentes en la ocurrencia en el momento del registro. | 1 |
| **organismQuantity** | Numérico o texto | Valor que expresa la cantidad de organismos observados o estimados, utilizando diferentes tipos de medidas o escalas. | 12.5 (organismQuantity) with % biomass (organismQuantityType) |
| **organismQuantityType** | Texto | Tipo de sistema o unidad utilizado para expresar la cantidad de organismos (por ejemplo individuos, biomasa o escalas ecológicas). | 27 (organismQuantity) with individuals (organismQuantityType) |
| **sex** | Texto | Sexo del individuo biológico representado en la ocurrencia (por ejemplo macho o hembra). | female |
| **lifeStage** | Texto | Etapa de vida del organismo en el momento del registro (por ejemplo juvenil o adulto). | juvenile |
| **reproductiveCondition** | Texto | Estado reproductivo del organismo en el momento del registro (por ejemplo en reproducción o no reproductivo). | non-reproductive |
| **caste** | Texto | Clasificación de individuos en especies eusociales según su rol dentro de la colonia. | queen |
| **behavior** | Texto | Comportamiento del organismo en el momento del registro. | running |
| **vitality** | Texto | Indica si el organismo estaba vivo o muerto en el momento del registro. | alive |
| **establishmentMeans** | Texto | Indica si el organismo es nativo o si fue introducido en el lugar de la ocurrencia, ya sea por acción humana directa o indirecta. | nativeReintroduced |
| **degreeOfEstablishment** | Texto | Nivel de establecimiento de una especie introducida en el ambiente, indicando si logra sobrevivir, reproducirse o expandirse. | colonising |
| **pathway** | Texto | Vía o mecanismo por el cual un organismo llegó a un lugar determinado, ya sea de forma natural o por acción humana. | transportContaminant |
| **georeferenceVerificationStatus** | Texto | Descripción categórica del grado de verificación de la georreferenciación del registro, indicando si la ubicación fue revisada o validada. | requires verification |
| **occurrenceStatus** | Texto | Indica si el taxón está presente o ausente en la ubicación registrada. El vocabulario recomendado es "present" o "absent". | PRESENT |
| **preparations** | Texto | Métodos de preparación o preservación del material biológico. | DNA extract |
| **disposition** | Texto | Estado actual del material biológico dentro de una colección. | destroyed |
| **associatedOccurrences** | Texto | Identificadores de otras ocurrencias relacionadas con el registro, permitiendo estableces asociaciones entre registros del dataset. | "parasite collected from":"https://arctos.database.museum/guid/MSB:Mamm:215895?seid=950760" |
| **associatedReferences** | Texto | Lista de referencias bibliográficas o identificadores de literatura asociados al registro de ocurrencia. | Christopher J. Conroy, Jennifer L. Neuwald. 2008. Phylogeographic study of the California vole, Microtus californicus Journal of Mammalogy, 89(3):755-767. |
| **associatedSequences** | Texto | Identificadores de secuencias genéticas asociadas al material biológico del registro, como datos de ADN en bases externas. | http://www.ncbi.nlm.nih.gov/nuccore/U34853.1 |
| **associatedTaxa** | Texto | Una lista (concatenada y separada) de identificadores o nombres de registros dwc:Taxon y las asociaciones de este dwc:Occurrence con cada uno de ellos. | "host":"Quercus alba" |
| **otherCatalogNumbers** | Texto | Una lista (concatenada y separada) de números de catálogo completos anteriores o alternativos u otros identificadores utilizados por humanos para la misma dwc:Occurrence, ya sea en el conjunto de datos o colección actual o en cualquier otro. | FMNH:Mammal:1234 |
| **occurrenceRemarks** | Texto | Comentarios o notas sobre dwc:Occurrence. | "Encontrado muerto en el camino" |
| **organismID** | Texto | Un identificador para la instancia dwc:Organism (a diferencia de un registro digital específico de dwc:Organism). Puede ser un identificador único global o un identificador específico del conjunto de datos. | http://arctos.database.museum/guid/WNMU:Mamm:1249 |
| **organismName** | Texto | Un nombre o etiqueta textual asignado a una instancia de dwc:Organism. | Boab Prison Tree |
| **organismScope** | Texto | Descripción del tipo de instancia dwc:Organism. Puede utilizarse para indicar si la instancia dwc:Organism representa un organismo individual o un tipo particular de agregación. | organismo multicelular |
| **associatedOrganisms** | Texto | Una lista (concatenada y separada) de identificadores de otros dwc:Organisms y las asociaciones de este dwc:Organism con cada uno de ellos. | "hermano de":"http://arctos.database.museum/guid/DMNS:Mamm:14171" |
| **previousIdentifications** | Texto | Una lista (concatenada y separada) de asignaciones previas de nombres al dwc:Organism. | Chalepidae <br> Pinus abies |
| **organismRemarks** | Texto | Notas o comentarios sobre una instancia particular de un organismo | "Uno de una camada de seis" |
| **materialEntityID** | Texto | Un identificador para una instancia particular de dwc:MaterialEntity. | 06809dc5-f143-459a-be1a-6f03e63fc083 |
| **materialEntityRemarks** | Texto | Comentarios o notas sobre la instancia dwc:MaterialEntity. | "Encontrado junto a restos carbonizados. Faltan algunos fragmentos originales." |
| **verbatimLabel** | Texto | El contenido de este término no debe incluir adornos, prefijos, encabezados ni otras adiciones al texto. No se deben expandir las abreviaturas ni corregir las supuestas faltas de ortografía. Se pueden usar líneas o puntos de ruptura entre bloques de texto que se puedan verificar consultando las etiquetas originales o sus imágenes. Es la transcripción exacta de lo que el investigador escribió físicamente en el papel o etiqueta sin corregir errores | "ILL: Union Co. Wolf Lake by Powder Plant Bridge. <br> 1 March 1975 Coll. S. Ketzler, S. Herbert <br> Monotoma longicollis 4 ♂ Det TC McElrath 2018 <br> INHS Insect Collection 456782" |
| **materialSampleID** | Texto | Un identificador para dwc:MaterialSample (a diferencia de un registro digital específico de dwc:MaterialSample). En ausencia de un identificador único global persistente, se crea uno a partir de una combinación de identificadores del registro que, en la medida de lo posible, haga que dwc:materialSampleID sea globalmente único. | 06809dc5-f143-459a-be1a-6f03e63fc083 |
| **eventID** | Texto | Un identificador para el conjunto de información asociado con un dwc:Event (algo que ocurre en un lugar y momento determinados). Puede ser un identificador único global o un identificador específico del conjunto de datos. | INBO:VIS:Ev:00009375 |
| **parentEventID** | Texto | Un identificador para el dwc:Event más amplio que agrupa este y potencialmente otros dwc:Events. | A1 (parentEventID para identificar el gráfico principal de Whittaker en muestras anidadas, cada una con su propio eventID - A1:1, A1:2). |
| **eventType** | Texto | La naturaleza del evento dwc:Event. | Muestra <br> Observación <br> Visita al sitio |
| **fieldNumber** | Texto | Un identificador asignado al dwc:Event en el campo. A menudo sirve como enlace entre las notas de campo y el dwc:Event. | RV Sol 87-03-08 |
| **eventDate** | Fecha | Fecha y hora o intervalo durante el cual ocurrió un evento dwc:Event. En el caso de sucesos, esta es la fecha y hora en que se registró el evento dwc:Event. No es adecuado para un período de tiempo en un contexto geológico. | 1906-06 (en el mes de junio de 1906) |
| **eventTime** | Texto | El tiempo o intervalo durante el cual ocurrió un dwc:Evento. | 14:07-06:00 (a partir de las 14:07 y antes de las 14:08 en la zona horaria seis horas anterior a UTC) |
| **startDayOfYear** | Numérico | El primer día (entero) del año en que ocurrió el dwc:Event (1 para el 1 de enero, 365 para el 31 de diciembre, excepto en un año bisiesto, en cuyo caso es 366). | 1 (Enero) <br> 366 (31 de diciembre) |
| **endDayOfYear** | Numérico | El último día (entero) del año en el que ocurrió el dwc:Event (1 para el 1 de enero, 365 para el 31 de diciembre, excepto en un año bisiesto, en cuyo caso es 366). | 32 (1 Febrero) |
| **year** | Numérico | El año de cuatro dígitos en el que ocurrió el dwc:Event, según el Calendario de la Era Común. | 2008 |
| **month** | Numérico | El mes (entero) en el que ocurrió el dwc:Event. | 10 (Octubre) |
| **day** | Numérico | El día (entero) en el que ocurrió el dwc:Event. | 9 <br> 27 |
| **verbatimEventDate** | Texto | La representación original textual de la información de fecha y hora para un dwc:Event. | Primavera 1910 <br> Mayo 2002 |
| **habitat** | Texto | Una categoría o descripción del hábitat en el que ocurrió el evento dwc:Event. | sabana de robles <br> estepa precordillerana |
| **samplingProtocol** | Texto | Los nombres, referencias o descripciones de los métodos o protocolos utilizados durante un dwc:Event. | Pingüinos del espacio: manchas fecales revelan la ubicación de colonias de pingüinos emperador, https://doi.org/10.1111/j.1466-8238.2009.00467.x |
| **sampleSizeValue** | Numérico | Un valor numérico para una medida del tamaño (duración en el tiempo, longitud, área o volumen) de una muestra en un dwc:Evento de muestreo. | 5 (sampleSizeValue) con metro (sampleSizeUnit) |
| **sampleSizeUnit** | Texto | La unidad de medida del tamaño (duración en el tiempo, longitud, área o volumen) de una muestra en un dwc:Event de muestreo. | minuto <br> día <br> metro cúbico |
| **samplingEffort** | Texto | La cantidad de esfuerzo invertido durante un dwc:Event. | m40 noches de trampeo <br> 10 horas de observación |
| **fieldNotes** | Texto | Uno de a) un indicador de la existencia de, b) una referencia a (publicación, URI), o c) el texto de las notas tomadas en el campo sobre el dwc:Event. | Apuntes disponibles en la Biblioteca Grinnell-Miller. |
| **eventRemarks** | Texto | Notas o comentarios sobre el dwc:Event. | "Tras las recientes lluvias, el río está prácticamente desbordado." |
| **locationID** | Texto | Un identificador para el conjunto de información de dcterms:Location. Puede ser un identificador único global o un identificador específico del conjunto de datos. | https://opencontext.org/subjects/768A875F-E205-4D0B-DE55-BAB7598D0FD1 |
| **higherGeographyID** | Texto | Un identificador para la región geográfica dentro de la cual ocurrió el dcterms:Location. | Antártida e Islas del Atlántico Sur, Territorio Nacional de la Tierra del Fuego, Argentina. |
| **higherGeography** | Texto | Una lista (concatenada y separada) de nombres geográficos menos específicos que la información capturada en el atributo dwc:locality. | Océano Atlántico Norte <br> América del Sur, Argentina, Patagonia, Parque Nacional Nahuel Huapi, Neuquén, Los Lagos |
| **continent** | Texto | El nombre del continente en el que se produce el término dcterms:Location. | Africa <br> Antartica <br> Asia |
| **waterBody** | Texto | El nombre del cuerpo de agua en el que ocurre el dcterms:Location. | Océano Índico <br> Mar Báltico <br> Río Hudson |
| **islandGroup** | Texto | El nombre del grupo de islas en el que se produce el término dcterms:Location. | Archipiélago Diego Ramírez |
| **island** | Texto | El código estándar para el país en el que se produce el dcterms:Location. | AR <br> UY |
| **stateProvince** | Texto | El nombre de la siguiente región administrativa más pequeña que el país (estado, provincia, cantón, departamento, región, etc.) en la que ocurre el término dcterms:Location. | Minas Gerais <br> Córdoba |
| **county** | Texto | El nombre completo, sin abreviar, de la siguiente región administrativa más pequeña que el stateProvince (condado, distrito, departamento, etc.) en la que se produce el término dcterms:Location. | Los Lagos <br> Mataró |
| **municipality** | Texto | El nombre completo, sin abreviar, de la región administrativa inmediatamente inferior al condado (ciudad, municipio, etc.) en la que se encuentra la ubicación especificada por dcterms:Location. No utilice este término para un lugar cercano con nombre que no contenga la ubicación especificada por dcterms:Location. | Holzminden <br> Araçatuba |
| **locality** | Texto | La descripción específica del lugar. | Bariloche, 25 km NNE via Ruta Nacional 40 (=Ruta 237) |
| **verbatimLocality** | Texto | La descripción textual original del lugar. | 25 km NNE Bariloche por R. Nac. 237 |
| **verbatimElevation** | Texto | La descripción original de la elevación (altitud, generalmente sobre el nivel del mar) de la ubicación. | 100-200 m |
| **geodeticDatum** | Texto | Sistema de referencia geográfica utilizado para las coordenadas del registro. Es un valor constante aplicado a todos los registros del dataset. | WGS84 |
| **gbifID** | Numérico | Identificador único y estable asignado por GBIF a cada registro de ocurrencia. | 1660908055 |
| **accessRights** | Texto | Indica las condiciones de acceso al recurso (si existen restricciones de uso o privacidad). | Restricted access / Open access |
| **bibliographicCitation** | Texto | Referencia bibliográfica del recurso utilizada para su citación. No tiene formato obligatorio, solo debe permitir identificar el dataset de forma clara. | GBIF Occurrence Download 0025550-260208012135463 (GBIF, 2026) |
| **language** | Texto | Idioma en el que está descrita la información del recurso. Se recomienda usar códigos estándar como ISO 639. | en (English) |
| **license** | Texto | Documento o condición legal que establece los permisos de uso del recurso, indicando cómo puede utilizarse o compartirse. | CC_BY_NC_4_0 |
| **modified** | Fecha | Fecha en la que el recurso fue modificado por última vez o actualizado. | 2015-05-19T00:00:00Z |
| **publisher** | Texto | Entidad responsable de publicar y poner a disposición el recurso. | GBIF Secretariat |
| **references** | Texto | Enlace a un recurso externo relacionado con el registro. |  https://www.gbif.org/occurrence/... |
| **rightsHolder** | Texto | Persona u organización que posee los derechos legales sobre el recurso o dataset. Se recomienda usar un identificador URI si está disponible, pero puede usarse un nombre en texto. | No especificado |
| **type** | Texto | Naturaleza o tipo del recurso según vocabulario controlado (DCMI Type). | Dataset |
| **institutionID** | Texto | Identificador de la institución que tiene la custodia del material o información del registro. | http://grscicoll.org/institution/museum-southwestern-biology |
| **collectionID** | Texto | Identificador de la colección o conjunto del cual proviene el registro. | https://scientific-collections.gbif.org/collection/fbd3ed74-5a21-4e01-b86a-33d36f032d9c |
| **datasetID** | Texto | Identificador del conjunto de datos, que puede ser global o específico de una institución. | 	b15d4952-7d20-46f1-8a3e-556a512b04c5 |
| **institutionCode** | Texto | Acrónimo o nombre corto de la institución que tiene la custodia del material o información del registro. | IADIZA |
| **collectionCode** | Texto | Código o abreviatura que identifica la colección de origen del registro. | COI |
| **datasetName** | Texto | Nombre del conjunto de datos del cual proviene el registro. | Grinnell Resurvey Mammals |
| **institutionCode** | Texto | Acrónimo o nombre utilizado por la institución que tiene la custodia del material o información del registro. | NPS |
| **basisOfRecord** | Texto | Indica la naturaleza del registro de datos, es decir, el tipo de evidencia en la que se basa (por ejemplo, observación o espécimen conservado). | PRESERVED_SPECIMEN |
| **informationWithheld** | Texto | Información adicional que existe sobre el registro pero que no fue publicada o fue restringida en el dataset. | location information not given for endangered species |
| **dataGeneralizations** | Texto | Indica si los datos fueron simplificados o generalizados respecto de su forma original para reducir el nivel de detalle publicado. | Coordinates generalized from original GPS coordinates to the nearest half degree grid cell. |
| **dynamicProperties** | Texto | Conjunto de propiedades adicionales del registro expresadas como pares clave:valor (preferentemente en formato JSON). Su objetivo es almacenar información estructurada no contemplada en otros campos del estándar. | {"targusLengthInMeters":0.014, "weightInGrams":120} |
| **occurrenceID** | Texto | Identificador único del registro biológico (ocurrencia), independiente del registro digital del dataset. Se recomienda un identificador único, persistente y global | IADIZA:COI:006861 |
| **catalogNumber** | Texto | Identificador (preferiblemente único) del registro dentro de una colección o dataset. | 006866 |
| **recordNumber** | Texto | Identificador asignado al registro en el momento de su recolección, generalmente utilizado en notas de campo del colector. | OPP 7101 |
| **recordedBy** | Texto | Nombre de la persona, grupo u organización responsable de la recolección o registro original del dato. | R.G. Spurr |
| **recordedByID** | Texto | Identificador global de la persona u organización que realizó el registro original del dato. | https://orcid.org/0000-0002-1825-0097 (for an individual) |
| **individualCount** | Numérico | Número de individuos presentes en la ocurrencia en el momento del registro. | 1 |
| **organismQuantity** | Numérico o texto | Valor que expresa la cantidad de organismos observados o estimados, utilizando diferentes tipos de medidas o escalas. | 12.5 (organismQuantity) with % biomass (organismQuantityType) |
| **organismQuantityType** | Texto | Tipo de sistema o unidad utilizado para expresar la cantidad de organismos (por ejemplo individuos, biomasa o escalas ecológicas). | 27 (organismQuantity) with individuals (organismQuantityType) |
| **sex** | Texto | Sexo del individuo biológico representado en la ocurrencia (por ejemplo macho o hembra). | female |
| **lifeStage** | Texto | Etapa de vida del organismo en el momento del registro (por ejemplo juvenil o adulto). | juvenile |
| **reproductiveCondition** | Texto | Estado reproductivo del organismo en el momento del registro (por ejemplo en reproducción o no reproductivo). | non-reproductive |
| **caste** | Texto | Clasificación de individuos en especies eusociales según su rol dentro de la colonia. | queen |
| **behavior** | Texto | Comportamiento del organismo en el momento del registro. | running |
| **vitality** | Texto | Indica si el organismo estaba vivo o muerto en el momento del registro. | alive |
| **establishmentMeans** | Texto | Indica si el organismo es nativo o si fue introducido en el lugar de la ocurrencia, ya sea por acción humana directa o indirecta. | nativeReintroduced |
| **degreeOfEstablishment** | Texto | Nivel de establecimiento de una especie introducida en el ambiente, indicando si logra sobrevivir, reproducirse o expandirse. | colonising |
| **pathway** | Texto | Vía o mecanismo por el cual un organismo llegó a un lugar determinado, ya sea de forma natural o por acción humana. | transportContaminant |
| **georeferenceVerificationStatus** | Texto | Descripción categórica del grado de verificación de la georreferenciación del registro, indicando si la ubicación fue revisada o validada. | requires verification |
| **occurrenceStatus** | Texto | Indica si el taxón está presente o ausente en la ubicación registrada. El vocabulario recomendado es "present" o "absent". | PRESENT |
| **preparations** | Texto | Métodos de preparación o preservación del material biológico. | DNA extract |
| **disposition** | Texto | Estado actual del material biológico dentro de una colección. | destroyed |
| **associatedOccurrences** | Texto | Identificadores de otras ocurrencias relacionadas con el registro, permitiendo estableces asociaciones entre registros del dataset. | "parasite collected from":"https://arctos.database.museum/guid/MSB:Mamm:215895?seid=950760" |
| **associatedReferences** | Texto | Lista de referencias bibliográficas o identificadores de literatura asociados al registro de ocurrencia. | Christopher J. Conroy, Jennifer L. Neuwald. 2008. Phylogeographic study of the California vole, Microtus californicus Journal of Mammalogy, 89(3):755-767. |
| **associatedSequences** | Texto | Identificadores de secuencias genéticas asociadas al material biológico del registro, como datos de ADN en bases externas. | http://www.ncbi.nlm.nih.gov/nuccore/U34853.1 |
| **associatedTaxa** | Texto | Una lista (concatenada y separada) de identificadores o nombres de registros dwc:Taxon y las asociaciones de este dwc:Occurrence con cada uno de ellos. | "host":"Quercus alba" |
| **otherCatalogNumbers** | Texto | Una lista (concatenada y separada) de números de catálogo completos anteriores o alternativos u otros identificadores utilizados por humanos para la misma dwc:Occurrence, ya sea en el conjunto de datos o colección actual o en cualquier otro. | FMNH:Mammal:1234 |
| **occurrenceRemarks** | Texto | Comentarios o notas sobre dwc:Occurrence. | "Encontrado muerto en el camino" |
| **organismID** | Texto | Un identificador para la instancia dwc:Organism (a diferencia de un registro digital específico de dwc:Organism). Puede ser un identificador único global o un identificador específico del conjunto de datos. | http://arctos.database.museum/guid/WNMU:Mamm:1249 |
| **organismName** | Texto | Un nombre o etiqueta textual asignado a una instancia de dwc:Organism. | Boab Prison Tree |
| **organismScope** | Texto | Descripción del tipo de instancia dwc:Organism. Puede utilizarse para indicar si la instancia dwc:Organism representa un organismo individual o un tipo particular de agregación. | organismo multicelular |
| **associatedOrganisms** | Texto | Una lista (concatenada y separada) de identificadores de otros dwc:Organisms y las asociaciones de este dwc:Organism con cada uno de ellos. | "hermano de":"http://arctos.database.museum/guid/DMNS:Mamm:14171" |
| **previousIdentifications** | Texto | Una lista (concatenada y separada) de asignaciones previas de nombres al dwc:Organism. | Chalepidae <br> Pinus abies |
| **organismRemarks** | Texto | Notas o comentarios sobre una instancia particular de un organismo | "Uno de una camada de seis" |
| **materialEntityID** | Texto | Un identificador para una instancia particular de dwc:MaterialEntity. | 06809dc5-f143-459a-be1a-6f03e63fc083 |
| **materialEntityRemarks** | Texto | Comentarios o notas sobre la instancia dwc:MaterialEntity. | "Encontrado junto a restos carbonizados. Faltan algunos fragmentos originales." |
| **verbatimLabel** | Texto | El contenido de este término no debe incluir adornos, prefijos, encabezados ni otras adiciones al texto. No se deben expandir las abreviaturas ni corregir las supuestas faltas de ortografía. Se pueden usar líneas o puntos de ruptura entre bloques de texto que se puedan verificar consultando las etiquetas originales o sus imágenes. Es la transcripción exacta de lo que el investigador escribió físicamente en el papel o etiqueta sin corregir errores | "ILL: Union Co. Wolf Lake by Powder Plant Bridge. <br> 1 March 1975 Coll. S. Ketzler, S. Herbert <br> Monotoma longicollis 4 ♂ Det TC McElrath 2018 <br> INHS Insect Collection 456782" |
| **materialSampleID** | Texto | Un identificador para dwc:MaterialSample (a diferencia de un registro digital específico de dwc:MaterialSample). En ausencia de un identificador único global persistente, se crea uno a partir de una combinación de identificadores del registro que, en la medida de lo posible, haga que dwc:materialSampleID sea globalmente único. | 06809dc5-f143-459a-be1a-6f03e63fc083 |
| **eventID** | Texto | Un identificador para el conjunto de información asociado con un dwc:Event (algo que ocurre en un lugar y momento determinados). Puede ser un identificador único global o un identificador específico del conjunto de datos. | INBO:VIS:Ev:00009375 |
| **parentEventID** | Texto | Un identificador para el dwc:Event más amplio que agrupa este y potencialmente otros dwc:Events. | A1 (parentEventID para identificar el gráfico principal de Whittaker en muestras anidadas, cada una con su propio eventID - A1:1, A1:2). |
| **eventType** | Texto | La naturaleza del evento dwc:Event. | Muestra <br> Observación <br> Visita al sitio |
| **fieldNumber** | Texto | Un identificador asignado al dwc:Event en el campo. A menudo sirve como enlace entre las notas de campo y el dwc:Event. | RV Sol 87-03-08 |
| **eventDate** | Fecha | Fecha y hora o intervalo durante el cual ocurrió un evento dwc:Event. En el caso de sucesos, esta es la fecha y hora en que se registró el evento dwc:Event. No es adecuado para un período de tiempo en un contexto geológico. | 1906-06 (en el mes de junio de 1906) |
| **eventTime** | Texto | El tiempo o intervalo durante el cual ocurrió un dwc:Evento. | 14:07-06:00 (a partir de las 14:07 y antes de las 14:08 en la zona horaria seis horas anterior a UTC) |
| **startDayOfYear** | Numérico | El primer día (entero) del año en que ocurrió el dwc:Event (1 para el 1 de enero, 365 para el 31 de diciembre, excepto en un año bisiesto, en cuyo caso es 366). | 1 (Enero) <br> 366 (31 de diciembre) |
| **endDayOfYear** | Numérico | El último día (entero) del año en el que ocurrió el dwc:Event (1 para el 1 de enero, 365 para el 31 de diciembre, excepto en un año bisiesto, en cuyo caso es 366). | 32 (1 Febrero) |
| **year** | Numérico | El año de cuatro dígitos en el que ocurrió el dwc:Event, según el Calendario de la Era Común. | 2008 |
| **month** | Numérico | El mes (entero) en el que ocurrió el dwc:Event. | 10 (Octubre) |
| **day** | Numérico | El día (entero) en el que ocurrió el dwc:Event. | 9 <br> 27 |
| **verbatimEventDate** | Texto | La representación original textual de la información de fecha y hora para un dwc:Event. | Primavera 1910 <br> Mayo 2002 |
| **habitat** | Texto | Una categoría o descripción del hábitat en el que ocurrió el evento dwc:Event. | sabana de robles <br> estepa precordillerana |
| **samplingProtocol** | Texto | Los nombres, referencias o descripciones de los métodos o protocolos utilizados durante un dwc:Event. | Pingüinos del espacio: manchas fecales revelan la ubicación de colonias de pingüinos emperador, https://doi.org/10.1111/j.1466-8238.2009.00467.x |
| **sampleSizeValue** | Numérico | Un valor numérico para una medida del tamaño (duración en el tiempo, longitud, área o volumen) de una muestra en un dwc:Evento de muestreo. | 5 (sampleSizeValue) con metro (sampleSizeUnit) |
| **sampleSizeUnit** | Texto | La unidad de medida del tamaño (duración en el tiempo, longitud, área o volumen) de una muestra en un dwc:Event de muestreo. | minuto <br> día <br> metro cúbico |
| **samplingEffort** | Texto | La cantidad de esfuerzo invertido durante un dwc:Event. | m40 noches de trampeo <br> 10 horas de observación |
| **fieldNotes** | Texto | Uno de a) un indicador de la existencia de, b) una referencia a (publicación, URI), o c) el texto de las notas tomadas en el campo sobre el dwc:Event. | Apuntes disponibles en la Biblioteca Grinnell-Miller. |
| **eventRemarks** | Texto | Notas o comentarios sobre el dwc:Event. | "Tras las recientes lluvias, el río está prácticamente desbordado." |
| **locationID** | Texto | Un identificador para el conjunto de información de dcterms:Location. Puede ser un identificador único global o un identificador específico del conjunto de datos. | https://opencontext.org/subjects/768A875F-E205-4D0B-DE55-BAB7598D0FD1 |
| **higherGeographyID** | Texto | Un identificador para la región geográfica dentro de la cual ocurrió el dcterms:Location. | Antártida e Islas del Atlántico Sur, Territorio Nacional de la Tierra del Fuego, Argentina. |
| **higherGeography** | Texto | Una lista (concatenada y separada) de nombres geográficos menos específicos que la información capturada en el atributo dwc:locality. | Océano Atlántico Norte <br> América del Sur, Argentina, Patagonia, Parque Nacional Nahuel Huapi, Neuquén, Los Lagos |
| **continent** | Texto | El nombre del continente en el que se produce el término dcterms:Location. | Africa <br> Antartica <br> Asia |
| **waterBody** | Texto | El nombre del cuerpo de agua en el que ocurre el dcterms:Location. | Océano Índico <br> Mar Báltico <br> Río Hudson |
| **islandGroup** | Texto | El nombre del grupo de islas en el que se produce el término dcterms:Location. | Archipiélago Diego Ramírez |
| **island** | Texto | El código estándar para el país en el que se produce el dcterms:Location. | AR <br> UY |
| **stateProvince** | Texto | El nombre de la siguiente región administrativa más pequeña que el país (estado, provincia, cantón, departamento, región, etc.) en la que ocurre el término dcterms:Location. | Minas Gerais <br> Córdoba |
| **county** | Texto | El nombre completo, sin abreviar, de la siguiente región administrativa más pequeña que el stateProvince (condado, distrito, departamento, etc.) en la que se produce el término dcterms:Location. | Los Lagos <br> Mataró |
| **municipality** | Texto | El nombre completo, sin abreviar, de la región administrativa inmediatamente inferior al condado (ciudad, municipio, etc.) en la que se encuentra la ubicación especificada por dcterms:Location. No utilice este término para un lugar cercano con nombre que no contenga la ubicación especificada por dcterms:Location. | Holzminden <br> Araçatuba |
| **locality** | Texto | La descripción específica del lugar. | Bariloche, 25 km NNE via Ruta Nacional 40 (=Ruta 237) |
| **verbatimLocality** | Texto | La descripción textual original del lugar. | 25 km NNE Bariloche por R. Nac. 237 |
| **verbatimElevation** | Texto | La descripción original de la elevación (altitud, generalmente sobre el nivel del mar) de la ubicación. | 100-200 m |
| **verticalDatum** | Texto | Superficie de referencia de elevación cero para medir alturas y elevacion | "EGM84" |
| **verbatimDepth** | Texto | Para registrar la descripción original y literal de la profundidad a la que se recolectó una muestra | "100-200 m" |
| **minimumDistanceAboveSurfaceInMeters** | Numero | La menor distancia dentro de un rango en dirección vertical, expresada en metros. Valores positivos para ubicaciones por encima de la superficie y valores negativos para ubicaciones por debajo. | "-1.5" "4.2" |
| **maximumDistanceAboveSurfaceInMeters** | Numero | La menor distancia dentro de un rango en dirección vertical, expresada en metros. Valores positivos para ubicaciones por encima de la superficie y valores negativos para ubicaciones por debajo. | "-1.5" "4.2" |
| **locationAccordingTo** | Texto | Información sobre la fuente de esta información de ubicación. Podría ser una publicación, una institución o un grupo de personas. | "GADM" "Getty Thesaurus of Geographic Names" |
| **locationRemarks** | Texto | Comentarios o notas sobre la ubicación. | "under water since 2005" |
| **decimalLatitude** | Numero | La latitud geográfica (en grados)  | "-41.0983423" |
| **decimalLongitude** | Numero | La longitud geográfica (en grados) | "-121.1761111" |
| **coordinateUncertaintyInMeters** | Numero | La distancia horizontal (en metros) que describe el círculo más pequeño que contiene toda la ubicación. Puede estar vacío. Cero no es un valor válido | "30" "100" "71" |
| **coordinatePrecision** | Numero | Una representación decimal de la precisión de las coordenadas dadas en la latitud y longitud | "0.00001" "0.01667" "1.0" |
| **pointRadiusSpatialFit** | Numero | La relación entre el área del radio del punto y el área de la representación espacial verdadera. Los valores válidos son 0, mayor o igual que 1 o indefinido. | "0" "1" "1.5708" |
| **verbatimCoordinateSystem** | Texto | El formato de coordenadas para la latitud y longitud | "decimal degrees" "degrees decimal minutes" "UTM" |
| **verbatimSRS** | Texto | El elipsoide, datum geodésico o sistema de referencia espacial (SRS) sobre el cual se basan las coordenadas dadas | "EPSG:4326" "European 1950" "Campo Inchauspe" "not recorded" |
| **footprintWKT** | Texto | Una representación en formato WKT de la forma (huella, geometría). Puede tener tanto una representación de radio de punto como una representación de huella, y estas pueden diferir entre sí. | "POLYGON ((10 20, 11 20, 11 21, 10 21, 10 20))" |
| **footprintSRS** | Texto | Código EPSG del SRS, si se conoce, o un nombre o código del elipsoid. Si ninguno se conoce se usa el "not recorded" | "EPSG:4326" "GEOGCS["GCS_WGS_1984", DATUM["D_WGS_1984", SPHEROID["WGS_1984",6378137,298.257223563]], PRIMEM["Greenwich",0], UNIT["Degree",0.0174532925199433]]"  "not recorded" |
| **footprintSpatialFit** | Numero | La relación entre el área WKT y el área de la representación espacial verdadera | "0" "1" "1.5708" |
| **georeferencedBy** | Texto | Una lista (concatenada y separada) de nombres de personas o grupos que determinaron la georreferencia (representación espacial) | "Brad Millen (ROM)" "Kristina Yamamoto | Janet Fang"|
| **georeferencedDate** | Numero | La fecha en la que se georreferenció la ubicacion. | "1963-03-08T14:07-06:00" "1809-02-12" "1900/1909" |
| **georeferenceProtocol** | Texto | Una descripción o referencia a los métodos utilizados para determinar la huella espacial, las coordenadas y las incertidumbres. | "Georeferencing Quick Reference Guide (Zermoglio et al. 2020, https://doi.org/10.35035/e09p-h128)" |
| **georeferenceSources** | Texto | Una lista (concatenada y separada) de mapas, nomenclátores u otros recursos utilizados para georreferenciar la ubicación | "USGS 1:24000 Florence Montana Quad 1967 | Terrametrics 2008 on Google Earth" "GeoLocate" |
| **georeferenceRemarks** | Texto | Comentarios o notas sobre la descripción de protocolo | "Assumed distance by road (Hwy. 101)" |
| **geologicalContextID** | Texto | Un identificador para el conjunto de información asociado con un contexto geológico. Puede ser un identificador único global o un identificador específico del conjunto de datos | "https://opencontext.org/subjects/e54377f7-4452-4315-b676-40679b10c4d9" |
| **earliestEonOrLowestEonothem** | Texto | El nombre completo del eón geocronológico más antiguo posible o del eonotema cronoestratigráfico más bajo o el nombre informal | "Phanerozoic" "Proterozoic" |
| **latestEonOrHighestEonothem** | Texto | El nombre completo del último eón geocronológico posible o del eonotema cronoestratigráfico más alto o el nombre informal | "Phanerozoic" "Proterozoic" |
| **earliestEraOrLowestErathem** | Texto | El nombre completo de la era geocronológica más temprana posible o la era cronoestratigráfica más baja atribuible al horizonte estratigráfico del que se recolectó la materia | "Cenozoic" "Mesozoic" |
| **latestEraOrLowestErathem** | Texto | El nombre completo de la última era geocronológica posible o la era cronoestratigráfica más alta atribuible al horizonte estratigráfico del que se recolectó la materia | "Cenozoic" "Mesozoic" |
| **earliestPeriodOrLowestSystem** | Texto | El nombre completo del período geocronológico más antiguo posible o del sistema cronoestratigráfico más bajo atribuible al horizonte estratigráfico del que se recolectó la materia | "Neogene" "Tertiary" "Quaternary" |
| **latestPeriodOrHighestSystem** | Texto | El nombre completo del ultimo período geocronológico posible o del sistema cronoestratigráfico más alto atribuible al horizonte estratigráfico del que se recolectó la materia | "Neogene" "Tertiary" "Quaternary" |
| **earliestEpochOrLowestSeries** | Texto | El nombre completo de la época geocronológica más temprana posible o la serie cronoestratigráfica más baja atribuible al horizonte estratigráfico del que se recolectó la materia | "Holocene" "Pleistocene" "Ibexian Series" |
|**latestEpochOrLowestSeries** | Texto | El nombre completo de la ultima época geocronológica posible o la serie cronoestratigráfica más alta atribuible al horizonte estratigráfico del que se recolectó la materia | "Holocene" "Pleistocene" "Ibexian Series" |
| **earliestAgeOrLowestStage** | Texto | El nombre completo de la edad geocronológica más temprana posible o la etapa cronoestratigráfica más baja atribuible al horizonte estratigráfico del que se recolectó la materia | "Atlantic" "Boreal" "Skullrockian" |
| **latestAgeOrLowestStage** | Texto | El nombre completo de la ultima edad geocronológica posible o la etapa cronoestratigráfica más alta atribuible al horizonte estratigráfico del que se recolectó la materia | "Atlantic" "Boreal" "Skullrockian" |
| **lowestBiostratigraphicZone** | Texto | El nombre completo de la zona bioestratigráfica geológica más baja posible del horizonte estratigráfico del que se recolectó la materia | "Maastrichtian" |
| **highestBiostratigraphicZone** | Texto | El nombre completo de la zona bioestratigráfica geológica más alta posible del horizonte estratigráfico del que se recolectó la materia | "Maastrichtian" |
| **lithostratigraphicTerms** | Texto | La combinación de todos los nombres litoestratigráficos de la roca de la que se extrajo la materia | "Pleistocene-Weichselien" |
| **group** | Texto | El nombre completo del grupo litoestratigráfico del que se extrajo la materia | "Bathurst" "Lower Wealden" |
| **formation** | Texto | El nombre completo de la formación litoestratigráfica de la que se extrajo la materia | "Notch Peak Formation" "House Limestone" "Fillmore Formation" |
| **member** | Texto | El nombre completo del miembro litoestratigráfico del que se extrajo la materia | "Lava Dam Member" "Hellnmaria Member" |
| **bed** | Texto | El nombre completo del estrato litoestratigráfico del que se extrajo la materia | "Harlem coal" |
| **identificationQualifier** | Numero | Un identificador para el campo "Identification". Puede ser un identificador único global o un identificador específico del conjunto de datos | "9992" |
| **verbatimIdentification** | Texto | Una cadena de caracteres que representa la identificación taxonómica tal como aparecía en el registro original | "Peromyscus sp." "Anser anser × Branta canadensis" "Pachyporidae?" |
| **identificationQualifier** | Texto | Una frase breve o un término estándar ("cf.", "aff.") para expresar las dudas del determinante sobre la dwc:Identification | "aff. agrifolia var. oxyadenia (for Quercus aff. agrifolia var. ...(etc)" |
| **typeStatus** | Texto | La práctica recomendada es separar los valores de una lista con un espacio vertical ( | ) | "holotype of Pinus abies | holotype of Picea abies" |
| **identifiedBy** | Texto | Una lista (concatenada y separada) de nombres de personas, grupos u organizaciones que asignaron el Taxon al sujeto. | "James L. Patton| Theodore Pappenfuss | Robert Macey" |
| **identifiedByID** | Texto | Una lista (concatenada y separada) del identificador único global de la persona, personas, grupos u organizaciones responsables de asignar el Taxon al sujeto | "https://orcid.org/0000-0002-1825-0097 | https://orcid.org/0000-0002-1825-0098" |
| **dateIdentified** | Numero | La fecha en la que se determinó que el sujeto representaba el Taxon | "1963-03-08T14:07-06:00" "2018-08-29T15:19" "1971" "1900/1909" |
| **identificationReferences** | Texto | Referencias bibliográficas usadas para identificar el ejemplar | vacío en este dataset |
| **identificationVerificationStatus** | Texto | Estado de verificación de la identificación | vacío en este dataset |
| **identificationRemarks** | Texto | Notas sobre la identificación | vacío en este dataset |
| **taxonID** | Texto | Identificador del taxón en el sistema | vacío en este dataset |
| **scientificNameID** | Texto | Identificador del nombre científico | vacío en este dataset |
| **acceptedNameUsageID** | Texto | ID del nombre aceptado actualmente | vacío en este dataset |
| **parentNameUsageID** | Texto | ID del taxón padre en la jerarquía | vacío en este dataset |
| **originalNameUsageID** | Texto | ID del nombre original con el que fue descripto | vacío en este dataset |
| **nameAccordingToID** | Texto | ID de la fuente que define el concepto del taxón | vacío en este dataset |
| **namePublishedInID** | Texto | ID de la publicación donde se describió el nombre | vacío en este dataset |
| **taxonConceptID** | Texto | Identificador del concepto taxonómico | vacío en este dataset |
| **scientificName** | Texto | Nombre científico completo con autor y fecha | `Chloephaga picta (J.F.Gmelin, 1789)` |
| **acceptedNameUsage** | Texto | Nombre científico aceptado actualmente | vacío en este dataset |
| **parentNameUsage** | Texto | Nombre del taxón padre | vacío en este dataset |
| **originalNameUsage** | Texto | Nombre original con el que fue descripto | vacío en este dataset |
| **nameAccordingTo** | Texto | Fuente que define el concepto del taxón | vacío en este dataset |
| **namePublishedIn** | Texto | Publicación donde se describió el nombre | vacío en este dataset |
| **namePublishedInYear** | Texto | Año de publicación del nombre | vacío en este dataset |
| **higherClassification** | Texto | Clasificación completa del taxón | vacío en este dataset |
| **kingdom** | Texto | Reino | `Animalia` |
| **phylum** | Texto | Filo | `Chordata` |
| **class** | Texto | Clase | `Aves` |
| **order** | Texto | Orden | `Anseriformes` |
| **superfamily** | Texto | Superfamilia | vacío en este dataset |
| **family** | Texto | Familia | `Anatidae` |
| **subfamily** | Texto | Subfamilia | vacío en este dataset |
| **tribe** | Texto | Tribu | vacío en este dataset |
| **subtribe** | Texto | Subtribu | vacío en este dataset |
| **genus** | Texto | Género al que pertenece la especie | `Chloephaga` |
| **genericName** | Texto | Nombre genérico tal cual aparece en el nombre científico | `Chloephaga` |
| **subgenus** | Texto | Subgénero | vacío en este dataset |
| **infragenericEpithet** | Texto | Epíteto infragenérico | vacío en este dataset |
| **specificEpitht** | Texto | Segunda parte del nombre científico, que identifica la especie dentro del género | `picta` |
| **infraspecificEpithet** | Texto | Epíteto infraespecífico para subespecies | vacío en este dataset |
| **cultivarEpithet** | Texto | Nombre del cultivar (solo para plantas cultivadas) | vacío en este dataset |
| **taxonRank** | Texto | Rango taxonómico del registro | `SPECIES` |
| **verbatimTaxonRank** | Texto | Rango taxonómico tal cual fue provisto originalmente | vacío en este dataset |
| **vernacularName** | Texto | Nombre común o popular | vacío en este dataset |
| **nomenclaturalCode** | Texto | Código nomenclatural utilizado | vacío en este dataset |
| **taxonomicStatus** | Texto | Indica si el nombre científico es aceptado, sinónimo o dudoso según las reglas de nomenclatura | `ACCEPTED` |
| **nomenclaturalStatus** | Texto | Estado nomenclatural del nombre | vacío en este dataset |
| **taxonRemarks** | Texto | Notas sobre el taxón | vacío en este dataset |
| **datasetKey** | Texto | Identificador del dataset en GBIF | `a0d072fc-e6be-45d7-9fa8-afa4b38b788a` |
| **publishingCountry** | Texto | País que publicó el dataset | `AR` |
| **lastInterpreted** | Texto | Fecha en que GBIF procesó el registro por última vez | `2025-11-25T07:12:45.267Z` |
| **elevation** | Numérico | Elevación del lugar de registro en metros | vacío en este dataset |
