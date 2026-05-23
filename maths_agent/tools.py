import math
import re

def solve_quadratic(a: float, b: float, c: float) -> dict:
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.
    Use this tool when students ask to solve quadratic equations or find roots.
    
    Args:
        a: The coefficient of x^2 (cannot be 0).
        b: The coefficient of x.
        c: The constant term.
        
    Returns:
        A dictionary containing the roots, the discriminant, and details of the solution.
    """
    if a == 0.0:
        return {
            "status": "error",
            "message": "Coefficient 'a' cannot be zero in a quadratic equation (it would be a linear equation)."
        }
        
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return {
            "status": "success",
            "equation": f"{a}x^2 + {b}x + {c} = 0",
            "discriminant": round(discriminant, 4),
            "root_type": "Two distinct real roots",
            "roots": [round(root1, 4), round(root2, 4)],
            "steps": [
                f"Calculate discriminant D = b^2 - 4ac = ({b})^2 - 4*({a})*({c}) = {discriminant}",
                f"Discriminant is positive, so there are two real roots: x = (-b +/- sqrt(D)) / (2a)",
                f"x1 = (-({b}) + sqrt({discriminant})) / (2*{a}) = {round(root1, 4)}",
                f"x2 = (-({b}) - sqrt({discriminant})) / (2*{a}) = {round(root2, 4)}"
            ]
        }
    elif discriminant == 0:
        root = -b / (2*a)
        return {
            "status": "success",
            "equation": f"{a}x^2 + {b}x + {c} = 0",
            "discriminant": 0.0,
            "root_type": "One repeated real root",
            "roots": [round(root, 4)],
            "steps": [
                f"Calculate discriminant D = b^2 - 4ac = ({b})^2 - 4*({a})*({c}) = 0",
                f"Discriminant is zero, so there is one repeated real root: x = -b / 2a",
                f"x = -({b}) / (2*{a}) = {round(root, 4)}"
            ]
        }
    else: # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        
        real_formatted = round(real_part, 4)
        imag_formatted = round(imaginary_part, 4)
        
        root1_str = f"{real_formatted} + {imag_formatted}i"
        root2_str = f"{real_formatted} - {imag_formatted}i"
        
        return {
            "status": "success",
            "equation": f"{a}x^2 + {b}x + {c} = 0",
            "discriminant": round(discriminant, 4),
            "root_type": "Two complex roots",
            "roots": [root1_str, root2_str],
            "steps": [
                f"Calculate discriminant D = b^2 - 4ac = ({b})^2 - 4*({a})*({c}) = {discriminant}",
                f"Discriminant is negative, so there are two complex roots: x = -b/2a +/- i*sqrt(-D)/2a",
                f"x1 = {root1_str}",
                f"x2 = {root2_str}"
            ]
        }

def calculate_geometry_properties(shape: str, parameters: dict) -> dict:
    """
    Calculates properties (area, perimeter/circumference, volume, surface area) of geometric shapes.
    Use this tool for geometry word problems, shape dimensions, or measurements.
    
    Args:
        shape: The name of the shape (circle, rectangle, triangle, sphere, cylinder, cone).
        parameters: A dictionary containing the dimensions required for that shape:
            - Circle: {'radius': float}
            - Rectangle: {'width': float, 'height': float}
            - Triangle: {'base': float, 'height': float, 'side_a': float, 'side_b': float, 'side_c': float}
            - Sphere: {'radius': float}
            - Cylinder: {'radius': float, 'height': float}
            - Cone: {'radius': float, 'height': float}
            
    Returns:
        A dictionary containing the calculated properties.
    """
    s = shape.lower().strip()
    
    try:
        if s == "circle":
            r = float(parameters["radius"])
            area = math.pi * r**2
            circumference = 2 * math.pi * r
            return {
                "status": "success",
                "shape": "Circle",
                "radius": r,
                "area": round(area, 4),
                "circumference": round(circumference, 4)
            }
            
        elif s == "rectangle":
            w = float(parameters["width"])
            h = float(parameters["height"])
            area = w * h
            perimeter = 2 * (w + h)
            return {
                "status": "success",
                "shape": "Rectangle",
                "width": w,
                "height": h,
                "area": round(area, 4),
                "perimeter": round(perimeter, 4)
            }
            
        elif s == "triangle":
            base = float(parameters.get("base", 0.0))
            height = float(parameters.get("height", 0.0))
            side_a = float(parameters.get("side_a", 0.0))
            side_b = float(parameters.get("side_b", 0.0))
            side_c = float(parameters.get("side_c", 0.0))
            
            # Area calculation
            if base > 0.0 and height > 0.0:
                area = 0.5 * base * height
            elif side_a > 0.0 and side_b > 0.0 and side_c > 0.0:
                # Heron's formula
                semi = (side_a + side_b + side_c) / 2.0
                area = math.sqrt(semi * (semi - side_a) * (semi - side_b) * (semi - side_c))
            else:
                return {"status": "error", "message": "To calculate triangle area, provide either ('base' and 'height') or all three sides ('side_a', 'side_b', 'side_c')."}
                
            # Perimeter calculation
            if side_a > 0.0 and side_b > 0.0 and side_c > 0.0:
                perimeter = side_a + side_b + side_c
            elif base > 0.0 and side_a > 0.0 and side_b > 0.0:
                perimeter = base + side_a + side_b
            else:
                perimeter = None
                
            res = {
                "status": "success",
                "shape": "Triangle",
                "area": round(area, 4)
            }
            if perimeter is not None:
                res["perimeter"] = round(perimeter, 4)
            return res
            
        elif s == "sphere":
            r = float(parameters["radius"])
            volume = (4.0 / 3.0) * math.pi * r**3
            surface_area = 4 * math.pi * r**2
            return {
                "status": "success",
                "shape": "Sphere",
                "radius": r,
                "volume": round(volume, 4),
                "surface_area": round(surface_area, 4)
            }
            
        elif s == "cylinder":
            r = float(parameters["radius"])
            h = float(parameters["height"])
            volume = math.pi * r**2 * h
            surface_area = 2 * math.pi * r * h + 2 * math.pi * r**2
            return {
                "status": "success",
                "shape": "Cylinder",
                "radius": r,
                "height": h,
                "volume": round(volume, 4),
                "surface_area": round(surface_area, 4)
            }
            
        elif s == "cone":
            r = float(parameters["radius"])
            h = float(parameters["height"])
            volume = (1.0 / 3.0) * math.pi * r**2 * h
            # Slant height slant = sqrt(r^2 + h^2)
            slant = math.sqrt(r**2 + h**2)
            surface_area = math.pi * r * slant + math.pi * r**2
            return {
                "status": "success",
                "shape": "Cone",
                "radius": r,
                "height": h,
                "volume": round(volume, 4),
                "surface_area": round(surface_area, 4)
            }
        else:
            return {"status": "error", "message": f"Unsupported shape: '{shape}'. Supported shapes are: circle, rectangle, triangle, sphere, cylinder, cone."}
            
    except KeyError as e:
        return {"status": "error", "message": f"Missing required parameter {str(e)} for shape '{shape}'."}
    except Exception as e:
        return {"status": "error", "message": f"Geometry calculation failed: {str(e)}"}

def differentiate_polynomial(polynomial_str: str) -> dict:
    """
    Finds the analytical derivative of a single-variable polynomial in 'x' using the power rule.
    Use this tool when students ask for derivatives of polynomials or rates of change.
    
    Args:
        polynomial_str: The polynomial expression (e.g., '3x^2 - 5x + 7', 'x^3 - x').
        
    Returns:
        A dictionary containing the input polynomial, the derivative expression, and term-by-term details.
    """
    original = polynomial_str.strip()
    poly = original.replace(" ", "").replace("*", "")
    
    # Replace '-' with '+-' (but not inside exponent)
    # A negative sign after a caret '^' is part of the exponent, so we ignore it
    poly = re.sub(r'(?<!\^)-', '+-', poly)
    
    # Split into terms
    raw_terms = [t for t in poly.split("+") if t]
    
    derivative_terms = []
    parsed_terms_info = []
    
    for term in raw_terms:
        # Regex to parse term: sign/coefficient, variable 'x', power
        # Group 1: coefficient (optional, e.g. '3', '-2', or just '-' / '+')
        # Group 2: variable 'x' (optional)
        # Group 3: power (optional, after '^')
        match = re.match(r'^([+-]?(?:\d*\.\d+|\d+)?)?(x)?(?:\^([+-]?\d+))?$', term)
        if not match:
            return {"status": "error", "message": f"Could not parse term '{term}' in polynomial."}
            
        coeff_str, var_str, power_str = match.groups()
        
        # Determine coefficient
        if coeff_str == "" or coeff_str == "+":
            coeff = 1.0
        elif coeff_str == "-":
            coeff = -1.0
        elif coeff_str is not None:
            coeff = float(coeff_str)
        else:
            coeff = 1.0
            
        # Determine power
        if var_str == "x":
            if power_str is not None:
                power = int(power_str)
            else:
                power = 1
        else:
            power = 0 # Constant term
            
        # Differentiate
        if power == 0:
            deriv_coeff = 0.0
            deriv_power = 0
        else:
            deriv_coeff = coeff * power
            deriv_power = power - 1
            
        parsed_terms_info.append({
            "term": term,
            "coefficient": coeff,
            "power": power,
            "deriv_coefficient": deriv_coeff,
            "deriv_power": deriv_power
        })
        
        if deriv_coeff != 0.0:
            derivative_terms.append((deriv_coeff, deriv_power))
            
    # Combine terms of the same power
    combined = {}
    for dc, dp in derivative_terms:
        combined[dp] = combined.get(dp, 0.0) + dc
        
    # Sort terms by power descending
    sorted_powers = sorted(combined.keys(), reverse=True)
    
    # Build result string
    result_parts = []
    for dp in sorted_powers:
        dc = combined[dp]
        if dc == 0.0:
            continue
            
        # Format coefficient
        if dc.is_integer():
            dc_val = int(dc)
        else:
            dc_val = round(dc, 4)
            
        # Sign formatting
        if dc_val > 0:
            sign = "+" if result_parts else ""
        else:
            sign = "-"
            dc_val = abs(dc_val)
            
        # Term formatting
        if dp == 0:
            term_str = f"{sign}{dc_val}"
        elif dp == 1:
            term_str = f"{sign}x" if dc_val == 1 else f"{sign}{dc_val}x"
        else:
            term_str = f"{sign}x^{dp}" if dc_val == 1 else f"{sign}{dc_val}x^{dp}"
            
        # Handle sign space for intermediate terms
        if result_parts and sign:
            # Add spaces around sign for readability
            last = result_parts.pop()
            result_parts.append(last)
            result_parts.append(f" {sign} {term_str.lstrip('+-')}")
        else:
            result_parts.append(term_str)
            
    deriv_str = "".join(result_parts) if result_parts else "0"
    
    return {
        "status": "success",
        "input_polynomial": original,
        "derivative": deriv_str,
        "steps": parsed_terms_info
    }

def evaluate_definite_integral(expression: str, a: float, b: float) -> dict:
    """
    Numerically evaluates the definite integral of a mathematical function f(x) over [a, b] using Simpson's rule.
    Supported functions: sin, cos, tan, exp, log, sqrt, abs, and operators +, -, *, /, ** (or ^).
    Use this tool when students ask to integrate functions over a specific interval.
    
    Args:
        expression: The mathematical expression in terms of 'x' (e.g. 'x^2', 'sin(x)', '2*x + 5').
        a: The lower limit of integration.
        b: The upper limit of integration.
        
    Returns:
        A dictionary containing the integration result, limits, and parameters used.
    """
    # 1. Safe eval function
    def f(x_val):
        allowed_names = {
            'x': x_val,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
            'pow': pow,
            'abs': abs
        }
        # Replace caret with python exponentiation
        cleaned_expr = expression.replace("^", "**")
        # Ensure we don't eval dangerous things
        return eval(cleaned_expr, {"__builtins__": None}, allowed_names)

    # Simpson's Rule parameters
    n = 1000 # Number of intervals (even)
    h = (b - a) / n
    
    try:
        y_a = f(a)
        y_b = f(b)
        
        sum_odd = 0.0
        sum_even = 0.0
        
        for i in range(1, n):
            x_i = a + i * h
            y_i = f(x_i)
            if i % 2 == 0:
                sum_even += y_i
            else:
                sum_odd += y_i
                
        integral_val = (h / 3) * (y_a + y_b + 4 * sum_odd + 2 * sum_even)
        
        return {
            "status": "success",
            "expression": expression,
            "lower_limit": a,
            "upper_limit": b,
            "result": round(integral_val, 6),
            "intervals": n
        }
    except Exception as e:
        return {"status": "error", "message": f"Could not integrate expression. Error: {str(e)}."}
