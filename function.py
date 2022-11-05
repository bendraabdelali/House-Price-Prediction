
def   MS_Zoning (MS):
  # MSZoning [3, 4, 0, 1, 2] ['RL' 'RM' 'C (all)' 'FV' 'RH']
   return {
        "C	Commercial": 0,
        "FV	Floating Village Residential": 1,
        "RH	Residential High Density" : 2,
        "RL	Residential Low Density": 3

    }.get(MS, 4)      

def Sale_Type(type):
  # [8, 6, 0, 3, 4, 1, 5, 2, 7] ['WD' 'New' 'COD' 'ConLD' 'ConLI' 'CWD' 'ConLw' 'Con' 'Oth']
    return {
        "WD 	Warranty Deed - Conventional": 8,
        "CWD	Warranty Deed - Cash": 1,
        "New	Home just constructed and sold" : 6,
        "COD	Court Officer Deed/Estate": 0,
        "Con	Contract 15% Down payment regular terms" : 2,
        "ConLw	Contract Low Down payment and low interest" : 5,
        "ConLI	Contract Low Interest" : 4,
        "ConLD	Contract Low Down": 3 
     }.get(type, 7)  
    
