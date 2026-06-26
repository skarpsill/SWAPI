---
title: "Insert BOM Table and BOM Balloon Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_VBNET.htm"
---

# Insert BOM Table and BOM Balloon Example (VB.NET)

This example shows how to insert a BOM table and a BOM balloon in a
drawing document.

```
'------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a parts-only BOM table.
' 2. Inserts a split-circle BOM balloon, which uses the BOM
'    table item number for its upper text,
'    to the selected edge.
' 3. Zoom to area and examine both the BOM table and BOM
'    balloon to verify.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save any changes.
'-------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDrawing As DrawingDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swView As View
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swBOMAnnotation As BomTableAnnotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swBOMFeature As BomFeature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swNote As Note
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim AnchorType As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BomType As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Configuration As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim TableTemplate As String

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View1")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swView = swDrawing.ActiveDrawingView

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Insert parts-only BOM table
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AnchorType = swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}BomType = swBomType_e.swBomType_PartsOnly
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Configuration = ""
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}TableTemplate = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\bom-standard.sldbomtbt"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swBOMAnnotation = swView.InsertBomTable2(False, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swBOMFeature = swBOMAnnotation.BomFeature

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Print the name of the configuration used for the BOM table
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Name of configuration used for BOM table: " & swBOMFeature.Configuration)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Insert BOM balloon for the selected edge
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -0.0004000000000133, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swNote = swModelDocExt.InsertBOMBalloon(swBalloonStyle_e.swBS_SplitCirc, swBalloonFit_e.swBF_Tightest, swBalloonTextContent_e.swBalloonTextItemNumber, "", swBalloonTextContent_e.swBalloonTextCustom, "Lower text", swBalloonFit_e.swBF_UserDef, True, 2, "Denotation Text")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get whether balloon is a BOM balloon;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' if so, print the name of the BOM balloon
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swNote.IsBomBalloon Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Name of BOM balloon: " & swNote.GetName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
