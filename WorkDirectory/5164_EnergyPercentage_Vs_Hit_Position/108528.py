import FWCore.ParameterSet.Config as cms

process = cms.Process("VlsbInfo")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("HcalTBSource",
    fileNames = cms.untracked.vstring("file:/home/yichen/TB2009/HTB_108528.root"),
    streams = cms.untracked.vstring('Chunk699', 'HCAL_Trigger', 'HCAL_SlowData', 'HCAL_QADCTDC', 'HCAL_DCC021')
)

process.tbunpack = cms.EDProducer("HcalTBObjectUnpacker",
    #IncludeUnmatchedHits = cms.untracked.bool(False),
    HcalTriggerFED = cms.untracked.int32(1),
    HcalVLSBFED = cms.untracked.int32(699),
    HcalTDCFED = cms.untracked.int32(8),
    HcalQADCFED = cms.untracked.int32(8),
    HcalSlowDataFED = cms.untracked.int32(3),
    ConfigurationFile = cms.untracked.string('configQADCTDC_TB2009.txt')
)

process.vlsbinfo = cms.EDProducer("VLSBInformationProducer",
    minSample = cms.untracked.uint32(0),
    maxSample = cms.untracked.uint32(31),
    baselineSamples = cms.untracked.uint32(2),
    mip = cms.untracked.string("SecondaryMIP.txt"),
    roughmip = cms.untracked.string("PercentageCorrectedGeV.txt"),
    secondaryShift = cms.untracked.string("PercentageCorrectedGeV_SecondaryShift.txt"),
    lowestSampleSubtraction = cms.untracked.bool(True),
    numberOfSamplesForSubtraction = cms.untracked.int32(16),
    numberOfSamplesToSkip = cms.untracked.int32(16),
    useMotherBoard0 = cms.untracked.bool(True),
    useMotherBoard1 = cms.untracked.bool(True),
    useMotherBoard2 = cms.untracked.bool(False),
    useMotherBoard3 = cms.untracked.bool(True),
    usePedestalMean = cms.untracked.bool(True),
    pedestalFile = cms.untracked.string("PedestalMean_108528.txt"),
    adcMap = cms.untracked.string("FinalAdcMapping_All.txt")
    # interCalibration = cms.untracked.string("InterCalibration.txt")
)

process.ABCcut = cms.EDFilter("SingleTowerParticleFilter")

process.percentage = cms.EDAnalyzer("FillCentralTowerEnergyPercentage",
   output = cms.untracked.string("CentralTowerEnergyPercentage_108528.root")
)

process.maxenergycut = cms.EDFilter("TotalEnergyCutFilter",
    cut = cms.untracked.double(200)
)

process.MessageLogger = cms.Service("MessageLogger",
    default = cms.untracked.PSet(
        reportEvery = cms.untracked.int32(250)
    )
)

process.muonveto = cms.EDFilter("MuonVetoFilter")

process.p = cms.Path(
   process.tbunpack *
   process.ABCcut *
   ~process.muonveto *
   process.vlsbinfo *
   process.percentage
)

