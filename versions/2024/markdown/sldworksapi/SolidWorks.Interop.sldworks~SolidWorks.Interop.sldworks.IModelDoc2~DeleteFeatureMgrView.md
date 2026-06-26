---
title: "DeleteFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeleteFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView.html"
---

# DeleteFeatureMgrView Method (IModelDoc2)

Removes the specified tab in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteFeatureMgrView( _
   ByRef AppView As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AppView As System.Integer

instance.DeleteFeatureMgrView(AppView)
```

### C#

```csharp
void DeleteFeatureMgrView(
   ref System.int AppView
)
```

### C++/CLI

```cpp
void DeleteFeatureMgrView(
   System.int% AppView
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `AppView`: View handle of the FeatureManager design tree view to delete

## VBA Syntax

See

[ModelDoc2::DeleteFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeleteFeatureMgrView.html)

.

## Remarks

If your application must be x64 compatible, then use[IModelDocExtension::DeleteFeatureMgrViewx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64.html).

On the appropriate notification, you can call this method to clean up and delete your FeatureManager design tree view.

Use this method with[IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html)or[IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html).

(Table)=========================================================

| If you created the FeatureManager design tree view using... | Then... |
| --- | --- |
| IModelViewManager::CreateFeatureMgrView2 | Calling IModelDoc2::DeleteFeatureMgrView destroys the CView object used for the FeatureManager design tree view. |
| IModelDoc2::AddFeatureMgrView3 | Your application allocated the CView object and calling IModelDoc2::DeleteFeatureMgrView does not destroy the CView object. In this case, you must destroy the CVew object using the appropriate destructor. Never use the delete operator directly on the CView object. Always use one of the appropriate MFC view destructors. |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
