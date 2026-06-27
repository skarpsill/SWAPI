---
title: "Release Notes"
project: "SOLIDWORKS Simulation API Help"
interface: ""
member: ""
kind: "topic"
source: "cworksapi/ReleaseNotes-swsimulationapi.html"
---

# Release Notes

This topic provides you with quick access to the enhancements in SOLIDWORKS Simulation API 2024.

###### Service Pack 1

###### New methods and property

##### ICWBearingConnector interface

- [ICWBearingConnector::LateralStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~LateralStiffnessValue.html)

  (obsoletes ICWBearingConnector::RotationalStiffnessValue)

##### ICWDynamicStudyOptions interface

- [ICWDynamicStudyOptions::GetExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequencies.html)
- [ICWDynamicStudyOptions::GetExtraFrequenciesTolerancePercentage](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTolerancePercentage.html)
- [ICWDynamicStudyOptions::GetExtraFrequenciesTotal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesTotal.html)
- [ICWDynamicStudyOptions::GetExtraFrequenciesUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetExtraFrequenciesUnit.html)
- [ICWDynamicStudyOptions::GetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetIncludeExtraFrequencies.html)
- [ICWDynamicStudyOptions::SetExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequencies.html)
- [ICWDynamicStudyOptions::SetExtraFrequenciesTolerancePercentage](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesTolerancePercentage.html)
- [ICWDynamicStudyOptions::SetExtraFrequenciesUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetExtraFrequenciesUnit.html)
- [ICWDynamicStudyOptions::SetIncludeExtraFrequencies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetIncludeExtraFrequencies.html)

###### Obsoleted property

##### ICWBearingConnector interface

- ICWBearingConnector::RotationalStiffnessValue (superseded by

  [ICWBearingConnector::LateralStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~LateralStiffnessValue.html)

  )

###### Service Pack 0

###### New interface

##### ICWBearingConnector interface

- [ICWBearingConnector::AllowLenByDiamRatioGreaterThan2ForShaft](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AllowLenByDiamRatioGreaterThan2ForShaft.html)
- [ICWBearingConnector::AllowShaftByBearingRatioGreaterThan2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AllowShaftByBearingRatioGreaterThan2.html)
- [ICWBearingConnector::AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AxialStiffnessValue.html)
- [ICWBearingConnector::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~BeginEdit.html)
- [ICWBearingConnector::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~ConnectionType.html)
- [ICWBearingConnector::EndEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~EndEdit.html)
- [ICWBearingConnector::GetLastErrorCode](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~GetLastErrorCode.html)
- [ICWBearingConnector::PerformAdvanceValidations](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~PerformAdvanceValidations.html)
- [ICWBearingConnector::ReplaceCircularFaceForShaft](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~ReplaceCircularFaceForShaft.html)
- [ICWBearingConnector::ReplaceCircularFaceOrEdgeForHousing](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~ReplaceCircularFaceOrEdgeForHousing.html)
- [ICWBearingConnector::RotationalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~RotationalStiffnessValue.html)
- [ICWBearingConnector::StabilizeShaftRotation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotation.html)
- [ICWBearingConnector::StabilizeShaftRotationalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotationalStiffnessValue.html)
- [ICWBearingConnector::StabilizeShaftRotationType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StabilizeShaftRotationType.html)
- [ICWBearingConnector::StiffnessType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~StiffnessType.html)
- [ICWBearingConnector::TiltStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~TiltStiffnessValue.html)
- [ICWBearingConnector::UnitType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~UnitType.html)

###### New methods and properties

##### ICWFrequencyStudyOptions interface

- [ICWFrequencyStudyOptions::CheckDecouple](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckDecouple.html)
- [ICWFrequencyStudyOptions::FrequencyCapOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FrequencyCapOption.html)
- [ICWFrequencyStudyOptions::FrequencyCapValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FrequencyCapValue.html)

##### ICWLoadsAndRestraintsManager interface

- [ICWLoadsAndRestraintsManager::AddBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddBearingConnector.html)
- [ICWLoadsAndRestraintsManager::GetBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetBearingConnector.html)

##### ICWStudyManager interface

- [ICWStudyManager::ConvertStudy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy2.html)

  (obsoletes ICWStudyManager::ConvertStudy)
- [ICWStudyManager::DuplicateStudy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy2.html)

  (obsoletes ICWStudyManager::DuplicateStudy)

##### Back to top
