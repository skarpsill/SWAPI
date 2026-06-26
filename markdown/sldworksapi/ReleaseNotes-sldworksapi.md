---
title: "Release Notes"
project: "SOLIDWORKS API Help"
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/ReleaseNotes-sldworksapi.html"
---

# Release Notes

This topic provides you with quick access to the enhancements in SOLIDWORKS API 2024.

###### Service Pack 1

###### New interfaces

##### IClearanceResult Interface

- [IClearanceResult::ClearanceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceType.html)
- [IClearanceResult::ClearanceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceValue.html)
- [IClearanceResult::ComponentsOrFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ComponentsOrFaces.html)

##### IClearanceVerificationMgr Interface

- [IClearanceVerificationMgr::CalculateClearances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CalculateClearances.html)
- [IClearanceVerificationMgr::CheckClearanceBetween](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CheckClearanceBetween.html)
- [IClearanceVerificationMgr::GetComponentsOrFacesToCheck](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetComponentsOrFacesToCheck.html)
- [IClearanceVerificationMgr::GetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetMinimumAcceptableClearance.html)
- [IClearanceVerificationMgr::IgnoreClearanceEqualToSpecifiedValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue.html)
- [IClearanceVerificationMgr::SetComponentsOrFacesToCheck](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetComponentsOrFacesToCheck.html)
- [IClearanceVerificationMgr::SetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetMinimumAcceptableClearance.html)
- [IClearanceVerificationMgr::TreatSubAssembliesAsComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~TreatSubAssembliesAsComponents.html)

###### New methods and property

##### IAssemblyDoc Interface

- [IAssemblyDoc::ClearanceVerificationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ClearanceVerificationManager.html)

##### IComponent2 Interface

- [IComponent2::GetConfigurationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetConfigurationCount.html)
- [IComponent2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetConfigurationNames.html)
- [IComponent2::GetPLMID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPLMID.html)
- [IComponent2::GetRepresentationParent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRepresentationParent.html)
- [IComponent2::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetType.html)

##### IModelDocExtension Interface

- [IModelDocExtension::GetCSYSDistances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances.html)
- [IModelDocExtension::GetCSYSEulersAngularRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation.html)
- [IModelDocExtension::GetCSYSXYZAngularRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation.html)

##### ISketchBlockInstance Interface

- [ISketchBlockInstance::GetScale3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetScale3.html)
- [ISketchBlockInstance::IsNested](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IsNested.html)

##### IView Interface

- [IView::EnumSectionLines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines2.html)

  (obsoletes IView::EnumSectionLines)

###### Obsoleted method

##### IView Interface

- IView::EnumSectionLines (superseded by

  [IView:EnumSectionLines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines2.html)

  )

###### Service Pack 0

- [New functionality](#NewFunctionality0)
- [New interfaces](#NewInterfaces0)
- [New delegates, methods, and properties](#NewMethods0)
- [Obsoleted methods](#obs)

###### New functionality

- Access the configuration-specific custom property manager of:

  - a cut list. See

    [ICutListItem::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem~CustomPropertyManager.html)

    and

    [IConfiguration::GetCutListItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCutListItems.html)

    .
  - an assembly component. See

    [IComponent2::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~CustomPropertyManager.html)

    .
- Retrieve errors that occurred during the last call to IFeatureManager::CreateFeature. See

  [IFeatureManager::GetCreateFeatureErrors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCreateFeatureErrors.html)

  .
- Untrim or extend a surface outside selected edges, optionally trimming inside selected edges. See

  [IFeatureManager::InsertUntrimSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface2.html)

  .
- Insert BOM tables in parts, assemblies, and drawings with detailed cut lists and specify whether to dissolve components in indented BOMs. See

  [IBomFeature::DissolvePartLevelRows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.html)

  ,

  [IModelDocExtension::InsertBomTable4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable4.html)

  , and

  [IView::InsertBomTable5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable5.html)

  .

##### Other major enhancements

- Get and set whether to display dual unit values in dimension range lengths of Gtols. See

  [IGtol::GetDisplayDualDimensionInRangeValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetDiplayDualDimensionInRangeValues.html)

  and

  [IGtol::SetDisplayDualDimensionInRangeValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetDiplayDualDimensionInRangeValues.html)

  .
- Get the diameter of the sphere encompassing the bounding box of a model. See

  [IModelDocExtension::GetSphericalBoxDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSphericalBoxDiameter.html)

  .
- Set whether to save as previous version. See

  [IAdvancedSaveAsOptions::SaveAsPreviousVersion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.html)

  .
- Insert all model annotations or all reference geometry into a drawing document's selected drawing view. See

  [IDrawingDoc::InsertModelAnnotations4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations4.html)

  .

[Back to top](#Top)

###### New interfaces

##### ICutListItem Interface

- [ICutListItem::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListItem~CustomPropertyManager.html)

###### New delegates, methods, and properties

##### DAssemblyDocEvents

- [DAssemblyDocEvents_ActiveAnnotationViewChangeNotifyEventHandler Delegate ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveAnnotationViewChangeNotifyEventHandler.html)

##### DPartDocEvents

- [DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler Delegate ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler.html)

##### IAdvancedSaveAsOptions Interface

- [IAdvancedSaveAsOptions::SaveAsPreviousVersion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.html)

##### IBomFeature Interface

- [IBomFeature::DissolvePartLevelRows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.html)

##### IComponent2 Interface

- [IComponent2::CustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~CustomPropertyManager.html)

##### IConfiguration Interface

- [IConfiguration::GetCutListItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCutListItems.html)

##### IDrawingDoc Interface

- [IDrawingDoc::InsertModelAnnotations4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations4.html)

  (obsoletes IDrawingDoc::InsertModelAnnotations3)

##### IFeatureManager Interface

- [IFeatureManager::InsertUntrimSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface2.html)

  (obsoletes IFeatureManager::InsertUntrimSurface)

##### IGtol Interface

- [IGtol::GetDisplayDualDimensionInRangeValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetDiplayDualDimensionInRangeValues.html)

- [IGtol::SetDisplayDualDimensionInRangeValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetDiplayDualDimensionInRangeValues.html)

##### IModelDocExtension Interface

- [IModelDocExtension::GetSphericalBoxDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSphericalBoxDiameter.html)
- [IModelDocExtension::InsertBomTable4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable4.html)

  (obsoletes IModelDocExtension::InsertBomTable3)

##### IView Interface

- [IView::InsertBomTable5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable5.html)

  (obsoletes IView::InsertBomTable4)

###### Obsoleted methods

##### IDrawingDoc Interface

- IDrawingDoc::InsertModelAnnotations3 (superseded by

  [IDrawingDoc::InsertModelAnnotations4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations4.html)

  )

##### IFeatureManager Interface

- IFeatureManager::InsertUntrimSurface (superseded by

  [IFeatureManager::InsertUntrimSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface2.html)

  )

##### IModelDocExtension Interface

- IModelDocExtension::InsertBomTable3 (superseded by

  [IModelDocExtension::InsertBomTable4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBomTable4.html)

  )

##### IView Interface

- IView::InsertBomTable4 (superseded by

  [IView::InsertBomTable5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable5.html)

  )

[Back to top](#Top)
