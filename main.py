from src.bhop import bhop
from src.esp import esp
from utils.output import print_success, print_error
from multiprocessing import Process

def main():
    print_success("tr3x cheat starting...")

    
    # start bhop
    bhop_process = Process(target=bhop)
    bhop_process.start()

    if bhop_process.is_alive():
        print_success("bhop started")
    else:
        print_error("bhop failed to start")


    # start esp
    esp_process = Process(target=esp)
    esp_process.start()

    if esp_process.is_alive():
        print_success("esp started")
    else:
        print_error("esp failed to start")





if __name__ == "__main__":
    main()

    
