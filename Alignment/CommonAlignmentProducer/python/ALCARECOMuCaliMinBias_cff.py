# The following comments couldn't be translated into the new config version:

# to be precisely defined!!!

# AlCaReco for muon calibration using MinBias events
import FWCore.ParameterSet.Config as cms

import HLTrigger.HLTfilters.hltHighLevel_cfi
ALCARECOMuCaliMinBiasHLT = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
    HLTPaths = ['HLTMuon'],
    andOr = True, ## choose logical OR between Triggerbits
    throw = False # tolerate triggers stated above, but not available
    )

import Alignment.CommonAlignmentProducer.AlignmentMuonSelector_cfi
ALCARECOMuCaliMinBias = Alignment.CommonAlignmentProducer.AlignmentMuonSelector_cfi.AlignmentMuonSelector.clone()

ALCARECOMuCaliMinBias.filter = True ##do not store empty events	

ALCARECOMuCaliMinBias.applyBasicCuts = True
ALCARECOMuCaliMinBias.ptMin = 1.5 ##GeV

ALCARECOMuCaliMinBias.ptMax = 9999
ALCARECOMuCaliMinBias.etaMin = -2.4
ALCARECOMuCaliMinBias.etaMax = 2.4
ALCARECOMuCaliMinBias.phiMin = -3.1416
ALCARECOMuCaliMinBias.phiMax = 3.1416
# Stand Alone Muons
ALCARECOMuCaliMinBias.nHitMinSA = 1
ALCARECOMuCaliMinBias.nHitMaxSA = 9999999
ALCARECOMuCaliMinBias.chi2nMaxSA = 9999999.
# Global Muons
ALCARECOMuCaliMinBias.nHitMinGB = 0
ALCARECOMuCaliMinBias.nHitMaxGB = 9999999
ALCARECOMuCaliMinBias.chi2nMaxGB = 9999999.
# Tracker Only
ALCARECOMuCaliMinBias.nHitMinTO = 0
ALCARECOMuCaliMinBias.nHitMaxTO = 9999999
ALCARECOMuCaliMinBias.chi2nMaxTO = 9999999.
ALCARECOMuCaliMinBias.applyNHighestPt = False
ALCARECOMuCaliMinBias.applyMultiplicityFilter = False
ALCARECOMuCaliMinBias.applyMassPairFilter = False

seqALCARECOMuCaliMinBias = cms.Sequence(ALCARECOMuCaliMinBiasHLT+ALCARECOMuCaliMinBias)
