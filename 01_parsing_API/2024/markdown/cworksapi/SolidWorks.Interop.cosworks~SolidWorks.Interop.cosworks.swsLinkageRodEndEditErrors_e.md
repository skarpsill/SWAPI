---
title: "swsLinkageRodEndEditErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsLinkageRodEndEditErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinkageRodEndEditErrors_e.html"
---

# swsLinkageRodEndEditErrors_e Enumeration

Linkage rod connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsLinkageRodEndEditErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsLinkageRodEndEditErrors_e
```

### C#

```csharp
public enum swsLinkageRodEndEditErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsLinkageRodEndEditErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsLinkageRodErrCode_InadequateEntitiesSelection | 24 = Insufficient number of entities selected for a valid linkage rod connector |
| swsLinkageRodErrCode_InvalidArray | 11 = Invalid array of section parameters |
| swsLinkageRodErrCode_InvalidCoAxialSelection | 6 = Select non-co-axial concentric cylindrical faces or edges (for shells or surface bodies) at one end |
| swsLinkageRodErrCode_InvalidJointTypeSel | 8 = Select a vertex that is not a pivot joint type |
| swsLinkageRodErrCode_InvalidLibraryMaterialDetails | 19 = Invalid library path/name or non-available material name |
| swsLinkageRodErrCode_InvalidMass | 23 |
| swsLinkageRodErrCode_InvalidMaterialSourceType | 16 = Select material source type from swsMaterialSourceType_e |
| swsLinkageRodErrCode_InvalidNonCoAxialSelection | 5 = Select co-axial concentric cylindrical faces or edges (for shells or surface bodies) at one end |
| swsLinkageRodErrCode_InvalidNonConcentricSelection | 7 = Select concentric cylindrical edges from shell or surface bodies |
| swsLinkageRodErrCode_InvalidParamDataType | 13 = Use double section parameter for given section type |
| swsLinkageRodErrCode_InvalidParamsCount | 12 = Invalid number of section parameters for given section type |
| swsLinkageRodErrCode_InvalidRodSectionType | 10 = Select section type from swsCRSectionType_e |
| swsLinkageRodErrCode_InvalidSelection | 4 = Select cylindrical faces or a single vertex for solid bodies; select edges for shells or surface bodies |
| swsLinkageRodErrCode_InvalidUnitType | 15 = Select unit type from swsUnit_e |
| swsLinkageRodErrCode_NoActiveDoc | 1 |
| swsLinkageRodErrCode_NoActiveStudy | 2 |
| swsLinkageRodErrCode_OffsetOptionNotAvailable | 9 = Offset direction and values not available for selected vertex |
| swsLinkageRodErrCode_OutOfRangePoissonRatio | 21 = 0 < Poisson Ratio < 1 |
| swsLinkageRodErrCode_OutOfRangeThermalCoefficient | 22 = 0 < Thermal Coefficient < 1e+16 |
| swsLinkageRodErrCode_OutOfRangeYoungsModulus | 20 = 0 < Young's Modulus < 1e+16 |
| swsLinkageRodErrCode_SetLibraryMaterialNA | 18 = Setting the library material is allowed only when Material Source Type = swsMaterial_Library |
| swsLinkageRodErrCode_SetMaterialPropertyNA | 17 = Setting material property is only allowed when Material Source Type = swsMaterial_Custom |
| swsLinkageRodErrCode_SetOperationNotSupported | 3 = Editing before calling BeginEdit not allowed |
| swsLinkageRodErrCode_Successful | 0 |
| swsLinkageRodErrCode_ZeroParamValue | 14 = Invalid section parameter value for given section type |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
