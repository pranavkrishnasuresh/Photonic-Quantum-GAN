def build_discriminator_circuit (circuit, phi_value_list): 

    phi_index = 0

    list = [0,1,2,4,5,6]
    for i in list:
        circuit.add(i, phi_value_list[phi_index])
        phi_index += 1

    circuit.add((0, 1), comp.BS())
    circuit.add((2, 3), comp.BS())
    circuit.add((4, 5), comp.BS())
    circuit.add((6, 7), comp.BS())

    # list lines with phase shift
    list = [0,2,4,6]
    for i in list:
        circuit.add(i, phi_value_list[phi_index])
        phi_index += 1


    circuit.add((0, 1), comp.BS())
    circuit.add((2, 3), comp.BS())
    circuit.add((4, 5), comp.BS())
    circuit.add((6, 7), comp.BS())

    circuit.add((1, 2), comp.BS())
    circuit.add((5, 6), comp.BS())

    # list lines with phase shift
    list = [1,5]
    for i in list:
        circuit.add(i, phi_value_list[phi_index])
        phi_index += 1

    circuit.add((1, 2), comp.BS())
    circuit.add((5, 6), comp.BS())


    pcvl.pdisplay(circuit, skin=SymbSkin())
    
    return circuit
