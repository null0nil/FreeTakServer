#######################################################
# 
# XMLCoTController.py
# Python implementation of the Class XMLCoTController
# Generated by Enterprise Architect
# Created on:      20-May-2020 1:07:38 PM
# Original author: Natha Paquette
# 
#######################################################
#TODO: add more rigid exception management

class XMLCoTController:
    def __init__(self):  
        pass

    def determineCoTGeneral(self, data):
        # this will establish the CoTs general type
        if type(data) == type([]):
            #this handels the event of a connection CoT
            serializedData = []
            try:
                for value in data:
                    serializedData.append(value)
                return ("clientConnected", serializedData)

            except Exception as e:
                print("exception in monitor raw 3")
        #this runs if it is infact regular data
        elif data.xmlString == b'' or data.xmlString == None:
            #this handeles a client dissconection CoT
            return ("clientDisconnected", data)
        else:
            #this is the default in the event of an generic CoT or a CoT without a specific associated use case in the orchestrator
            try:

                return ("dataRecieved", data)

            except Exception as e:
                print('exception in monitor raw 4')
                print(e)

    def determineCoTType(self, RawCoT):
        # this function is to establish which specific controller applys to the CoT if any
        xml = RawCoT.xmlString
        # TODO: the below if statement is probably unnecessary but this needs to be verified
        if RawCoT == b'' or RawCoT == None:
            RawCoT.disconnect = 1
            return RawCoT
        # TODO: this needs to be expanded for more use cases
        else:
            CoTTypes = {
                        "*": "SendOtherController"
                        }
            RawCoT.CoTType = CoTTypes['*']
            return RawCoT

    def findCallsign(self):
        pass

    def findMarti(self):
        pass

    def findUID(self):
        pass