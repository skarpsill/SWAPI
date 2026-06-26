---
title: "SetSceneBkgDIB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetSceneBkgDIB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.html"
---

# SetSceneBkgDIB Method (IModelDoc2)

Sets background image described by DIBSECTION data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSceneBkgDIB( _
   ByVal L_dib As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim L_dib As System.Integer

instance.SetSceneBkgDIB(L_dib)
```

### C#

```csharp
void SetSceneBkgDIB(
   System.int L_dib
)
```

### C++/CLI

```cpp
void SetSceneBkgDIB(
   System.int L_dib
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `L_dib`: DIBSECTION

## VBA Syntax

See

[ModelDoc2::SetSceneBkgDIB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetSceneBkgDIB.html)

.

## Remarks

If your application must be x64 compatible, then use[IModelDocExtension::SetSceneBkgDIBx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.html).

Old background images are deleted automatically.

For more information about DIBSECTION, see Microsoft's documentation.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.html)

[IModelDocExtension::GetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.html)

[IModelDocExtension::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html)

[IModelDocExtension::DeleteBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBkgImage.html)

[IModelDocExtension::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
