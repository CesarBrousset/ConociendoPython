{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "None\n",
      "El año 2000 no es bisiesto\n",
      "El año 1900 no es bisiesto\n"
     ]
    }
   ],
   "source": [
    "#Consigna: Realizar una función llamada año_bisiesto:\n",
    "\n",
    "#Recibirá un año por parámetro\n",
    "#Imprimirá “El año año es bisiesto” si el año es bisiesto\n",
    "#Imprimirá “El año año no es bisiesto” si el año no es bisiesto\n",
    "#Si se ingresa algo que no sea número debe indicar que se ingrese un número.\n",
    "\n",
    "#Se recuerda que los años bisiestos son múltiplos de 4, \n",
    "# pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. \n",
    "# Estos son algunos ejemplos de posibles respuestas: \n",
    "# 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.\n",
    "\n",
    "\n",
    "def identificar_si_el_año_es_bisiesto(dato):\n",
    "    if dato % 4 == 0 and dato % 100 == 0:\n",
    "        return f'El año {dato} no es bisiesto'\n",
    "    else: \n",
    "        pass\n",
    "    if dato % 4 == 0 and dato % 400 == 0:\n",
    "        return f'El año {dato} es bisiesto'\n",
    "    else:\n",
    "       'debe ingresar un número'\n",
    "\n",
    "    \n",
    "año = identificar_si_el_año_es_bisiesto(2012)\n",
    "print(año)\n",
    "año = identificar_si_el_año_es_bisiesto(2010)\n",
    "print(año)\n",
    "año = identificar_si_el_año_es_bisiesto(2000)\n",
    "print(año)\n",
    "año = identificar_si_el_año_es_bisiesto(1900)\n",
    "print(año)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.5 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "2406143cb3293c6f26dd99450e8195f7bd25a7328b6e4b716954e94e61f82fa7"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
