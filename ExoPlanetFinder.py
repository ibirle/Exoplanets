import kplr
import pyfits
import math

#This function just takes the average of a group of numbers given to it
def Avg(x):
    count = 0
    total = 0
    for num in x: #loops through every number given
        if(not math.isnan(num)):#this accounts for potential data points that are not numbers or missing
            count = count + 1
            total = total + num
    return (total/count)


c = kplr.API()
names = []

stars = c.kois()#gets a list of kepler objects of interest
for star in stars:
    cad = []#holds the average of each cadence
    for chart in star.get_light_curves(short_cadence=False): #gets light curves that are 30 minute exposures of the koi
        with chart.open() as f:
            data = f[1].data
            flux = data["sap_flux"]#sap_flux is the flux of the koi for every point taken
            cad.append(Avg(flux))
    for day in cad:
        #this if statment sees if any individual cadence is less than 80% of the average flux
        if(day/Avg(cad) < .8 and not star.star.kic_teff in names): 
            print star.star.kic_teff
            names.append(star.star.kic_teff)
