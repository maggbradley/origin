import HW
def main():
    handler_list = {
        "HW": HW.handler,

    }
    handler_to_run = "HW"
    handler_list[handler_to_run]()


if __name__ == "__main__":
    main()

