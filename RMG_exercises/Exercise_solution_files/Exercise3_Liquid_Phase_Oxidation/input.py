# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# Constraints on generated species
generatedSpeciesConstraints(
    maximumRadicalElectrons = 3,
)

# List of species
species(
    label='pentane',
    reactive=True,
    structure=SMILES("CCCCC"),
)

species(
    label='oxygen',
    reactive=True,
    structure=SMILES("[O][O]"),
)

# Reaction systems
liquidReactor(
    temperature=(500,'K'),
    initialConcentrations={
        "pentane": (6.154e-3,'mol/cm^3'),
        "oxygen": (4.953e-6,'mol/cm^3')
    },
    terminationTime=(5,'s'),
)

solvation(
	solvent='pentane'
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=1E-9,
    toleranceMoveToCore=0.001,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000
)

options(
    units='si',
    generateOutputHTML=False,
    generatePlots=False,
    saveSimulationProfiles=True,
)
