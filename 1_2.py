num_ss = int(input('Введите число в секундах, но не более 86399, т.к. оно равно 1 суткам = '))

hh = num_ss // 3600
mm = num_ss // 60 - hh * 60
ss = num_ss % 60

print('Время в формате чч:мм:сс')
print('   ', hh, ':  ', mm, ':  ', ss)

print(' Или, используя форматирование с выравниванием по левой стороне ')

print("%-6s %-6s %-6s" % ('hh', 'mm', 'ss'))
print("%-6s %-6s %-6s" % (hh, mm, ss))
