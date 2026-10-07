# The actual Tm is influenced by the concentratin of Mg(2+), K(+) and cosolvents. An alternative formula is:
# Tm = 81.5 + 16.6 * log10([Na+]) + 0.41 * (%GC) - (600 / length of primer)
# Implement an app that calculates the Tm of a DNA seq. using one of these formulas or both.
# Input= ACGCGTGGCA

import math

def calculate_tm(sequence, na_conc):
   
    seq = sequence.upper()
    length = len(seq)
    
    if length == 0:
        raise ValueError("Sequence length cannot be zero.")
        

    g_count = seq.count('G')
    c_count = seq.count('C')
    gc_percent = ((g_count + c_count) / length) * 100
    

    tm = 81.5 + (16.6 * math.log10(na_conc)) + (0.41 * gc_percent) - (600 / length)
    
    return tm, gc_percent


def main():
    dna_input = "ACGCGTGGCA"
    na_concentration = 0.05  # Default Na+ concentration in Molar
    
    try:
        
        tm, gc_percent = calculate_tm(dna_input, na_concentration)
        
        print("-> DNA Melting Temperature Calculator [...]")
        print(f"Sequence:    {dna_input}")
        print(f"Length:      {len(dna_input)} bp")
        print(f"GC Content:  {gc_percent:.1f}%")
        print(f"Tm Result:   {tm:.2f} °C")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()