---
title: "swsTopologyPreservedRegionOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyPreservedRegionOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyPreservedRegionOption_e.html"
---

# swsTopologyPreservedRegionOption_e Enumeration

Topology study preserved region options

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyPreservedRegionOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyPreservedRegionOption_e
```

### C#

```csharp
public enum swsTopologyPreservedRegionOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyPreservedRegionOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| PreservedRegion_FixturesOnly | 1 = Exclude from optimization faces where fixtures are applied |
| PreservedRegion_LoadsAndFixtures | 2 = Exclude from optimization faces where loads or fixtures are applied |
| PreservedRegion_LoadsOnly | 0 = Exclude from optimization faces where loads are applied |
| PreservedRegion_None | 3 = Select which regions to exclude from optimization |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
