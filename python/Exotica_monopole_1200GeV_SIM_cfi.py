import FWCore.ParameterSet.Config as cms

def customise(process):

  process.g4SimHits.Physics.MonopoleMass = 1200

  return process
  

