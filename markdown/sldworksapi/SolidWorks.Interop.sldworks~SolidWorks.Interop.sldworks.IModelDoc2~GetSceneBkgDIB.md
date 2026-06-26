---
title: "GetSceneBkgDIB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetSceneBkgDIB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.html"
---

# GetSceneBkgDIB Method (IModelDoc2)

Gets background image as a LPDIBSECTION.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSceneBkgDIB() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetSceneBkgDIB()
```

### C#

```csharp
System.int GetSceneBkgDIB()
```

### C++/CLI

```cpp
System.int GetSceneBkgDIB();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Background image as DIBSECTION

## VBA Syntax

See

[ModelDoc2::GetSceneBkgDIB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetSceneBkgDIB.html)

.

## Remarks

If your application must be x64 compatible, then use[IModelDocExtension::GetSceneBkgDIBx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.html).

The memory for the image bits (DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS application and must be deleted by the caller.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.html)

[IModelDocExtension::SetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.html)

[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.html)

[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html)

[IModelDoc2::DeleteBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBkgImage.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
