---
title: "gtError_e Enumeration"
project: "SOLIDWORKS Utilities API Help"
interface: "gtError_e"
member: ""
kind: "enum"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtError_e.html"
---

# gtError_e Enumeration

Error codes returned by SOLIDWORKS Utilities APIs.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum gtError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As gtError_e
```

### C#

```csharp
public enum gtError_e : System.Enum
```

### C++/CLI

```cpp
public enum class gtError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| gtErrArgument1Incorrect | 11001 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrArgument2Incorrect | 11002 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrArgumentOutofRange | 22 |
| gtErrAssemblyInEditPartMode | 26 = Returned by ICompareGeometry::CompareGeometry3 if an assembly is in edit part mode |
| gtErrBsdAlreadyOpen | Not used |
| gtErrBsdDefaultDrwTemplate | Not used |
| gtErrBsdDocNotSaved | Not used |
| gtErrBsdInvalidArg | Not used |
| gtErrBsdInvalidSaveLocationPath | Not used |
| gtErrBsdInvalidSheetFormatPath | Not used |
| gtErrBsdLowMemory | Not used |
| gtErrBsdNoActivePartDoc | Not used |
| gtErrBsdNoSheetMetalFeatureFound | Not used |
| gtErrBsdNotInitialized | Not used |
| gtErrBsdOpenedReadOnly | Not used |
| gtErrBsdUserCanceled | Not used |
| gtErrBsdVirtualComponent | Not used |
| gtErrCompareFacesFailed | 7001 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrCompareFeaturesFailed | 6001 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompareGeometryNotExecuted | 7007 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrCompareVolFailed | 7002 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrCompareVolumeNotExecuted | 7013 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrCompDocsAlreadyOpen | 5001 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompDocsInvalidModConfig | 5008 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompDocsInvalidModFile | 5006 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompDocsInvalidRefConfig | 5007 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompDocsInvalidRefFile | 5005 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompDocsNotExecuted | 5002 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompDocsOperationOptions | 5003 = = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods); Operation out of range |
| gtErrCompDocsResultOptions | 5004 = = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods); Result option out of range |
| gtErrCompDocsSameRefModFilesConfigs | 5009 = Compare document error (errors 5001 through 6000 are returned by ICompareDocument methods) |
| gtErrCompFeatAlreadyRunning | 6004 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatInvalidModConfig | 6010 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatInvalidModFile | 6003 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatInvalidRefConfig | 6009 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatInvalidRefFile | 6002 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatModNoSolidBodies | 6007 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatNotExecuted | 6008 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatRefNoSolidBodies | 6006 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatResultOptions | 6005 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompFeatSameRefModFilesConfigs | 6011 = Compare feature error (errors 6001 through 7000 are returned by ICompareFeature methods) |
| gtErrCompGeomAlreadyOpen | 7008 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrCompGeomInvalidModConfig | 7015 = Returned by ICompareGeometry::CompareGeometry3 if the model configuration is invalid; face/volume comparison cannot be done |
| gtErrCompGeomInvalidModFile | 7010 = Returned by ICompareGeometry::CompareGeometry3 if the model file is invalid; face/volume comparison cannot be done |
| gtErrCompGeomInvalidRefConfig | 7014 = Returned by ICompareGeometry::CompareGeometry3 if the reference configuration is invalid; face/volume comparison cannot be done |
| gtErrCompGeomInvalidRefFile | 7009 = Returned by ICompareGeometry::CompareGeometry3 if the reference file is invalid; face/volume comparison cannot be done |
| gtErrCompGeomOperationOptions | 7011 = Returned by ICompareGeometry::CompareGeometry3 if the operation options are invalid; face/volume comparison cannot be done |
| gtErrCompGeomResultOptions | 7012 = Returned by ICompareGeometry::CompareGeometry3 if the result options are invalid; face/volume comparison cannot be done |
| gtErrCompGeomSameRefModFilesConfigs | 7016 = Returned by ICompareGeometry::CompareGeometry3 if reference, model, or configurations are identical; face/volume comparison cannot be done |
| gtErrCouldNotCreateReportFolders | 14 |
| gtErrDesignBinderReportAlreadyExists | 30 |
| gtErrDoc1NotSelected | 33 |
| gtErrDoc2NotSelected | 34 |
| gtErrDocInEditSketchMode | 12 |
| gtErrDocIsEmpty | 5 |
| gtErrDocNotSelected | 2 |
| gtErrDocOpenedViewOnly | 8 |
| gtErrDocsAreSame | 4 = Returned by ICompareGeometry::CompareGeometry3 if the documents to compare are identical; face/volume comparison cannot be done |
| gtErrDocsConfigNotExist | 29 |
| gtErrDocsConfigsAreSame | 28 = Returned by ICompareGeometry::CompareGeometry3 if the configurations of the documents to compare are identical; face/volume comparison cannot be done |
| gtErrEdrawingFileAlreadyExists | 12018= Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrFaceComparisonNotPossibleInAssemblies | 27 = Returned by ICompareGeometry::CompareGeometry3 if an assembly; face comparison cannot be done in assemblies |
| gtErrFacesIdentical | 7003 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrFileAlreadyExists | 20 |
| gtErrFileNotFound | 18 |
| gtErrFindText | 12019 = Property IFindReplaceAnnotations::FindText is not set |
| gtErrGckAlreadyOpen | 8001 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckDRTError | 8003 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckInsufficientMemoryProvided | 8006 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckInvalidEntityParamater | 8008 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckNoActivePartDoc | 8002 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckNoGetCountFunctionCalled | 8005 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckNotInitialized | 8007 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrGckResultsAlreadyPresent | 8004 = Geometry analysis error (errors 8001 through 9000 are returned by IGeometryAnalysis methods) |
| gtErrIncompatibleFile | 6 |
| gtErrIncorrectFileName | 3 |
| gtErrIncorrectReportPath | 15 |
| gtErrInvalidFile | 17 |
| gtErrNonSimilarParts | 7004 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrNoPartDocs | 25 |
| gtErrNoSolidBodies | 19 |
| gtErrNoSourceFeature | 11003 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrNoTargetFeature | 11004 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrNoUI | 12022= Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrNoValidIndex | 12023= Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrOpeningFile | 1 |
| gtErrPslAlreadyRunning | 10014 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrPslAngleOutofRange | 10006 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslBothConvexConcaveNotSet | 10004 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslColorOutofRange | 10007 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslErrFilterTypeOutofRange | 10010 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslErrOperatorOutofRange | 10005 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslErrorInSelection | 10017 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslFeatureTypeOutofRange | 10008 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslIncorrectFeatureNameString | 10009 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslIncorrectFeatureTypeArray | 10018 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslNoActivePartDoc | 10016 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslNoFeatureTypeFilterSet | 10011 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslNoFilterSet | 10002 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslNoSelectEntitySet | 10001 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslNotInitialized | 10015 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslNotRun | 10013 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslResultOptions | 10019 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslSpecifiedFilterNotSet | 10003 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrPslUIRunning | 10012 = PowerSelect error (errors 10001 through 10019 are returned by IPowerSelect methods) |
| gtErrReferenceBOMNotSelected | 31 |
| gtErrReplaceText | 12020 = Property IFindReplaceAnnotations::ReplaceText is not set |
| gtErrReportAlreadyExists | 13 |
| gtErrResultUIOn | 23 |
| gtErrRollback | 11008 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrSameNameDocAlreadyOpen | 7 |
| gtErrSameSourceTargetFeature | 11005 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrSavingFile | 16 |
| gtErrSavingVolDiffResults | 7005 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtErrSharedByCompDocs | 11 |
| gtErrSharedByFeatDiff | 10 |
| gtErrSharedByGeomDiff | 9 |
| gtErrSourceFeatErr | 11006 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrSourceFeatureRolledBack | 11009 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrSourceNoBodyFeature | 11011 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrTargetFeatErr | 11007 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrTargetFeatureRolledBack | 11010 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrTargetNoBodyFeature | 11012 = Feature paint error (errors 11001 through 12000 are returned by IFeaturePaint methods) |
| gtErrtckBodyDoesNotExist | 12005 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrtckBodyNotSet | 12006 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrtckNoActivePartDoc | 12001 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTckNotInitialized | 12004 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTckNotPerformed | 12015 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTckNotValid | 12016 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTckResolution | 12003 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTckResultOptions | 12002 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrtckTesselationFailed | 12008 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTcktThickRegnLimitNotInRange | 12014 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrTcktTrgThicknessNotInRange | 12013 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrtckUIRunning | 12007 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrThicknessRangeNotValid | 12017 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtErrToBeComparedBOMNotSelected | 32 |
| gtErrToolNotSupported | 21 = Returned by IUtilities::GetToolInterface |
| gtErrUIInvoked | 12021 = = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods); PropertyManager page is already displayed |
| gtErrUtilityAlreadyRunning | 24 = Returned by ICompareGeometry::CompareGeometry3 if the utility is already running; face/volume comparison cannot be done |
| gtErrVolDiffResultsAlreadySaved | 7006 = Compare geometry error (errors 7001 through 8000 are returned by ICompareGeometry methods) |
| gtNOErr | 0 = No error |
| gtUnknownErr | -1 = Common -1 through 5000 |
| gtWarningTckThickAnalRangeAboveMaxThick | 12011 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtWarningTckThickAnalRangeBelowMaxThick | 12012 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtWarningTckThinAnalMinMaxThckSameAsTrg | 12010 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |
| gtWarningTckThinAnalRangeBelowMaxThick | 12009 = Thickness analysis error (errors 12001 through 13000 are returned by IThicknessAnalysis methods) |

## See Also

[SolidWorks.Interop.gtswutilities Namespace](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html)
