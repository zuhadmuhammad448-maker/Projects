import math

def calculate_rms_speed(temperature, molar_mass):
    """
    Calculates the root-mean-square (RMS) speed of gas molecules.
    Formula: v_rms = sqrt(3 * R * T / M)
    """
    # Ideal gas constant in J/(mol·K)
    R = 8.314 
    
    # Convert molar mass from g/mol to kg/mol
    molar_mass_kg = molar_mass / 1000 
    
    # Calculate velocity
    rms_speed = math.sqrt((3 * R * temperature) / molar_mass_kg)
    return rms_speed

def main():
    print("=" * 50)
    print("  Ideal Gas Molecular Kinetics Calculator (Physics)")
    print("=" * 50)
    
    try:
        # Get inputs from the user
        temp = float(input("Enter temperature in Kelvin (e.g., 298.15): "))
        if temp < 0:
            print("Error: Temperature cannot be below Absolute Zero (0 K).")
            return
            
        print("\nCommon Molar Masses (g/mol):")
        print("- Helium (He): 4.00")
        print("- Nitrogen (N2): 28.01")
        print("- Oxygen (O2): 32.00")
        print("- Carbon Dioxide (CO2): 44.01")
        
        m_mass = float(input("\nEnter molar mass of the gas in g/mol: "))
        if m_mass <= 0:
            print("Error: Molar mass must be greater than zero.")
            return
        
        # Perform calculation
        velocity = calculate_rms_speed(temp, m_mass)
        
        # Display results
        print("\n" + "-" * 40)
        print(f"Results for Gas at {temp:.2f} K:")
        print(f"Molar Mass: {m_mass:.2f} g/mol")
        print(f"Root-Mean-Square Speed (v_rms): {velocity:.2f} m/s")
        print("-" * 40)
        
    except ValueError:
        print("\nError: Please enter valid numerical values.")

if __name__ == "__main__":
    main()