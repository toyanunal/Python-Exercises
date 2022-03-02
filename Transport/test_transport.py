import transport as tp

def test_transport_system(capacities):
    transport = tp.TransportSystem(capacities)
    cmd = ""
    while cmd != 'Q':
        if cmd > '0' and cmd <= '9':
            try:
                if not transport.add(int(cmd)):
                    print("could not add plate")
            except Exception as x:
                print("Error:", x)
        elif cmd == 'E':
            try:
                transport.add(None)
            except Exception as x:
                print("Error:", x)
        elif cmd == '-':
            e = transport.remove()
            if e == 0:
                print("nothing removed")
            else:
                print("removed", e)
        else:
            print("Enter Q to quit, - to pick up, any integer to feed new crate")
        print(transport, end="")
        cmd = input("Command:").upper()

test_transport_system([9, 20, 10, 15])