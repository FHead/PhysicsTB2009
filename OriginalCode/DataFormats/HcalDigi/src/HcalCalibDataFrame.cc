#include "DataFormats/HcalDigi/interface/HcalCalibDataFrame.h"

HcalCalibDataFrame::HcalCalibDataFrame() : id_(0), 
			     size_(0),
			     hcalPresamples_(0)
{
}

HcalCalibDataFrame::HcalCalibDataFrame(const HcalCalibDetId& id) : 
  id_(id), 
  size_(0),
  hcalPresamples_(0)
{
  // TODO : test id for HcalForward
}
  
void HcalCalibDataFrame::setSize(int size) {
  if (size>MAXSAMPLES) size_=MAXSAMPLES;
  else if (size<=0) size_=0;
  else size_=size;
}
void HcalCalibDataFrame::setPresamples(int ps) {
  hcalPresamples_|=ps&0xF;
}
void HcalCalibDataFrame::setReadoutIds(const HcalElectronicsId& eid) {
  electronicsId_=eid;
}

bool HcalCalibDataFrame::validate(int firstSample, int nSamples) const {
  int capid=-1;
  bool ok=true;
  for (int i=0; ok && i<nSamples && i+firstSample<size_; i++) {
    if (data_[i+firstSample].er() || !data_[i+firstSample].dv()) ok=false;
    if (i==0) capid=data_[i+firstSample].capid();
    if (capid!=data_[i+firstSample].capid()) ok=false;
    capid=(capid+1)%4;
  }
  return ok;
}

void HcalCalibDataFrame::setZSInfo(bool unsuppressed, bool markAndPass) {
  if (markAndPass) hcalPresamples_|=0x10;
  if (unsuppressed) hcalPresamples_|=0x20;
}

int HcalCalibDataFrame::fiberIdleOffset() const {
  int val=(hcalPresamples_&0xF00)>>8;
  return (val==0)?(-1000):(((val&0x8)==0)?(-(val&0x7)):(val&0x7));
}

void HcalCalibDataFrame::setFiberIdleOffset(int offset) {
  hcalPresamples_&=0xFFFF0FF;
  if (offset>=7) hcalPresamples_|=0xF00;
  else if (offset>=0) hcalPresamples_|=(0x800)|(offset<<8);
  else if (offset>=-7) hcalPresamples_|=((-offset)<<8);
  else hcalPresamples_|=0x700;
}  

std::ostream& operator<<(std::ostream& s, const HcalCalibDataFrame& digi) {
  s << digi.id() << " " << digi.size() << " samples  " << digi.presamples() << " presamples ";
  if (digi.zsUnsuppressed()) s << " zsUS ";
  if (digi.zsMarkAndPass()) s << " zsM&P ";
  if (digi.fiberIdleOffset()!=0)
    if (digi.fiberIdleOffset()==-1000) s << " nofiberOffset";
    else s << " fiberOffset=" << digi.fiberIdleOffset();
  s << std::endl;
  for (int i=0; i<digi.size(); i++) 
    s << "  " << digi.sample(i) << std::endl;
  return s;
}
  

