
print("USB sticks cost: £6",
      "\nCurrent Balance: £50")
usb = 6
cb = 50

totalUSB = int(cb/usb)
balanceLeft = cb-(totalUSB*usb)
print("Total USB that can be bought with current balance: ",totalUSB,"USB Sticks",
      "\nTotal balance remaining: £", balanceLeft)