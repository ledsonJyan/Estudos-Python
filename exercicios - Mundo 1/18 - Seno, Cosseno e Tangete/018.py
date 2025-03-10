import math
an=float(input('Digite um angulo:'))
sen=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print('O Seno do angulo de {} é: {:.2f}'.format(an,sen))
print('O Cosseno do angulo de {} é: {:.2f}'.format(an,cos))
print( 'A Tangente do angulo de {} é: {:.2f}'.format(an,tan))