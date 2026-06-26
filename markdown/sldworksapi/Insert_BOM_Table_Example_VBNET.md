---
title: "Insert BOM Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_Example_VBNET.htm"
---

# Insert BOM Table Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swFeatMgr As FeatureManager
        Dim swView As View
        Dim swBomAnn As BomTableAnnotation
        Dim swBomFeat As BomFeature
        Dim AnchorType As Integer
        Dim BomType As Integer
        Dim Configuration As String
        Dim TableTemplate As String
        Dim Names As Object
        Dim Visible As Object = Nothing
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swFeatMgr = swModel.FeatureManager

        ' Get selected drawing view
        swView = swSelMgr.GetSelectedObject6(1, 0)
        AnchorType = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft
        BomType = swBomType_e.swBomType_TopLevelOnly
        Configuration = ""
        TableTemplate = ""

        ' Insert BOM table
        swBomAnn = swView.InsertBomTable2(True, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate)

        swModel.ClearSelection2(True)

        ' Because BOM type is swBomType_TopLevelOnly,
        ' then work with BomFeature to get and set configurations
        swBomFeat = swBomAnn.BomFeature
        Names = swBomFeat.GetConfigurations(False, Visible)
        Visible(0) = True
        boolstatus = swBomFeat.SetConfigurations(True, Visible, Names)

        ' Update FeatureManager design tree
        swFeatMgr.UpdateFeatureTree()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
