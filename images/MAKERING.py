# Andrew Tuckwell BIOMOD2015
#run YOUR DIRECTORY WITH MAKERING SAVED/MAKERING.py 
from pymol import cmd, stored
	
#SET THE STUFF
#set orientation of monomer, single symmetry, and radius of ring
xrot=0
yrot=0
zrot=0
symm=0
radius=0


#LOAD THE MONOMER
infiledir = 'YOUR DIRECTORY WITH MONOMER FILE'
infilename = 'YOUR MONOMER FILE'
#SAVE THE RING
outfiledir = 'YOUR DIRECTORY FOR SAVING'
outfilename= infilename + '_rad'+str(radius)+'_X'+str(xrot)+'_Y'+str(yrot)+'_Z'+str(zrot)


#_________________________________________________________________________________________________________________
#DO THE STUFF
#load and depict monomer, move to radius length

cmd.load(infiledir+infilename+'.pdb')

cmd.create(infilename+'_00', infilename)
cmd.origin(infilename)
cmd.rotate('x', xrot, infilename+'_00')
cmd.rotate('y', yrot, infilename+'_00')
cmd.rotate('z', zrot, infilename+'_00')
cmd.translate([radius,0,0], infilename+'_00')

#copy and rotate monomers around centre
for n in range(1,symm+1,1):
		
	name = infilename+'_0' + str(n)
	cmd.create(name, infilename+'_00')
	cmd.origin(infilename)
	cmd.rotate('z', n*(360.00/symm), name)
	cmd.alter('chain A+ obj '+name, 'chain='+str(n))
	print name

cmd.delete(infilename) 
cmd.delete(infilename+'_00') 

#save final ring
cmd.save(outfiledir+outfilename+'.pdb', 'all', -1, 'pdb')
cmd.zoom('all')

#load and display final tube
#cmd.delete(all) 
cmd.delete('all')
cmd.load(outfiledir+outfilename+'.pdb')
cmd.hide('all')
cmd.show('cartoon')
cmd.spectrum('count','rainbow')
cmd.zoom('all')
cmd.set('ray_opaque_background', 'off')