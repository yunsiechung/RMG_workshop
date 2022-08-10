# Data sources
database(
    thermoLibraries=['surfaceThermoPt111', 'primaryThermoLibrary','DFT_QCI_thermo', 'thermo_DFT_CCSDTF12_BAC'], 
    reactionLibraries = [('Surface/Deutschmann_Ni', True)], 
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
    bindingEnergies = {  # values for Ni(111) calculated with VASP
                        'H': (-2.76, 'eV/molecule'),
                        'O': (-4.7, 'eV/molecule'),
                        'C': (-6.45, 'eV/molecule'),
                        'N': (-4.352, 'eV/molecule'), 
                      },
    surfaceSiteDensity=(3.16e-9, 'mol/cm^2'), # values for Ni(111)
)

#catalystProperties(
#	metal='Ru0001'
#)

# List of species

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
    label='CO2',
    reactive=True,
    structure=SMILES("O=C=O"),
)

species(
    label='H2O',
    reactive=True,
    structure=SMILES("O"),
)

species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
)

#-------
species(
    label='site',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)

#----------
# Reaction systems

surfaceReactor(
    temperature=(673,'K'),
    initialPressure=(1.0, 'bar'),
    initialGasMoleFractions={
        "CH4": 0.0,
        "CO2": 1.0,
        "H2O": 0.0,
        "H2": 4.0,
    },
    initialSurfaceCoverages={
        "site": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationConversion={
                'CO2': 0.9,
        },
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=1e-3,
    toleranceMoveToCore=1e-1,
    toleranceInterruptSimulation=1e-1,
    maximumEdgeSpecies=10000
)

generatedSpeciesConstraints(maximumSurfaceSites=1)

options(
    units='si',
    saveRestartPeriod=None,
    generateSeedEachIteration=False,
    saveSeedToDatabase=False,
    generateOutputHTML=True,
    generatePlots=False, 
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
    verboseComments=False,
    saveSeedModulus=-1
)
