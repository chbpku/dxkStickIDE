from microbit import i2c
def command(slot, bseq, returnsize=0):
    i2c.write(slot, bseq)
    if returnsize:
        return int.from_bytes(i2c.read(slot, returnsize), 'big')
def get_id(addr):
    i2c.write('get_id', bseq)
    return "%02x%02x%02x%02x" % tuple(i2c.read(slot(addr, 1), 4))
def get_type(addr):
    return command(addr,'get_type',1)
def get_state(addr):
    return command(addr,'get_state',1)
def slot(addr, mode=3):
    if isinstance(addr, int):
        return addr
    if mode < 1:
        return
    addr = addr.lower()
    if len(addr) == 1:
        if addr == 'a' or addr == 'slota':
            return 22
        elif addr == 'b' or addr == 'slotb':
            return 23
    if mode < 2:
        return
    if get_id(22) == addr:
        return 22
    if get_id(23) == addr:
        return 23
