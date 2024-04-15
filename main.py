from Hub import *
from Hub import Device
from Physical_Layer import physicalLayer
from Data_link_layer import Data_link_layer

def main():
    SD_Data, SourceDevice = physicalLayer()
    print("*" * 60)
    print("Entering into Data Link Layer part\n")
    SD_Data = Data_link_layer(SD_Data, SourceDevice)

if __name__ == "__main__":
    main()