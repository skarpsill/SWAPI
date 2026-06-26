---
title: "SaveAsPreviousVersion Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "SaveAsPreviousVersion"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.html"
---

# SaveAsPreviousVersion Property (IAdvancedSaveAsOptions)

Sets whether to save as previous version.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property SaveAsPreviousVersion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.SaveAsPreviousVersion = value
```

### C#

```csharp
System.int SaveAsPreviousVersion {set;}
```

### C++/CLI

```cpp
property System.int SaveAsPreviousVersion {
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to save as previous version, false to not

## VBA Syntax

See

[AdvancedSaveAsOptions::SaveAsPreviousVersion](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~SaveAsPreviousVersion.html)

.

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)

[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
