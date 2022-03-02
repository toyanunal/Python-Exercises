import transport as tp

def test_conveyor_class():
    conveyor = tp.CrateConveyor()
    cmd = ""
    while cmd != 'Q':
        try:
            cap = int(cmd)
        except:
            cap = None
        if cap != None:
            try:
                conveyor.feed(tp.Crate(cap))
            except Exception as x:
                print("Error:", x)
        elif cmd == 'E':
            try:
                conveyor.feed(None)
            except Exception as x:
                print("Error:", x)
        elif cmd == '-':
            try:
                e = conveyor.pick_up()
                print("picked", e)
            except Exception as x:
                print("Error", x)
        else:
            print("Enter Q to quit, - to pick up, any integer to feed new crate")
        print(conveyor, end="")
        cmd = input("Command:").upper()

test_conveyor_class()
