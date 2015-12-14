import FWCore.ParameterSet.Config as cms

process = cms.Process("EventDisplay")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("HcalTBSource",
    fileNames = cms.untracked.vstring("file:/tmp/chenyi/HTB_108532.root"),
    streams = cms.untracked.vstring('Chunk699', 'HCAL_Trigger', 'HCAL_SlowData', 'HCAL_QADCTDC', 'HCAL_DCC021')
)

process.tbunpack = cms.EDFilter("HcalTBObjectUnpacker",
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
    baselineSamples = cms.untracked.uint32(3),
    mip = cms.untracked.string("MIPCalibration.txt"),
    useMotherBoard0 = cms.untracked.bool(True),
    useMotherBoard1 = cms.untracked.bool(True),
    useMotherBoard2 = cms.untracked.bool(False),
    useMotherBoard3 = cms.untracked.bool(True)
)

process.averagecharge = cms.EDProducer("FillAverageChargeLayerAnalyzer",
    output = cms.untracked.string("TotalEnergy_108532.root"),
    textOutput = cms.untracked.bool(True),
    interpolate = cms.untracked.bool(True)  # interpolate for missing channels by averaging neighboring channels
)

process.ABCcut = cms.EDFilter("SingleTowerParticleFilter")

process.energycut = cms.EDFilter("TotalEnergyCutFilter",
   cut = cms.untracked.double(30),
   interpolate = cms.untracked.bool(True),
)

process.eventdisplay = cms.EDAnalyzer("FillEventDisplayAnalyzer",
   maxEvent = cms.untracked.int32(100),
   output = cms.untracked.string("EventDisplay_108532.root")
)

process.MessageLogger = cms.Service("MessageLogger",
    default = cms.untracked.PSet(
        reportEvery = cms.untracked.int32(100)
    )
)

process.p = cms.Path(process.tbunpack*process.ABCcut*process.vlsbinfo*process.energycut*process.eventdisplay)
