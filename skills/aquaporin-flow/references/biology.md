# Biological basis and limits

This skill originates from the user's description of aquaporins and intracellular
protein delivery. The software patterns are engineering analogies, not biological
claims or guarantees of security or performance.

## Aquaporins

Aquaporin pores support narrow, single-file water arrangements. Structural and
simulation work connected water orientation with the channel's electrostatic
environment: [Tajkhorshid et al., 2002](https://pubmed.ncbi.nlm.nih.gov/11964478/).

Proton movement along hydrogen-bond networks is described by the Grotthuss mechanism,
not literal teleportation. Do not reduce proton exclusion to a broken water chain or
a change in the magnitude of water's dipole. Electrostatic and solvation free-energy
barriers matter; water orientation alone is not a sufficient explanation:
[de Groot et al., 2003](https://pubmed.ncbi.nlm.nih.gov/14529616/) and
[Chen et al., 2006](https://pubmed.ncbi.nlm.nih.gov/16581846/).

Do not generalize absolute water-only selectivity across all family members. The
2002 structural study concerns the aquaglyceroporin GlpF. Specify the channel when
making substrate or quantitative throughput claims. The dictated billion-per-second
figure is not retained as a universal constant or an engineering benchmark.

Water permeation is passive; it is not a sequence of intentional inspections.
Avoid translating absence of direct ATP-powered pumping into zero energy cost for
protein production, cellular gradients, or transport machinery.

## Protein delivery

For eukaryotic secretory-pathway membrane proteins, synthesis and membrane insertion
can be coupled at the ER. Subsequent vesicular traffic preserves membrane topology;
a membrane protein is embedded in the carrier membrane rather than simply stored as
free contents. Routing involves molecular recognition and sorting signals, not a
universal newly stamped three-dimensional barcode at every step.

Background: [The Endoplasmic Reticulum, The Cell](https://www.ncbi.nlm.nih.gov/books/NBK9889/).
Experimental example showing that export depends on multiple signal interactions:
[Otte and Barlowe, 2002](https://pubmed.ncbi.nlm.nih.gov/12426381/).

## Engineering correspondence

| Biological inspiration | Engineering question | Limit |
| --- | --- | --- |
| Selective pore | What is allowed across this interface? | Molecule size is not semantic validation. |
| Proton exclusion | Can allowed content carry an unintended effect? | An analogy does not prove attack resistance. |
| Narrow water arrangement | What is the smallest meaningful processing unit? | Parallel software execution may still be appropriate. |
| Vesicular transport | What must accompany an artifact during delivery? | A software package is not a vesicle. |
| Sorting signals | How is the intended recipient identified and authorized? | An address does not authenticate itself. |
| Membrane incorporation | Has the destination actually accepted and used the artifact? | Delivery alone is not activation. |

“Protein robots,” “checks,” and “warehouse barcodes” are explanatory metaphors.
Keep them separate from descriptions of molecular mechanism.
