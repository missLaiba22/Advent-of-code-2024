#Day 2 Puzzle 1 
def is_safe(report):
  increasing = True
  decreasing = True
  for i in range (len(report)-1):
    diff=report[i+1] -report[i]
    if abs(diff)<1 or abs(diff)>3:
      return False
    if diff<0:
      increasing=False
    if diff>0:
      decreasing=False
  return increasing or decreasing
with open("/content/day2.txt","r") as file:
    reports = [list(map(int, line.split())) for line in file]
safe_count = sum(1 for report in reports if is_safe(report))

# Output the result
print(f"Number of safe reports: {safe_count}")


#Day 2 Puzzle 2
def is_safe(report):
    """Check if a report is safe as-is."""
    increasing = True
    decreasing = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        # Check the difference is between 1 and 3 inclusive
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        # Update the flags for increasing and decreasing
        if diff < 0:
            increasing = False
        if diff > 0:
            decreasing = False
    # A report is safe if it is either entirely increasing or decreasing
    return increasing or decreasing

def is_safe_with_dampener(report):
    """Check if a report is safe considering the Problem Dampener."""
    if is_safe(report):
        return True  # The report is already safe as-is

    # Try removing each level and check if the modified report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True  # The report is safe after removing one level
    
    return False  # The report is not safe, even with the Problem Dampener

# Read the input file and process the reports
with open("/content/day2.txt", "r") as file:
    reports = [list(map(int, line.split())) for line in file]

# Count the number of safe reports considering the Problem Dampener
safe_count = sum(1 for report in reports if is_safe_with_dampener(report))

# Output the result
print(f"Number of safe reports: {safe_count}")
