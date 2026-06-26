---
title: "swsStressHotSpotResultsRestoreOptions_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStressHotSpotResultsRestoreOptions_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStressHotSpotResultsRestoreOptions_e.html"
---

# swsStressHotSpotResultsRestoreOptions_e Enumeration

Restore options after stress hot spot detection

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStressHotSpotResultsRestoreOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStressHotSpotResultsRestoreOptions_e
```

### C#

```csharp
public enum swsStressHotSpotResultsRestoreOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStressHotSpotResultsRestoreOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStressHotSpotResultsRestoreOption_FinalMesh | 1 = Overwrite the existing mesh and results with final level settings |
| swsStressHotSpotResultsRestoreOption_OriginalMesh | 0 = Restore the study with the original mesh settings |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
