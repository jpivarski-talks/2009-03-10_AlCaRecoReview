# last update: $Date: 2008/12/15 17:44:36 $ by $Author: flucke $

import FWCore.ParameterSet.Config as cms

# AlCaReco for track based alignment using Cosmic muon events
OutALCARECOTkAlCosmics0THLT = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlCosmicsCTF0THLT', 
            'pathALCARECOTkAlCosmicsCosmicTF0THLT', 
            'pathALCARECOTkAlCosmicsRS0THLT')
    ),
    outputCommands = cms.untracked.vstring()
)
# We have the same producers as in the non-HLT path, just HLT sel. in front,
# ==> identical keep statements:
import Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmics0T_Output_cff
OutALCARECOTkAlCosmics0THLT.outputCommands = Alignment.CommonAlignmentProducer.ALCARECOTkAlCosmics0T_Output_cff.OutALCARECOTkAlCosmics0T.outputCommands
