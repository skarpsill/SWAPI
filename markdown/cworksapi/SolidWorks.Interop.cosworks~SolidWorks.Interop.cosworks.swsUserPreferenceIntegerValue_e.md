---
title: "swsUserPreferenceIntegerValue_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsUserPreferenceIntegerValue_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUserPreferenceIntegerValue_e.html"
---

# swsUserPreferenceIntegerValue_e Enumeration

User preference integer values

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsUserPreferenceIntegerValue_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsUserPreferenceIntegerValue_e
```

### C#

```csharp
public enum swsUserPreferenceIntegerValue_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsUserPreferenceIntegerValue_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsColorChartColorOptionBaseChartColorNumber | 23 = Get or set the number of colors in the color chart; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Color Options > No of chart colors |
| swsColorChartColorOptionChartColorNumber | 22 = Get or set the user-defined number of colors in the color chart; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Color Options > User defined |
| swsColorChartColorOptionLegendType | 24 = Get or set the color legend type as defined in swsColorChartOptionLegendTypeValue_e ; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Color Options > (Default, Rainbow, Gray scale, User Defined) |
| swsColorChartColorOptionvonMisesColorValue | 27 = Get or set the color for values above yield for vonMises plots; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Color Options > Specify color for values above yield for vonMises plot |
| swsColorChartNumberFormatLegendPrecision | 25 = Get or set the number of decimal places for precision of number formats; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Number format > No. of decimal places: |
| swsColorChartNumberFormatOption | 21 = Get or set the number format as defined in swsColorChartNumberFormatOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Number format > (Scientific, Floating, or General) |
| swsColorChartNumberFormatUseDiffNoFormatOption | 26 = Get or set which notation other than scientific to use for small numbers as defined in swsColorNumberFormatUseDiffNumberFormatOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Number format > Scientific > Use different number format for small numbers (0.001 < \|x\| < 1000) > (Floating or General) |
| swsColorChartPosition | 3 = Get or set the position of the color bar as defined in swsColorChartPositionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Position > (Predefined positions or user defined) |
| swsColorChartPositionUserDefinedXValue | 18 = Get or set the color bar's horizontal distance from the left of the graphics area as a percentage of the width of the window; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Position > User defined > Horizontal from left: |
| swsColorChartPositionUserDefinedYValue | 19 = Get or set the color bar's vertical distance from the top of the graphics area as a percentage of the height of the window; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Position > User defined > Vertical from top: |
| swsColorChartWidthOption | 20 = Get or set the color chart width as defined in swsColorChartWidthOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Color Chart > Width |
| swsDefaultResultFolder | 1 = Get or set the results folder option as defined in swsResultFolderValue_e ; corresponds to Simulation > Options > Default Options > Results > Results folder > (SOLIDWORKS document folder or User defined) |
| swsDefaultSolverValue | 0 = Get or set the default solver as defined in swsSolverType_e ; corresponds to Simulation > Options > Default Options > Results > Default Solver > (Automatic, Direct sparse, or FFEPlus) |
| swsEMailType | 30 |
| swsMesherType | 31 = Get or set the mesher type as defined in swsMesherTypeNew_e |
| swsPlotBoundaryOptionMeshColor | 9 = Get or set the mesh color for boundaries (see Remarks ); corresponds to Simulation > Options > Default Options > Plot > Settings options > Boundary options > Mesh > color select box |
| swsPlotBoundaryOptionModelColor | 29 = Get or set the model color for boundaries (see Remarks ); corresponds to Simulation > Options > Default Options > Plot > Settings options > Boundary options > Model |
| swsPlotBoundaryOptionTranslucentSingleColorSetting | 8 = Get or set the translucent color for boundaries (see Remarks ); corresponds to Simulation > Options > Default Options > Plot > Settings options > Boundary options > Translucent (Single color) > color select box |
| swsPlotDeformedShapeOptionSetSuperImposeOption | 16 = Get or set the translucent color option for superimposing the model on deformed shape as defined in swsPlotDeformedShapeOptionSuperImposeValue_e ; corresponds to Simulation > Options > Default Options > Plot > Deformed shape options > Show results on deformed shape > Superimpose model on deformed shape > Translucent (part colors or single color) |
| swsPlotDeformedShapeOptionSetting | 12 = Get or set how to show deformed shape results as defined in swsPlotDeformedShapeOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Deformed shape options > Show results on undeformed shape or Show results on deformed shape |
| swsPlotDeformedShapeOptionTranslucentColor | 28 = Get or set the translucent color for superimposing the model on deformed shape (see Remarks ); corresponds to Simulation > Options > Default Options > Plot > Deformed shape options > Show results on deformed shape > Superimpose model on deformed shape > Translucent (single color) > color select box |
| swsPlotDeformedShapeResultOther | 15 = Get or set the deformation scale factor for all other studies as defined in swsPlotDeformedShapeOptionScaleFactorOtherValue_e ; corresponds to Simulation > Options > Default Options > Plot > Deformed shape options > Show results on deformed shape > Deformation scale factor for: > all other studies: > Automatic or True(1.0) |
| swsPlotDeformedShapeResultScaleContact | 13 = Get or set the deformation scale factor for all studies with "No penetration" contact as defined in swsPlotDeformedShapeOptionScaleFactorContactValue_e ; corresponds to Simulation > Options > Default Options > Plot > Deformed shape options > Show results on deformed shape > Deformation scale factor for: > all studies with "No penetration" contact: > Automatic or True(1.0) |
| swsPlotDeformedShapeResultScaleLarge | 14 = Get or set the deformation scale factor for studies with the "Large displacement" option as defined in swsPlotDeformedShapeOptionScaleFactorLargeDispValue_e ; corresponds to Simulation > Options > Default Options > Plot > Deformed shape options > Show results on deformed shape > Deformation scale factor for: > studies with the "Large displacement" option: > Automatic or True(1.0) |
| swsPlotSettingsBoundaryOption | 5 = Get or set the boundary option as defined in swsPlotBoundarySettingsOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Settings options > Boundary options |
| swsPlotSettingsFringeOption | 4 = Get or set the fringe option as defined in swsPlotFringeSettingsOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Settings options > Fringe options |
| swsPlotShowExcludedBodiesOption | 6 = Get or set the translucent color option for excluded bodies as defined in swsPlotShowExcludedBodiesOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Settings options > Show excluded bodies > Translucent (Single color or Part colors) |
| swsPlotShowExcludedBodyTranslucentSingleColor | 10 = Get or set the translucent color for all excluded bodies (see Remarks ); corresponds to Simulation > Options > Default Options > Plot > Settings options > Show excluded bodies > Translucent (Single color) > color select box |
| swsPlotShowHiddenBodiesOption | 7 = Get or set the translucent color option for hidden bodies as defined in swsPlotShowHiddenBodiesOptionValue_e ; corresponds to Simulation > Options > Default Options > Plot > Settings options > Show hidden bodies > Translucent (Single color or Part colors) |
| swsPlotShowHiddenBodyTranslucentSingleColor | 11 = Get or set the translucent color for all hidden bodies (see Remarks ); corresponds to Simulation > Options > Default Options > Plot > Settings options > Show hidden bodies > Translucent (Single color) > color select box |
| swsReportPublishOption | 2 = Get or set the report folder location as defined in swsReportFolderValue_e ; corresponds to Simulation > Options > Default Options > Report > Report publish options > Report folder |
| swsReportPublishOptionReportFolderUserDefinedPath | 17 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
