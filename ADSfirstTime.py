import pyads

AMSNETID = ""

plc = pyads.Connection(AMSNETID, pyads.PORT_TC3PLC1)
plc.open()
print(f"Connected?: {plc.is_open}") #debugging statement, optional
print(f"Local Address? : {plc.get_local_address()}") # debugging statement, optional
print(plc.read_state())

bOut1 = plc.read_by_name("GVL.bOut1")
print(f"bOut1 State {bOut1}")

plc.write_by_name("GVL.bOut1", True) #override values

bOut1 = plc.read_by_name("GVL.bOut1") #reads to confirm
print(f"Final state {bOut1}")

plc.close()