import FWCore.ParameterSet.Config as cms

#include "CondCore/DBCommon/data/CondDBCommon.cfi"
#replace CondDBCommon.connect = "oracle://cms_orcoff_int2r/CMS_COND_HCAL"
#replace CondDBCommon.DBParameters.authenticationPath="/afs/cern.ch/cms/DB/conddb"
#replace CondDBCommon.timetype = "runnumber"
from CondCore.DBCommon.CondDBSetup_cfi import *
hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)

es_pool = cms.ESSource("PoolDBESSource",
    CondDBSetup,
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('HcalPedestalsRcd'),
        tag = cms.string('hcal_pedestals_fC_v1_zdc')
    ), 
        cms.PSet(
            record = cms.string('HcalPedestalWidthsRcd'),
            tag = cms.string('hcal_widths_fC_v1_zdc')
        ), 
        cms.PSet(
            record = cms.string('HcalGainsRcd'),
            tag = cms.string('hcal_gains_v1_zdc')
        ), 
        cms.PSet(
            record = cms.string('HcalQIEDataRcd'),
            tag = cms.string('qie_normalmode_v3_zdc')
        ), 
        cms.PSet(
            record = cms.string('HcalElectronicsMapRcd'),
            tag = cms.string('official_emap_16x_v4_9Nov07')
        )),
    connect = cms.string('frontier://FrontierDev/CMS_COND_HCAL'), ##FrontierDev/CMS_COND_HCAL"

    authenticationMethod = cms.untracked.uint32(0)
)

es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('GainWidths', 
        'channelQuality')
)


