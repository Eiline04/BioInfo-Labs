# PROF GITHUB: https://github.com/Gagniuc/Gagniuc
# Calculates the Melting Temperature (Tm) using the basic Wallace rule.
# Formula: Tm = 4(G+C) + 2(A+T)

def calculate_tm_wallace(sequence):
    seq = sequence.upper()
    
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')
    
    tm = 4 * (g_count + c_count) + 2 * (a_count + t_count)
    
    return tm, g_count + c_count, a_count + t_count

def main():
    dna_input = "ATCGCGTA"

    tm, gc_pairs, at_pairs = calculate_tm_wallace(dna_input)
    
    print("-> Basic Wallace Tm Calculator [...]")
    print(f"Sequence:   {dna_input}")
    print(f"Length:     {len(dna_input)} bp")
    print(f"G+C count:  {gc_pairs}")
    print(f"A+T count:  {at_pairs}")
    print(f"Tm Result:  {tm} °C")

if __name__ == "__main__":
    main()