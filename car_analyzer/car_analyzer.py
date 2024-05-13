import math
import numpy as np
import os

os.system('cls' if os.name == 'nt' else 'clear')

geo = {
    "coilover_front_top": [0.22,0.5588,0.0],
    "coilover_front_bottom": [0.1905,0.0762,0.0],
    "lca_pivot": [0.0889,-0.0762,0.01778],
    "coilover_back_top": [0.185,0.635,-0.046],
    "coilover_back_bottom": [0.1778,0.0508,0.0],
    "cg": 0.63,
    "wheelbase": 2.6
}

mass = {
    "na": 1311, #na total mass
    "turbo": 1364, #turbo total mass
    "front_hub": 52.049724,
    "rear_hub": 45,
    "lca": 9.07185
}

def get_zoffset(geo):

    zoffset = geo["wheelbase"] * (0.5 - geo["cg"])
    zoffset = print(f"Z Graphic Offset: {zoffset}")

def get_rear_chassis_weight(mass, geo):
    weight = (mass["na"] - ((mass["front_hub"] * 2) + (mass["rear_hub"] *2) + (1 * mass["lca"]))) * (1 - geo["cg"])
    print(f"Rear chassis weight = {weight}")

def get_distance(geo):
    suspdesignHeightFront = (
        (geo["coilover_front_top"][0] - geo["coilover_front_bottom"][0])**2 +\
        (geo["coilover_front_top"][1] - geo["coilover_front_bottom"][1])**2 +\
        (geo["coilover_front_top"][2] - geo["coilover_front_bottom"][2])**2
        )
    suspdesignHeightFront = math.sqrt(suspdesignHeightFront)
    print(f"Geo front 0 design height: {suspdesignHeightFront}")

    suspdesignHeightBack = (
        (geo["coilover_back_top"][0] - geo["coilover_back_bottom"][0])**2 +\
        (geo["coilover_back_top"][1] - geo["coilover_back_bottom"][1])**2 +\
        (geo["coilover_back_top"][2] - geo["coilover_back_bottom"][2])**2
        )
    suspdesignHeightBack = math.sqrt(suspdesignHeightBack)
    print(f"Geo rear 0 design height: {suspdesignHeightBack}")

def get_KPI(geo):
    KPI = np.arctan((geo["coilover_front_top"][0] - geo["lca_pivot"][0]) /
                    (geo["coilover_front_top"][1] - geo["lca_pivot"][1]))
    KPI = np.rad2deg(KPI)
    print(f"KPI: {KPI}")

def get_Caster(geo):
    caster = np.arctan((geo["coilover_front_top"][2]) - (geo["lca_pivot"][2]) /
                       (geo["coilover_front_top"][1]) - (geo["lca_pivot"][1]))
    caster = np.rad2deg(caster)
    print(f"Caster: {caster}")

def get_Trail(geo):
    trail = geo["coilover_front_top"][2] - geo["lca_pivot"][2] * (geo["coilover_front_top"][2]) - (geo["lca_pivot"][2]) /\
           (geo["coilover_front_top"][1] - geo["lca_pivot"][1])
    trail *= 100
    print(f"Trail: {trail}")

def main():

    print()
    get_zoffset(geo)
    get_rear_chassis_weight(mass, geo)
    get_distance(geo)
    get_KPI(geo)
    get_Caster(geo)
    get_Trail(geo)
    print()

main()