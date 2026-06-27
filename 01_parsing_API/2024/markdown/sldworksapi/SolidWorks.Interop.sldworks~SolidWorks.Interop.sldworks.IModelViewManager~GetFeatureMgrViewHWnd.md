---
title: "GetFeatureMgrViewHWnd Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetFeatureMgrViewHWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.html"
---

# GetFeatureMgrViewHWnd Method (IModelViewManager)

Gets the window handle for the specified FeatureManager design tree view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureMgrViewHWnd( _
   ByVal FeatMgrViewPane As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim FeatMgrViewPane As System.Integer
Dim value As System.Integer

value = instance.GetFeatureMgrViewHWnd(FeatMgrViewPane)
```

### C#

```csharp
System.int GetFeatureMgrViewHWnd(
   System.int FeatMgrViewPane
)
```

### C++/CLI

```cpp
System.int GetFeatureMgrViewHWnd(
   System.int FeatMgrViewPane
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `FeatMgrViewPane`: FeatureManager design tree view as defined by

[swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

Window handle for the specified FeatMgrViewPane

## VBA Syntax

See

[ModelViewManager::GetFeatureMgrViewHWnd](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetFeatureMgrViewHWnd.html)

.

## Remarks

If your application must be x64 compatible, then use

[IModelViewManager::GetFeatureMgrViewHWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.html)

.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)

[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
