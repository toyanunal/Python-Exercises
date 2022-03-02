import assignment3 as tp

def test_crate_class(capacity):
    crate = tp.Crate(capacity)
    cmd = ""
    while cmd != 'Q':
      if cmd > '0' and cmd <= '9':
        try:
            crate.push(int(cmd))
        except Exception as x:
            print("Error:", x)
      elif cmd == '-':
            try:
                e = crate.pop()
                print("popped", e)
            except Exception as x:
                print("Error:", x)
      else:
            print("Enter Q to quit, - to pop, 1 to 9 to push")
      print(crate, end="")
      cmd = input("Command:").upper()

test_crate_class(20)