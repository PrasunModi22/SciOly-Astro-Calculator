import importlib

def main():
    print("Available formulas:")
    formulas = [
        "distance_modulus", "parallax", "spectroscopic_parallax", "wien_law",
        "stefan_boltzmann", "inverse_square", "doppler_shift", "angular_size",
        "escape_velocity", "orbital_velocity", "blackbody_flux", "centripetal_force",
        "kepler_third_mass", "surface_gravity", "angular_momentum", "transit_depth",
        "luminosity_distance_temp", "transit_duration", "radial_velocity",
        "kepler_third_simple"
    ]
    while True:
        for idx, name in enumerate(formulas):
            print(f"{idx + 1}. {name}")

        choice = int(input("Choose a formula by number: ")) - 1
        formula_name = formulas[choice]

        knowns = {}
        while True:
            var = input("Enter known variable (or press enter to solve): ")
            if not var:
                break
            val = float(input(f"Value for {var}: "))
            knowns[var] = val

        module = importlib.import_module(f"formulas.{formula_name}")
        try:
            result = module.solve(knowns)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
        
        cont = input("Do you want to solve another formula? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
