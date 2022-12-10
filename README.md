# huffman_coding
Project to show how huffman coding works.

URL to check [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding).
It is used for lossless data compression.

## Example 1 (It build frequency dict using input data to encode)
```
Cadena original:  Electronica y comunicaciones

Codificando en bytes:  b'\x08\xe7l\x9cZ\xf2\xb7:8ayG\xb5r\x00'
Decodificado:  Electronica y comunicaciones

Tabla resumen ordenado por probabilidad
CARACTER  FRECUENCIA     PROBABILIDAD             CODIGO    NUM_DE_BITS
c         5              0.17857142857142858      00        2
n         3              0.10714285714285714      010       3
o         3              0.10714285714285714      011       3
i         3              0.10714285714285714      1111      4
a         2              0.07142857142857142      1010      4
e         2              0.07142857142857142      1011      4
          2              0.07142857142857142      1101      4
m         1              0.03571428571428571      10000     5
r         1              0.03571428571428571      10001     5
s         1              0.03571428571428571      10010     5
t         1              0.03571428571428571      10011     5
u         1              0.03571428571428571      11000     5
y         1              0.03571428571428571      11001     5
E         1              0.03571428571428571      11100     5
l         1              0.03571428571428571      11101     5

Arbol de huffman en formato json
{
    "char": null,
    "freq": 28,
    "left": {
        "char": null,
        "freq": 11,
        "left": {
            "char": "c",
            "freq": 5,
            "left": null,
            "right": null
        },
        "right": {
            "char": null,
            "freq": 6,
            "left": {
                "char": "n",
                "freq": 3,
                "left": null,
                "right": null
            },
            "right": {
                "char": "o",
                "freq": 3,
                "left": null,
                "right": null
            }
        }
    },
    "right": {
        "char": null,
        "freq": 17,
        "left": {
            "char": null,
            "freq": 8,
            "left": {
                "char": null,
                "freq": 4,
                "left": {
                    "char": null,
                    "freq": 2,
                    "left": {
                        "char": "m",
                        "freq": 1,
                        "left": null,
                        "right": null
                    },
                    "right": {
                        "char": "r",
                        "freq": 1,
                        "left": null,
                        "right": null
                    }
                },
                "right": {
                    "char": null,
                    "freq": 2,
                    "left": {
                        "char": "s",
                        "freq": 1,
                        "left": null,
                        "right": null
                    },
                    "right": {
                        "char": "t",
                        "freq": 1,
                        "left": null,
                        "right": null
                    }
                }
            },
            "right": {
                "char": null,
                "freq": 4,
                "left": {
                    "char": "a",
                    "freq": 2,
                    "left": null,
                    "right": null
                },
                "right": {
                    "char": "e",
                    "freq": 2,
                    "left": null,
                    "right": null
                }
            }
        },
        "right": {
            "char": null,
            "freq": 9,
            "left": {
                "char": null,
                "freq": 4,
                "left": {
                    "char": null,
                    "freq": 2,
                    "left": {
                        "char": "u",
                        "freq": 1,
                        "left": null,
                        "right": null
                    },
                    "right": {
                        "char": "y",
                        "freq": 1,
                        "left": null,
                        "right": null
                    }
                },
                "right": {
                    "char": " ",
                    "freq": 2,
                    "left": null,
                    "right": null
                }
            },
            "right": {
                "char": null,
                "freq": 5,
                "left": {
                    "char": null,
                    "freq": 2,
                    "left": {
                        "char": "E",
                        "freq": 1,
                        "left": null,
                        "right": null
                    },
                    "right": {
                        "char": "l",
                        "freq": 1,
                        "left": null,
                        "right": null
                    }
                },
                "right": {
                    "char": "i",
                    "freq": 3,
                    "left": null,
                    "right": null
                }
            }
        }
    }
}

Longitud promedio
3.714285714285713  bits por simbolo
Entropia
3.668986958453061
Eficiencia
0.9878041811219783
```

## Example 2 (It uses a frequency dict precalculated)
```
Cadena original:  EDCML

Codificando en bytes:  b'\x08^\xfe\x00'
Decodificado:  EDCML

Tabla resumen ordenado por probabilidad
CARACTER  FRECUENCIA     PROBABILIDAD             CODIGO    NUM_DE_BITS
E         120            0.39215686274509803      0         1
D         42             0.13725490196078433      101       3
L         42             0.13725490196078433      110       3
U         37             0.12091503267973856      100       3
C         32             0.10457516339869281      1110      4
M         24             0.0784313725490196       11111     5
K         7              0.02287581699346405      111101    6
Z         2              0.006535947712418301     111100    6

Arbol de huffman en formato json
{
    "char": null,
    "freq": 306,
    "left": {
        "char": "E",
        "freq": 120,
        "left": null,
        "right": null
    },
    "right": {
        "char": null,
        "freq": 186,
        "left": {
            "char": null,
            "freq": 79,
            "left": {
                "char": "U",
                "freq": 37,
                "left": null,
                "right": null
            },
            "right": {
                "char": "D",
                "freq": 42,
                "left": null,
                "right": null
            }
        },
        "right": {
            "char": null,
            "freq": 107,
            "left": {
                "char": "L",
                "freq": 42,
                "left": null,
                "right": null
            },
            "right": {
                "char": null,
                "freq": 65,
                "left": {
                    "char": "C",
                    "freq": 32,
                    "left": null,
                    "right": null
                },
                "right": {
                    "char": null,
                    "freq": 33,
                    "left": {
                        "char": null,
                        "freq": 9,
                        "left": {
                            "char": "Z",
                            "freq": 2,
                            "left": null,
                            "right": null
                        },
                        "right": {
                            "char": "K",
                            "freq": 7,
                            "left": null,
                            "right": null
                        }
                    },
                    "right": {
                        "char": "M",
                        "freq": 24,
                        "left": null,
                        "right": null
                    }
                }
            }
        }
    }
}

Longitud promedio
2.565359477124183  bits por simbolo
Entropia
2.4854208688808206
Eficiencia
0.9688392176783834
```
