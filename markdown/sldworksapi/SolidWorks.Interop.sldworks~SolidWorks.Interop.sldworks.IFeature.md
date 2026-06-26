---
title: "IFeature Interface"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html"
---

# IFeature Interface

Allows access to the feature type, name, parameter data, and the next feature in the FeatureManager design tree.

**NOTE:**Click the**Members**link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
```

### C#

```csharp
public interface IFeature
```

### C++/CLI

```cpp
public interface class IFeature
```

## VBA Syntax

See

[Feature](ms-its:sldworksapivb6.chm::/sldworks~Feature.html)

.

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)

[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)

[Traverse Assembly At Component and Feature Levels (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)

[Get Areas of MidSurface Faces (C#)](Get_Areas_of_MidSurface_Faces_Example_CSharp.htm)

[Get Areas of MidSurface Faces (VB.NET)](Get_Areas_of_MidSurface_FAces_Example_VBNET.htm)

[Get Areas of MidSurface Faces (VBA)](Get_Areas_of_MidSurface_Faces_Example_VB.htm)

[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)

[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)

## Accessors

[IAssemblyDoc::GetActiveGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.html)

[IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html)

[IAssemblyDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~FeatureByName.html)and[IAssemblyDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IFeatureByName.html)

[IBody2::GetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFeatures.html)and[IBody2::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetFeatures.html)

[IBodyFolder::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~GetFeature.html)

[IBomFeature::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetFeature.html)

[ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html)

[IComment::FeatureOwner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment~FeatureOwner.html)

[ICommentFolder::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~GetFeature.html)

[IComplexCornerTreatmentFeatureData::GetTrimToolMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember.html)

[IComponent2::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FeatureByName.html)

[IComponent2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FirstFeature.html)

[IConfiguration::GetDisplayStateFeatureProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.html)

[ICoreFeatureData::BoundingSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoreFeatureData~BoundingSketch.html)

[ICornerManagementFolder::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetFeature.html)

[ICornerManagementFolder::GetStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder~GetStructureSystemFolder.html)

[ICornerMember::GetUnderlyingMemberFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~GetUnderlyingMemberFeature.html)

[ICornerTreatmentFeatureData::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~GetFeature.html)

[ICornerTreatmentGroupFolder::GetCornerTreatments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.html)

[ICornerTreatmentGroupFolder::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetFeature.html)

[ICosmosMotionStudyResults::GetPlotFeatures](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~GetPlotFeatures.html)and[ICosmosMotionStudyResults::IGetPlotFeatures](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~IGetPlotFeatures.html)

[ICosmosMotionStudyResults::InsertPlotFeature](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.ICosmosMotionStudyResults~InsertPlotFeature.html)

[ICurveDrivenPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFeatureArray.html)

[ICutListSortOptions::GetFacesOrFeaturesToExclude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~GetFacesOrFeaturesToExclude.html)

[IDerivedPatternFeatureData::IGetSeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDerivedPatternFeatureData~IGetSeedComponentArray.html)

[IDerivedPatternFeatureData::PatternFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~PatternFeature.html)

[IDerivedPatternFeatureData::SeedComponentArray](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDerivedPatternFeatureData~SeedComponentArray.html)

[IDimension::GetFeatureOwner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetFeatureOwner.html)

[IDimXpertAnnotation::GetModelFeature](ms-its:swdimxpertapi.chm::/SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation~GetModelFeature.html)

[IDimXpertFeature::GetModelFeature](ms-its:swdimxpertapi.chm::/SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature~GetModelFeature.html)

[IDrawingDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~FeatureByName.html)and[IDrawingDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IFeatureByName.html)

[IFace2::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFeature.html)and[IFeature::IGetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetFeature.html)

[IFace2::GetPatternSeedFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetPatternSeedFeature.html)and[IFace2::IGetPatternSeedFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetPatternSeedFeature.html)

[IFeature::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetChildren.html)and[IFeature::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetChildren.html)

[IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html)and[IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html)

[IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html)and[IFeature::IGetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextFeature.html)

[IFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextSubFeature.html)and[IFeature::IGetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextSubFeature.html)

[IFeature::GetOwnerFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetOwnerFeature.html)

[IFeature::GetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetParents.html)and[IFeature::IGetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetParents.html)

[IFeatureFolder::GetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureFolder~GetFeatures.html)and[IFeatureFolder::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureFolder~IGetFeatures.html)

[IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.html)

[IFeatureManager::CreateFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateFeature.html)

[IFeatureManager::CreateFormTool2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateFormTool2.html)

[IFeatureManager::CreateCoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem.html)

[IFeatureManager::CreateCoordinateSystemUsingNumericalValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystemUsingNumericalValues.html)

[IFeatureManager::CreateSaveBodyFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateSaveBodyFeature.html)

[IFeatureManager::DraftXpertChange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~DraftXpertChange.html)

[IFeatureManager::DraftXpertRemove](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~DraftXpertRemove.html)

[IFeatureManager::EndVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html)

[IFeatureManager::FeatureAdvancedTableDrivenPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern.html)

[IFeatureManager::FeatureBossThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureBossThicken.html)

[IFeatureManager::FeatureChainPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureChainPattern.html)

[IFeatureManager::FeatureCircularPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCircularPattern2.html)

[IFeatureManager::FeatureCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCut.html)

[IFeatureManager::FeatureCutThicken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCutThicken.html)

[IFeatureManager::FeatureCutThin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureCutThin.html)

[IFeatureManager::FeatureExtrusion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureExtrusion2.html)

[IFeatureManager::FeatureExtrusionThin2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureExtrusionThin2.html)

[IFeatureManager::FeatureFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillet.html)and[IFeatureManager::IFeatureFillet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IFeatureFillet.html)

[IFeatureManager::FeatureFillPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFillPattern.html)

[IFeatureManager::FeatureFolderLocation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureFolderLocation.html)

[IFeatureManager::FeatureLinearPattern2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLinearPattern2.html)

[IFeatureManager::FeatureLocalCurveDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLocalCurveDrivenPattern.html)

[IFeatureManager::FeatureLocalSketchDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureLocalSketchDrivenPattern.html)

[IFeatureManager::FeatureRevolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve.html)

[IFeatureManager::FeatureRevolveCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveCut.html)

[IFeatureManager::FeatureRevolveThin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html)

[IFeatureManager::FeatureRevolveThinCut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThinCut.html)

[IFeatureManager::FeatureSketchDrivenPattern](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureSketchDrivenPattern.html)

[IFeatureManager::FilletXpertChange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FilletXpertChange.html)

[IFeatureManager::FilletXpertRemove](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)

[IFeatureManager::FinishCornerRelief](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FinishCornerRelief.html)

[IFeatureManager::FinishSMNormalCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishSMNormalCut.html)

[IFeatureManager::GetCornerManagementFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCornerManagementFolders.html)

[IFeatureManager::GetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetFeatures.html)and[IFeatureManager::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IGetFeatures.html)

[IFeatureManager::GetStructureSystemFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetStructureSystemFolders.html)

[IFeatureManager::HoleWizard5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~HoleWizard5.html)

[IFeatureManager::InsertCenterofMass](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCenterOfMass.html)

[IFeatureManager::InsertCenterOfMassReferencePoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCenterOfMassReferencePoint.html)

[IFeatureManager::InsertCombineFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCombineFeature.html)and[IFeatureManager::IInsertCombineFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IInsertCombineFeature.html)

[IFeatureManager::InsertCosmeticThread2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCosmeticThread2.html)

[IFeatureManager::InsertCosmeticWeldBead2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.html)

[IFeatureManager::InsertCrossBreak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCrossBreak.html)

[IFeatureManager::InsertCutBlend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutBlend.html)

[IFeatureManager::InsertCutSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutSwept3.html)

IFeatureManager::InsertCutSurface

[IFeatureManager::InsertDeleteBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDeleteBody.html)

[IFeatureManager::InsertDeleteHoleForSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDeleteHoleForSurface.html)

IFeatureManager::InsertDerivedPattern

IFeatureManager::InsertDwgOrDxfFile

IFeatureManager::InsertEdgeMerge

IFeatureManager::InsertEndCapFeature

IFeatureManager::InsertEndCapFeature2

IFeatureManager::InsertFeatureChamfer

IFeatureManager::InsertFeatureLock

IFeatureManager::InsertFeatureTreeFolder2

IFeatureManager::InsertFilletBeadFeature2

IFeatureManager::InsertFilletBeadFeature3

IFeatureManager::InsertFillSurface2

IFeatureManager::InsertFlattenSurface

IFeatureManager::InsertFlexFeature

IFeatureManager::InsertFormToolFeature

IFeatureManager::InsertFreeform

IFeatureManager::InsertGlobalBoundingBox

IFeatureManager::InsertGroundPlane

IFeatureManager::InsertGussetFeature

IFeatureManager::InsertGussetFeature2

IFeatureManager::InsertIndent

IFeatureManager::InsertMacroFeature3 and IFeatureManager::IInsertMacroFeature3

IFeatureManager::InsertMateReference2

IFeatureManager::InsertMirrorFeature

IFeatureManager::InsertMoldCoreCavitySolids

IFeatureManager::InsertMoldPartingLine

IFeatureManager::InsertMoldPartingSurface

IFeatureManager::InsertMoldShutOffSurface

IFeatureManager::InsertMoveCopyBody2

IFeatureManager::InsertMoveFace

IFeatureManager::InsertMultifaceDraft

IFeatureManager::InsertNetBlend

IFeatureManager::InsertProtrusionBlend

IFeatureManager::InsertProtrusionSwept3

IFeatureManager::InsertReferencePoint and IFeatureManager::IInsertReferencePoint

IFeatureManager::InsertRevolvedRefSurface

IFeatureManager::InsertRuledSurfaceFromEdge2

IFeatureManager::InsertScale

IFeatureManager::InsertSheetMetal3dBend

IFeatureManager::InsertSheetMetalBaseFlange2

IFeatureManager::InsertSheetMetalCornerTrim

IFeatureManager::InsertSheetMetalEdgeFlange2 and IFeatureManager::IInsertSheetMetalEdgeFlange2

IFeatureManager::InsertSheetMetalGussetFeature3

IFeatureManager::InsertSheetMetalHem2

IFeatureManager::InsertSheetMetalLoftedBend

IFeatureManager::InsertSheetMetalMiterFlange

IFeatureManager::InsertSplitLineIntersect

IFeatureManager::InsertStructuralWeldment2

IFeatureManager::InsertStructuralWeldment3

IFeatureManager::InsertSubFolder

IFeatureManager::InsertSubWeldFolder

IFeatureManager::InsertSubWeldFolder2

IFeatureManager::InsertSweepSurface2

IFeatureManager::InsertTableDrivenPattern and IFeatureManager::IInsertTableDrivenPattern

IFeatureManager::InsertUntrimSurface

IFeatureManager::InsertWeldmentCutList

IFeatureManager::InsertWeldmentCutList2

IFeatureManager::InsertWeldmentFeature

IFeatureManager::InsertWeldmentTrimFeature

IFeatureManager::InsertWeldmentTrimFeature2

IFeatureManager::InsertWrapFeature

[IFeatureManager::PostIntersect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PostIntersect.html)

IFeatureManager::PostSplitBody

IFeatureManager::PostTrimSurface

IFeatureManager::SetNetBlendCurveData

IFeatureManager::SetNetBlendDirectionData

IFeatureManager::SimpleHole

IFeatureStatistics::Features

IFillPatternFeatureData::PatternFeatureArray

IFlatPatternFeatureData::GetAddCornerTrim

IFlatPatternFeatureData::GetBreakCorners

IFlatPatternFolder::GetFeature

IFlatPatternFolder::GetFlatPatterns

IFoldsFeatureData::Bends

IFoldsFeatureData::IGetBends

IGeneralTableFeature::GetFeature

IGeneralToleranceTableFeature::GetFeature

IHoleTable::GetFeature

ILinearPatternFeatureData::PatternFeatureArray

ILocalCircularPatternFeatureData::IGetSeedComponentArray

ILocalCircularPatternFeatureData::SeedComponentArray

ILocalLinearPatternFeatureData::IGetSeedComponentArray

ILocalLinearPatternFeatureData::SeedComponentArray

ILoftFeatureData::GuideCurves

ILoftFeatureData::IGetGuideCurves

IMacroFeatureData::IGetParents

IMacroFeatureData::Parents

IModelDoc2::FeatureByPositionReverse

IModelDoc2::FirstFeature

IModelDoc2::InsertProjectedSketch2 and IModelDoc2::IInsertProjectedSketch2

IModelDoc2::InsertSketchForEdgeFlange and IModelDoc2::IInsertSketchForEdgeFlange

IModelDocExtension::CreateStructureSystem

IModelDocExtension::GetLastFeatureAdded

IModelDocExtension::GetTemplateSheetMetal

IMotionPlotFeatureData::GetXAxis

IMotionPlotFeatureData::GetYAxis and IMotionPlotFeatureData::IGetYAxis

IPartDoc::CreateFeatureFromBody3

IPartDoc::CreateSurfaceFeatureFromBody and IPartDoc::ICreateSurfaceFeatureFromBody

IPartDoc::FeatureById and IPartDoc::IFeatureById

IPartDoc::FeatureByName and IPartDoc::IFeatureByName

IPartDoc::FirstFeature and IPartDoc::IFirstFeature

IPartDoc::ICreateFeatureFromBody4

IPartDoc::InsertPart

IPartDoc::MirrorPart2

IProfileGroupFolder::GetFeature

IProfileGroupFolder::GetStructureSystemMembers

IPunchTable::GetFeature

IReplaceFaceFeatureData::IGetReplacementSurfaces

IReplaceFaceFeatureData::ReplacementSurfaces

IRevisionTableFeature::GetFeature

ISelectionMgr::GetSelectedObject6

ISheetMetalFolder::GetFeature

ISheetMetalFolder::GetSheetMetals

ISimpleFilletFeatureData2::IGetFeatures

ISimpleFilletFeatureData2::Features

ISimulation::GetFeature

ISketchBlockDefinition::GetFeature

ISketchPatternFeatureData::PatternFeatureArray

ISketchPicture::GetFeature

IStructureSystemFolder::GetCornerManagementFolder

IStructureSystemFolder::GetFeature

IStructureSystemMemberFeatureData::GetFeature

ISweepFeatureData::IGetGuideCurves

ISweepFeatureData::GuideCurves

ISweepFeatureData::Path

ISweepFeatureData::Profile

ITableAnchor::GetFeature

ITablePatternFeatureData::PatternFeatureArray

ITitleBlockTableFeature::GetFeature

IWeldmentCutListFeature::GetFeature

## Access Diagram

[Feature](SWObjectModel.pdf#Feature)

## See Also

[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
