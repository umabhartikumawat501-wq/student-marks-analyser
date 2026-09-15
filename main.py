# Calculate CGPA

grade_points = {
    "A+": 10,
    "A": 9,
    "B": 8,
    "B+": 7,
    "D": 6,
    "F": 0
}

cgpa = grade_points[grade]

print(f"CGPA         :  {cgpa:.2f}")