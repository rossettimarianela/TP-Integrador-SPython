import csv

# from validation.validator import (
#     validate_coordinates,
#     validate_coordinate_pair,
#     validate_date,
#     validate_duplicates,
#     validate_country_code,
#     validate_coordinate_uncertainty
# )

def get_headers(filepath, delimiter):
    """
    Lee el archivo csv y retorna una lista con los headers (nombres de columnas).
    """
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter)
        headers = next(reader)  # Leer la primera fila para obtener los headers
    return headers

# 4a - 4b
def get_empty_record(filepath, delimiter):
    """
    Crea un diccionario con las claves correspondientes a los headers del csv y valores vacíos.
    """
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        columns = reader.fieldnames
    return {col: "" for col in columns} # Crear un diccionario con claves de los headers y valores vacíos

# 4c - VALIDADOR

# def validate_record(record):
#     """
#     Valida un registro antes de insertarlo
#     """
#     errors = []
#     errors += validate_coordinates(record["decimalLatitude"], record["decimalLongitude"])
#     errors += validate_coordinate_pair(record["decimalLatitude"], record["decimalLongitude"])
#     errors += validate_date(record["eventDate"])
#     errors += validate_duplicates(record["occurrenceID"])
#     errors += validate_country_code(record["countryCode"])
#     errors += validate_coordinate_uncertainty(record["coordinateUncertaintyInMeters"])

#     if errors:
#         print("El registro tiene los siguientes errores:")
#         for error in errors:
#             print(f"  - {error}")
#         return False

#     return True


def record_to_row(record, input_path, output_path, delimiter):
    """
    Convierte un diccionario de registro a una fila lista para escribir en el csv.
    Asegura que los campos estén en el orden correcto según los headers del csv.
    """
    columns = get_headers(input_path, delimiter)
    id_column = columns[0]
    last_id = 0

    import os
    if os.path.exists(output_path): # Verificar si el archivo existe para asignar un nuevo ID porque sino no incrementa el ID
        with open(output_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row in reader:
                value = row.get(id_column, "")
                if value != "":
                    try:
                        # Caso Xeno-canto ID con formato "12345@67890", tomar solo la parte numérica antes del "@"
                        if "@" in value:
                            number = int(value.split("@")[0])
                        else:
                            number = int(value)

                        if number > last_id:
                            last_id = number
                    except:
                        pass # Ignorar valores no numéricos en la columna de ID
    if last_id == 0: # Si el archivo de salida no existe o no tiene registros, revisar el archivo de entrada para asignar el nuevo ID (el de raw_datasets)
        with open(input_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row in reader:
                value = row.get(id_column, "")
                if value != "":
                    try:
                        if "@" in value:
                            number = int(value.split("@")[0])
                        else:
                            number = int(value)

                        if number > last_id:
                            last_id = number
                    except:
                        pass
    new_number = last_id + 1
    if "xeno" in str(input_path).lower(): # Si el dataset es Xeno-canto, el nuevo ID se formatea como "12345@XC"
        new_id = str(new_number) + "@XC"
    else:
        new_id = str(new_number)

    record[id_column] = new_id
    row = []
    for col in columns:
        row.append(record.get(col, ""))

    return row

# 4d - INSERT RECORDS

def insert_record(input_path, output_path, delimiter):
    """
    Insertar un nuevo registro
    """

    columns = get_headers(input_path, delimiter)
    record = get_empty_record(input_path, delimiter)

    print("\nIngrese los valores para el nuevo registro: (Enter para dejar vacío)")

    for col in columns:
        if col == columns[0]:  # Saltar la columna de ID, se asigna automáticamente
            continue
        value = input(f"{col}: ")  # Pedir al usuario que ingrese el valor para esta columna
        record[col] = value.strip()  # Guardar el valor ingresado en el registro, eliminando espacios extra


    # if not validate_record(record):  # Validar el registro antes de insertarlo
    #     print("No se pudo agregar el registro debido a errores de validación.")
    #     return


    # Convertir el registro a una fila lista para escribir en el csv
    row = record_to_row(record, input_path, output_path, delimiter)


    # Verificar si el archivo de salida ya existe
    import os
    file_exists = os.path.exists(output_path)


    # Abrir el archivo en modo 'a' (append) Si no existe, se crea automáticamente
    with open(output_path, 'a', encoding='utf-8', newline='') as f_output:
        writer = csv.writer(f_output, delimiter=delimiter)

        # Si el archivo no existía, escribir primero los headers
        if not file_exists:
            headers = get_headers(input_path, delimiter)
            writer.writerow(headers)

        # Escribir la nueva fila al final del csv
        writer.writerow(row)


    print(f"Registro agregado correctamente en {output_path}.")


def insert_multiple_records(input_path, output_path, delimiter):
    """
    Insertar múltiples registros
    """

    keep_going = "y"
    while keep_going.lower() == "y":
        insert_record(input_path, output_path, delimiter)
        keep_going = input("\nQuiere agregar otro registro? (y/n): ")