This file is for the generation of the entire metadata for the entire collection before the generate_individual_jsons.py was used. I want to know if something is possible in the current code and how hard/easy it would be to do. Without automating this it will be an extensive task for me to move/change names of over 1000 metadata files.



Basically in this file the second 5555 group of metadata take in the following logic to remove Bodz S1 or Bodz S2 and my question is with the second lot of 5555 metadata, is it possible to randomize those? Atm the first 1555 have Bodz S2 and the next 4000 have Bodz S1 but I want the Bodz S2 to be mixed in between the Bodz S1's as that is how they will need to be for the Public Sale we have.



if (outputs > 5555) and (outputs <= 5555 + 1555): #Lines to alter to effect the changes?
del staging_dict['Bodz S1']
del metadata_dict['Bodz S1']
if (outputs > 5555) and (outputs > 5555 + 1555):
del staging_dict['Bodz S2']
del metadata_dict['Bodz S2']
del staging_dict['Bodz Mapping']
del metadata_dict['Bodz Mapping']


