---
title: "swsMultipleContactsEditErrorCode_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMultipleContactsEditErrorCode_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html"
---

# swsMultipleContactsEditErrorCode_e Enumeration

Error codes for the simultaneous editing of component contacts and contact sets

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMultipleContactsEditErrorCode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMultipleContactsEditErrorCode_e
```

### C#

```csharp
public enum swsMultipleContactsEditErrorCode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMultipleContactsEditErrorCode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMultipleContactsEditErrorCode_BondedContactsWithBeamsCannotBeEditedWithOtherNonBeamContactTypes | 12 = Bonded contact sets with beams cannot be edited together with other contact types |
| swsMultipleContactsEditErrorCode_GivenContactIsAlreadyAdded | 8 = Contact has already been added |
| swsMultipleContactsEditErrorCode_GivenContactIsNotAddedYet | 3 = Specified contact set is not yet added to the selection list |
| swsMultipleContactsEditErrorCode_GivenContactSetDidNotMeetMinCriteria | 7 = Specified contact set/component contact does not meet the qualifying criteria for editing multiple contacts interactively |
| swsMultipleContactsEditErrorCode_InvalidPropertiesAreApplied | 6 = Attempted to set one or more properties that are inconsistent with each other |
| swsMultipleContactsEditErrorCode_MultipleContactSetMgrIsNull | 5 = Multiple contact sets cannot be simultaneously edited |
| swsMultipleContactsEditErrorCode_NoDefaultContactIsSelected | 2 = Default contact must be set when the same type of contact is selected for editing |
| swsMultipleContactsEditErrorCode_NoPenetrationSelfContactSetsCannotBeEditedWithOtherContactTypes | 10 = No Penetration self contact sets cannot be edited with other contact types |
| swsMultipleContactsEditErrorCode_NoSuchContactExists | 4 = Specified name of contact set does not exist in the current study |
| swsMultipleContactsEditErrorCode_NoTypeSelectedForMixedContactTypesSelection | 1 = Contact type must be set when different types of contacts are selected for editing |
| swsMultipleContactsEditErrorCode_OperationNotSupported | 9 = Operation cannot be performed out of sequence |
| swsMultipleContactsEditErrorCode_Success | 0 = Success |
| swsMultipleContactsEditErrorCode_VirtualWallContactSetsCannotBeEditedWithOtherContactTypes | 11 = Virtual wall contact sets cannot be edited together with other contact types |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
