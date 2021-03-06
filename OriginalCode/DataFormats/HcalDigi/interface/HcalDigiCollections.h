#ifndef DIGIHCAL_HCALDIGICOLLECTION_H
#define DIGIHCAL_HCALDIGICOLLECTION_H

#include "DataFormats/Common/interface/SortedCollection.h"
#include "DataFormats/HcalDigi/interface/HBHEDataFrame.h"
#include "DataFormats/HcalDigi/interface/HODataFrame.h"
#include "DataFormats/HcalDigi/interface/HFDataFrame.h"
#include "DataFormats/HcalDigi/interface/HcalCalibDataFrame.h"
#include "DataFormats/HcalDigi/interface/HcalTriggerPrimitiveDigi.h"
#include "DataFormats/HcalDigi/interface/HcalHistogramDigi.h"
#include "DataFormats/HcalDigi/interface/ZDCDataFrame.h"
#include "DataFormats/HcalDigi/interface/CastorDataFrame.h"
#include "DataFormats/HcalDigi/interface/HOTriggerPrimitiveDigi.h"

typedef edm::SortedCollection<HBHEDataFrame> HBHEDigiCollection;
typedef edm::SortedCollection<HODataFrame> HODigiCollection;
typedef edm::SortedCollection<HFDataFrame> HFDigiCollection;
typedef edm::SortedCollection<HcalCalibDataFrame> HcalCalibDigiCollection;
typedef edm::SortedCollection<HcalTriggerPrimitiveDigi> HcalTrigPrimDigiCollection;
typedef edm::SortedCollection<HcalHistogramDigi> HcalHistogramDigiCollection;
typedef edm::SortedCollection<ZDCDataFrame> ZDCDigiCollection;
typedef edm::SortedCollection<CastorDataFrame> CastorDigiCollection;
typedef edm::SortedCollection<HOTriggerPrimitiveDigi> HOTrigPrimDigiCollection;

#endif
