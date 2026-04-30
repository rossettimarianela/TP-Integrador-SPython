from src.config.dataset_config import (
    IADIZA_INPUT,
    IADIZA_OUTPUT,
    XENO_INPUT,
    XENO_OUTPUT,
    INATURALIST_INPUT,
    INATURALIST_OUTPUT,
    IADIZA_DELIMITER,
    XENO_DELIMITER,
    INATURALIST_DELIMITER
)

from src.insert.insert import (
    insert_record,
    insert_multiple_records
)


def run_menu():
    print("Select dataset:")
    print("1. IADIZA")
    print("2. Xeno-canto")
    print("3. iNaturalist")

    dataset = input("Ingresa el número del dataset: ")

    if dataset == "1":
        input_path = IADIZA_INPUT
        output_path = IADIZA_OUTPUT
        delimiter = IADIZA_DELIMITER

    elif dataset == "2":
        input_path = XENO_INPUT
        output_path = XENO_OUTPUT
        delimiter = XENO_DELIMITER

    elif dataset == "3":
        input_path = INATURALIST_INPUT
        output_path = INATURALIST_OUTPUT
        delimiter = INATURALIST_DELIMITER

    else:
        print("Opción inválida.")
        return

    print("\nQue queres hacer?")
    print("1. Agregar un nuevo registro")
    print("2. Agregar múltiples registros")

    option = input("Ingresa el número de la opción: ")

    if option == "1":
        insert_record(input_path, output_path, delimiter)

    elif option == "2":
        insert_multiple_records(input_path, output_path, delimiter)

    else:
        print("Opción inválida.")


if __name__ == "__main__":
    run_menu()