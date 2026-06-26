---
title: "Insert BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_Example_VB.htm"
---

# Insert BOM Table Example (VBA)

This example shows how to insert a BOM table using IView::InsertBomTable2.

```
'-----------------------------------------------------
' Preconditions: Open a drawing document and select
' a drawing view.
'
' Postconditions:
' 1. Inserts a BOM at the anchor point, if the
'    drawing view does not already contain a BOM.
' 2. Examine the drawing and FeatureManager design tree.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeatMgr As SldWorks.FeatureManager
Dim swView As SldWorks.View
Dim swBomAnn As BomTableAnnotation
Dim swBomFeat As SldWorks.BomFeature
Dim AnchorType As Long
Dim BomType As Long
Dim Configuration As String
Dim TableTemplate As String
Dim Names As Variant
Dim Visible As Variant
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeatMgr = swModel.FeatureManager
```

```
    ' Get selected drawing view
    Set swView = swSelMgr.GetSelectedObject6(1, 0)
    AnchorType = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft
    BomType = swBomType_e.swBomType_TopLevelOnly
    Configuration = ""
    TableTemplate = ""
```

```
    ' Insert BOM table
    Set swBomAnn = swView.InsertBomTable2(True, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate)
```

```
    swModel.ClearSelection2 True
```

```
    ' Because BOM type is swBomType_TopLevelOnly,
    ' then work with BomFeature to get and set configurations
    Set swBomFeat = swBomAnn.BomFeature
    Names = swBomFeat.GetConfigurations(False, Visible)
    Visible(0) = True
    boolstatus = swBomFeat.SetConfigurations(True, Visible, Names)
```

```
    ' Update FeatureManager design tree
    swFeatMgr.UpdateFeatureTree
```

```
End Sub
```
