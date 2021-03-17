import numpy as np
from netCDF4 import Dataset
import sys

def ncscan(rootgroup, printGlobal, printDimensions, printVariables):
    # NetCDF global attributes
    nc_attrs = rootgroup.ncattrs()		# list of global attributes
    if printGlobal:
        print("\nNetCDF Global Attributes:")
        for nc_attr in nc_attrs:
            print('\t%s:' % nc_attr, repr(rootgroup.getncattr(nc_attr)))

    def print_ncattr(key):	# print attributes for a dimension or a variable
        try:
            print("\t\ttype:", repr(rootgroup.variables[key].dtype))
            for ncattr in rootgroup.variables[key].ncattrs():
                print('\t\t%s:' % ncattr, repr(rootgroup.variables[key].getncattr(ncattr)))
        except KeyError:
            #print "\t\tWARNING: %s does not contain any attributes" % key
            print("\t\t%s no type specified, probably integer" % key)

    # Dimensions
    nc_dims = [dim for dim in rootgroup.dimensions]  # list of nc dimensions
    if printDimensions:
        print("\nNetCDF dimension information:")
        for dim in nc_dims:
            print("\tName:", dim )
            print("\t\tsize:", len(rootgroup.dimensions[dim]))
            print_ncattr(dim)

    # Variables
    nc_vars = [var for var in rootgroup.variables]  # list of nc variables
    if printVariables:
        print("\nNetCDF variable information:")
        for var in nc_vars:
            #if var not in nc_dims:
                print('\tName:', var)
                print("\t\tdimensions:", rootgroup.variables[var].dimensions)
                print("\t\tsize:", rootgroup.variables[var].size)
                print_ncattr(var)

    return nc_attrs, nc_dims, nc_vars

print(__name__)

if __name__ == '__main__':

    fileName = sys.argv[1]

    rootgroup = Dataset(fileName, "r")

    attrs, dims, vars = ncscan(rootgroup, True, True, True)

