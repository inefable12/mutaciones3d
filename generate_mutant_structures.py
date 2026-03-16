from pymol import cmd

wt = "MRTGNAN"
chain = "G"

with open("C7_133_mutants.txt") as f:
    mutants = [x.strip() for x in f if x.strip()]

for seq in mutants:

    cmd.reinitialize()
    cmd.load("C7.pdb","prot")

    for i,(a,b) in enumerate(zip(wt,seq),start=1):

        if a != b:

            cmd.wizard("mutagenesis")
            wiz = cmd.get_wizard()

            wiz.set_mode(b)
            wiz.do_select(f"/prot//{chain}/{i}")
            wiz.apply()

            cmd.set_wizard()

    filename = f"mut_{seq}.pdb"
    cmd.save(filename,"prot")

print("133 estructuras generadas")
