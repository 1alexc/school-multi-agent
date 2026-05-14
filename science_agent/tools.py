def periodic_table_lookup(element_name: str) -> dict:
    """
    Look up factual information about a chemical element from the periodic table.
    
    Args:
        element_name: The name or symbol of the element (e.g., "Hydrogen", "H", "Carbon").
        
    Returns:
        A dictionary containing the element's atomic number, symbol, mass, and category.
    """
    elements = {
        "H": {"name": "Hydrogen", "atomic_number": 1, "symbol": "H", "mass": 1.008, "category": "Nonmetal"},
        "HE": {"name": "Helium", "atomic_number": 2, "symbol": "He", "mass": 4.0026, "category": "Noble Gas"},
        "LI": {"name": "Lithium", "atomic_number": 3, "symbol": "Li", "mass": 6.94, "category": "Alkali Metal"},
        "BE": {"name": "Beryllium", "atomic_number": 4, "symbol": "Be", "mass": 9.0122, "category": "Alkaline Earth Metal"},
        "B": {"name": "Boron", "atomic_number": 5, "symbol": "B", "mass": 10.81, "category": "Metalloid"},
        "C": {"name": "Carbon", "atomic_number": 6, "symbol": "C", "mass": 12.011, "category": "Nonmetal"},
        "N": {"name": "Nitrogen", "atomic_number": 7, "symbol": "N", "mass": 14.007, "category": "Nonmetal"},
        "O": {"name": "Oxygen", "atomic_number": 8, "symbol": "O", "mass": 15.999, "category": "Nonmetal"},
        "F": {"name": "Fluorine", "atomic_number": 9, "symbol": "F", "mass": 18.998, "category": "Halogen"},
        "NE": {"name": "Neon", "atomic_number": 10, "symbol": "Ne", "mass": 20.180, "category": "Noble Gas"},
        "NA": {"name": "Sodium", "atomic_number": 11, "symbol": "Na", "mass": 22.990, "category": "Alkali Metal"},
        "MG": {"name": "Magnesium", "atomic_number": 12, "symbol": "Mg", "mass": 24.305, "category": "Alkaline Earth Metal"},
        "AL": {"name": "Aluminum", "atomic_number": 13, "symbol": "Al", "mass": 26.982, "category": "Post-transition Metal"},
        "SI": {"name": "Silicon", "atomic_number": 14, "symbol": "Si", "mass": 28.085, "category": "Metalloid"},
        "P": {"name": "Phosphorus", "atomic_number": 15, "symbol": "P", "mass": 30.974, "category": "Nonmetal"},
        "S": {"name": "Sulfur", "atomic_number": 16, "symbol": "S", "mass": 32.06, "category": "Nonmetal"},
        "CL": {"name": "Chlorine", "atomic_number": 17, "symbol": "Cl", "mass": 35.45, "category": "Halogen"},
        "AR": {"name": "Argon", "atomic_number": 18, "symbol": "Ar", "mass": 39.95, "category": "Noble Gas"},
        "K": {"name": "Potassium", "atomic_number": 19, "symbol": "K", "mass": 39.098, "category": "Alkali Metal"},
        "CA": {"name": "Calcium", "atomic_number": 20, "symbol": "Ca", "mass": 40.078, "category": "Alkaline Earth Metal"},
        "FE": {"name": "Iron", "atomic_number": 26, "symbol": "Fe", "mass": 55.845, "category": "Transition Metal"},
        "CU": {"name": "Copper", "atomic_number": 29, "symbol": "Cu", "mass": 63.546, "category": "Transition Metal"},
        "ZN": {"name": "Zinc", "atomic_number": 30, "symbol": "Zn", "mass": 65.38, "category": "Transition Metal"},
        "AG": {"name": "Silver", "atomic_number": 47, "symbol": "Ag", "mass": 107.87, "category": "Transition Metal"},
        "AU": {"name": "Gold", "atomic_number": 79, "symbol": "Au", "mass": 196.97, "category": "Transition Metal"},
        "U": {"name": "Uranium", "atomic_number": 92, "symbol": "U", "mass": 238.03, "category": "Actinide"}
    }
    
    # Create reverse lookup for names
    name_lookup = {v["name"].upper(): k for k, v in elements.items()}
    
    query = element_name.upper().strip()
    
    if query in elements:
        return elements[query]
    elif query in name_lookup:
        return elements[name_lookup[query]]
    else:
        return {"error": f"Element '{element_name}' not found. Currently supporting common elements up to Calcium + Fe, Cu, Zn, Ag, Au, U."}

def unit_converter(value: float, from_unit: str, to_unit: str) -> dict:
    """
    Converts a value from one scientific unit to another.
    
    Args:
        value: The numerical value to convert.
        from_unit: The unit to convert from (e.g., 'celsius', 'fahrenheit', 'meters', 'feet', 'kg', 'lbs').
        to_unit: The unit to convert to (e.g., 'celsius', 'fahrenheit', 'meters', 'feet', 'kg', 'lbs').
        
    Returns:
        A dictionary containing the original value, converted value, and units.
    """
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()
    
    result = None
    
    # Temperature
    if from_unit in ['celsius', 'c'] and to_unit in ['fahrenheit', 'f']:
        result = (value * 9/5) + 32
    elif from_unit in ['fahrenheit', 'f'] and to_unit in ['celsius', 'c']:
        result = (value - 32) * 5/9
    elif from_unit in ['celsius', 'c'] and to_unit in ['kelvin', 'k']:
        result = value + 273.15
    elif from_unit in ['kelvin', 'k'] and to_unit in ['celsius', 'c']:
        result = value - 273.15
        
    # Distance
    elif from_unit in ['meters', 'm'] and to_unit in ['feet', 'ft']:
        result = value * 3.28084
    elif from_unit in ['feet', 'ft'] and to_unit in ['meters', 'm']:
        result = value / 3.28084
    elif from_unit in ['kilometers', 'km'] and to_unit in ['miles', 'mi']:
        result = value * 0.621371
    elif from_unit in ['miles', 'mi'] and to_unit in ['kilometers', 'km']:
        result = value / 0.621371
        
    # Mass
    elif from_unit in ['kilograms', 'kg'] and to_unit in ['pounds', 'lbs']:
        result = value * 2.20462
    elif from_unit in ['pounds', 'lbs'] and to_unit in ['kilograms', 'kg']:
        result = value / 2.20462
        
    if result is not None:
        return {
            "status": "success",
            "original": f"{value} {from_unit}",
            "converted": f"{round(result, 4)} {to_unit}",
            "value": round(result, 4)
        }
    else:
        return {"error": f"Conversion from {from_unit} to {to_unit} is not supported."}
