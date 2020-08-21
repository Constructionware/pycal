# pycal/library.py

class Library:
    cmulib:dict = {
            "150": {
                "type": "cmu-150",
                "thickness": 150,
                "cmu": {
                "vol": 1,
                "unit": "mm",
                "length": 400,
                "height": 200,
                "breadth": 150,
                "kg": 0,
                 "lb": 0,
                "cores": 2,
                "corevolume":0,
                "mortar": 0
                },
                "volume":0

            },
            "200": {
                "type": "cmu-200",
                "vol": 1,
                "unit": "mm",
                "length": 400,
                "height": 200,
                "thickness": 200,
                "kg": 0,
                 "lb": 0,
                "volume":0
                },
            "250": {
                "type": "cmu-250",
                "vol": 1,
                "unit": "mm",
                "length": 400,
                "height": 200,
                "thickness": 250,
                "kg": 0,
                 "lb": 0,
                "volume":0
                },
                "note": """General Cmu Notes"""
    }
    sheetrocklib:dict = {
            "75": {
                "type": "drywall-75",
                "thickness": 75,
                "sheetrock": {
                "vol": 1,
                "unit": "mm",
                "length": 2400,
                "bredth": 1200,
                "thickness": 15,
                "kg": 0,
                 "lb": 0,
                "layers": 1,
                "compound": 1.2,
                "screws": 36,
                "tape": 7200
                },
                "estimate":{}

            },
            "100": {
                "type": "drywall-100",
                "thickness": 100,
                "sheetrock": {
                "vol": 1,
                "unit": "mm",
                "length": 2400,
                "bredth": 1200,
                "thickness": 15,
                "kg": 0,
                 "lb": 0,
                "layers": 1,
                "compound": 1.2,
                "screws": 36,
                "tape": 7200
                },
                "estimate":{}

            },
            "150": {
                "type": "drywall-150",
                "thickness": 150,
                "sheetrock": {
                "vol": 1,
                "unit": "mm",
                "length": 2400,
                "bredth": 1200,
                "thickness": 15,
                "kg": 0,
                 "lb": 0,
                "layers": 1,
                "compound": 1.2,
                "screws": 36,
                "tape": 7200
                },
                "estimate":{}

            },

            "note": """General Sheet Rock  Notes"""
    }
    structuralnotes:dict = {
        "category": "concrete",
      "title": "Concrete Mix Design",
      "notes": "Concrete mix design is the process of finding right proportions of cement, sand and aggregates for concrete to achieve target strength in structures. So, concrete mix design can be stated as Concrete Mix = Cement:Sand:Aggregates. Benefits of concrete mix design is that it provides the right proportions of materials, thus making the concrete construction economical in achieving required strength of structural members. As, the quantity of concrete required for large constructions are huge, economy in quantity of materials such as cement makes the project construction economical.",
      "design_specification": {
        "curing": {
          "period": 28,
          "unit": "days"
        },
        "grades": [
          "M20",
          "M25",
          "M30"
        ]
      },
      "grades": {
        "m20": {
          "mix_ratio": "",
          "quality_controll": [
            "ASTM-",
            "BSC-",
            "CIB",
            "IS:456"
          ],
          "exposure": "Mild",
          "placement_method": "pumpable",
          "curing": {
            "period": 28,
            "unit": "days"
          },
          "cement": {
            "type": "Portland Cement",
            "quality_controll": [
              "ASTM-",
              "BSC-",
              "CIB",
              "IS:455"
            ],
            "specific_gravity": 3.15
          },
          "aggregates": {
            "nominal": {
              "type": "crushed stone",
              "condition": "saturated, surface dry",
              "shape": "angular",
              "specific_gravity": 2.84,
              "quality_controll": [
                "ASTM-",
                "BSC-",
                "CIB",
                "IS:Z II 383"
              ],
              "size": {
                "d": 20,
                "unit": "mm"
              }
            },
            "fine": {
              "quality_controll": [
                "ASTM-",
                "BSC-",
                "CIB",
                "IS:Z II 383"
              ],
              "type": "washed sand",
              "shape": "n/a",
              "size": {
                "d": 0.5,
                "unit": "mm"
              },
              "specific_gravity": 2.64,
              "condition": "saturated, surface dry"
            }
          },
          "slump": {
            "min": 50,
            "max": 75,
            "unit": "mm"
          },
          "mix_procedure": {
            "quality_controll": [
              "T1 of IS10262-2009"
            ],
            "h_constant": "5%",
            "risk_factor": 1.65,
            "standard_deviation": 4,
            "target_strength": {
              "formula": "tg = Fck + (Rf * Sd)",
              "calculation": "ts = 20 + (1.65 * 4)",
              "value": 26.6,
              "unit": "N/mm2"
            },
            "water_ratio": {
              "quality_controll": [
                "ASTM",
                "BSC",
                "IS456",
                "T2 of IS10262-2009"
              ],
              "condition": "mild",
              "max": 0.55,
              "min": 0.5
            },
            "aggregate_content": {
              "notes": {
                "n1": "For every ±0.05 change in w/c, the coarse aggregate proportion is to be changed by 0.01. If the w/c is less than 0.5 (standard value), volume of coarse aggregate is required to be increased to reduce the fine aggregate content. If the w/c is more than 0.5, volume of coarse aggregate is to be reduced to increase the fine aggregate content. If coarse aggregate is not angular, volume of coarse aggregate may be required to be increased suitably, based on experience.",
                "n2": "For pump able concrete or congested reinforcement the coarse aggregate proportion may be reduced up to 10%.",
                "n3": "Volume of coarse aggregate per unit volume of total aggregate = 0.62 x 90% = 0.558"
              },
              "volume": {
                "formula": "Volume of total aggregates = a – (b + c ) = Volume of Concrete – (0.122 + 0.1916) ",
                "unit": "m3"
              },
              "nominal": {
                "size": "20mm",
                "shape": "angular",
                "volume": {
                  "formula": "Mass of coarse aggregates = total Volume of Aggreates x 0.558 x 2.84 x 1000",
                  "unit": "kg/m3"
                }
              },
              "fine": {
                "size": "0.5mm",
                "shape": "n/a",
                "volume": {
                  "formula": "Volume of fine aggregate = Volume of Concrete  – Volume of Coarse Aggregates",
                  "unit": "m3"
                },
                "mass": {
                  "formula": "Mass of fine aggregates = total Volume of Aggreates  0.442 x 2.64 x 1000 ",
                  "unit": "kg/m3"
                }
              }
            },
            "cement_content": {
              "note": "Minimum cement Content for mild exposure condition = 260 kg/m3",
              "volume": {
                "min": 260,
                "max": 300,
                "unit": "kg/m3",
                "formula": "Volume of cement = (Mass of cement / Specific gravity of cement) x (Volume of Concrete / 100)"
              },
              "water_cement_ratio": 0.5,
              "water_content": {
                "value": 191.6,
                "unit": "kg/m3"
              }
            },
            "max_water_content": {
              "note": "Maximum water content = 186 Kg (for Nominal maximum size of aggregate — 20 mm)",
              "volume": {
                "formula": "Volume of water = (Mass of water / Specific gravity of water) x (Volume of Concrete / 1000)",
                "unit": "m3"
              }
            }
          }
        },
        "m25": {
          "mix_ratio": "",
          "quality_controll": [
            "ASTM-",
            "BSC-",
            "CIB",
            "IS:456"
          ],
          "exposure": "Mild",
          "placement_method": "pumpable",
          "curing": {
            "period": 28,
            "unit": "days"
          },
          "cement": {
            "type": "Portland Cement",
            "quality_controll": [
              "ASTM-",
              "BSC-",
              "CIB",
              "IS:455"
            ],
            "specific_gravity": 3.15
          },
          "aggregates": {
            "nominal": {
              "type": "crushed stone",
              "condition": "saturated, surface dry",
              "shape": "angular",
              "specific_gravity": 2.84,
              "quality_controll": [
                "ASTM-",
                "BSC-",
                "CIB",
                "IS:Z II 383"
              ],
              "size": {
                "d": 20,
                "unit": "mm"
              }
            },
            "fine": {
              "quality_controll": [
                "ASTM-",
                "BSC-",
                "CIB",
                "IS:Z II 383"
              ],
              "type": "washed sand",
              "shape": "n/a",
              "size": {
                "d": 0.5,
                "unit": "mm"
              },
              "specific_gravity": 2.64,
              "condition": "saturated, surface dry"
            }
          },
          "slump": {
            "min": 50,
            "max": 75,
            "unit": "mm"
          },
          "mix_procedure": {
            "quality_controll": [
              "T1 of IS10262-2009"
            ],
            "h_constant": "5%",
            "risk_factor": 1.65,
            "standard_deviation": 4,
            "target_strength": {
              "formula": "tg = Fck + (Rf * Sd)",
              "calculation": "ts = 25 + (1.65 * 4)",
              "value": 31.6,
              "unit": "N/mm2"
            },
            "water_ratio": {
              "quality_controll": [
                "ASTM",
                "BSC",
                "IS456",
                "T2 of IS10262-2009"
              ],
              "condition": "mild",
              "max": 0.55,
              "min": 0.5
            },
            "aggregate_content": {
              "notes": {
                "n1": "For every ±0.05 change in w/c, the coarse aggregate proportion is to be changed by 0.01. If the w/c is less than 0.5 (standard value), volume of coarse aggregate is required to be increased to reduce the fine aggregate content. If the w/c is more than 0.5, volume of coarse aggregate is to be reduced to increase the fine aggregate content. If coarse aggregate is not angular, volume of coarse aggregate may be required to be increased suitably, based on experience.",
                "n2": "For pump able concrete or congested reinforcement the coarse aggregate proportion may be reduced up to 10%.",
                "n3": "Volume of coarse aggregate per unit volume of total aggregate = 0.62 x 90% = 0.558"
              },
              "volume": {
                "formula": "Volume of total aggregates = a – (b + c ) = Volume of Concrete – (0.122 + 0.1916) ",
                "unit": "m3"
              },
              "nominal": {
                "size": "20mm",
                "shape": "angular",
                "volume": {
                  "formula": "Mass of coarse aggregates = total Volume of Aggreates x 0.558 x 2.84 x 1000",
                  "unit": "kg/m3"
                }
              },
              "fine": {
                "size": "0.5mm",
                "shape": "n/a",
                "volume": {
                  "formula": "Volume of fine aggregate = Volume of Concrete  – Volume of Coarse Aggregates",
                  "unit": "m3"
                },
                "mass": {
                  "formula": "Mass of fine aggregates = total Volume of Aggreates  0.442 x 2.64 x 1000 ",
                  "unit": "kg/m3"
                }
              }
            },
            "cement_content": {
              "note": "Minimum cement Content for mild exposure condition = 300 kg/m3",
              "volume": {
                "min": 300,
                "max": 450,
                "unit": "kg/m3",
                "formula": "Volume of cement = (Mass of cement / Specific gravity of cement) x (Volume of Concrete / 100)"
              },
              "water_cement_ratio": 0.5,
              "water_content": {
                "value": 191.6,
                "unit": "kg/m3"
              }
            },
            "max_water_content": {
              "note": "Maximum water content = 186 Kg (for Nominal maximum size of aggregate — 20 mm)",
              "volume": {
                "formula": "Volume of water = (Mass of water / Specific gravity of water) x (Volume of Concrete / 1000)",
                "unit": "m3"
              }
            }
          }
        },
        "m30": {
          "mix_ratio": "",
          "quality_controll": [
            "ASTM-",
            "BSC-",
            "CIB",
            "IS:456"
          ],
          "exposure": "Mild",
          "placement_method": "pumpable",
          "curing": {
            "period": 28,
            "unit": "days"
          },
          "cement": {
            "type": "Portland Cement",
            "quality_controll": [
              "ASTM-",
              "BSC-",
              "CIB",
              "IS:455"
            ],
            "specific_gravity": 3.15
          },
          "aggregates": {
            "nominal": {
              "type": "crushed stone",
              "condition": "saturated, surface dry",
              "shape": "angular",
              "specific_gravity": 2.84,
              "quality_controll": [
                "ASTM-",
                "BSC-",
                "CIB",
                "IS:Z II 383"
              ],
              "size": {
                "d": 20,
                "unit": "mm"
              }
            },
            "fine": {
              "quality_controll": [
                "ASTM-",
                "BSC-",
                "CIB",
                "IS:Z II 383"
              ],
              "type": "washed sand",
              "shape": "n/a",
              "size": {
                "d": 0.5,
                "unit": "mm"
              },
              "specific_gravity": 2.64,
              "condition": "saturated, surface dry"
            }
          },
          "slump": {
            "min": 50,
            "max": 75,
            "unit": "mm"
          },
          "mix_procedure": {
            "quality_controll": [
              "T1 of IS10262-2009"
            ],
            "h_constant": "5%",
            "risk_factor": 1.65,
            "standard_deviation": 4,
            "target_strength": {
              "formula": "tg = Fck + (Rf * Sd)",
              "calculation": "ts = 30 + (1.65 * 4)",
              "value": 36.6,
              "unit": "N/mm2"
            },
            "water_ratio": {
              "quality_controll": [
                "ASTM",
                "BSC",
                "IS456",
                "T2 of IS10262-2009"
              ],
              "condition": "mild",
              "max": 0.55,
              "min": 0.5
            },
            "aggregate_content": {
              "notes": {
                "n1": "For every ±0.05 change in w/c, the coarse aggregate proportion is to be changed by 0.01. If the w/c is less than 0.5 (standard value), volume of coarse aggregate is required to be increased to reduce the fine aggregate content. If the w/c is more than 0.5, volume of coarse aggregate is to be reduced to increase the fine aggregate content. If coarse aggregate is not angular, volume of coarse aggregate may be required to be increased suitably, based on experience.",
                "n2": "For pump able concrete or congested reinforcement the coarse aggregate proportion may be reduced up to 10%.",
                "n3": "Volume of coarse aggregate per unit volume of total aggregate = 0.62 x 90% = 0.558"
              },
              "volume": {
                "formula": "Volume of total aggregates = a – (b + c ) = Volume of Concrete – (0.122 + 0.1916) ",
                "unit": "m3"
              },
              "nominal": {
                "size": "20mm",
                "shape": "angular",
                "volume": {
                  "formula": "Mass of coarse aggregates = total Volume of Aggreates x 0.558 x 2.84 x 1000",
                  "unit": "kg/m3"
                }
              },
              "fine": {
                "size": "0.5mm",
                "shape": "n/a",
                "volume": {
                  "formula": "Volume of fine aggregate = Volume of Concrete  – Volume of Coarse Aggregates",
                  "unit": "m3"
                },
                "mass": {
                  "formula": "Mass of fine aggregates = total Volume of Aggreates  0.442 x 2.64 x 1000 ",
                  "unit": "kg/m3"
                }
              }
            },
            "cement_content": {
              "note": "Minimum cement Content for mild exposure condition = 300 kg/m3",
              "volume": {
                "min": 300,
                "max": 450,
                "unit": "kg/m3",
                "formula": "Volume of cement = (Mass of cement / Specific gravity of cement) x (Volume of Concrete / 100)"
              },
              "water_cement_ratio": 0.5,
              "water_content": {
                "value": 191.6,
                "unit": "kg/m3"
              }
            },
            "max_water_content": {
              "note": "Maximum water content = 186 Kg (for Nominal maximum size of aggregate — 20 mm)",
              "volume": {
                "formula": "Volume of water = (Mass of water / Specific gravity of water) x (Volume of Concrete / 1000)",
                "unit": "m3"
              }
            }
          }
        }
      }
    }
    soilnotes:dict = {
      "notes": {
        "n1": "Bearing capacity of soil is the maximum load per unit area. This is the ultimate bearing capacity of soil shown in table. Dividing the ultimate soil bearing capacity by a safety factor we get the maximum safe bearing capacity of soil for design of foundations.",
        "n2": "The safe bearing capacity value may be increased by an amount equal to weight of the material removed from above the bearing level that is the base of foundation."
      },
      "soil_types": [
        {
          "category": "cohesive",
          "soil": "very-soft-clay",
          "description": "Very soft clay which can be penetrated several centimeters with the thumb",
          "bearing_capacity": {
            "kg": {
              "value": 0.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 50,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "cohesive",
          "soil": "soft-clay",
          "description": "Soft clay indented with moderate thumb pressure",
          "bearing_capacity": {
            "kg": {
              "value": 1,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 100,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "cohesive",
          "soil": "moist-clay",
          "description": "Moist clay and sand clay mixture which can be indented with strong thumb pressure",
          "bearing_capacity": {
            "kg": {
              "value": 1.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 150,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "cohesive",
          "soil": "medium-clay",
          "description": "Medium clay, readily indented with thumb nail",
          "bearing_capacity": {
            "kg": {
              "value": 2.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 250,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "cohesive",
          "soil": "soft-shale",
          "description": "Soft shale, hard or stiff clay in deep bed, dry",
          "bearing_capacity": {
            "kg": {
              "value": 4,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 450,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "cohesive",
          "soil": "black-cotton",
          "description": "Black cotton soil",
          "bearing_capacity": {
            "kg": {
              "value": 1.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 150,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "sand-gravel",
          "description": "Gravel, sand and gravel mixture, compact and offering high resistance to penetration when excavated by tools. (Refer Note 5)",
          "bearing_capacity": {
            "kg": {
              "value": 4.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 450,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "compact-coarse-sand",
          "description": "Coarse sand, compact and dry (with ground water level at a depth greater than width of foundation below the base of footing)",
          "bearing_capacity": {
            "kg": {
              "value": 4.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 450,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "compact-medium-sand",
          "description": "Medium sand, compact and dry",
          "bearing_capacity": {
            "kg": {
              "value": 2.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 250,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "medium-clay",
          "description": "Medium clay, readily indented with thumb nail",
          "bearing_capacity": {
            "kg": {
              "value": 2.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 250,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "fine-dry-silt-sand",
          "description": "Fine sand, silt (dry lumps easily pulverized by fingers)",
          "bearing_capacity": {
            "kg": {
              "value": 1.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 150,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "loose-sand-gravel",
          "description": "Loose gravel or sand gravel mixture; loose coarse to medium sand, dry (Refer Note 5)",
          "bearing_capacity": {
            "kg": {
              "value": 2.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 250,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "non-cohesive",
          "soil": "fine-dry-sand",
          "description": "Fine sand, loose and dry",
          "bearing_capacity": {
            "kg": {
              "value": 1,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 100,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "rocks",
          "soil": "hard-granite",
          "description": "Rocks (hard) without lamination and defects, for example granite, trap and diorite",
          "bearing_capacity": {
            "kg": {
              "value": 33,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 3300,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "rocks",
          "soil": "stone-limestone",
          "description": "Laminated rocks, for example sand stone and lime stone in sound condition",
          "bearing_capacity": {
            "kg": {
              "value": 16.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 1650,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "rocks",
          "soil": "bedrock-shale-cemented",
          "description": "Residual deposits of shattered and broken bed rock and hard shale, cemented material",
          "bearing_capacity": {
            "kg": {
              "value": 9,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 900,
              "unit": "kn/m2"
            }
          }
        },
        {
          "category": "rocks",
          "soil": "soft",
          "description": "Soft rock",
          "bearing_capacity": {
            "kg": {
              "value": 4.5,
              "unit": "kg/cm2"
            },
            "kn": {
              "value": 450,
              "unit": "kn/m2"
            }
          }
        }
      ]
    }

library = Library()


# Construction notes
class Notes:
    ''' A library of construction notations where keys are mapped to a
        costruction statement.
        Use: to word construction documents.
        '''
    def __init__(self):
        self.notes='Use: to word construction documents.'

    def connote(self):
        ''' returns a dictionary mapping abreviated keywords to a string
            representing a costruction statement.
        '''
        cnote={'excavation':{'exc':'to excavate for foundation','topsoil':'topsoil',
                             'soil':'solid earth','marl':'solid marl',
                             'stone':'solid stone','loosestone':'loose stone',
                             'softclay':'soft clay','sand':'loose sand',
                             'dispose':'cart away and dispose of excavated material',
                             'backfill':'To backfill with suitable fill and compact'
                             },


        	'concrete':{'mix':'mix place and vibrate', 'conc':'concrete to',
                            'r121':'1:2:1', 'r122':'1:2:2', 'r123':'1:2:3',
                            'r124':'1:2:4','r131':'1:3:1', 'r132':'1:3:2',
                            'r133':'1:3:3','r134':'1:3:4','r135':'1:3:5','r136':'1:3:6'
                            },

               'rebar':{'cut':'cut bend and install','fab':'cut and fabticate',
                        'lnk':'links to', 'str':'stirrups', 'brs':'bars to','rbr':'re-bar',
                        'm5':'6mm', 'm10':'10mm', 'm12':'12mm','m16':'16mm', 'm20':'20mm',
                        'm25':'25mm',
                        '1/4':'1/4 inch','3/8':'1/2 inch','5/8':'5/8 inch',
                        '3/4':'3/4 inch','1':'1 inch'
                        },

               'structural':{'fdn':'foundation','stf':'stiffeners', 'clm':'columns',
                             'lnt':'lintels','bms':'beams','blt':'beltcourse',
                            'slb':'slab', 'wll':'block walls','blk':'block cores'},

               'Wall':{'erect':'to erect ', 'wll':'block wall ',
                       'acore':'fill alternate cores ', 'core':'fill all cores',
                       'drw':'dry wall','cstone':'cut stone wall',
                       'dstone':'dressed stone wall','rstone':'rubble stone wall',
                       'ply':'plyboard wall','brd':'boarded wall'

                       },

               'form':{'make':'make formwork','erect':'erect and remove formwork to',
                       'mprop':'install and remove metal shores to',
                       'wprop':'install and remove wooden shores to'
                       },

               'roof':{'install':'install roofing','erect':'erect roof',
                       'decra':'decra metal','metro':'metro romano',
                       'fiber':'fiber glass shingle','zinc':'zinc sheet',
                       'alsheet':'aluminum sheeting','stseam':'standing seam'
                       },

               'floor':{'install':'install flooring','lay':'level and lay',
                        'cer':'ceramic tiles','porc':'porcelain tiles',
                        'prk':'pakae tile','wood':'wooden flooring',
                        'thset':'thinset mortar',
                        'grt':'grouted in matching grout',
                        'plsh':'polish'
                        }
                 }
        return cnote
