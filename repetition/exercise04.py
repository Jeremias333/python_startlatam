n_term = int(input("Quantos termos devemos calcular na sequencia de fibonacci: "))

_next = 0
_preview = 0
for x in range (1, n_term):
    print(_next)
    _next = _next + _preview
    _preview = _next - _preview
    if(_next == 0):
        _next += 1




