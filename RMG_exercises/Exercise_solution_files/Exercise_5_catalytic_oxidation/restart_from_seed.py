restartFromSeed(path='seed')

# Data sources
database(
    thermoLibraries=['surfaceThermoPt111', 'primaryThermoLibrary', 'DFT_QCI_thermo', 'thermo_DFT_CCSDTF12_BAC'], 
    reactionLibraries = [('Surface/CPOX_Pt/Deutschmann2006', True)],
    seedMechanisms = [],
    kineticsDepositories = ['!training'],
    kineticsFamilies = ['surface'],
    kineticsEstimator = 'rate rules',
)

catalystProperties(
   metal='Pt111'
)

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

species(
    label='CO',
    reactive=True,
    structure=SMILES("[C-]#[O+]"),
)

species(
    label='O2',
    reactive=True,
    structure=adjacencyList(
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
)

species(
    label='N2',
    reactive=False,
    structure=SMILES("N#N"),
)


#-------
species(
    label='Pt',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)
#----------
# Reaction systems
surfaceReactor(
    temperature=[(523,'K'),(873,'K')],
    initialPressure=(1.0, 'bar'),
    nSims=3,
    initialGasMoleFractions={
        "O2": 0.9335,
        "CO2": 12,
        "H2O": 12,
        "H2": 0.167,
	"CH4": 0.3,
	"CO": 0.5,
	"N2": 74.0995,
    },
    initialSurfaceCoverages={
        "Pt": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationRateRatio=(1e-10),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=1e-8,
    toleranceMoveToCore=1e-2,
    toleranceInterruptSimulation=1e-2,
    maximumEdgeSpecies=10000
)

generatedSpeciesConstraints(maximumSurfaceSites=1)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False, # Enable to make plots of core and edge size etc.. But takes a lot of the total runtime!
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
    verboseComments=True,
)

