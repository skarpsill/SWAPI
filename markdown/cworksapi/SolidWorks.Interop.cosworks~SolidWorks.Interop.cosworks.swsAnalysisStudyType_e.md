---
title: "swsAnalysisStudyType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsAnalysisStudyType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsAnalysisStudyType_e.html"
---

# swsAnalysisStudyType_e Enumeration

Analysis study types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsAnalysisStudyType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsAnalysisStudyType_e
```

### C#

```csharp
public enum swsAnalysisStudyType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsAnalysisStudyType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsAnalysisStudyTypeBuckling | 2 = Buckling (analysis or study) |
| swsAnalysisStudyTypeDropTest | 6 = Drop test (study only) |
| swsAnalysisStudyTypeDynamic | 8 = Linear dynamic (study only) |
| swsAnalysisStudyTypeFatigue | 7 = Fatigue (study only) |
| swsAnalysisStudyTypeFrequency | 1 = Frequency (analysis or study) |
| swsAnalysisStudyTypeNonlinear | 5 = Nonlinear (analysis or study) |
| swsAnalysisStudyTypeOptimization | 4 = Optimization (study only) |
| swsAnalysisStudyTypePressureVessel | 9 = Pressure Vessel (study only) |
| swsAnalysisStudyTypeReserved1 | 10 |
| swsAnalysisStudyTypeReserved2 | 11 |
| swsAnalysisStudyTypeReserved3 | 12 |
| swsAnalysisStudyTypeStatic | 0 = Static (analysis or study) |
| swsAnalysisStudyTypeThermal | 3 = Thermal (analysis or study) |
| swsAnalysisStudyTypeTopology_Static | 13 = Topology (analysis or study) |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
