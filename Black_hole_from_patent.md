# Original Source: https://patentimages.storage.googleapis.com/e5/d2/b6/ed813b1b6b9be8/US4619741.pdf
## Carbon Black Hole Preparation for Circuit Boards
## This is my slightly modified version of the process, here from posterity. For a better modern formula, see [Proven_Black_hole_solution.md](./Proven_Black_hole_solution.md) 

## Materials Needed:
- Carbon black particles (preferably with pH 2-4, such as Cabot Monarch 1300 or Columbian Raven 3500)
- Surfactant (preferably anionic phosphate ester type like MAPHOS 56)
- Potassium hydroxide (KOH) (can substitute with sodium hydroxide (NaOH))
- Fumed silica (such as CAB-O-SIL MS-7SD)
- Deionized water
- Cleaner/conditioner solution (patent suggests AC-102 aluminum cleaner (oxalic acid), Grout cleaner with oxalic acid is fine, you can use a diluted solution of sodium hydroxide (NaOH) or potassium hydroxide (KOH) as well)
- Sodium persulfate microetch solution (80gm of sodium persulfate per liter and 0.5% by weight sulfuric acid)
- 10% sulfuric acid solution (Battery acid (37% H2SO4 ) diluted to 10% works well)


## Preparation of Carbon Black Dispersion:
1. Prepare a concentrated carbon black dispersion by combining:
   - 0.21% carbon black
   - 0.06% anionic surfactant
   - 0.46% KOH (86% basis) (can substitute with NaOH at .33%)
   - 0.31% fumed silica
   - Balance: deionized water

2. Ball mill this mixture for 6 hours using glass, mineral, or plastic beads (beads and mixture should occupy about 1/3 of container volume).

3. Dilute to working concentration with deionized water and keep agitated during use.

## Process Steps for Circuit Board Through-Hole Preparation:
1. **Pre-cleaning**:
   - Mechanically scrub board surfaces
   - Immerse in cleaner/conditioner solution (5 minutes at 60°C)
   - Rinse with deionized water (2 minutes)

2. **Surface Preparation**:
   - Immerse in sodium persulfate microetch solution (1 minute at room temperature)
   - Rinse with deionized water (2 minutes)
   - Immerse in 10% H₂SO₄ solution (2 minutes at room temperature)
   - Rinse with deionized water (2 minutes)

3. **Carbon Black Application**:
   - Immerse board in carbon black dispersion (4 minutes at room temperature)
   - Remove and use compressed air to clear any plugged holes (optional, you can also just smack the board on the table and it will clear the holes)

4. **Drying**:
   - Dry at 80-98°C for 10 minutes to remove water and deposit carbon black layer (pop it in the toaster oven!)

5. **Copper Surface Cleaning**:
   - Immerse in sodium persulfate microetch solution (1 minute) to remove carbon black from copper surfaces while leaving it on hole walls (avoid aggiating the board too much)
   - Rinse with deionized water (2 minutes)

6. **Electroplating**:
   - Place in copper electroplating bath (typical composition: 2.25 oz/gal copper, 9 oz/gal copper sulfate, 23 oz/gal H₂SO₄, 50 mg/l chloride ion)
   - Electroplate at 15 amps per square foot for 60-90 minutes at 20-25°C
   - Rinse and dry


## Patent states the following plating solution, but we have better ones here in the repo, see [Plating_solution.md](Plating_solution.md):
   - Copper sulfate 8.5 oz/gal 
   - H2SO4 (by weight) 30 oz/gal 
   - Chloride ion 24.3 mg/gal 