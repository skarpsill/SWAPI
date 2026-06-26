---
title: "CreateFeatureMgrWindowFromHandle Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateFeatureMgrWindowFromHandle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle.html"
---

# CreateFeatureMgrWindowFromHandle Method (IModelViewManager)

Creates a new view in the FeatureManager design tree using the specified .NET tab control.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrWindowFromHandle( _
   ByVal BitMapFile As System.String, _
   ByVal WindowHandle As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim WindowHandle As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.CreateFeatureMgrWindowFromHandle(BitMapFile, WindowHandle, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView CreateFeatureMgrWindowFromHandle(
   System.string BitMapFile,
   System.int WindowHandle,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ CreateFeatureMgrWindowFromHandle(
   System.String^ BitMapFile,
   System.int WindowHandle,
   System.String^ ToolTip,
   System.int WhichPane
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `BitMapFile`: Fully qualified path to the bitmap file that you want to use for the control
- `WindowHandle`: Handle of the .NET tab control
- `ToolTip`: Text for the ToolTip
- `WhichPane`: Pane to use as defined in

[swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

[IFeatMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html)

## VBA Syntax

See

[ModelViewManager::CreateFeatureMgrWindowFromHandle](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateFeatureMgrWindowFromHandle.html)

.

## Remarks

If your application must be x64 compatible, then use

[IModelViewManager::CreateFeatureMgrWindowFromHandlex64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64.html)

.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)

[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)

[IModelViewManager::DisplayWindowFromHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandle.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
