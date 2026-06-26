---
title: "swsBaseExcitationEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBaseExcitationEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBaseExcitationEndEditError_e.html"
---

# swsBaseExcitationEndEditError_e Enumeration

Base excitation editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBaseExcitationEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBaseExcitationEndEditError_e
```

### C#

```csharp
public enum swsBaseExcitationEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBaseExcitationEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBaseExcitationError_ExcitationTypeNotAvailable | 3 = Excitation type not available for this study type |
| swsBaseExcitationError_ImproperUnits | 6 = Units given are not correct |
| swsBaseExcitationError_InvalidExcitationType | 2 = Invalid excitation type |
| swsBaseExcitationError_InvalidFixtureNameOrEntity | 5 = Fixture name given or entity name given is not proper |
| swsBaseExcitationError_InvalidValue | 11 = Invalid value |
| swsBaseExcitationError_NoError | 0 = Success |
| swsBaseExcitationError_NoProperFixtures | 4 = No proper fixtures are available for base excitation |
| swsBaseExcitationError_NotAvailableForThisStudy | 1 = Not available for this study type |
| swsBaseExcitationError_SelectAtleastOneDirection | 7 = Select at least one direction |
| swsBaseExcitationError_SelectAtleastOneDirectionOfThatInRestraint | 10 = Select at least one direction that is present in the given restraint |
| swsBaseExcitationError_SelectOnlyOneDirection | 8 = Select only one direction |
| swsBaseExcitationError_SelectOnlyThirdDirection | 9 = Select only the third direction for edge reference entities |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
