#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "TBDataFormats/HcalTBObjects/interface/HcalTBTriggerData.h"
#include "TBDataFormats/HcalTBObjects/interface/HcalTBRunData.h"
#include "TBDataFormats/HcalTBObjects/interface/HcalTBEventPosition.h"
#include "TBDataFormats/HcalTBObjects/interface/HcalTBTiming.h"
#include "FWCore/Framework/interface/Selector.h"
#include <iostream>

using namespace std;

namespace cms {

  /** \class HcalTBObjectDump
      
  $Date: 2007/04/10 23:11:20 $
  $Revision: 1.6 $
  \author J. Mans - Minnesota
  */
  class HcalTBObjectDump : public edm::EDAnalyzer {
  public:
    explicit HcalTBObjectDump(edm::ParameterSet const& conf);
    virtual void analyze(edm::Event const& e, edm::EventSetup const& c);
  };


  HcalTBObjectDump::HcalTBObjectDump(edm::ParameterSet const& conf) {
  }
  
  void HcalTBObjectDump::analyze(edm::Event const& e, edm::EventSetup const& c) {
    
    try {
      edm::Handle<HcalTBTriggerData> td;

      e.getByType(td);
      const HcalTBTriggerData& info=*(td);

      cout << "TRIGGER DATA: ";
      cout << info;    
    } catch (...) {
      cout << "No HcalTBTriggerData." << endl;
    }

    try {
      edm::Handle<HcalTBRunData> td;

      e.getByType(td);
      const HcalTBRunData& info=*(td);

      cout << "RUN DATA: ";
      cout << info;      
    } catch (...) {
      cout << "No HcalTBRunData." << endl;
    }

    try {
      edm::Handle<HcalTBEventPosition> td;

      e.getByType(td);
      const HcalTBEventPosition& info=*td;

      cout << "Event position info: ";
      cout << info;      
    } catch (...) {
      cout << "No HcalTBEventPosition." << endl;
    }

    try {
      
      edm::Handle<HcalTBTiming>td;

      e.getByType(td);
      const HcalTBTiming& info=*(td);

      cout << "Timing: ";
      cout << info;
      
    } catch (...) {
      cout << "No HcalTBTiming." << endl;
    }

    cout << endl;    
  }
}

#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using namespace cms;

DEFINE_SEAL_MODULE();
DEFINE_ANOTHER_FWK_MODULE(HcalTBObjectDump);

